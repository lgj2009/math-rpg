"""GET /api/learn/* — Learning hall endpoints."""
from fastapi import APIRouter, HTTPException
from services import learn_service

router = APIRouter(prefix="/api/learn", tags=["learn"])


@router.get("/modules")
def get_learn_modules():
    """Return modules with their learning concepts (like hunting ground but for learning)."""
    return learn_service.get_learn_modules()


@router.get("/concepts")
def get_concepts():
    return learn_service.get_concept_tree()


@router.get("/concept/{name}")
def get_concept(name: str):
    lesson = learn_service.get_lesson(name)
    if not lesson:
        raise HTTPException(404, f"Concept '{name}' not found or no lesson available")
    return lesson
