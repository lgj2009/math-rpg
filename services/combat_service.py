"""Combat-style practice: one question at a time, instant feedback, combo system."""
import json, time
from database import get_db
from services.player_service import spend_energy, award_xp, get_player
from services.gacha_service import roll_gacha
import config

# In-memory session store
_sessions: dict[str, dict] = {}


def start_combat(player_id: int, module_id: int, count: int = 10, lang: str = "zh") -> dict | None:
    """Start a combat session — returns first question + boss info."""
    from services.question_service import get_questions_for_module, generate_session_id

    questions = get_questions_for_module(module_id, player_id, count, lang)
    if not questions:
        return None

    session_id = generate_session_id()
    cost = sum(config.FOCUS_COSTS.get(q["type"], 1) for q in questions)

    db = get_db()
    mod = db.execute("SELECT name FROM modules WHERE id=?", (module_id,)).fetchone()

    _sessions[session_id] = {
        "player_id": player_id,
        "module_id": module_id,
        "questions": questions,
        "current_idx": 0,
        "correct": 0,
        "wrong": 0,
        "combo": 0,
        "max_combo": 0,
        "crits": 0,
        "total_time_ms": 0,
        "focus_cost": cost,
        "started_at": time.time(),
        "per_question": [],
    }

    first_q = questions[0]
    if first_q.get("options"):
        try:
            first_q["options"] = json.loads(first_q["options"]) if isinstance(first_q["options"], str) else first_q["options"]
        except:
            pass

    return {
        "session_id": session_id,
        "module_id": module_id,
        "module_name": mod["name"],
        "total_questions": len(questions),
        "boss_hp": len(questions),
        "boss_name": _boss_name(mod["name"]),
        "focus_cost": cost,
        "question": first_q,
        "question_number": 1,
    }


def answer_question(session_id: str, answer: str, time_ms: int) -> dict:
    """Submit one answer — returns instant feedback + next question or results."""
    session = _sessions.get(session_id)
    if not session:
        return {"detail": "session not found", "finished": True}

    current_q_idx = session["current_idx"]
    q = session["questions"][current_q_idx]
    correct_answer = str(q.get("answer", "")).strip()
    user_answer = str(answer).strip()
    is_correct = user_answer == correct_answer

    # Update combo
    if is_correct:
        session["correct"] += 1
        session["combo"] += 1
        session["max_combo"] = max(session["max_combo"], session["combo"])
        # Crit: first 15 seconds = double
        crit = time_ms < 15000
        if crit:
            session["crits"] += 1
    else:
        session["wrong"] += 1
        session["combo"] = 0
        crit = False

    session["total_time_ms"] += time_ms
    session["current_idx"] += 1

    # XP for this question
    base_xp = config.XP_PER_QUESTION
    combo_mult = 1.0
    if session["combo"] >= 8:
        combo_mult = 3.0
    elif session["combo"] >= 5:
        combo_mult = 2.0
    elif session["combo"] >= 3:
        combo_mult = 1.5
    xp_gained = int(base_xp * combo_mult * (2 if crit else 1))

    # Save per-question result
    session["per_question"].append({
        "content": q.get("content", ""),
        "correct_answer": correct_answer,
        "user_answer": user_answer,
        "is_correct": is_correct,
        "crit": crit,
        "combo": session["combo"] if is_correct else 0,
        "xp": xp_gained,
        "solution": q.get("solution", ""),
        "source_ref": q.get("source_ref", ""),
    })

    # Award XP immediately
    if xp_gained > 0:
        award_xp(session["player_id"], xp_gained)

    # Boss HP remaining
    total_qs = len(session["questions"])
    boss_hp = total_qs - session["current_idx"]
    finished = session["current_idx"] >= total_qs

    # Build feedback
    feedback = {
        "is_correct": is_correct,
        "correct_answer": correct_answer,
        "solution": q.get("solution", ""),
        "xp_gained": xp_gained,
        "combo": session["combo"] if is_correct else 0,
        "max_combo": session["max_combo"],
        "crit": crit,
        "boss_hp_remaining": boss_hp,
        "boss_hp_total": total_qs,
        "question_number": session["current_idx"],
        "total_questions": total_qs,
        "finished": finished,
    }

    if finished:
        # Combat complete — finalize
        feedback["final"] = _finalize_combat(session, session_id)

    if not finished:
        # Next question
        next_q = session["questions"][session["current_idx"]]
        if next_q.get("options") and isinstance(next_q["options"], str):
            try:
                next_q["options"] = json.loads(next_q["options"])
            except:
                pass
        feedback["next_question"] = next_q

    return feedback


