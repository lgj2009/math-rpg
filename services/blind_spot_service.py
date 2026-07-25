import json
from datetime import date, timedelta
from database import get_db
from services.player_service import award_xp, spend_energy
import config


def list_blind_spots(player_id: int) -> list:
    db = get_db()
    rows = db.execute(
        "SELECT * FROM blind_spots WHERE player_id=? AND status='active'",
        (player_id,)
    ).fetchall()
    result = []
    for r in rows:
        d = dict(r)
        d["module_ids"] = json.loads(d["module_ids"])
        result.append(d)
    return result


def get_due_today(player_id: int) -> list:
    db = get_db()
    today = date.today().isoformat()
    rows = db.execute("""
        SELECT bsr.*, bs.name as spot_name, bs.hp_current, bs.status as spot_status
        FROM blind_spot_rounds bsr
        JOIN blind_spots bs ON bsr.blind_spot_id = bs.id
        WHERE bs.player_id=? AND bsr.scheduled_date=? AND bsr.result='pending'
    """, (player_id, today)).fetchall()
    return [dict(r) for r in rows]


def schedule_rounds(blind_spot_id: int):
    """Schedule 4 rounds: day 0 (today), day 2, day 7, day 21"""
    db = get_db()
    spot = db.execute("SELECT * FROM blind_spots WHERE id=?", (blind_spot_id,)).fetchone()
    if not spot:
        return

    today = date.today()
    intervals = [0, 2, 7, 21]
    for round_num, offset in enumerate(intervals, 1):
        sched_date = (today + timedelta(days=offset)).isoformat()
        # Reuse original question text from the mistake for round 1
        mistake = db.execute("SELECT question FROM mistakes WHERE id=?",
                             (spot["created_from_mistake_id"],)).fetchone()
        q_text = mistake["question"] if mistake else spot["name"]
        db.execute(
            """INSERT OR IGNORE INTO blind_spot_rounds
               (blind_spot_id, round, question, question_type, scheduled_date)
               VALUES (?,?,?,?,?)""",
            (blind_spot_id, round_num, q_text,
             "original" if round_num == 1 else "variant", sched_date)
        )
    db.commit()


def attack_blind_spot(player_id: int, blind_spot_id: int, answer: str, round_number: int) -> dict:
    db = get_db()
    spot = db.execute(
        "SELECT * FROM blind_spots WHERE id=? AND player_id=?",
        (blind_spot_id, player_id)
    ).fetchone()
    if not spot:
        return {"detail": "not found"}

    # Find the pending round
    round_row = db.execute(
        """SELECT * FROM blind_spot_rounds
           WHERE blind_spot_id=? AND round=? AND result='pending'""",
        (blind_spot_id, round_number)
    ).fetchone()
    if not round_row:
        return {"detail": "round not pending or not found"}

    # For MVP: self-graded — assume correct
    correct = True

    # Spend energy for boss fight
    has_energy = spend_energy(player_id, config.FOCUS_COSTS.get("boss_fight", 40))
    if not has_energy:
        return {"detail": "not enough focus energy"}

    damage = 25 if correct else 0
    new_hp = max(0, spot["hp_current"] - damage)
    boss_killed = new_hp == 0

    db.execute(
        "UPDATE blind_spot_rounds SET result=?, answered_date=date('now') WHERE id=?",
        ("correct" if correct else "wrong", round_row["id"])
    )
    db.execute(
        """UPDATE blind_spots
           SET hp_current=?, status=?, defeat_count=defeat_count+?
           WHERE id=?""",
        (new_hp, "cleared" if boss_killed else "active", 1 if correct else 0, blind_spot_id)
    )
    db.commit()

    # Award XP — 80 for correct answer
    xp_res = award_xp(player_id, 80 if correct else 0)

    if boss_killed:
        return {
            "damage": damage, "hp_remaining": 0, "boss_killed": True,
            "xp_gained": 80
        }

    return {
        "damage": damage,
        "hp_remaining": new_hp,
        "boss_killed": False,
        "xp_gained": 80 if correct else 0
    }
