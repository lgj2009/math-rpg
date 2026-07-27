import json
from datetime import date, timedelta
from database import get_db_ctx
from services.player_service import award_xp, spend_energy
from services.blind_spot_service import schedule_rounds
import config


def create_mistake(player_id: int, data: dict) -> dict:
    with get_db_ctx() as db:
        cur = db.execute(
            """INSERT INTO mistakes (player_id, module_id, question, wrong_step, correct_thought, knowledge_point, error_type)
               VALUES (?,?,?,?,?,?,?)""",
            (player_id, data["module_id"], data["question"], data.get("wrong_step", ""),
             data.get("correct_thought", ""), data.get("knowledge_point", ""), data.get("error_type", "knowledge_gap"))
        )
        mid = cur.lastrowid
        db.commit()

        # Auto-create blind spot if name provided
        if data.get("blind_spot_name"):
            _ensure_blind_spot(db, player_id, data["blind_spot_name"], data["module_id"], mid)

    return get_mistake(mid)


def _ensure_blind_spot(db, player_id, name, module_id, mistake_id):
    """Create or extend a blind spot. `db` is an open connection from the caller."""
    existing = db.execute("SELECT id FROM blind_spots WHERE player_id=? AND name=?",
                          (player_id, name)).fetchone()
    if existing:
        # Extend module_ids
        spot = db.execute("SELECT module_ids FROM blind_spots WHERE id=?", (existing["id"],)).fetchone()
        mods = json.loads(spot["module_ids"])
        if module_id not in mods:
            mods.append(module_id)
            db.execute("UPDATE blind_spots SET module_ids=? WHERE id=?", (json.dumps(mods), existing["id"]))
        db.commit()
        return existing["id"]

    cur = db.execute(
        "INSERT INTO blind_spots (player_id, name, module_ids, created_from_mistake_id) VALUES (?,?,?,?)",
        (player_id, name, json.dumps([module_id]), mistake_id)
    )
    db.commit()
    # Schedule the 4 rounds for the newly created blind spot
    schedule_rounds(cur.lastrowid)
    return cur.lastrowid


def get_mistake(mistake_id: int) -> dict:
    with get_db_ctx() as db:
        row = db.execute("SELECT * FROM mistakes WHERE id=?", (mistake_id,)).fetchone()
    return dict(row)


def list_mistakes(player_id: int, module_id: int = None, mastered: int = None) -> list:
    with get_db_ctx() as db:
        query = "SELECT * FROM mistakes WHERE player_id=?"
        params = [player_id]
        if module_id is not None:
            query += " AND module_id=?"
            params.append(module_id)
        if mastered is not None:
            query += " AND mastered=?"
            params.append(mastered)
        query += " ORDER BY created_date DESC"
        rows = db.execute(query, params).fetchall()
    return [dict(r) for r in rows]


def retry_mistake(player_id: int, mistake_id: int, user_answer: str) -> dict:
    with get_db_ctx() as db:
        m = db.execute("SELECT * FROM mistakes WHERE id=? AND player_id=?", (mistake_id, player_id)).fetchone()
        if not m:
            return {"detail": "not found"}
        m = dict(m)

        # Try to find the correct answer by matching question text in questions table
        is_correct = None  # None = can't determine, trust self-grade later
        qrow = db.execute("SELECT answer FROM questions WHERE content=? LIMIT 1", (m["question"],)).fetchone()
        if qrow:
            is_correct = str(user_answer).strip() == str(qrow["answer"]).strip()

        new_retry = m["retry_count"] + 1
        db.execute("UPDATE mistakes SET retry_count=?, last_retry_date=date('now'), last_retry_correct=? WHERE id=?",
                   (new_retry, 1 if is_correct else 0, mistake_id))

        # Check mastery: requires current retry correct AND previous retry was also correct
        # (two consecutive correct answers to clear the mistake)
        is_mastered = is_correct and m["last_retry_correct"] == 1
        if is_mastered:
            db.execute("UPDATE mistakes SET mastered=1 WHERE id=?", (mistake_id,))

            # Also update blind spot HP (each mastered mistake deals damage to the boss)
            spot = db.execute("SELECT id, hp_current FROM blind_spots WHERE created_from_mistake_id=?",
                              (mistake_id,)).fetchone()
            if spot:
                new_hp = max(0, spot["hp_current"] - 25)
                status = "cleared" if new_hp == 0 else "active"
                db.execute("UPDATE blind_spots SET hp_current=?, status=?, defeat_count=defeat_count+1 WHERE id=?",
                           (new_hp, status, spot["id"]))

        # Refund 50% energy on retry
        player = db.execute("SELECT focus_energy, focus_max FROM players WHERE id=?", (player_id,)).fetchone()
        refund = int(config.FOCUS_COSTS.get("fill", 3) * config.ENERGY_REFUND_RATE)
        db.execute("UPDATE players SET focus_energy=MIN(focus_max, focus_energy+?) WHERE id=?",
                   (refund, player_id))
        db.commit()

    # Award XP for retry (more if correct, small participation XP otherwise)
    xp_gained = config.XP_MISTAKE_RETRY if is_correct else 10
    award_xp(player_id, xp_gained)

    return {
        "retry_count": new_retry,
        "mastered": is_mastered,
        "is_correct": is_correct,
        "xp_gained": xp_gained
    }
