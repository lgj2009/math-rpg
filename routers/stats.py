"""Stats & dashboard endpoints."""
from fastapi import APIRouter, HTTPException
from database import get_db_ctx
from services.player_service import get_player
from services.mastery_service import calculate_mastery

router = APIRouter(prefix="/api/players", tags=["stats"])


@router.get("/{player_id}/dashboard")
def dashboard(player_id: int):
    p = get_player(player_id)
    if not p:
        raise HTTPException(404, "Player not found")

    with get_db_ctx() as db:
        modules = db.execute("SELECT * FROM modules ORDER BY sort_order").fetchall()

    masteries = []
    estimated_score = 0

    for m in modules:
        mas = calculate_mastery(player_id, m["id"])
        masteries.append({
            "module_id": m["id"],
            "module_name": m["name"],
            "icon": m["icon"],
            **mas,
        })
        if mas["status"] == "mastered":
            estimated_score += m["weight"]
        elif mas["status"] == "practicing":
            estimated_score += m["weight"] * 0.6

    # Compute totals from practice_records (players table lacks these columns)
    with get_db_ctx() as db:
        totals = db.execute("""
            SELECT COALESCE(SUM(total_questions), 0) as total_q,
                   COALESCE(SUM(correct_count), 0) as total_c
            FROM practice_records WHERE player_id=?
        """, (player_id,)).fetchone()

    return {
        "player": p,
        "estimated_score": min(150, int(estimated_score)),
        "module_masteries": masteries,
        "streak_days": p.get("streak_days", 0),
        "total_questions": totals["total_q"],
        "total_correct": totals["total_c"],
    }


@router.get("/{player_id}/progress")
def progress(player_id: int):
    p = get_player(player_id)
    if not p:
        raise HTTPException(404, "Player not found")

    with get_db_ctx() as db:
        modules = db.execute("SELECT * FROM modules ORDER BY sort_order").fetchall()

    module_details = []

    for m in modules:
        mas = calculate_mastery(player_id, m["id"])
        module_details.append({
            "module_id": m["id"],
            "module_name": m["name"],
            "icon": m["icon"],
            "weight": m["weight"],
            "tier": m["tier"],
            **mas,
        })

    # Aggregate stats
    with get_db_ctx() as db:
        totals = db.execute("""
            SELECT COALESCE(SUM(total_questions), 0) as total_q,
                   COALESCE(SUM(correct_count), 0) as total_c
            FROM practice_records WHERE player_id=?
        """, (player_id,)).fetchone()

    return {
        "player_id": player_id,
        "username": p["username"],
        "level": p["level"],
        "modules": module_details,
        "total_questions": totals["total_q"],
        "total_correct": totals["total_c"],
        "overall_accuracy": round(totals["total_c"] / totals["total_q"], 4) if totals["total_q"] > 0 else 0,
    }
