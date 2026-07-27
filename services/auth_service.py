"""User authentication — register, login, logout, session validation.

Password hashing:
  v1 (legacy): sha256("math-rpg-salt-v1:{password}")            — 64 hex chars
  v2 (current): "$v2${random_salt}${sha256(random_salt:password)}" — random salt per user
"""

import hashlib
import secrets
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from database import get_db
from services.player_service import create_player, get_player
import config


def _hash_password(password: str) -> str:
    """Hash a new password with v2 format (random salt)."""
    salt = secrets.token_hex(16)
    h = hashlib.sha256(f"{salt}:{password}".encode()).hexdigest()
    return f"$v2${salt}${h}"


def _verify_password(password: str, stored: str) -> bool:
    """Verify a password against a stored hash (handles v1 and v2 formats)."""
    if stored.startswith("$v2$"):
        # v2: $v2${salt}${hash}
        parts = stored.split("$", 3)
        if len(parts) != 4:
            return False
        _, _, salt, expected_hash = parts
        actual_hash = hashlib.sha256(f"{salt}:{password}".encode()).hexdigest()
        return actual_hash == expected_hash
    else:
        # v1 (legacy): sha256("math-rpg-salt-v1:{password}")
        expected = hashlib.sha256(f"math-rpg-salt-v1:{password}".encode()).hexdigest()
        return stored == expected


def _make_token() -> str:
    return secrets.token_hex(32)


def _send_reset_email(email_to: str, username: str, reset_url: str) -> bool:
    """Send a password-reset email. Returns True if sent successfully."""
    if not config.SMTP_ENABLED:
        return False
    if config.SMTP_PASSWORD == "YOUR_QQ_AUTH_CODE":
        return False  # SMTP not configured

    try:
        ctx = ssl.create_default_context()
        msg = MIMEMultipart()
        msg["From"] = config.SMTP_USER
        msg["To"] = email_to
        msg["Subject"] = "[Math RPG] 密码重置 / Password Reset"

        body = f"""您好 {username}，

我们收到了您重置密码的请求。请点击以下链接重置密码（30分钟内有效）：

{reset_url}

如果您没有请求重置密码，请忽略此邮件。

---
Hi {username},

We received a request to reset your password. Click the link below to reset
(valid for 30 minutes):

{reset_url}

If you did not request this, please ignore this email.
"""
        msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT, context=ctx) as server:
            server.login(config.SMTP_USER, config.SMTP_PASSWORD)
            server.sendmail(config.SMTP_USER, email_to, msg.as_string())
        return True
    except Exception as e:
        print(f"[auth] Reset email send failed: {e}")
        return False


def register(email: str, username: str, password: str) -> dict:
    """Register a new user, create their player, return session."""
    db = get_db()
    existing = db.execute("SELECT id FROM users WHERE email=?", (email,)).fetchone()
    if existing:
        db.close()
        return {"detail": "Email already registered"}

    pw_hash = _hash_password(password)
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
    if not user or not _verify_password(password, user["password_hash"]):
        db.close()
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
    # Cleanup old sessions (keep last 5)
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
    db.close()


def validate_session(token: str) -> dict | None:
    """Return user info if token is valid, None otherwise."""
    if not token:
        return None
    db = get_db()
    row = db.execute(
        "SELECT s.*, u.email, u.username FROM sessions s JOIN users u ON s.user_id=u.id "
        "WHERE s.token=? AND s.expires_at > datetime('now')",
        (token,),
    ).fetchone()
    db.close()
    if not row:
        return None
    return {
        "user_id": row["user_id"],
        "player_id": row["player_id"],
        "username": row["username"],
        "email": row["email"],
        "token": token,
    }


def change_password(user_id: int, old_password: str, new_password: str) -> dict:
    db = get_db()
    user = db.execute("SELECT password_hash FROM users WHERE id=?", (user_id,)).fetchone()
    if not user or not _verify_password(old_password, user["password_hash"]):
        db.close()
        return {"detail": "Current password is incorrect"}
    new_hash = _hash_password(new_password)
    db.execute("UPDATE users SET password_hash=? WHERE id=?", (new_hash, user_id))
    db.commit()
    db.close()
    return {"ok": True, "message": "Password changed"}


def forgot_password(email: str, reset_base_url: str = "") -> dict:
    """Initiate password reset. Generates a token, sends it via email.

    Never returns the token in the response — it's only sent via email.
    """
    db = get_db()
    user = db.execute("SELECT id, username FROM users WHERE email=?", (email,)).fetchone()
    if not user:
        db.close()
        # Don't reveal whether the email exists
        return {"ok": True, "message": "If that email is registered, a reset link has been sent."}

    # Invalidate old tokens for this user
    db.execute("UPDATE password_reset_tokens SET used=1 WHERE user_id=? AND used=0",
               (user["id"],))

    # Generate new token (valid 30 minutes)
    token = secrets.token_urlsafe(32)
    expires = (datetime.utcnow() + timedelta(minutes=30)).isoformat()
    db.execute(
        "INSERT INTO password_reset_tokens (user_id, token, expires_at) VALUES (?,?,?)",
        (user["id"], token, expires),
    )
    db.commit()
    db.close()

    # Build reset URL
    if not reset_base_url:
        reset_base_url = "http://127.0.0.1:8000"
    reset_url = f"{reset_base_url}/#reset-password?token={token}"

    # Try to send email
    email_sent = _send_reset_email(email, user["username"], reset_url)

    import sys
    if not email_sent:
        # Log the reset URL for development (token is NOT returned to the caller)
        print(f"[auth] SMTP not configured — reset URL for {email}: {reset_url}", file=sys.stderr)

    return {"ok": True, "message": "If that email is registered, a reset link has been sent."}


def reset_password(token: str, new_password: str) -> dict:
    """Complete password reset using a valid token."""
    db = get_db()
    row = db.execute(
        "SELECT user_id FROM password_reset_tokens WHERE token=? AND used=0 AND expires_at > datetime('now')",
        (token,),
    ).fetchone()
    if not row:
        db.close()
        return {"detail": "Invalid or expired reset token. Please request a new one."}

    user_id = row["user_id"]

    # Update password
    new_hash = _hash_password(new_password)
    db.execute("UPDATE users SET password_hash=? WHERE id=?", (new_hash, user_id))

    # Mark token as used
    db.execute("UPDATE password_reset_tokens SET used=1 WHERE token=?", (token,))

    # Invalidate all sessions for security
    db.execute("DELETE FROM sessions WHERE user_id=?", (user_id,))

    db.commit()
    db.close()

    return {"ok": True, "message": "Password has been reset. Please log in with your new password."}
