"""User authentication — register, login, logout, session validation."""
import hashlib, secrets, uuid
from datetime import datetime, timedelta
from database import get_db
from services.player_service import create_player, get_player


def _hash(password: str) -> str:
    salt = "math-rpg-salt-v1"
    return hashlib.sha256(f"{salt}:{password}".encode()).hexdigest()


def _make_token() -> str:
    return secrets.token_hex(32)


def register(email: str, username: str, password: str) -> dict:
    """Register a new user, create their player, return session."""
    db = get_db()
    existing = db.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
    if existing:
        return {"detail": "Email already registered"}

    pw_hash = _hash(password)
    cur = db.execute("INSERT INTO users (email, username, password_hash) VALUES (?,?,?)",
                     (email, username, pw_hash))
    user_id = cur.lastrowid
    db.commit()
    db.close()

    # Create a player for this user (player_service manages its own connections)
    player = create_player(username)
    player_id = player["id"]

    # Create session
    db2 = get_db()
    token = _make_token()
    expires = (datetime.utcnow() + timedelta(days=30)).isoformat()
    db2.execute("INSERT INTO sessions (token, user_id, player_id, expires_at) VALUES (?,?,?,?)",
               (token, user_id, player_id, expires))
    db2.commit()
    db2.close()

    return {
        "token": token,
        "user_id": user_id,
        "player_id": player_id,
        "username": username,
        "email": email,
        "player": player,
    }


def login(email: str, password: str) -> dict:
    """Login with email + password, return session."""
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    if not user or user["password_hash"] != _hash(password):
        return {"detail": "Invalid email or password"}

    user_id = user["id"]
    # Find existing player
    player_row = db.execute("SELECT player_id FROM sessions WHERE user_id=? ORDER BY expires_at DESC LIMIT 1",
                            (user_id,)).fetchone()
    db.close()

    if not player_row:
        player = create_player(user["username"])
        player_id = player["id"]
    else:
        player_id = player_row["player_id"]

    # Create session
    db2 = get_db()
    token = _make_token()
    expires = (datetime.utcnow() + timedelta(days=30)).isoformat()
    db2.execute("INSERT INTO sessions (token, user_id, player_id, expires_at) VALUES (?,?,?,?)",
               (token, user_id, player_id, expires))
    db2.execute("""DELETE FROM sessions WHERE user_id=? AND token NOT IN (
        SELECT token FROM sessions WHERE user_id=? ORDER BY expires_at DESC LIMIT 5
    )""", (user_id, user_id))
    db2.commit()
    db2.close()

    return {
        "token": token,
        "user_id": user_id,
        "player_id": player_id,
        "username": user["username"],
        "email": user["email"],
        "player": get_player(player_id),
    }


def logout(token: str):
    db = get_db()
    db.execute("DELETE FROM sessions WHERE token=?", (token,))
    db.commit()


def validate_session(token: str) -> dict | None:
    """Return user info if token is valid, None otherwise."""
    if not token:
        return None
    db = get_db()
    row = db.execute(
        "SELECT s.*, u.email, u.username FROM sessions s JOIN users u ON s.user_id=u.id WHERE s.token=? AND s.expires_at > datetime('now')",
        (token,),
    ).fetchone()
    if not row:
        return None
    return {
        "user_id": row["user_id"],
        "player_id": row["player_id"],
        "username": row["username"],
        "email": row["email"],
        "token": token,
    }
