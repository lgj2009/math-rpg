"""Membership system — plan management, Stripe integration, feature gating."""
import json, os, stripe
from datetime import datetime, timedelta
from database import get_db

# Membership plans
PLANS = {
    "free": {
        "name": "Free", "name_zh": "免费版", "name_vi": "Miễn Phí",
        "price_monthly": 0, "price_yearly": 0, "price_lifetime": 0,
        "features": [
            "每日30题", "30 questions/day", "30 câu/ngày",
            "3个模块", "3 modules", "3 mô-đun",
            "基础战斗模式", "Basic combat", "Chiến đấu cơ bản",
        ],
        "limits": {"daily_questions": 30, "modules": 3},
        "color": "var(--text-muted)",
        "icon": "🆓",
    },
    "warrior": {
        "name": "Warrior", "name_zh": "战士版", "name_vi": "Chiến Binh",
        "price_monthly": 499, "price_yearly": 2999, "price_lifetime": 0,
        "stripe_price_id_monthly": "price_warrior_monthly",  # Replace with real Stripe price ID
        "stripe_price_id_yearly": "price_warrior_yearly",
        "features": [
            "无限刷题", "Unlimited questions", "Không giới hạn câu hỏi",
            "全部8个模块", "All 8 modules", "Tất cả 8 mô-đun",
            "赛季通行证付费奖励", "Premium season rewards", "Phần thưởng season premium",
            "自定义头像框", "Custom avatar frames", "Khung avatar tùy chỉnh",
            "专属称号颜色", "Exclusive title colors", "Màu danh hiệu độc quyền",
        ],
        "limits": {"daily_questions": 9999, "modules": 8},
        "color": "var(--sapphire)",
        "icon": "⚔️",
    },
    "legend": {
        "name": "Legend", "name_zh": "传说版", "name_vi": "Huyền Thoại",
        "price_monthly": 999, "price_yearly": 5999, "price_lifetime": 4999,
        "stripe_price_id_monthly": "price_legend_monthly",
        "stripe_price_id_yearly": "price_legend_yearly",
        "stripe_price_id_lifetime": "price_legend_lifetime",
        "features": [
            "Warrior全部功能", "All Warrior features", "Tất cả tính năng Warrior",
            "AI批改大题", "AI answer review", "AI chấm bài tự luận",
            "详细学情报告", "Detailed analytics", "Phân tích chi tiết",
            "优先支持", "Priority support", "Hỗ trợ ưu tiên",
            "自定义题库", "Custom question bank", "Ngân hàng câu hỏi tùy chỉnh",
            "去广告", "Ad-free", "Không quảng cáo",
        ],
        "limits": {"daily_questions": 9999, "modules": 8},
        "color": "var(--gold)",
        "icon": "👑",
    },
    "lifetime": {
        "name": "Lifetime", "name_zh": "永久版", "name_vi": "Vĩnh Viễn",
        "price_monthly": 0, "price_yearly": 0, "price_lifetime": 4999,
        "stripe_price_id_lifetime": "price_lifetime",
        "features": [
            "Legend全部功能 · 永久有效", "All Legend features · Forever", "Tất cả tính năng Legend · Mãi mãi",
        ],
        "limits": {"daily_questions": 9999, "modules": 8},
        "color": "var(--purple)",
        "icon": "💎",
    },
}


def get_user_membership(player_id: int) -> dict:
    """Get the current membership status for a player."""
    db = get_db()
    row = db.execute(
        "SELECT * FROM user_memberships WHERE player_id=? AND (expires_at IS NULL OR expires_at > datetime('now')) ORDER BY created_at DESC LIMIT 1",
        (player_id,),
    ).fetchone()
    db.close()

    if not row:
        return {"plan": "free", "expires_at": None, "is_premium": False,
                **PLANS["free"]}

    plan = row["plan"]
    plan_info = PLANS.get(plan, PLANS["free"])
    return {
        "plan": plan,
        "expires_at": row["expires_at"],
        "is_premium": plan != "free",
        "started_at": row["created_at"],
        **plan_info,
    }


def create_checkout_session(player_id: int, plan: str, billing: str, success_url: str, cancel_url: str) -> dict:
    """Create a Stripe checkout session for plan purchase."""
    plan_info = PLANS.get(plan)
    if not plan_info or plan == "free":
        return {"detail": "Invalid plan"}

    price_key = f"stripe_price_id_{billing}"
    price_id = plan_info.get(price_key)
    if not price_id:
        return {"detail": f"No Stripe price for {plan} {billing}"}

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{"price": price_id, "quantity": 1}],
            mode="subscription" if billing in ("monthly", "yearly") else "payment",
            success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=cancel_url,
            metadata={"player_id": str(player_id), "plan": plan, "billing": billing},
        )
        return {"url": session.url}
    except Exception as e:
        return {"detail": str(e)}


def handle_stripe_webhook(payload: bytes, sig_header: str, webhook_secret: str) -> dict:
    """Process Stripe webhook events."""
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except Exception as e:
        return {"detail": str(e)}

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        metadata = session.get("metadata", {})
        player_id = int(metadata.get("player_id", 0))
        plan = metadata.get("plan", "free")
        billing = metadata.get("billing", "monthly")

        if player_id and plan != "free":
            _activate_membership(player_id, plan, billing)

    return {"ok": True}


def _activate_membership(player_id: int, plan: str, billing: str):
    """Activate a membership for a player."""
    db = get_db()
    now = datetime.utcnow()
    if billing == "monthly":
        expires = now + timedelta(days=30)
    elif billing == "yearly":
        expires = now + timedelta(days=365)
    elif billing == "lifetime":
        expires = None  # Never expires
    else:
        expires = now + timedelta(days=30)

    db.execute(
        "INSERT INTO user_memberships (player_id, plan, expires_at, created_at) VALUES (?,?,?,?)",
        (player_id, plan, expires.isoformat() if expires else None, now.isoformat()),
    )
    db.commit()
    db.close()


def ensure_membership_table():
    """Create membership tables if they don't exist."""
    db = get_db()
    db.execute("""CREATE TABLE IF NOT EXISTS user_memberships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER NOT NULL,
        plan TEXT NOT NULL DEFAULT 'free',
        expires_at TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )""")
    db.commit()
    db.close()
