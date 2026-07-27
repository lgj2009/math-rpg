"""Feedback service — saves to DB and sends email via QQ SMTP."""
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from database import get_db_ctx
import config


def submit_feedback(player_id: int | None, username: str, category: str, message: str, page: str = "") -> dict:
    """Save feedback to DB and attempt email delivery."""
    with get_db_ctx() as db:
        cur = db.execute(
            "INSERT INTO feedback (player_id, username, category, message, page) VALUES (?,?,?,?,?)",
            (player_id, username, category, message, page),
        )
        fid = cur.lastrowid
        db.commit()

    # Try to send email (non-blocking — failure is logged but doesn't break)
    email_result = _send_email(username, category, message, page)

    return {
        "id": fid,
        "saved": True,
        "email_sent": email_result,
    }


def _send_email(username: str, category: str, message: str, page: str) -> bool:
    """Send feedback via QQ SMTP. Returns True if sent successfully."""
    if not config.SMTP_ENABLED:
        return False
    if config.SMTP_PASSWORD == "YOUR_QQ_AUTH_CODE":
        return False  # SMTP not configured

    try:
        ctx = ssl.create_default_context()
        msg = MIMEMultipart()
        msg["From"] = config.SMTP_USER
        msg["To"] = config.SMTP_TO
        msg["Subject"] = f"[MathRPG反馈] {category} — 来自 {username}"

        body = f"""Math RPG 用户反馈

用户: {username}
分类: {category}
页面: {page or '未知'}
时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

反馈内容:
{message}
"""
        msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT, context=ctx) as server:
            server.login(config.SMTP_USER, config.SMTP_PASSWORD)
            server.sendmail(config.SMTP_USER, config.SMTP_TO, msg.as_string())
        return True
    except Exception as e:
        print(f"[feedback] Email send failed: {e}")
        return False
