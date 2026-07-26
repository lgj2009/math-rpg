"""GET /api/achievements/{player_id} — achievement list."""
from fastapi import APIRouter, Query
from services import achievement_service

router = APIRouter(prefix="/api", tags=["achievements"])


@router.get("/achievements/{player_id}")
def get_achievements(player_id: int, lang: str = Query("zh")):
    return achievement_service.get_player_achievements(player_id, lang)
