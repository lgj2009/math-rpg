"""Combat-style practice endpoints."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import combat_service

router = APIRouter(prefix="/api", tags=["combat"])


class CombatStart(BaseModel):
    player_id: int
    module_id: int
    count: int = 10
    lang: str = "zh"


class CombatAnswer(BaseModel):
    session_id: str
    answer: str
    time_ms: int = 0


@router.post("/combat/start")
def start_combat(body: CombatStart):
    result = combat_service.start_combat(body.player_id, body.module_id, body.count, body.lang)
    if not result:
        raise HTTPException(404, "No questions available for this module")
    return result


@router.post("/combat/answer")
def answer_question(body: CombatAnswer):
    result = combat_service.answer_question(body.session_id, body.answer, body.time_ms)
    if "detail" in result:
        raise HTTPException(404, result["detail"])
    return result
