import random
from datetime import date
from database import get_db
import config


def generate_daily_tasks(player_id: int) -> list:
    db = get_db()
    today = date.today().isoformat()

    # Check if already generated
    existing = db.execute(
        "SELECT id FROM daily_tasks WHERE player_id=? AND scheduled_date=?",
        (player_id, today)
    ).fetchone()
    if existing:
        return list_tasks(player_id, today)

    tasks = []

    # Main quest: lowest mastery module
    lowest = db.execute("""
        SELECT mm.module_id, m.name FROM module_mastery mm
        JOIN modules m ON mm.module_id = m.id
        WHERE mm.player_id=? AND mm.status != 'mastered'
        ORDER BY mm.accuracy_avg ASC LIMIT 1
    """, (player_id,)).fetchone()
    if lowest:
        tasks.append((
            player_id, lowest["module_id"], "main",
            f"讨伐「{lowest['name']}」— 完成10道练习题",
            30, config.XP_DAILY_TASK["main"], today
        ))

    # Side quests: up to 3 pending blind spot retries
    due = db.execute("""
        SELECT bs.id, bs.name FROM blind_spot_rounds bsr
        JOIN blind_spots bs ON bsr.blind_spot_id = bs.id
        WHERE bs.player_id=? AND bsr.scheduled_date=? AND bsr.result='pending'
        LIMIT 3
    """, (player_id, today)).fetchall()
    for d in due:
        tasks.append((
            player_id, None, "side",
            f"炼金: 复测盲点「{d['name']}」",
            15, config.XP_DAILY_TASK["side"], today
        ))

    # Challenge: rotate daily
    challenges = [
        ("⏱️ 限时挑战: 5分钟做完前8道选择", 5, config.XP_DAILY_TASK["challenge"]),
        ("🎯 精准挑战: 一次练习正确率100%", 0, config.XP_DAILY_TASK["challenge"]),
        ("🧠 心算挑战: 完成3道纯心算题", 0, config.XP_DAILY_TASK["challenge"]),
        ("⚡ 速攻挑战: 10道题限时10分钟", 10, config.XP_DAILY_TASK["challenge"]),
    ]
    chal = random.choice(challenges)
    tasks.append((player_id, None, "challenge", chal[0], chal[1], chal[2], today))

    cur = db.cursor()
    cur.executemany(
        """INSERT INTO daily_tasks
           (player_id, module_id, task_type, content, time_limit_min, xp_reward, scheduled_date)
           VALUES (?,?,?,?,?,?,?)""",
        tasks
    )
    db.commit()
    return list_tasks(player_id, today)


def list_tasks(player_id: int, dt: str) -> list:
    db = get_db()
    return [
        dict(r) for r in db.execute(
            "SELECT * FROM daily_tasks WHERE player_id=? AND scheduled_date=?",
            (player_id, dt)
        ).fetchall()
    ]


def complete_task(player_id: int, task_id: int, actual_time_min: int = 0) -> dict:
    db = get_db()
    task = db.execute(
        "SELECT * FROM daily_tasks WHERE id=? AND player_id=? AND completed=0",
        (task_id, player_id)
    ).fetchone()
    if not task:
        return {"detail": "not found or already completed"}

    db.execute(
        "UPDATE daily_tasks SET completed=1, actual_time_min=?, completed_date=datetime('now') WHERE id=?",
        (actual_time_min, task_id)
    )
    db.commit()

    from services.player_service import award_xp
    xp_res = award_xp(player_id, task["xp_reward"])

    return {"task_id": task_id, "completed": True, "xp_gained": task["xp_reward"]}
