"""Achievement tracking — check conditions and unlock badges."""
import json
import re
from database import get_db_ctx

ACHIEVEMENTS = [
    # Combat
    {"key": "first_blood", "name": "初战告捷", "name_en": "First Blood", "name_vi": "Chiến Thắng Đầu",
     "desc": "完成第一次练习", "desc_en": "Complete your first practice", "desc_vi": "Hoàn thành bài tập đầu tiên",
     "icon": "⚔️", "category": "combat", "rarity": "common", "condition": "practice_count >= 1"},
    {"key": "warrior_10", "name": "身经百战", "name_en": "Battle Hardened", "name_vi": "Chiến Binh",
     "desc": "完成10次练习", "desc_en": "Complete 10 practices", "desc_vi": "Hoàn thành 10 bài tập",
     "icon": "🛡️", "category": "combat", "rarity": "common", "condition": "practice_count >= 10"},
    {"key": "perfect_score", "name": "完美无瑕", "name_en": "Flawless", "name_vi": "Hoàn Hảo",
     "desc": "一次练习正确率100%", "desc_en": "Get 100% accuracy in a practice", "desc_vi": "Đạt 100% chính xác",
     "icon": "💎", "category": "combat", "rarity": "rare", "condition": "has_perfect"},
    {"key": "combo_5", "name": "连击大师", "name_en": "Combo Master", "name_vi": "Bậc Thầy Combo",
     "desc": "达到5连击", "desc_en": "Reach 5 combo", "desc_vi": "Đạt 5 combo",
     "icon": "🔥", "category": "combat", "rarity": "common", "condition": "max_combo >= 5"},
    {"key": "combo_8", "name": "无双连击", "name_en": "Unstoppable", "name_vi": "Không Thể Ngăn Cản",
     "desc": "达到8连击", "desc_en": "Reach 8 combo", "desc_vi": "Đạt 8 combo",
     "icon": "💥", "category": "combat", "rarity": "rare", "condition": "max_combo >= 8"},
    {"key": "boss_slayer_10", "name": "Boss猎手", "name_en": "Boss Slayer", "name_vi": "Thợ Săn Boss",
     "desc": "击败10个盲点Boss", "desc_en": "Defeat 10 blind spot bosses", "desc_vi": "Đánh bại 10 boss",
     "icon": "🐉", "category": "combat", "rarity": "rare", "condition": "boss_kills >= 10"},

    # Learning
    {"key": "scholar", "name": "学海无涯", "name_en": "Scholar", "name_vi": "Học Giả",
     "desc": "阅读5章学艺堂课程", "desc_en": "Read 5 lessons", "desc_vi": "Đọc 5 bài học",
     "icon": "📖", "category": "learning", "rarity": "common", "condition": "lessons_read >= 5"},
    {"key": "master_module", "name": "模块大师", "name_en": "Module Master", "name_vi": "Bậc Thầy Mô-đun",
     "desc": "掌握一个模块（5维全部达标）", "desc_en": "Master a module", "desc_vi": "Làm chủ một mô-đun",
     "icon": "👑", "category": "learning", "rarity": "epic", "condition": "modules_mastered >= 1"},
    {"key": "question_bank", "name": "题库行者", "name_en": "Question Banker", "name_vi": "Ngân Hàng Đề",
     "desc": "累计刷题100道", "desc_en": "Answer 100 questions", "desc_vi": "Trả lời 100 câu hỏi",
     "icon": "📚", "category": "learning", "rarity": "common", "condition": "total_questions >= 100"},
    {"key": "question_500", "name": "题库霸主", "name_en": "Quiz Lord", "name_vi": "Chúa Tể Câu Hỏi",
     "desc": "累计刷题500道", "desc_en": "Answer 500 questions", "desc_vi": "Trả lời 500 câu hỏi",
     "icon": "🏛️", "category": "learning", "rarity": "epic", "condition": "total_questions >= 500"},

    # Streak
    {"key": "streak_3", "name": "三日之约", "name_en": "Three Day Streak", "name_vi": "Ba Ngày",
     "desc": "连续打卡3天", "desc_en": "3 day streak", "desc_vi": "3 ngày liên tiếp",
     "icon": "📅", "category": "streak", "rarity": "common", "condition": "max_streak >= 3"},
    {"key": "streak_7", "name": "七日轮回", "name_en": "Weekly Warrior", "name_vi": "Chiến Binh Tuần",
     "desc": "连续打卡7天", "desc_en": "7 day streak", "desc_vi": "7 ngày liên tiếp",
     "icon": "🔥", "category": "streak", "rarity": "rare", "condition": "max_streak >= 7"},
    {"key": "streak_30", "name": "月之恒", "name_en": "Moon Walker", "name_vi": "Một Tháng",
     "desc": "连续打卡30天", "desc_en": "30 day streak", "desc_vi": "30 ngày liên tiếp",
     "icon": "🌙", "category": "streak", "rarity": "epic", "condition": "max_streak >= 30"},

    # Social
    {"key": "guild_join", "name": "团队精神", "name_en": "Team Player", "name_vi": "Đồng Đội",
     "desc": "加入一个公会", "desc_en": "Join a guild", "desc_vi": "Tham gia công hội",
     "icon": "🏰", "category": "social", "rarity": "common", "condition": "in_guild"},
    {"key": "guild_chat", "name": "公会话痨", "name_en": "Guild Chatter", "name_vi": "Người Nói Chuyện",
     "desc": "在公会发送10条消息", "desc_en": "Send 10 guild messages", "desc_vi": "Gửi 10 tin nhắn",
     "icon": "💬", "category": "social", "rarity": "common", "condition": "guild_messages >= 10"},

    # Hidden
    {"key": "night_owl", "name": "夜猫子", "name_en": "Night Owl", "name_vi": "Cú Đêm",
     "desc": "晚上10点后完成练习", "desc_en": "Complete practice after 10 PM", "desc_vi": "Làm bài sau 10 giờ tối",
     "icon": "🦉", "category": "hidden", "rarity": "rare", "condition": "night_practice"},
    {"key": "early_bird", "name": "早起鸟", "name_en": "Early Bird", "name_vi": "Chim Sớm",
     "desc": "早上6点前打卡", "desc_en": "Check in before 6 AM", "desc_vi": "Điểm danh trước 6 giờ sáng",
     "icon": "🌅", "category": "hidden", "rarity": "rare", "condition": "early_checkin"},
]


