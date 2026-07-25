import json
import uuid
from database import get_db


def get_questions_for_module(module_id: int, player_id: int, count: int = 10) -> list:
    """Return questions matched to the player's difficulty level.

    Uses the player's module mastery accuracy to pick appropriately
    challenging questions. When the questions table is empty (seeding
    happens in Task 9) an empty list is returned — callers handle it.
    """
    db = get_db()

    # Determine target difficulty from module mastery
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

    # Fetch questions for this module, ordered by how close their
    # difficulty is to the target, then randomized within that band.
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
