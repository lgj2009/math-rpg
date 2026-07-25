from fastapi import APIRouter, HTTPException
from models.blind_spot import BlindSpotResponse, BlindSpotRoundResponse, AttackRequest, AttackResponse
from services import blind_spot_service

router = APIRouter(prefix="/api/players/{player_id}/blind-spots", tags=["blind-spots"])


@router.get("", response_model=list[BlindSpotResponse])
def list_blind_spots(player_id: int):
    return blind_spot_service.list_blind_spots(player_id)


@router.get("/due-today", response_model=list[BlindSpotRoundResponse])
def get_due_today(player_id: int):
    return blind_spot_service.get_due_today(player_id)


@router.post("/{blind_spot_id}/attack", response_model=AttackResponse)
def attack_blind_spot(player_id: int, blind_spot_id: int, body: AttackRequest):
    result = blind_spot_service.attack_blind_spot(
        player_id, blind_spot_id, body.answer, body.round_number
    )
    if "detail" in result:
        detail = result["detail"]
        if "energy" in detail.lower():
            raise HTTPException(403, detail)
        raise HTTPException(404, detail)
    return result
