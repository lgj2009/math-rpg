from pydantic import BaseModel
from typing import Optional


class BlindSpotResponse(BaseModel):
    id: int
    name: str
    hp_total: int
    hp_current: int
    boss_type: str
    status: str
    defeat_count: int
    module_ids: list[int]
    parent_id: Optional[int] = None


class AttackRequest(BaseModel):
    answer: str
    round_number: int  # 1-4


class AttackResponse(BaseModel):
    damage: int         # 25 if correct, 0 if wrong
    hp_remaining: int
    boss_killed: bool
    xp_gained: int