def _evaluate_condition(condition: str, stats: dict) -> bool:
    """Safely evaluate a simple achievement condition without using eval().

    Supported formats:
      - "identifier"              → truthy check (bool or non-zero)
      - "identifier OP number"    → numeric comparison (>=, <=, >, <, ==)
    """
    condition = condition.strip()
    # Pattern: identifier OP number
    m = re.match(r'^(\w+)\s*(>=|<=|>|<|==)\s*(\d+(?:\.\d+)?)$', condition)
    if m:
        key, op, val_str = m.group(1), m.group(2), m.group(3)
        actual = stats.get(key, 0)
        expected = float(val_str) if '.' in val_str else int(val_str)
        try:
            actual_num = float(actual) if isinstance(actual, bool) else actual
        except (TypeError, ValueError):
            return False
        if op == '>=': return actual_num >= expected
        if op == '<=': return actual_num <= expected
        if op == '>':  return actual_num > expected
        if op == '<':  return actual_num < expected
        if op == '==': return actual_num == expected
        return False

    # Pattern: bare identifier → truthy check
    if re.match(r'^[A-Za-z_]\w*$', condition):
        return bool(stats.get(condition, False))

    # Unknown format — log and reject
    import sys
    print(f"[achievement] Unknown condition format: {condition!r}", file=sys.stderr)
    return False


