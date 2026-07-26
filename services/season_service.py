"""Season pass — tiered rewards with free/premium tracks."""
import json
from datetime import date, datetime
from database import get_db

SEASON_REWARDS = [
    # tier: free_reward, premium_reward
    {"tier": 1,  "xp": 100,   "free": {"name": "100 金币", "icon": "🪙"}, "premium": {"name": "铁剑头像框", "icon": "⚔️"}},
    {"tier": 2,  "xp": 250,   "free": {"name": "连击护盾", "icon": "🛡️"}, "premium": {"name": "蓝色称号", "icon": "🔷"}},
    {"tier": 3,  "xp": 500,   "free": {"name": "200 金币", "icon": "🪙"}, "premium": {"name": "闪电特效", "icon": "⚡"}},
    {"tier": 4,  "xp": 800,   "free": {"name": "翻牌券×1", "icon": "🎴"}, "premium": {"name": "紫色称号", "icon": "💜"}},
    {"tier": 5,  "xp": 1200,  "free": {"name": "300 金币", "icon": "🪙"}, "premium": {"name": "秘银头像框", "icon": "🔮"}},
    {"tier": 6,  "xp": 1600,  "free": {"name": "翻牌券×2", "icon": "🎴"}, "premium": {"name": "星光披风", "icon": "🌌"}},
    {"tier": 7,  "xp": 2000,  "free": {"name": "500 金币", "icon": "🪙"}, "premium": {"name": "金色称号", "icon": "👑"}},
    {"tier": 8,  "xp": 2500,  "free": {"name": "翻牌券×3", "icon": "🎴"}, "premium": {"name": "龙翼披风", "icon": "🐉"}},
    {"tier": 9,  "xp": 3000,  "free": {"name": "传奇翻牌×1", "icon": "🎴"}, "premium": {"name": "彩虹称号", "icon": "🌈"}},
    {"tier": 10, "xp": 4000,  "free": {"name": "1000 金币", "icon": "🪙"}, "premium": {"name": "虚空披风", "icon": "🌀"}},
]


def get_current_season(player_id: int = 0) -> dict:
    """Return current season with player progress."""
    db = get_db()
    now = date.today().isoformat()
    season = db.execute(
        "SELECT * FROM seasons WHERE start_date <= ? AND end_date >= ? AND active=1 ORDER BY id DESC LIMIT 1",
        (now, now),
    ).fetchone()

    if not season:
        # Create a default season
        from datetime import timedelta
        start = date.today().isoformat()
        end = (date.today() + timedelta(days=60)).isoformat()
        db.execute("INSERT INTO seasons (name, start_date, end_date, reward_tiers, active) VALUES (?,?,?,?,?)",
                   ("第1赛季: 函数觉醒", start, end, json.dumps(SEASON_REWARDS), 1))
        db.commit()
        season = db.execute("SELECT * FROM seasons WHERE id=?", (db.execute("SELECT last_insert_rowid()").fetchone()[0],)).fetchone()

    season = dict(season)
    season["reward_tiers"] = json.loads(season["reward_tiers"]) if isinstance(season["reward_tiers"], str) else SEASON_REWARDS

    # Player progress
    player_xp = 0
    if player_id > 0:
        p = db.execute("SELECT season_xp, battle_pass_tier FROM players WHERE id=?", (player_id,)).fetchone()
        if p:
            player_xp = p["season_xp"] or 0
            season["battle_pass_tier"] = p["battle_pass_tier"] or 0

    # Find current tier
    current_tier = 0
    for tier in season["reward_tiers"]:
        if player_xp >= tier["xp"]:
            current_tier = tier["tier"]

    # Days remaining
    try:
        end_date = datetime.strptime(season["end_date"], "%Y-%m-%d")
        days_left = max(0, (end_date.date() - date.today()).days)
    except:
        days_left = 30

    db.close()

    tiers_with_status = []
    for t in season["reward_tiers"]:
        tiers_with_status.append({
            **t,
            "unlocked": player_xp >= t["xp"],
            "claimed": t["tier"] <= season.get("battle_pass_tier", 0),
        })

    return {
        "id": season["id"],
        "name": season["name"],
        "start_date": season["start_date"],
        "end_date": season["end_date"],
        "days_left": days_left,
        "player_xp": player_xp,
        "current_tier": current_tier,
        "total_tiers": len(season["reward_tiers"]),
        "tiers": tiers_with_status,
        "next_tier_xp": season["reward_tiers"][current_tier]["xp"] if current_tier < len(season["reward_tiers"]) else None,
    }


def add_season_xp(player_id: int, amount: int):
    """Add XP to player's season progress."""
    db = get_db()
    db.execute("UPDATE players SET season_xp = season_xp + ? WHERE id=?", (amount, player_id))
    db.commit()
    db.close()


def claim_tier(player_id: int, tier: int) -> dict:
    """Claim a season tier reward. Returns the reward or error."""
    db = get_db()
    p = db.execute("SELECT season_xp, battle_pass_tier FROM players WHERE id=?", (player_id,)).fetchone()
    if not p: db.close(); return {"detail": "Player not found"}

    if p["battle_pass_tier"] and p["battle_pass_tier"] >= tier:
        db.close(); return {"detail": "Already claimed"}

    season = get_current_season(player_id)
    target = None
    for t in season["tiers"]:
        if t["tier"] == tier:
            target = t; break
    if not target or not target["unlocked"]:
        db.close(); return {"detail": "Tier not unlocked yet"}

    db.execute("UPDATE players SET battle_pass_tier = ? WHERE id=?", (tier, player_id))
    db.commit(); db.close()

    return {"ok": True, "reward": target["free"], "premium_reward": target["premium"]}
