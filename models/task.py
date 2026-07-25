from pydantic import BaseModel
from typing import Optional


class DailyTaskResponse(BaseModel):
    id: int
    player_id: int
    module_id: Optional[int] = None
    task_type: str
    content: str
    time_limit_min: Optional[int] = None
    xp_reward: int
    completed: int
    actual_time_min: Optional[int] = None
    scheduled_date: str
    completed_date: Optional[str] = None


class CompleteTaskResponse(BaseModel):
    task_id: int
    completed: bool
    xp_gained: int
