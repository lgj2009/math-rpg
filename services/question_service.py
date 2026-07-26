import json
import uuid
from database import get_db


def get_questions_for_module(module_id: int, player_id: int, count: int = 10, lang: str = "zh") -> list:
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

    # Difficulty lock: only increase if accuracy >= 80%
    target_difficulty = 1
    if mastery:
        if mastery["accuracy_avg"] >= 0.80:
            target_difficulty = 2
        if mastery["accuracy_avg"] >= 0.90 and mastery["status"] in ("practicing", "mastered"):
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
    rows = None
    if answered_set:
        placeholders = ",".join("?" * len(answered_set))
        rows = db.execute(
            f"""
            SELECT id, module_id, type, difficulty, content, content_en, content_vi,
                   options, options_en, options_vi, answer, answer_en, answer_vi,
                   solution, solution_en, solution_vi, time_limit_sec, source_type, source_ref
            FROM questions
            WHERE module_id = ? AND id NOT IN ({placeholders})
            AND difficulty <= ?
            ORDER BY RANDOM()
            LIMIT ?
            """,
            (module_id, *list(answered_set), target_difficulty, count),
        )
        fetched = rows.fetchall()
        # If too few available, fall back to ignoring answered filter
        if len(fetched) < min(3, count):
            rows = None  # trigger fallback below
        else:
            rows = fetched

    if rows is None:
        rows = db.execute(
            """
            SELECT id, module_id, type, difficulty, content, content_en, content_vi,
                   options, options_en, options_vi, answer, answer_en, answer_vi,
                   solution, solution_en, solution_vi, time_limit_sec, source_type, source_ref
            FROM questions
            WHERE module_id = ? AND difficulty <= ?
            ORDER BY RANDOM()
            LIMIT ?
            """,
            (module_id, target_difficulty, count),
        ).fetchall()

    # Select translated columns
    content_col = f"content_{lang}" if lang != "zh" else "content"
    options_col = f"options_{lang}" if lang != "zh" else "options"
    answer_col = f"answer_{lang}" if lang != "zh" else "answer"
    solution_col = f"solution_{lang}" if lang != "zh" else "solution"

    questions = []
    for r in rows:
        q = dict(r)
        # Use translated content if available, fall back to Chinese
        if lang != "zh":
            q["content"] = r[content_col] or r["content"]
            raw_opts = r[options_col] or r["options"]
            q["answer"] = r[answer_col] or r["answer"]
            q["solution"] = r[solution_col] or r["solution"]
        else:
            raw_opts = q.get("options")

        if raw_opts:
            try:
                q["options"] = json.loads(raw_opts)
            except (json.JSONDecodeError, TypeError):
                raw = str(raw_opts)
                if raw.startswith('[') and raw.endswith(']'):
                    import re
                    parts = re.findall(r'"([^"]*)"', raw)
                    q["options"] = parts if parts else [raw]
                else:
                    q["options"] = [raw]
        else:
            q["options"] = None
        questions.append(q)
    return questions


def generate_session_id() -> str:
    return uuid.uuid4().hex[:12]
