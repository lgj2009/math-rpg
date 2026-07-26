import json
import uuid
import random
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

    # --- Fetch ALL available questions matching difficulty ---
    all_rows = db.execute(
        """
        SELECT id, module_id, type, difficulty, content, content_en, content_vi,
               options, options_en, options_vi, answer, answer_en, answer_vi,
               solution, solution_en, solution_vi, time_limit_sec, source_type, source_ref
        FROM questions
        WHERE module_id = ? AND difficulty <= ?
        ORDER BY RANDOM()
        """,
        (module_id, target_difficulty),
    ).fetchall()

    # Split into unanswered and answered pools
    unanswered = []
    answered = []
    for r in all_rows:
        if r["id"] in answered_set:
            answered.append(r)
        else:
            unanswered.append(r)

    # Build result: prefer unanswered, fill with answered if needed
    random.shuffle(unanswered)
    random.shuffle(answered)
    result = unanswered[:count]
    if len(result) < count:
        result.extend(answered[:count - len(result)])

    # Deduplicate by ID (safety net)
    seen = set()
    unique = []
    for r in result:
        if r["id"] not in seen:
            seen.add(r["id"])
            unique.append(r)
    rows = unique[:count]

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
