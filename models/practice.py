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


class PerQuestionResult(BaseModel):
    question_id: int
    content: str
    type: str
    difficulty: int
    user_answer: str
    correct_answer: str
    solution: str
    is_correct: bool

class PracticeResult(BaseModel):
    total: int
    correct: int
    wrong: int = 0
    accuracy: float
    xp_gained: int
    near_miss: bool
    gacha_result: dict
    per_question: list[dict] = []
    mistakes_created: int = 0
    tasks_auto_done: int = 0
