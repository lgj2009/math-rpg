import json
from database import get_db
from services.player_service import spend_energy, award_xp, get_player
from services.gacha_service import roll_gacha
from services.question_service import get_questions_for_module, generate_session_id
import config

# In-memory session store: session_id -> {focus_cost, ...}
# Populated by start_practice, consumed by submit_practice.
_sessions: dict[str, dict] = {}


def start_practice(player_id: int, module_id: int, count: int = 10) -> dict | None:
    """Prepare a practice session for *player_id* on *module_id*.

    Returns a session dict (including chosen questions and focus cost)
    or *None* when the module has no questions available.
    """
    questions = get_questions_for_module(module_id, player_id, count)
    if not questions:
        return None

    session_id = generate_session_id()
    cost = sum(config.FOCUS_COSTS.get(q["type"], 2) for q in questions)

    db = get_db()
    mod = db.execute("SELECT name FROM modules WHERE id=?", (module_id,)).fetchone()

    # Cache session metadata for submit_practice to consume
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
    """Grade submitted answers, deduct energy, award XP, and roll gacha."""
    db = get_db()

    # Fetch correct answers for each question
    question_ids = [a["question_id"] for a in answers]
    placeholders = ",".join("?" * len(question_ids))
    rows = db.execute(
        f"SELECT id, answer FROM questions WHERE id IN ({placeholders})",
        question_ids,
    ).fetchall()
    answer_map = {r["id"]: r["answer"] for r in rows}

    # Grade
    total = len(answers)
    correct_count = 0
    for a in answers:
        if str(a["answer"]).strip() == str(answer_map.get(a["question_id"], "")).strip():
            correct_count += 1

    accuracy = correct_count / total if total > 0 else 0

    # Record practice in history (includes session_id + answered question IDs)
    db.execute(
        """INSERT INTO practice_records
               (player_id, module_id, total_questions, correct_count,
                time_used_sec, session_id, answered_question_ids)
           VALUES (?,?,?,?,?,?,?)""",
        (
            player_id,
            module_id,
            total,
            correct_count,
            time_used_sec,
            session_id,
            json.dumps(question_ids),
        ),
    )
    db.commit()

    # Spend energy (use focus_cost cached from start_practice)
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

    return {
        "total": total,
        "correct": correct_count,
        "accuracy": round(accuracy, 4),
        "xp_gained": base_xp,
        "near_miss": near_miss,
        "gacha_result": gacha,
    }
