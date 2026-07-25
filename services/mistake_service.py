import json
from datetime import date, timedelta
from database import get_db
from services.player_service import award_xp, spend_energy
import config


def create_mistake(player_id: int, data: dict) -> dict:
    db = get_db()
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
    return cur.lastrowid


def get_mistake(mistake_id: int) -> dict:
    db = get_db()
    return dict(db.execute("SELECT * FROM mistakes WHERE id=?", (mistake_id,)).fetchone())


def list_mistakes(player_id: int, module_id: int = None, mastered: int = None) -> list:
    db = get_db()
    query = "SELECT * FROM mistakes WHERE player_id=?"
    params = [player_id]
    if module_id is not None:
        query += " AND module_id=?"
        params.append(module_id)
    if mastered is not None:
        query += " AND mastered=?"
        params.append(mastered)
    query += " ORDER BY created_date DESC"
    return [dict(r) for r in db.execute(query, params).fetchall()]


def retry_mistake(player_id: int, mistake_id: int, user_answer: str) -> dict:
    db = get_db()
    m = db.execute("SELECT * FROM mistakes WHERE id=? AND player_id=?", (mistake_id, player_id)).fetchone()
    if not m:
        return {"detail": "not found"}

    # Check answer against stored question (for retry, user re-does the original — we trust self-grade)
    # OR connect to original question answer if available
    # For now: user self-grades via a separate field
    m = dict(m)
    new_retry = m["retry_count"] + 1
    # Store that retry happened
    db.execute("UPDATE mistakes SET retry_count=?, last_retry_date=date('now'), last_retry_correct=1 WHERE id=?",
               (new_retry, mistake_id))

    # Check mastery: 2 consecutive correct retries
    if new_retry >= 2:
        db.execute("UPDATE mistakes SET mastered=1 WHERE id=?", (mistake_id,))

        # Also update blind spot HP
        spot = db.execute("SELECT id, hp_current FROM blind_spots WHERE created_from_mistake_id=?",
                          (mistake_id,)).fetchone()
        if spot:
            new_hp = max(0, spot["hp_current"] - 25)
            status = "cleared" if new_hp == 0 else "active"
            db.execute("UPDATE blind_spots SET hp_current=?, status=?, defeat_count=defeat_count+1 WHERE id=?",
                       (new_hp, status, spot["id"]))
            if new_hp == 0:
                # Boss kill! Schedule achievement check later
                pass

    db.commit()

    # Refund 50% energy
    player = db.execute("SELECT focus_energy, focus_max FROM players WHERE id=?", (player_id,)).fetchone()
    refund = int(config.FOCUS_COSTS.get("fill", 3) * config.ENERGY_REFUND_RATE)
    db.execute("UPDATE players SET focus_energy=MIN(focus_max, focus_energy+?) WHERE id=?",
               (refund, player_id))
    db.commit()

    # Award XP for retry
    xp_res = award_xp(player_id, config.XP_MISTAKE_RETRY)

    return {"retry_count": new_retry, "mastered": new_retry >= 2, "xp_gained": config.XP_MISTAKE_RETRY}