def get_player_achievements(player_id: int, lang: str = "zh") -> list:
    """Return all achievements with unlock status for a player."""
    with get_db_ctx() as db:
        # Get player stats
        p = db.execute("SELECT * FROM players WHERE id=?", (player_id,)).fetchone()
        if not p:
            return []

        # Compute stats
        practice_count = db.execute("SELECT COUNT(*) FROM practice_records WHERE player_id=?", (player_id,)).fetchone()[0]
        has_perfect = db.execute("SELECT COUNT(*) FROM practice_records WHERE player_id=? AND correct_count=total_questions AND total_questions>0", (player_id,)).fetchone()[0] > 0
        max_combo_row = db.execute("SELECT MAX(correct_count) as mc FROM practice_records WHERE player_id=?", (player_id,)).fetchone()
        max_combo = max_combo_row["mc"] or 0
        boss_kills_row = db.execute("SELECT COUNT(*) FROM blind_spots WHERE player_id=? AND status='cleared'", (player_id,)).fetchone()
        boss_kills = boss_kills_row[0]
        total_qs = db.execute("SELECT COALESCE(SUM(total_questions),0) FROM practice_records WHERE player_id=?", (player_id,)).fetchone()[0]
        modules_mastered = db.execute("SELECT COUNT(*) FROM module_mastery WHERE player_id=? AND status='mastered'", (player_id,)).fetchone()[0]
        lessons_read = 0  # simplified
        guild_messages = db.execute("SELECT COUNT(*) FROM guild_messages WHERE player_id=?", (player_id,)).fetchone()[0]
        in_guild = p["guild_id"] is not None

    # Night owl / early bird
    from datetime import datetime
    night_practice = False
    early_checkin = False
    now = datetime.now()
    if now.hour >= 22 or now.hour < 6:
        night_practice = True
    if now.hour < 6:
        early_checkin = True

    stats = {
        "practice_count": practice_count, "has_perfect": has_perfect, "max_combo": max_combo,
        "boss_kills": boss_kills, "total_questions": total_qs, "modules_mastered": modules_mastered,
        "max_streak": p["max_streak"], "in_guild": in_guild, "guild_messages": guild_messages,
        "lessons_read": lessons_read, "night_practice": night_practice, "early_checkin": early_checkin,
    }

    # Check each achievement
    with get_db_ctx() as db:
        unlocked = set()
        for row in db.execute("SELECT badge_key FROM achievements WHERE player_id=?", (player_id,)).fetchall():
            unlocked.add(row["badge_key"])

    results = []
    for ach in ACHIEVEMENTS:
        is_unlocked = ach["key"] in unlocked
        results.append({
            "key": ach["key"],
            "name": ach.get(f"name_{lang}", ach["name"]) if lang != "zh" else ach["name"],
            "desc": ach.get(f"desc_{lang}", ach["desc"]) if lang != "zh" else ach["desc"],
            "icon": ach["icon"],
            "category": ach["category"],
            "rarity": ach["rarity"],
            "unlocked": is_unlocked,
        })
    return results


def check_and_unlock(player_id: int) -> list:
    """Check all achievement conditions and unlock any newly earned. Returns newly unlocked keys."""
    with get_db_ctx() as db:
        p = db.execute("SELECT * FROM players WHERE id=?", (player_id,)).fetchone()
        if not p:
            return []

        # Same stats as above
        practice_count = db.execute("SELECT COUNT(*) FROM practice_records WHERE player_id=?", (player_id,)).fetchone()[0]
        has_perfect = db.execute("SELECT COUNT(*) FROM practice_records WHERE player_id=? AND correct_count=total_questions AND total_questions>0", (player_id,)).fetchone()[0] > 0
        max_combo_row = db.execute("SELECT MAX(correct_count) as mc FROM practice_records WHERE player_id=?", (player_id,)).fetchone()
        max_combo = max_combo_row["mc"] or 0
        boss_kills = db.execute("SELECT COUNT(*) FROM blind_spots WHERE player_id=? AND status='cleared'", (player_id,)).fetchone()[0]
        total_qs = db.execute("SELECT COALESCE(SUM(total_questions),0) FROM practice_records WHERE player_id=?", (player_id,)).fetchone()[0]
        modules_mastered = db.execute("SELECT COUNT(*) FROM module_mastery WHERE player_id=? AND status='mastered'", (player_id,)).fetchone()[0]
        guild_messages = db.execute("SELECT COUNT(*) FROM guild_messages WHERE player_id=?", (player_id,)).fetchone()[0]
        in_guild = p["guild_id"] is not None

    from datetime import datetime; now = datetime.now()

    stats = {
        "practice_count": practice_count, "has_perfect": has_perfect, "max_combo": max_combo,
        "boss_kills": boss_kills, "total_questions": total_qs, "modules_mastered": modules_mastered,
        "max_streak": p["max_streak"], "in_guild": in_guild, "guild_messages": guild_messages,
        "lessons_read": 0, "night_practice": now.hour >= 22 or now.hour < 6,
        "early_checkin": now.hour < 6,
    }

    with get_db_ctx() as db:
        already = set(r[0] for r in db.execute("SELECT badge_key FROM achievements WHERE player_id=?", (player_id,)).fetchall())
        newly = []

        for ach in ACHIEVEMENTS:
            if ach["key"] in already:
                continue
            if _evaluate_condition(ach["condition"], stats):
                db.execute("INSERT INTO achievements (player_id, badge_key, unlocked_date) VALUES (?,?,datetime('now'))",
                           (player_id, ach["key"]))
                newly.append(ach["key"])

        db.commit()
    return newly
