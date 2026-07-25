from pydantic import BaseModel, Field
from typing import Optional


class MistakeCreate(BaseModel):
    module_id: int
    question: str
    wrong_step: str = ""
    correct_thought: str = ""
    knowledge_point: str = ""
    error_type: str = "knowledge_gap"   # 'calculation'|'logic'|'knowledge_gap'
    blind_spot_name: Optional[str] = None  # Auto-create blind spot if provided


class MistakeRetry(BaseModel):
    answer: str


class MistakeResponse(BaseModel):
    id: int
    module_id: int
    question: str
    wrong_step: str
    correct_thought: str
    knowledge_point: str
    error_type: str
    retry_count: int
    mastered: bool
    created_date: str
