from pydantic import BaseModel
from typing import Optional


class ModuleResponse(BaseModel):
    id: int
    name: str
    weight: int
    tier: int
    icon: str
    description: Optional[str] = None


class QuestionItem(BaseModel):
    id: int
    type: str
    difficulty: int
    content: str
    options: Optional[list[str]] = None
    time_limit_sec: Optional[int] = None


class PracticeSession(BaseModel):
    session_id: str
    module_id: int
    module_name: str
    questions: list[QuestionItem]
    focus_cost: int


class Answer(BaseModel):
    question_id: int
    answer: str


class PracticeSubmit(BaseModel):
    session_id: str
    module_id: int
    answers: list[Answer]
    time_used_sec: int


class PracticeResult(BaseModel):
    total: int
    correct: int
    accuracy: float
    xp_gained: int
    near_miss: bool
    gacha_result: dict
