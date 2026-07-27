import json
from datetime import datetime, date, timedelta
from database import get_db, get_db_ctx
import config


def create_player(username: str) -> dict:
    with get_db_ctx() as db:
        cur = db.execute("INSERT INTO players (username, last_login) VALUES (?, datetime('now'))", (username,))
        db.commit()
        pid = cur.lastrowid
        # Create module_mastery rows for all modules
        modules = db.execute("SELECT id FROM modules").fetchall()
        for m in modules:
            db.execute("INSERT OR IGNORE INTO module_mastery (player_id, module_id) VALUES (?, ?)", (pid, m["id"]))
        db.commit()
    return get_player(pid)


def get_player(player_id: int) -> dict:
    with get_db_ctx() as db:
        row = db.execute("SELECT * FROM players WHERE id=?", (player_id,)).fetchone()
        if not row:
            return None
        p = dict(row)
        p["owned_cosmetics"] = json.loads(p.get("owned_cosmetics", "[]"))
    _recalc_energy(p)
    return p


def _recalc_energy(p: dict) -> dict:
    """Apply passive regen since last refill timestamp.

    Updates both the in-memory dict AND the database, so callers can safely
    re-invoke this function without double-counting energy.
    """
    if not p.get("last_energy_refill"):
        return p
    try:
        last = datetime.fromisoformat(p["last_energy_refill"])
    except (ValueError, TypeError):
        return p
    elapsed = (datetime.now() - last).total_seconds()
    gained = int(elapsed / config.ENERGY_REGEN_SECONDS)
    if gained > 0:
        p["focus_energy"] = min(p["focus_max"], p["focus_energy"] + gained)
        now_str = datetime.now().isoformat()
        p["last_energy_refill"] = now_str  # sync dict with DB
        with get_db_ctx() as db:
            db.execute("UPDATE players SET focus_energy=?, last_energy_refill=? WHERE id=?",
                       (p["focus_energy"], now_str, p["id"]))
            db.commit()
    return p


def checkin(player_id: int) -> dict:
    with get_db_ctx() as db:
        today = date.today().isoformat()
        # Avoid duplicate
        existing = db.execute("SELECT id FROM checkins WHERE player_id=? AND checkin_date=?",
                              (player_id, today)).fetchone()
        if existing:
            return {"detail": "already checked in today"}

        db.execute("INSERT INTO checkins (player_id, checkin_date) VALUES (?, ?)", (player_id, today))

        p = get_player(player_id)
        yesterday = date.today() - timedelta(days=1)
        # Check if yesterday was checked in to continue streak
        yesterday_check = db.execute("SELECT id FROM checkins WHERE player_id=? AND checkin_date=?",
                                     (player_id, yesterday.isoformat())).fetchone()
        if yesterday_check:
            new_streak = p["streak_days"] + 1
        else:
            new_streak = 1

        # Apply streak bonuses
        multiplier = 1.0
        bonus = False
        if new_streak >= 7:
            multiplier = config.XP_STREAK_COMBO_MULTIPLIER.get(7, 2.0)
            bonus = True
        elif new_streak >= 3:
            multiplier = config.XP_STREAK_COMBO_MULTIPLIER.get(3, 1.5)
            bonus = True

        base_xp = 30
        xp_gained = int(base_xp * multiplier)

        # Weekly streak shield (Sunday)
        shields = p["streak_shields"]
        if date.today().weekday() == 6:  # Sunday
            shields = min(shields + 1, 3)

        db.execute("""UPDATE players SET streak_days=?, max_streak=MAX(max_streak,?),
                      xp=xp+?, streak_shields=?, last_login=datetime('now') WHERE id=?""",
                   (new_streak, new_streak, xp_gained, shields, player_id))
        db.commit()

    # Gacha roll on checkin (outside ctx — roll_gacha manages its own connection)
    from services.gacha_service import roll_gacha  # noqa: F811
    streak_bonus = new_streak >= 7
    gacha = roll_gacha(player_id, streak_bonus=streak_bonus)

    return {"streak_days": new_streak, "xp_gained": xp_gained, "bonus_applied": bonus, "gacha_result": gacha}


def claim_energy(player_id: int, hour: int) -> dict:
    if hour not in config.ENERGY_CLAIM_HOURS:
        return {"detail": "not a claim window"}
    p = get_player(player_id)
    new_energy = min(p["focus_max"], p["focus_energy"] + config.ENERGY_CLAIM_AMOUNT)
    with get_db_ctx() as db:
        db.execute("UPDATE players SET focus_energy=?, last_energy_refill=datetime('now') WHERE id=?",
                   (new_energy, player_id))
        db.commit()
    return {"focus_energy": new_energy, "claimed": config.ENERGY_CLAIM_AMOUNT}


def spend_energy(player_id: int, amount: int) -> bool:
    p = get_player(player_id)  # get_player already calls _recalc_energy internally
    if p["focus_energy"] < amount:
        return False
    with get_db_ctx() as db:
        db.execute("UPDATE players SET focus_energy=focus_energy-?, last_energy_refill=datetime('now') WHERE id=?",
                   (amount, player_id))
        db.commit()
    return True


def award_xp(player_id: int, amount: int):
    p = get_player(player_id)
    new_xp = p["xp"] + amount
    # Determine new level
    new_level = p["level"]
    for lvl, threshold in sorted(config.LEVEL_THRESHOLDS.items(), reverse=True):
        if new_xp >= threshold:
            new_level = lvl
            break
    new_title = config.TITLES.get(new_level, p["title"])
    with get_db_ctx() as db:
        db.execute("UPDATE players SET xp=?, level=?, title=? WHERE id=?",
                   (new_xp, new_level, new_title, player_id))
        db.commit()
    return {"xp": new_xp, "level": new_level, "title": new_title, "leveled_up": new_level > p["level"]}
