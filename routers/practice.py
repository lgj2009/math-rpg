from fastapi import APIRouter, HTTPException
from models.practice import PracticeSubmit, PracticeResult, PracticeSession, ModuleResponse
from services import practice_service

router = APIRouter(prefix="/api", tags=["practice"])


@router.get("/modules", response_model=list[ModuleResponse])
def list_modules():
    from database import get_db

    db = get_db()
    rows = db.execute("SELECT * FROM modules ORDER BY sort_order").fetchall()
    return [dict(r) for r in rows]


@router.get("/modules/{module_id}/practice")
def start_practice(module_id: int, player_id: int, count: int = 10):
    result = practice_service.start_practice(player_id, module_id, count)
    if not result:
        raise HTTPException(404, "No questions available for this module")
    return result


@router.post("/players/{player_id}/practice", response_model=PracticeResult)
def submit_practice(player_id: int, body: PracticeSubmit):
    return practice_service.submit_practice(
        player_id,
        body.module_id,
        body.session_id,
        [{"question_id": a.question_id, "answer": a.answer} for a in body.answers],
        body.time_used_sec,
    )
