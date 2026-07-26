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


@router.post("/{player_id}/reset")
def reset_progress(player_id: int):
    from database import get_db
    db = get_db()
    db.execute("DELETE FROM practice_records WHERE player_id=?", (player_id,))
    db.execute("DELETE FROM mistakes WHERE player_id=?", (player_id,))
    db.execute("DELETE FROM blind_spots WHERE player_id=?", (player_id,))
    db.execute("DELETE FROM blind_spot_rounds WHERE blind_spot_id IN (SELECT id FROM blind_spots WHERE player_id=?)", (player_id,))
    db.execute("DELETE FROM module_mastery WHERE player_id=?", (player_id,))
    db.execute("DELETE FROM checkins WHERE player_id=?", (player_id,))
    db.execute("UPDATE players SET xp=0, level=1, title='数学学徒', streak_days=0, max_streak=0, focus_energy=100, season_xp=0, battle_pass_tier=0, coins=0 WHERE id=?", (player_id,))
    db.execute("DELETE FROM guild_members WHERE player_id=?", (player_id,))
    # Re-create module_mastery rows
    modules = db.execute("SELECT id FROM modules").fetchall()
    for m in modules:
        db.execute("INSERT OR IGNORE INTO module_mastery (player_id, module_id) VALUES (?,?)", (player_id, m["id"]))
    db.commit()
    return {"ok": True}


@router.post("/{player_id}/claim-energy")
def claim_energy(player_id: int, hour: int | None = None):
    h = hour if hour is not None else datetime.now().hour
    result = player_service.claim_energy(player_id, h)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result
