"""GET /api/bank — full question bank with answers and solutions."""
from fastapi import APIRouter, Query
from database import get_db
import json

router = APIRouter(prefix="/api", tags=["bank"])


@router.get("/bank")
def browse_bank(
    module_id: int | None = Query(None),
    difficulty: int | None = Query(None),
    source: str | None = Query(None),
    keyword: str | None = Query(None),
    lang: str = Query("zh"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """Browse all questions with full answers and solutions.
    Supports filtering by module, difficulty, source, and keyword search.
    """
    db = get_db()

    where = ["1=1"]
    params = []

    if module_id is not None:
        where.append("q.module_id = ?")
        params.append(module_id)
    if difficulty is not None:
        where.append("q.difficulty = ?")
        params.append(difficulty)
    if source is not None:
        where.append("q.source_type = ?")
        params.append(source)
    if keyword:
        where.append("(q.content LIKE ? OR q.solution LIKE ? OR q.source_ref LIKE ?)")
        kw = f"%{keyword}%"
        params.extend([kw, kw, kw])

    where_clause = " AND ".join(where)

    # Count total
    count_row = db.execute(
        f"SELECT COUNT(*) FROM questions q WHERE {where_clause}", params
    ).fetchone()
    total = count_row[0]

    # Fetch page
    offset = (page - 1) * page_size
    rows = db.execute(
        f"""SELECT q.id, q.module_id, q.type, q.difficulty, q.content, q.options,
                   q.answer, q.solution, q.source_type, q.source_ref, q.concepts,
                   m.name as module_name, m.icon as module_icon
            FROM questions q
            LEFT JOIN modules m ON q.module_id = m.id
            WHERE {where_clause}
            ORDER BY q.source_type DESC, q.source_ref, q.id
            LIMIT ? OFFSET ?""",
        params + [page_size, offset],
    ).fetchall()

    questions = []
    for r in rows:
        q = dict(r)
        if q.get("options"):
            try:
                q["options"] = json.loads(q["options"])
            except (json.JSONDecodeError, TypeError):
                q["options"] = None
        if q.get("concepts"):
            try:
                q["concepts"] = json.loads(q["concepts"])
            except (json.JSONDecodeError, TypeError):
                q["concepts"] = []
        questions.append(q)

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": max(1, (total + page_size - 1) // page_size),
        "questions": questions,
    }


@router.get("/bank/modules")
def bank_modules():
    """List all modules for the filter dropdown."""
    db = get_db()
    rows = db.execute(
        "SELECT id, name, icon, weight FROM modules ORDER BY sort_order"
    ).fetchall()
    return [dict(r) for r in rows]
