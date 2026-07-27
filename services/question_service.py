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

    # Smooth difficulty: gradual mix instead of hard jump
    target_difficulty = 1
    difficulty_mix = 0  # 0=all d1, 1=all d2, 2=all d3
    if mastery:
        acc = mastery["accuracy_avg"]
        if acc >= 0.90 and mastery["status"] in ("practicing", "mastered"):
            target_difficulty = 3; difficulty_mix = 2
        elif acc >= 0.80:
            target_difficulty = 2; difficulty_mix = 1
        elif acc >= 0.65:
            target_difficulty = 2; difficulty_mix = 0.5  # mix d1 and d2

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
    # Use difficulty mix for smooth progression
    all_rows = db.execute(
        """
        SELECT id, module_id, type, difficulty, content, content_en, content_vi,
               options, options_en, options_vi, answer, answer_en, answer_vi,
               solution, solution_en, solution_vi, time_limit_sec, source_type, source_ref
        FROM questions
        WHERE module_id = ? AND difficulty <= ?
        """,
        (module_id, target_difficulty),
    ).fetchall()

    # Split by difficulty for smooth mixing
    d1_rows = [r for r in all_rows if r["difficulty"] <= 1]
    d2_rows = [r for r in all_rows if r["difficulty"] == 2]
    d3_rows = [r for r in all_rows if r["difficulty"] == 3]
    random.shuffle(d1_rows); random.shuffle(d2_rows); random.shuffle(d3_rows)

    # Mix based on difficulty_mix ratio
    if difficulty_mix == 0:
        all_rows = d1_rows
    elif difficulty_mix == 0.5:
        # 50% d1, 50% d2
        take_d2 = min(len(d2_rows), count // 2)
        all_rows = d1_rows + d2_rows[:take_d2]
    elif difficulty_mix == 1:
        # 20% d1, 80% d2
        take_d1 = min(len(d1_rows), max(2, count // 5))
        all_rows = d1_rows[:take_d1] + d2_rows
    elif difficulty_mix == 2:
        # 30% d2, 70% d3
        take_d2 = min(len(d2_rows), max(3, count * 3 // 10))
        all_rows = d2_rows[:take_d2] + d3_rows

    # Split into unanswered and answered pools
    unanswered = []
    answered = []
    for r in all_rows:
        if r["id"] in answered_set:
            answered.append(r)
        else:
            unanswered.append(r)

    # Shuffle aggressively with multiple passes for true randomness
    for _ in range(3):
        random.shuffle(unanswered)
        random.shuffle(answered)

    # If unanswered pool is big enough, ONLY use unanswered (no recycling)
    if len(unanswered) >= count:
        rows = unanswered[:count]
    else:
        # Fill gaps with answered questions
        rows = unanswered[:]
        needed = count - len(rows)
        rows.extend(answered[:needed])

    # Final shuffle + dedup
    random.shuffle(rows)
    seen = set()
    unique = []
    for r in rows:
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
