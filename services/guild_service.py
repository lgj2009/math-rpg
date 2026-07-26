"""Guild/community service — create, join, chat, feed, boss."""
import json
from datetime import date
from database import get_db


def create_guild(name: str, description: str, player_id: int, username: str) -> dict:
    db = get_db()
    existing = db.execute("SELECT id FROM guilds WHERE name=?", (name,)).fetchone()
    if existing:
        db.close(); return {"detail": "Guild name already taken"}
    # Check player not already in a guild
    in_guild = db.execute("SELECT guild_id FROM guild_members WHERE player_id=?", (player_id,)).fetchone()
    if in_guild:
        db.close(); return {"detail": "You are already in a guild"}
    cur = db.execute("INSERT INTO guilds (name, description, owner_id) VALUES (?,?,?)",
                     (name, description, player_id))
    gid = cur.lastrowid
    db.execute("INSERT INTO guild_members (guild_id, player_id, role) VALUES (?,?,?)",
               (gid, player_id, 'owner'))
    db.commit(); db.close()
    return get_guild(gid, player_id)


def join_guild(guild_id: int, player_id: int, username: str) -> dict:
    db = get_db()
    in_guild = db.execute("SELECT guild_id FROM guild_members WHERE player_id=?", (player_id,)).fetchone()
    if in_guild:
        db.close(); return {"detail": "Already in guild " + str(in_guild["guild_id"])}
    db.execute("INSERT INTO guild_members (guild_id, player_id) VALUES (?,?)", (guild_id, player_id))
    db.execute("UPDATE guilds SET member_count = member_count + 1 WHERE id=?", (guild_id,))
    # Log activity
    db.execute("INSERT INTO guild_activity (guild_id, player_id, username, action, detail) VALUES (?,?,?,?,?)",
               (guild_id, player_id, username, 'joined', ''))
    db.commit(); db.close()
    return get_guild(guild_id, player_id)


def leave_guild(guild_id: int, player_id: int):
    db = get_db()
    db.execute("DELETE FROM guild_members WHERE guild_id=? AND player_id=?", (guild_id, player_id))
    db.execute("UPDATE guilds SET member_count = MAX(0, member_count - 1) WHERE id=?", (guild_id,))
    db.commit(); db.close()


def post_message(guild_id: int, player_id: int, username: str, message: str) -> dict:
    db = get_db()
    db.execute("INSERT INTO guild_messages (guild_id, player_id, username, message) VALUES (?,?,?,?)",
               (guild_id, player_id, username, message[:500]))
    db.commit()
    # Return last 20 messages
    rows = db.execute(
        "SELECT * FROM guild_messages WHERE guild_id=? ORDER BY created_at DESC LIMIT 20",
        (guild_id,)).fetchall()
    db.close()
    return [dict(r) for r in reversed(rows)]


def get_messages(guild_id: int) -> list:
    db = get_db()
    rows = db.execute(
        "SELECT * FROM guild_messages WHERE guild_id=? ORDER BY created_at DESC LIMIT 50",
        (guild_id,)).fetchall()
    db.close()
    return [dict(r) for r in reversed(rows)]


def get_activity(guild_id: int) -> list:
    db = get_db()
    rows = db.execute(
        "SELECT * FROM guild_activity WHERE guild_id=? ORDER BY created_at DESC LIMIT 30",
        (guild_id,)).fetchall()
    db.close()
    return [dict(r) for r in rows]


def get_guild(guild_id: int, player_id: int = 0) -> dict:
    db = get_db()
    g = db.execute("SELECT * FROM guilds WHERE id=?", (guild_id,)).fetchone()
    if not g: db.close(); return {"detail": "Not found"}
    members = db.execute(
        "SELECT gm.*, p.username, p.level, p.title, p.xp FROM guild_members gm JOIN players p ON gm.player_id=p.id WHERE gm.guild_id=? ORDER BY gm.weekly_xp DESC",
        (guild_id,)).fetchall()
    is_member = any(m["player_id"] == player_id for m in members)
    db.close()
    return {
        **dict(g),
        "members": [dict(m) for m in members],
        "is_member": is_member,
        "is_owner": g["owner_id"] == player_id,
    }


def list_guilds() -> list:
    db = get_db()
    rows = db.execute("SELECT * FROM guilds ORDER BY weekly_xp DESC LIMIT 20").fetchall()
    db.close()
    return [dict(r) for r in rows]


def attack_guild_boss(guild_id: int, player_id: int, username: str, damage: int) -> dict:
    db = get_db()
    g = db.execute("SELECT * FROM guilds WHERE id=?", (guild_id,)).fetchone()
    if not g: db.close(); return {"detail": "Not found"}
    new_hp = max(0, g["boss_hp"] - damage)
    killed = new_hp == 0
    db.execute("UPDATE guilds SET boss_hp=? WHERE id=?", (new_hp, guild_id))
    # Log activity
    db.execute("INSERT INTO guild_activity (guild_id, player_id, username, action, detail, xp) VALUES (?,?,?,?,?,?)",
               (guild_id, player_id, username, 'boss_damage', f'Dealt {damage} damage', damage))
    if killed:
        db.execute("INSERT INTO guild_activity (guild_id, player_id, username, action, detail) VALUES (?,?,?,?,?)",
                   (guild_id, player_id, username, 'boss_kill', 'Slayed the guild boss!'))
        # Respawn with more HP
        new_max = g["boss_max_hp"] + 200
        db.execute("UPDATE guilds SET boss_hp=?, boss_max_hp=? WHERE id=?", (new_max, new_max, guild_id))
    db.commit(); db.close()
    return {"boss_hp": new_hp if not killed else new_max, "boss_max_hp": g["boss_max_hp"] if not killed else new_max,
            "killed": killed, "damage": damage}


def contribute_xp(guild_id: int, player_id: int, xp: int):
    db = get_db()
    db.execute("UPDATE guilds SET daily_xp=daily_xp+?, weekly_xp=weekly_xp+? WHERE id=?", (xp, xp, guild_id))
    db.execute("UPDATE guild_members SET weekly_xp=weekly_xp+? WHERE guild_id=? AND player_id=?", (xp, guild_id, player_id))
    db.commit(); db.close()
