"""Membership API — plans, checkout, webhook."""
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from services import membership_service

router = APIRouter(prefix="/api/membership", tags=["membership"])


class CheckoutBody(BaseModel):
    player_id: int
    plan: str = Field(..., pattern="^(warrior|legend|lifetime)$")
    billing: str = Field(..., pattern="^(monthly|yearly|lifetime)$")


@router.get("/{player_id}")
def get_membership(player_id: int):
    return membership_service.get_user_membership(player_id)


@router.get("/plans")
def get_plans():
    """Return all plans with prices (used by frontend)."""
    return {k: {"name": v["name"], "name_zh": v["name_zh"], "name_vi": v["name_vi"],
                "price_monthly": v["price_monthly"], "price_yearly": v["price_yearly"],
                "price_lifetime": v["price_lifetime"], "features": v["features"],
                "color": v["color"], "icon": v["icon"]} for k, v in membership_service.PLANS.items()}


@router.post("/checkout")
def checkout(body: CheckoutBody):
    success_url = f"http://127.0.0.1:8000/#settings?checkout=success"
    cancel_url = f"http://127.0.0.1:8000/#settings?checkout=cancel"
    result = membership_service.create_checkout_session(body.player_id, body.plan, body.billing, success_url, cancel_url)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result


@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.body()
    sig = request.headers.get("stripe-signature", "")
    wh_secret = "whsec_your_webhook_secret"  # Set this in config
    result = membership_service.handle_stripe_webhook(payload, sig, wh_secret)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result
