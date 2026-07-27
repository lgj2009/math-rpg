import random
import json
from database import get_db_ctx
import config

COSMETIC_POOL = {
    "common": [
        {"name": "木剑头像框", "type": "avatar_frame", "emoji": "⚪"},
        {"name": "绿色称号", "type": "title_color", "emoji": "🟢"},
        {"name": "新手光环", "type": "effect", "emoji": "✨"},
        {"name": "白色披风", "type": "cape", "emoji": "🤍"},
    ],
    "rare": [
        {"name": "铁剑头像框", "type": "avatar_frame", "emoji": "🔵"},
        {"name": "蓝色称号", "type": "title_color", "emoji": "🔷"},
        {"name": "闪电特效", "type": "effect", "emoji": "⚡"},
        {"name": "蓝色披风", "type": "cape", "emoji": "💙"},
    ],
    "epic": [
        {"name": "秘银头像框", "type": "avatar_frame", "emoji": "🟣"},
        {"name": "紫色称号", "type": "title_color", "emoji": "💜"},
        {"name": "暗焰特效", "type": "effect", "emoji": "🔥"},
        {"name": "星光披风", "type": "cape", "emoji": "🌌"},
    ],
    "legendary": [
        {"name": "金色头像框", "type": "avatar_frame", "emoji": "🟡"},
        {"name": "金色称号", "type": "title_color", "emoji": "👑"},
        {"name": "雷神特效", "type": "effect", "emoji": "⚡"},
        {"name": "龙翼披风", "type": "cape", "emoji": "🐉"},
    ],
    "mythic": [
        {"name": "彩虹头像框", "type": "avatar_frame", "emoji": "🌈"},
        {"name": "彩虹称号", "type": "title_color", "emoji": "💎"},
        {"name": "星辰爆发", "type": "effect", "emoji": "💫"},
        {"name": "虚空披风", "type": "cape", "emoji": "🌀"},
    ],
}


def _validate_odds(odds: dict) -> dict:
    """Ensure probability odds sum to 1.0. Normalize if they don't."""
    total = sum(odds.values())
    if abs(total - 1.0) < 0.001:
        return odds
    # Normalize to 1.0
    import sys
    print(f"[gacha] Warning: odds sum to {total:.4f}, normalizing to 1.0", file=sys.stderr)
    return {k: v / total for k, v in odds.items()}


def roll_gacha(player_id: int, streak_bonus: bool = False) -> dict:
    odds = dict(config.GACHA_ODDS)
    if streak_bonus:
        # Shift legendary probability, reduce common
        odds["legendary"] = odds.get("legendary", 0.015) + config.GACHA_STREAK_BONUS
        odds["common"] = max(0, odds.get("common", 0.70) - config.GACHA_STREAK_BONUS)

    # Validate and normalize if needed
    odds = _validate_odds(odds)

    roll = random.random()
    cumulative = 0
    result_rarity = "common"
    for rarity, prob in odds.items():
        cumulative += prob
        if roll <= cumulative:
            result_rarity = rarity
            break

    item = random.choice(COSMETIC_POOL[result_rarity])

    # Grant to player
    with get_db_ctx() as db:
        row = db.execute("SELECT owned_cosmetics FROM players WHERE id=?", (player_id,)).fetchone()
        owned = json.loads(row["owned_cosmetics"]) if row else []
        owned.append(item["name"])
        db.execute("UPDATE players SET owned_cosmetics=? WHERE id=?", (json.dumps(owned), player_id))

        # Log drop for broadcast
        db.execute("INSERT INTO cosmetic_drops_log (player_id, item_rarity, item_name) VALUES (?,?,?)",
                   (player_id, result_rarity, item["name"]))
        db.commit()

    return {
        "rarity": result_rarity,
        "item_name": item["name"],
        "item_type": item["type"],
        "animation_class": f"gacha-{result_rarity}",
    }
