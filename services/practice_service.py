import json
from database import get_db
from services.player_service import spend_energy, award_xp, get_player
from services.gacha_service import roll_gacha
from services.question_service import get_questions_for_module, generate_session_id
import config

# In-memory session store: session_id -> {focus_cost, ...}
_sessions: dict[str, dict] = {}


def start_practice(player_id: int, module_id: int, count: int = 10) -> dict | None:
    questions = get_questions_for_module(module_id, player_id, count)
    if not questions:
        return None

    session_id = generate_session_id()
    cost = sum(config.FOCUS_COSTS.get(q["type"], 2) for q in questions)

    db = get_db()
    mod = db.execute("SELECT name FROM modules WHERE id=?", (module_id,)).fetchone()
    _sessions[session_id] = {"focus_cost": cost}

    return {
        "session_id": session_id,
        "module_id": module_id,
        "module_name": mod["name"],
        "questions": questions,
        "focus_cost": cost,
    }


def submit_practice(
    player_id: int,
    module_id: int,
    session_id: str,
    answers: list[dict],
    time_used_sec: int,
) -> dict:
    db = get_db()
    question_ids = [a["question_id"] for a in answers]
    placeholders = ",".join("?" * len(question_ids))
    rows = db.execute(
        f"SELECT id, type, difficulty, content, answer, solution, source_ref FROM questions WHERE id IN ({placeholders})",
        question_ids,
    ).fetchall()
    qmap = {r["id"]: dict(r) for r in rows}

    # Grade and collect per-question results
    total = len(answers)
    correct_count = 0
    per_question = []
    wrong_count = 0

    for a in answers:
        q = qmap.get(a["question_id"], {})
        user_ans = str(a["answer"]).strip() if a["answer"] else ""
        correct_ans = str(q.get("answer", "")).strip()
        is_correct = user_ans == correct_ans
        if is_correct:
            correct_count += 1
        else:
            wrong_count += 1

        per_question.append({
            "question_id": a["question_id"],
            "content": q.get("content", ""),
            "type": q.get("type", "unknown"),
            "difficulty": q.get("difficulty", 1),
            "user_answer": user_ans,
            "correct_answer": correct_ans,
            "solution": q.get("solution", ""),
            "source_ref": q.get("source_ref", ""),
            "is_correct": is_correct,
        })

    accuracy = correct_count / total if total > 0 else 0

    # Record practice
    db.execute(
        """INSERT INTO practice_records
               (player_id, module_id, total_questions, correct_count,
                time_used_sec, session_id, answered_question_ids)
           VALUES (?,?,?,?,?,?,?)""",
        (player_id, module_id, total, correct_count, time_used_sec, session_id, json.dumps(question_ids)),
    )
    db.commit()

    # Auto-create mistakes for wrong answers with 三问法 data
    mistakes_created = 0
    for pq in per_question:
        if not pq["is_correct"]:
            existing = db.execute(
                "SELECT id FROM mistakes WHERE player_id=? AND question=? AND mastered=0",
                (player_id, pq["content"]),
            ).fetchone()
            if not existing:
                wrong_step = f"你的答案: {pq['user_answer']}，正确答案: {pq['correct_answer']}"
                correct_thought = pq.get("solution", "") or f"正确答案是 {pq['correct_answer']}"
                # Extract knowledge point from question concepts
                qrow = db.execute("SELECT concepts FROM questions WHERE id=?", (pq["question_id"],)).fetchone()
                concepts_str = ""
                if qrow and qrow["concepts"]:
                    try:
                        concepts = json.loads(qrow["concepts"])
                        concepts_str = ", ".join(concepts)
                    except: pass
                db.execute(
                    """INSERT INTO mistakes (player_id, module_id, question, wrong_step, correct_thought, knowledge_point, error_type)
                       VALUES (?,?,?,?,?,?,?)""",
                    (player_id, module_id, pq["content"], wrong_step, correct_thought, concepts_str, "knowledge_gap"),
                )
                mistakes_created += 1
    db.commit()

    # Spend energy
    session_data = _sessions.pop(session_id, {})
    cost = session_data.get("focus_cost", 0)
    if cost:
        spend_energy(player_id, cost)

    # Award XP
    base_xp = total * config.XP_PER_QUESTION
    if accuracy == 1.0:
        base_xp += config.XP_PERFECT_BONUS
    award_xp(player_id, base_xp)

    # Near-miss check
    near_miss = config.NEAR_MISS_MIN <= accuracy <= config.NEAR_MISS_MAX

    # Gacha roll
    p = get_player(player_id)
    streak_bonus = p["streak_days"] >= 7
    gacha = roll_gacha(player_id, streak_bonus=streak_bonus)

    # Auto-complete relevant daily tasks
    tasks_auto_done = _auto_complete_tasks(db, player_id)

    # Recalculate module mastery (updates 5-dim scores + difficulty for next practice)
    try:
        from services.mastery_service import calculate_mastery
        mastery = calculate_mastery(player_id, module_id)
    except Exception:
        mastery = None

    return {
        "total": total,
        "correct": correct_count,
        "wrong": wrong_count,
        "accuracy": round(accuracy, 4),
        "xp_gained": base_xp,
        "near_miss": near_miss,
        "gacha_result": gacha,
        "per_question": per_question,
        "mistakes_created": mistakes_created,
        "tasks_auto_done": tasks_auto_done,
    }


def _auto_complete_tasks(db, player_id: int) -> int:
    """Auto-complete any pending daily tasks that are now satisfied."""
    from datetime import date
    today = date.today().isoformat()
    auto_done = 0

    # Auto-complete "main" quests (practice-based)
    tasks = db.execute(
        "SELECT id, content FROM daily_tasks WHERE player_id=? AND scheduled_date=? AND completed=0",
        (player_id, today),
    ).fetchall()

    for t in tasks:
        # Main tasks mentioning "完成10道" or practice — auto-complete after any practice
        if "完成" in t["content"]:
            db.execute(
                "UPDATE daily_tasks SET completed=1, completed_date=datetime('now') WHERE id=?",
                (t["id"],),
            )
            auto_done += 1

    if auto_done:
        db.commit()
    return auto_done
