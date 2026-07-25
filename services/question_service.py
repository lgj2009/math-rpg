import json
import uuid
from database import get_db


def get_questions_for_module(module_id: int, player_id: int, count: int = 10) -> list:
    """Return questions matched to the player's difficulty level.

    Excludes questions the player has already answered in any past practice
    session. Uses the player's module mastery accuracy to pick appropriately
    challenging questions.
    """
    db = get_db()

    # --- Determine target difficulty from module mastery ---
    mastery = db.execute(
        "SELECT accuracy_avg, status FROM module_mastery WHERE player_id=? AND module_id=?",
        (player_id, module_id),
    ).fetchone()

    target_difficulty = 1
    if mastery:
        if mastery["accuracy_avg"] >= 0.80:
            target_difficulty = 2
        if mastery["accuracy_avg"] >= 0.90 and mastery["status"] == "practicing":
            target_difficulty = 3

    # --- Collect IDs of questions the player has already answered ---
    answered_rows = db.execute(
        "SELECT answered_question_ids FROM practice_records "
        "WHERE player_id=? AND module_id=? AND answered_question_ids IS NOT NULL",
        (player_id, module_id),
    ).fetchall()

    answered_set: set[int] = set()
    for row in answered_rows:
        try:
            ids = json.loads(row["answered_question_ids"])
            if isinstance(ids, list):
                answered_set.update(int(qid) for qid in ids)
        except (json.JSONDecodeError, TypeError, ValueError):
            pass

    # --- Fetch questions excluding already-answered ones ---
    if answered_set:
        placeholders = ",".join("?" * len(answered_set))
        rows = db.execute(
            f"""
            SELECT id, module_id, type, difficulty, content, options, time_limit_sec
            FROM questions
            WHERE module_id = ? AND id NOT IN ({placeholders})
            ORDER BY ABS(difficulty - ?), RANDOM()
            LIMIT ?
            """,
            (module_id, *list(answered_set), target_difficulty, count),
        )
    else:
        rows = db.execute(
            """
            SELECT id, module_id, type, difficulty, content, options, time_limit_sec
            FROM questions
            WHERE module_id = ?
            ORDER BY ABS(difficulty - ?), RANDOM()
            LIMIT ?
            """,
            (module_id, target_difficulty, count),
        )

    questions = []
    for r in rows.fetchall():
        q = dict(r)
        q["options"] = json.loads(q["options"]) if q.get("options") else None
        questions.append(q)
    return questions


def generate_session_id() -> str:
    return uuid.uuid4().hex[:12]
