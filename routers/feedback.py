"""POST /api/feedback — submit user feedback."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from services import feedback_service
from database import get_db_ctx

router = APIRouter(prefix="/api", tags=["feedback"])


class FeedbackSubmit(BaseModel):
    player_id: int | None = None
    username: str = "匿名用户"
    category: str = "general"
    message: str = Field(..., min_length=1, max_length=5000)
    page: str = ""


@router.post("/feedback")
def submit(body: FeedbackSubmit):
    result = feedback_service.submit_feedback(
        player_id=body.player_id,
        username=body.username,
        category=body.category,
        message=body.message,
        page=body.page,
    )
    return result


@router.get("/admin/feedback")
def list_feedback():
    """List all feedback (simple admin view)."""
    with get_db_ctx() as db:
        rows = db.execute(
            "SELECT * FROM feedback ORDER BY created_at DESC LIMIT 50"
        ).fetchall()
    return [dict(r) for r in rows]
