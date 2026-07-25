from pydantic import BaseModel, Field
from typing import Optional


class PlayerCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=20)


class PlayerResponse(BaseModel):
    id: int
    username: str
    xp: int
    level: int
    title: str
    prestige_count: int
    streak_days: int
    max_streak: int
    streak_shields: int
    focus_energy: int
    focus_max: int
    season_xp: int
    battle_pass_tier: int
    coins: int
    owned_cosmetics: list = []
    guild_id: Optional[int] = None
    guild_role: str = "member"
    last_login: Optional[str] = None


class CheckinResponse(BaseModel):
    streak_days: int
    xp_gained: int
    bonus_applied: bool
    gacha_result: Optional[dict] = None


class EnergyResponse(BaseModel):
    focus_energy: int
    claimed: int
