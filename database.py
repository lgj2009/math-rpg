import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "math_rpg.db")


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    # All CREATE TABLE statements from the spec data model section
    # (16 tables total — defined in the spec's data model and question bank sections)
    tables = [
        # 1. players
        """CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            xp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            title TEXT DEFAULT '数学学徒',
            prestige_count INTEGER DEFAULT 0,
            streak_days INTEGER DEFAULT 0,
            max_streak INTEGER DEFAULT 0,
            streak_shields INTEGER DEFAULT 1,
            focus_energy INTEGER DEFAULT 100,
            focus_max INTEGER DEFAULT 100,
            last_energy_refill TEXT,
            season_xp INTEGER DEFAULT 0,
            battle_pass_tier INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            owned_cosmetics TEXT DEFAULT '[]',
            guild_id INTEGER,
            guild_role TEXT DEFAULT 'member',
            last_login TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        )""",

        # 2. modules (知识模块)
        """CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            name_en TEXT, name_vi TEXT,
            weight INTEGER NOT NULL DEFAULT 10,
            tier INTEGER NOT NULL DEFAULT 1,
            sort_order INTEGER NOT NULL DEFAULT 0,
            icon TEXT DEFAULT '📐',
            description TEXT
        )""",

        # 3. module_mastery (模块掌握度)
        """CREATE TABLE IF NOT EXISTS module_mastery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL,
            accuracy_avg REAL DEFAULT 0,
            speed_qualify INTEGER DEFAULT 0,
            retention_score REAL DEFAULT 0,
            mistake_clear_rate REAL DEFAULT 0,
            stability_score REAL DEFAULT 0,
            status TEXT DEFAULT 'new',
            mastered_date TEXT,
            UNIQUE(player_id, module_id)
        )""",

        # 4. daily_tasks (每日任务)
        """CREATE TABLE IF NOT EXISTS daily_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            module_id INTEGER,
            task_type TEXT NOT NULL,
            content TEXT NOT NULL,
            time_limit_min INTEGER,
            xp_reward INTEGER DEFAULT 30,
            completed INTEGER DEFAULT 0,
            actual_time_min INTEGER,
            scheduled_date TEXT NOT NULL,
            completed_date TEXT
        )""",

        # 5. mistakes (错题本)
        """CREATE TABLE IF NOT EXISTS mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            wrong_step TEXT,
            correct_thought TEXT,
            knowledge_point TEXT,
            error_type TEXT,
            retry_count INTEGER DEFAULT 0,
            last_retry_date TEXT,
            last_retry_correct INTEGER DEFAULT 0,
            mastered INTEGER DEFAULT 0,
            created_date TEXT DEFAULT (datetime('now'))
        )""",

        # 6. blind_spots (知识盲点 → 怪物)
        """CREATE TABLE IF NOT EXISTS blind_spots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            parent_id INTEGER,
            textbook_ref TEXT,
            module_ids TEXT NOT NULL DEFAULT '[]',
            hp_total INTEGER DEFAULT 100,
            hp_current INTEGER DEFAULT 100,
            boss_type TEXT DEFAULT 'normal',
            guild_id INTEGER,
            status TEXT DEFAULT 'active',
            defeat_count INTEGER DEFAULT 0,
            created_from_mistake_id INTEGER,
            created_date TEXT DEFAULT (datetime('now'))
        )""",

        # 7. blind_spot_rounds (盲点复测轮次)
        """CREATE TABLE IF NOT EXISTS blind_spot_rounds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            blind_spot_id INTEGER NOT NULL,
            round INTEGER NOT NULL CHECK(round BETWEEN 1 AND 4),
            question TEXT NOT NULL,
            question_type TEXT DEFAULT 'variant',
            scheduled_date TEXT NOT NULL,
            result TEXT DEFAULT 'pending',
            answered_date TEXT
        )""",

        # 8. practice_records (刷题记录)
        """CREATE TABLE IF NOT EXISTS practice_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            module_id INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            correct_count INTEGER NOT NULL,
            time_used_sec INTEGER,
            session_id TEXT,
            answered_question_ids TEXT DEFAULT '[]',
            practice_date TEXT DEFAULT (datetime('now'))
        )""",

        # 9. checkins (打卡)
        """CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            checkin_date TEXT NOT NULL,
            UNIQUE(player_id, checkin_date)
        )""",

        # 10. achievements (成就)
        """CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            badge_key TEXT NOT NULL,
            unlocked_date TEXT,
            displayed INTEGER DEFAULT 0,
            UNIQUE(player_id, badge_key)
        )""",

        # 11. seasons (赛季)
        """CREATE TABLE IF NOT EXISTS seasons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            reward_tiers TEXT NOT NULL DEFAULT '[]',
            active INTEGER DEFAULT 1
        )""",

        # 12. cosmetic_drops_log (掉落播报)
        """CREATE TABLE IF NOT EXISTS cosmetic_drops_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER NOT NULL,
            item_rarity TEXT NOT NULL,
            item_name TEXT NOT NULL,
            module_name TEXT,
            timestamp TEXT DEFAULT (datetime('now'))
        )""",

        # 14. question_patterns (出题模式)
        """CREATE TABLE IF NOT EXISTS question_patterns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            template TEXT NOT NULL,
            difficulty_base INTEGER DEFAULT 1,
            variant_axes TEXT NOT NULL,
            source_question TEXT
        )""",

        # 15. questions (题目)
        """CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_id INTEGER NOT NULL,
            pattern_id INTEGER,
            type TEXT NOT NULL,
            difficulty INTEGER DEFAULT 1,
            difficulty_dynamic REAL,
            total_attempts INTEGER DEFAULT 0,
            total_correct INTEGER DEFAULT 0,
            concepts TEXT NOT NULL DEFAULT '[]',
            step_count INTEGER DEFAULT 1,
            has_trap INTEGER DEFAULT 0,
            content TEXT NOT NULL,
            content_en TEXT, content_vi TEXT,
            options TEXT,
            options_en TEXT, options_vi TEXT,
            answer TEXT NOT NULL,
            answer_en TEXT, answer_vi TEXT,
            solution TEXT,
            solution_en TEXT, solution_vi TEXT,
            time_limit_sec INTEGER,
            variant_of INTEGER,
            variant_axis TEXT,
            source_type TEXT DEFAULT 'generated',
            source_ref TEXT
        )""",

        # 16. concept_dependencies (知识点依赖图)
        """CREATE TABLE IF NOT EXISTS concept_dependencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_name TEXT NOT NULL,
            parent_concept TEXT,
            textbook_ref TEXT
        )""",
    ]
    for sql in tables:
        cur.execute(sql)

    # Migration: add columns that may not exist in older databases
    for col_sql in [
        "ALTER TABLE practice_records ADD COLUMN session_id TEXT",
        "ALTER TABLE practice_records ADD COLUMN answered_question_ids TEXT DEFAULT '[]'",
    ]:
        try:
            cur.execute(col_sql)
        except sqlite3.OperationalError:
            pass  # column already exists

    # Unique index for INSERT OR IGNORE idempotency in seed_data.py
    cur.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS idx_concept_deps_unique "
        "ON concept_dependencies(concept_name, COALESCE(parent_concept, ''))"
    )
    cur.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS idx_questions_content "
        "ON questions(module_id, content)"
    )

    # Guild tables
    cur.execute("""CREATE TABLE IF NOT EXISTS guilds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT DEFAULT '',
        owner_id INTEGER NOT NULL,
        member_count INTEGER DEFAULT 1,
        daily_xp INTEGER DEFAULT 0,
        weekly_xp INTEGER DEFAULT 0,
        boss_hp INTEGER DEFAULT 500,
        boss_max_hp INTEGER DEFAULT 500,
        created_at TEXT DEFAULT (datetime('now'))
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS guild_members (
        guild_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        role TEXT DEFAULT 'member',
        weekly_xp INTEGER DEFAULT 0,
        joined_at TEXT DEFAULT (datetime('now')),
        PRIMARY KEY (guild_id, player_id)
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS guild_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guild_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        username TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS guild_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guild_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        username TEXT NOT NULL,
        action TEXT NOT NULL,
        detail TEXT DEFAULT '',
        xp INTEGER DEFAULT 0,
        created_at TEXT DEFAULT (datetime('now'))
    )""")

    # Membership table
    cur.execute("""CREATE TABLE IF NOT EXISTS user_memberships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER NOT NULL,
        plan TEXT NOT NULL DEFAULT 'free',
        expires_at TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )""")

    # Concept notes — per-layer user annotations
    cur.execute("""CREATE TABLE IF NOT EXISTS concept_notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER NOT NULL,
        concept_name TEXT NOT NULL,
        layer_id INTEGER NOT NULL DEFAULT 0,
        note_text TEXT NOT NULL DEFAULT '',
        updated_at TEXT DEFAULT (datetime('now')),
        UNIQUE(player_id, concept_name, layer_id)
    )""")

    # Auth tables
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS sessions (
        token TEXT PRIMARY KEY,
        user_id INTEGER NOT NULL,
        player_id INTEGER,
        expires_at TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")

    # Feedback table
    cur.execute("""CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER,
        username TEXT,
        category TEXT DEFAULT 'general',
        message TEXT NOT NULL,
        page TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )""")

    conn.commit()
    conn.close()
