"""GET /api/season/{player_id}, POST /api/season/claim"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import season_service

router = APIRouter(prefix="/api/season", tags=["season"])


class ClaimBody(BaseModel):
    player_id: int
    tier: int


@router.get("/{player_id}")
def get_season(player_id: int):
    return season_service.get_current_season(player_id)


@router.post("/claim")
def claim_tier(body: ClaimBody):
    result = season_service.claim_tier(body.player_id, body.tier)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result
