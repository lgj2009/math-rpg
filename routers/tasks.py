from fastapi import APIRouter, HTTPException, Query
from models.task import DailyTaskResponse, CompleteTaskResponse
from services import task_service

router = APIRouter(prefix="/api/players/{player_id}/tasks", tags=["tasks"])


@router.post("/generate", response_model=list[DailyTaskResponse])
def generate_tasks(player_id: int):
    return task_service.generate_daily_tasks(player_id)


@router.get("", response_model=list[DailyTaskResponse])
def list_tasks(player_id: int, date: str = Query(default=None, description="YYYY-MM-DD")):
    from datetime import date as d
    dt = date if date else d.today().isoformat()
    return task_service.list_tasks(player_id, dt)


@router.post("/{task_id}/complete", response_model=CompleteTaskResponse)
def complete_task(player_id: int, task_id: int, actual_time_min: int = 0):
    result = task_service.complete_task(player_id, task_id, actual_time_min)
    if "detail" in result:
        raise HTTPException(404, result["detail"])
    return result
