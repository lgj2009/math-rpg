"""Mastery calculation — 5-dimension scoring per module."""
from datetime import date
from database import get_db_ctx
import config


def calculate_mastery(player_id: int, module_id: int) -> dict:
    with get_db_ctx() as db:
        # ── 1. Recent accuracy (last 3 practice records) ──────────────────
        records = db.execute("""
            SELECT correct_count*1.0/total_questions as acc
            FROM practice_records WHERE player_id=? AND module_id=?
            ORDER BY practice_date DESC LIMIT 3
        """, (player_id, module_id)).fetchall()
        accuracy_avg = sum(r["acc"] for r in records) / len(records) if records else 0

        # ── 2. Speed qualify (avg time per question ≤ 150s) ───────────────
        speed_records = db.execute("""
            SELECT time_used_sec*1.0/total_questions as avg_time, total_questions
            FROM practice_records WHERE player_id=? AND module_id=?
            ORDER BY practice_date DESC LIMIT 3
        """, (player_id, module_id)).fetchall()
        time_ok = all(
            r["avg_time"] is not None and r["avg_time"] <= 150
            for r in speed_records
        ) if speed_records else False

        # ── 3. Mindset/retention: blind-spot clear rate ───────────────────
        spots = db.execute("""
            SELECT COUNT(*) as total,
                   SUM(CASE WHEN status='cleared' THEN 1 ELSE 0 END) as cleared
            FROM blind_spots
            WHERE player_id=? AND module_ids LIKE ?
        """, (player_id, f'%{module_id}%')).fetchone()
        mistake_clear = spots["cleared"] / spots["total"] if spots["total"] > 0 else 1.0

        # ── 4. Stability: variance of last 5 accuracies ───────────────────
        all_acc = db.execute("""
            SELECT correct_count*1.0/total_questions as acc
            FROM practice_records WHERE player_id=? AND module_id=?
            ORDER BY practice_date DESC LIMIT 5
        """, (player_id, module_id)).fetchall()
        accs = [r["acc"] for r in all_acc]
        stability = 0
        if len(accs) >= 2:
            mean = sum(accs) / len(accs)
            variance = sum((a - mean) ** 2 for a in accs) / len(accs)
            stability = max(0, 1 - variance * 10)  # low variance = high stability

        # ── 5. Determine status ───────────────────────────────────────────
        if accuracy_avg >= config.MASTERY_ACCURACY and mistake_clear >= config.MASTERY_MISTAKE_CLEAR and stability >= 0.7:
            status = "mastered"
        elif accuracy_avg >= 0.70:
            status = "practicing"
        elif accuracy_avg > 0:
            status = "learning"
        else:
            status = "new"

        # ── Persist to module_mastery table ───────────────────────────────
        mastered_val = date.today().isoformat() if status == "mastered" else None
        db.execute("""
            UPDATE module_mastery
            SET accuracy_avg=?, speed_qualify=?, retention_score=?,
                mistake_clear_rate=?, stability_score=?, status=?, mastered_date=?
            WHERE player_id=? AND module_id=?
        """, (accuracy_avg, int(time_ok), mistake_clear, mistake_clear, stability,
              status, mastered_val, player_id, module_id))
        db.commit()

    return {
        "accuracy_avg": accuracy_avg,
        "speed_qualify": time_ok,
        "retention_score": mistake_clear,
        "mistake_clear_rate": mistake_clear,
        "stability_score": stability,
        "status": status,
    }
