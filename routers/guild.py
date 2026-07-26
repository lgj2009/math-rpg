"""Guild API — create, join, chat, feed, boss."""
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from services import guild_service
from services.auth_service import validate_session

router = APIRouter(prefix="/api/guild", tags=["guild"])


def _get_user(authorization: str = Header(None)) -> dict | None:
    token = authorization[7:] if authorization and authorization.startswith("Bearer ") else None
    if not token: return None
    return validate_session(token)


class CreateGuild(BaseModel):
    name: str = Field(..., min_length=2, max_length=30)
    description: str = ""

class JoinGuild(BaseModel):
    guild_id: int

class PostMsg(BaseModel):
    guild_id: int
    message: str = Field(..., min_length=1, max_length=500)

class AttackBoss(BaseModel):
    guild_id: int
    damage: int = Field(..., ge=1)


def _require_user(authorization: str = Header(None)):
    u = _get_user(authorization)
    if not u: raise HTTPException(401, "Not authenticated")
    return u


@router.get("/list")
def list_guilds():
    return guild_service.list_guilds()


@router.post("/create")
def create(body: CreateGuild, authorization: str = Header(None)):
    u = _require_user(authorization)
    result = guild_service.create_guild(body.name, body.description, u["player_id"], u["username"])
    if "detail" in result: raise HTTPException(400, result["detail"])
    return result


@router.post("/join")
def join(body: JoinGuild, authorization: str = Header(None)):
    u = _require_user(authorization)
    result = guild_service.join_guild(body.guild_id, u["player_id"], u["username"])
    if "detail" in result: raise HTTPException(400, result["detail"])
    return result


@router.post("/leave")
def leave(body: JoinGuild, authorization: str = Header(None)):
    u = _require_user(authorization)
    guild_service.leave_guild(body.guild_id, u["player_id"])
    return {"ok": True}


@router.get("/{guild_id}")
def get_guild(guild_id: int, authorization: str = Header(None)):
    u = _get_user(authorization)
    pid = u["player_id"] if u else 0
    result = guild_service.get_guild(guild_id, pid)
    if "detail" in result: raise HTTPException(404, result["detail"])
    return result


@router.post("/messages")
def post_message(body: PostMsg, authorization: str = Header(None)):
    u = _require_user(authorization)
    return guild_service.post_message(body.guild_id, u["player_id"], u["username"], body.message)


@router.get("/{guild_id}/messages")
def get_messages(guild_id: int):
    return guild_service.get_messages(guild_id)


@router.get("/{guild_id}/activity")
def get_activity(guild_id: int):
    return guild_service.get_activity(guild_id)


@router.post("/boss/attack")
def attack_boss(body: AttackBoss, authorization: str = Header(None)):
    u = _require_user(authorization)
    return guild_service.attack_guild_boss(body.guild_id, u["player_id"], u["username"], body.damage)