def _finalize_combat(session: dict, sid: str) -> dict:
    """End combat: deduct energy, roll gacha, create mistakes, record practice, check mastery."""
    db = get_db()
    pid = session["player_id"]
    mid = session["module_id"]
    total = len(session["questions"])
    correct = session["correct"]
    accuracy = correct / total if total > 0 else 0

    # Deduct energy
    cost = session["focus_cost"]
    if cost:
        spend_energy(pid, cost)

    # Record practice
    question_ids = [q["id"] for q in session["questions"]]
    time_sec = int(session["total_time_ms"] / 1000)
    db.execute(
        """INSERT INTO practice_records (player_id, module_id, total_questions, correct_count, time_used_sec, session_id, answered_question_ids)
           VALUES (?,?,?,?,?,?,?)""",
        (pid, mid, total, correct, time_sec, sid, json.dumps(question_ids)),
    )
    db.commit()

    # Auto-create mistakes
    mistakes_created = 0
    for pq in session["per_question"]:
        if not pq["is_correct"]:
            existing = db.execute(
                "SELECT id FROM mistakes WHERE player_id=? AND question=? AND mastered=0",
                (pid, pq["content"]),
            ).fetchone()
            if not existing:
                db.execute(
                    """INSERT INTO mistakes (player_id, module_id, question, wrong_step, correct_thought, knowledge_point, error_type)
                       VALUES (?,?,?,?,?,?,?)""",
                    (pid, mid, pq["content"],
                     f"你的答案: {pq['user_answer']}，正确答案: {pq['correct_answer']}",
                     pq.get("solution", ""), "", "knowledge_gap"),
                )
                mistakes_created += 1
    db.commit()

    # Tasks auto-complete
    from services.practice_service import _auto_complete_tasks
    tasks_done = _auto_complete_tasks(db, pid)

    # Mastery recalc
    try:
        from services.mastery_service import calculate_mastery
        calculate_mastery(pid, mid)
    except:
        pass

    # Gacha
    p = get_player(pid)
    gacha = roll_gacha(pid, streak_bonus=p["streak_days"] >= 7)
    # Perfect bonus: extra gacha roll
    if accuracy == 1.0:
        gacha2 = roll_gacha(pid, streak_bonus=True)
        gacha = gacha2  # Use the better roll

    # Title based on performance
    if accuracy == 1.0:
        title = "完美讨伐"
        title_emoji = "🏆"
    elif accuracy >= 0.8:
        title = "讨伐成功"
        title_emoji = "🎉"
    elif accuracy >= 0.6:
        title = "勉强过关"
        title_emoji = "👍"
    else:
        title = "讨伐失败"
        title_emoji = "💪"

    return {
        "title": title,
        "title_emoji": title_emoji,
        "total": total,
        "correct": correct,
        "accuracy": accuracy,
        "max_combo": session["max_combo"],
        "crits": session["crits"],
        "xp_total": sum(pq["xp"] for pq in session["per_question"]),
        "gacha_result": gacha,
        "per_question": session["per_question"],
        "mistakes_created": mistakes_created,
        "tasks_auto_done": tasks_done,
    }


def _boss_name(module_name: str) -> str:
    """Generate a boss name from module name."""
    bosses = {
        "三角": "🐉 三角魔龙",
        "数列": "🔢 数列蛇妖",
        "概率": "🎲 概率幽灵",
        "立体": "📦 立方巨像",
        "解析": "📈 曲线魔兽",
        "导数": "📉 导数恶魔",
        "集合": "🔤 逻辑石像",
        "复数": "🧮 复数幻影",
    }
    for key, name in bosses.items():
        if key in module_name:
            return name
    return f"🐲 {module_name}之守卫"
