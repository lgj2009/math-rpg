from datetime import datetime
from fastapi import APIRouter, HTTPException
from models.player import PlayerCreate, PlayerResponse
from services import player_service

router = APIRouter(prefix="/api/players", tags=["players"])


@router.post("", response_model=PlayerResponse, status_code=201)
def create_player(body: PlayerCreate):
    return player_service.create_player(body.username)


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int):
    p = player_service.get_player(player_id)
    if not p:
        raise HTTPException(404, "Player not found")
    return p


@router.post("/{player_id}/checkin")
def checkin(player_id: int):
    result = player_service.checkin(player_id)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result


@router.post("/{player_id}/claim-energy")
def claim_energy(player_id: int, hour: int | None = None):
    h = hour if hour is not None else datetime.now().hour
    result = player_service.claim_energy(player_id, h)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result
