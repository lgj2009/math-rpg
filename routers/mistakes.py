from fastapi import APIRouter, HTTPException
from models.mistake import MistakeCreate, MistakeRetry, MistakeResponse
from services import mistake_service

router = APIRouter(prefix="/api/players/{player_id}/mistakes", tags=["mistakes"])


@router.post("", response_model=MistakeResponse, status_code=201)
def create_mistake(player_id: int, body: MistakeCreate):
    return mistake_service.create_mistake(player_id, body.model_dump())


@router.get("")
def list_mistakes(player_id: int, module_id: int | None = None, mastered: int | None = None):
    return mistake_service.list_mistakes(player_id, module_id, mastered)


@router.post("/{mistake_id}/retry")
def retry_mistake(player_id: int, mistake_id: int, body: MistakeRetry):
    result = mistake_service.retry_mistake(player_id, mistake_id, body.answer)
    if "detail" in result:
        raise HTTPException(404, result["detail"])
    return result
