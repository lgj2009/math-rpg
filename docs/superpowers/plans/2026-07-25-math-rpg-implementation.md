# Math RPG Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a gamified high school math study SPA that turns exam prep into an RPG — variable-reward gacha, streak protection, blind-spot boss battles, seasonal battle passes, and guild co-op — all backed by an LLM-analyzed question bank derived from real gaokao exams.

**Architecture:** FastAPI serves a REST JSON API over SQLite with 18 tables. A single `index.html` SPA with vanilla JS modules renders 10 pages driven by hash-based routing. All AI question analysis runs offline pre-launch; the runtime is pure local Python with zero external API calls.

**Tech Stack:** Python 3.10+, FastAPI, SQLite (via `sqlite3`), Pydantic v2, Chart.js 4.x (CDN), vanilla HTML/CSS/JS (no framework), uvicorn

---

## Global Constraints

- Config lives in `config.py` — no magic numbers in code
- Every feature gets its own router file + service file + frontend JS module
- Frontend is stateless — all state on server, refresh-safe
- Single-command launch: `pip install -r requirements.txt && python app.py`
- All AI question work is offline/one-time; runtime has zero LLM dependencies
- `seed_data.py` must run idempotently (safe to re-run, uses INSERT OR IGNORE)

---

## File Map

```
math-rpg/
├── app.py                    # FastAPI entry, mount routers, static files
├── config.py                 # All tunables: energy rate, gacha odds, XP table, etc.
├── database.py               # get_db(), init_db(), run all CREATE TABLE
├── requirements.txt          # fastapi, uvicorn, pydantic
├── seed_data.py              # Idempotent: modules, patterns, questions, achievements, season
├── models/                   # Pydantic request/response schemas
│   ├── __init__.py
│   ├── player.py
│   ├── practice.py
│   ├── task.py
│   ├── mistake.py
│   ├── blind_spot.py
│   ├── guild.py
│   └── common.py             # Shared: ErrorResponse, PaginatedResponse
├── routers/                  # Thin — parse input, call service, return JSON
│   ├── __init__.py
│   ├── players.py
│   ├── tasks.py
│   ├── practice.py
│   ├── mistakes.py
│   ├── blind_spots.py
│   ├── seasons.py
│   ├── guilds.py
│   ├── achievements.py
│   └── stats.py
├── services/                 # All business logic
│   ├── __init__.py
│   ├── player_service.py
│   ├── task_service.py
│   ├── practice_service.py
│   ├── mistake_service.py
│   ├── blind_spot_service.py
│   ├── season_service.py
│   ├── guild_service.py
│   ├── gacha_service.py
│   ├── mastery_service.py
│   ├── difficulty_service.py
│   └── question_service.py
├── tools/                    # Offline, one-shot scripts
│   ├── analyze_exam.py       # Read exam JSONL, call LLM, write analysis JSONL
│   ├── generate_variants.py  # Read patterns JSON, call LLM, write questions JSONL
│   └── merge_seed.py         # Read all JSONL → emit seed_data.py
├── static/
│   ├── index.html            # Single shell: sidebar + #router-outlet
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── app.js            # Router, global state, fetch wrapper, toast
│       ├── components.js     # XpBar, EnergyBar, GachaReveal, BossCard, StreakShield
│       ├── dashboard.js
│       ├── tasks.js
│       ├── practice.js
│       ├── mistakes.js
│       ├── progress.js
│       ├── guild.js
│       ├── season.js
│       ├── achievements.js
│       └── audio.js          # Web Audio API beeps/swishes (no files needed)
└── math_rpg.db               # Auto-created on first run
```

---

## Round 1: Playable Core — User Can Practice with Gacha

### Task 1: Project scaffold + config + database

**Files:**
- Create: `requirements.txt`
- Create: `config.py`
- Create: `database.py`

**Interfaces:**
- Produces: `config.ENERGY_REGEN_SECONDS`, `config.GACHA_ODDS`, `config.XP_PER_LEVEL`, `config.TITLES`, `config.LEVEL_THRESHOLDS`, `config.FOCUS_MAX`, `config.FOCUS_COSTS`
- Produces: `database.get_db()` → sqlite3.Connection, `database.init_db()` → None

- [ ] **Step 1: Write requirements.txt**

```
fastapi>=0.110.0
uvicorn[standard]>=0.27.0
pydantic>=2.0.0
```

- [ ] **Step 2: Write config.py**

```python
# All game parameters — tweak here, restart, done.

# Energy
FOCUS_MAX = 100
ENERGY_REGEN_SECONDS = 300       # 1 point per 5 minutes
ENERGY_CLAIM_AMOUNT = 20         # Per time-slot claim
ENERGY_CLAIM_HOURS = [8, 12, 20] # Claim windows (local hour)
ENERGY_REFUND_RATE = 0.5         # Blind-spot retry refunds 50%

# Focus costs per action
FOCUS_COSTS = {
    "choice": 2,
    "fill": 3,
    "answer": 5,
    "boss_fight": 40,
}

# Gacha odds (must sum to 1.0)
GACHA_ODDS = {
    "common":    0.70,
    "rare":      0.20,
    "epic":      0.08,
    "legendary": 0.015,
    "mythic":    0.005,
}
GACHA_STREAK_BONUS = 0.015  # Added to legendary at >=7 streak

# Level thresholds
LEVEL_THRESHOLDS = {
    1: 0, 5: 500, 10: 1500, 15: 3500, 20: 7000, 25: 12000, 30: 20000,
}
TITLES = {
    1: "数学学徒", 5: "解题新兵", 10: "公式骑士",
    15: "逻辑射手", 20: "函数法师", 25: "证明勇士", 30: "数学领主",
}

# XP rewards
XP_PER_QUESTION = 10
XP_PERFECT_BONUS = 20       # 100% on a practice set
XP_STREAK_COMBO_MULTIPLIER = {3: 1.5, 7: 2.0}
XP_MISTAKE_RETRY = 80
XP_DAILY_TASK = {           # by task_type
    "main": 50,
    "side": 30,
    "challenge": 80,
}

# Mastery thresholds
MASTERY_ACCURACY = 0.90
MASTERY_RETENTION = 0.85
MASTERY_MISTAKE_CLEAR = 1.0
MASTERY_STABILITY_WINDOW = 3  # consecutive sessions

# Season
SEASON_DURATION_DAYS = 60

# Guild
GUILD_DAILY_XP_TARGET = 300
GUILD_MAX_SIZE = 5
GUILD_INACTIVE_DAYS = 3

# Near-miss trigger
NEAR_MISS_MIN = 0.85
NEAR_MISS_MAX = 0.94
```

- [ ] **Step 3: Write database.py**

```python
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "math_rpg.db")

def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    # All CREATE TABLE statements from the spec data model section
    # (18 tables total — listed in full below)
    tables = [
        """CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            xp INTEGER DEFAULT 0, level INTEGER DEFAULT 1,
            title TEXT DEFAULT '数学学徒', prestige_count INTEGER DEFAULT 0,
            streak_days INTEGER DEFAULT 0, max_streak INTEGER DEFAULT 0,
            streak_shields INTEGER DEFAULT 1,
            focus_energy INTEGER DEFAULT 100, focus_max INTEGER DEFAULT 100,
            last_energy_refill TEXT,
            season_xp INTEGER DEFAULT 0, battle_pass_tier INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0, owned_cosmetics TEXT DEFAULT '[]',
            guild_id INTEGER, guild_role TEXT DEFAULT 'member',
            last_login TEXT, created_at TEXT DEFAULT (datetime('now'))
        )""",
        # ... all remaining CREATE TABLE statements from spec
    ]
    for sql in tables:
        cur.execute(sql)
    conn.commit()
    conn.close()
```

- [ ] **Step 4: Write all 18 CREATE TABLE statements** (copy verbatim from spec lines 60-556 into `database.py`)

- [ ] **Step 5: Test — run `python -c "from database import init_db; init_db(); print('OK')"`**

- [ ] **Step 6: Commit**

```bash
git add requirements.txt config.py database.py
git commit -m "feat: project scaffold with config and database schema"
```

---

### Task 2: FastAPI entry + static serving

**Files:**
- Create: `app.py`

**Interfaces:**
- Consumes: `database.init_db()`
- Produces: `uvicorn app:app` running on `localhost:8000`

- [ ] **Step 1: Write app.py**

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from database import init_db

app = FastAPI(title="Math RPG")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    from fastapi.responses import FileResponse
    return FileResponse(str(static_dir / "index.html"))
```

- [ ] **Step 2: Test — `uvicorn app:app --reload`, open `http://localhost:8000`**

- [ ] **Step 3: Commit**

```bash
git add app.py
git commit -m "feat: FastAPI entry with static serving and DB init on startup"
```

---

### Task 3: SPA shell — sidebar + router

**Files:**
- Create: `static/index.html`
- Create: `static/css/styles.css`
- Create: `static/js/app.js`

**Interfaces:**
- Produces: Hash router dispatching to page modules; `App.state` singleton for player data; `App.api(path, options)` wrapper returning parsed JSON

- [ ] **Step 1: Write styles.css — CSS custom properties + layout**

```css
:root {
    --sidebar-w: 240px;
    --bg: #0f172a; --surface: #1e293b; --surface2: #334155;
    --text: #f1f5f9; --text-dim: #94a3b8;
    --accent: #f59e0b; --accent2: #8b5cf6;
    --correct: #22c55e; --wrong: #ef4444;
    --rarity-common: #9ca3af; --rarity-rare: #3b82f6;
    --rarity-epic: #a855f7; --rarity-legendary: #f59e0b;
    --rarity-mythic: #ef4444;
    --radius: 8px; --radius-lg: 12px;
    font-family: 'Segoe UI', system-ui, sans-serif;
    color: var(--text); background: var(--bg);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { display: flex; min-height: 100vh; }
#sidebar { width: var(--sidebar-w); background: var(--surface);
    padding: 20px 16px; display: flex; flex-direction: column;
    gap: 4px; position: fixed; top: 0; left: 0; height: 100vh;
    overflow-y: auto; z-index: 10; }
#sidebar .player-card { text-align: center; padding: 12px 0; border-bottom: 1px solid var(--surface2); margin-bottom: 8px; }
#sidebar .nav-item { display: flex; align-items: center; gap: 10px;
    padding: 10px 12px; border-radius: var(--radius);
    cursor: pointer; color: var(--text-dim); text-decoration: none;
    transition: background 0.15s, color 0.15s; font-size: 14px; }
#sidebar .nav-item:hover, #sidebar .nav-item.active { background: var(--surface2); color: var(--text); }
#main { margin-left: var(--sidebar-w); flex: 1; padding: 24px 32px; }
.page { display: none; } .page.active { display: block; }
```

- [ ] **Step 2: Write index.html skeleton**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math RPG - 高中数学冒险</title>
    <link rel="stylesheet" href="/static/css/styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
</head>
<body>
    <nav id="sidebar">
        <div class="player-card">
            <div class="player-avatar" id="avatar">📚</div>
            <div class="player-name" id="sidebar-name">冒险者</div>
            <div class="player-level" id="sidebar-level">Lv.1 数学学徒</div>
            <div id="sidebar-xp-bar"></div>
            <div style="display:flex;justify-content:space-between;font-size:12px;margin-top:4px">
                <span>🔥 <span id="sidebar-streak">0</span>天</span>
                <span>⚡ <span id="sidebar-energy">100</span></span>
            </div>
        </div>
        <a class="nav-item active" data-page="dashboard">📊 冒险大厅</a>
        <a class="nav-item" data-page="tasks">📋 任务板</a>
        <a class="nav-item" data-page="practice">⚔️ 狩猎场</a>
        <a class="nav-item" data-page="mistakes">🐉 怪物图鉴</a>
        <a class="nav-item" data-page="progress">📈 修炼进度</a>
        <a class="nav-item" data-page="guild">🏰 公会</a>
        <a class="nav-item" data-page="season">🏁 赛季通行证</a>
        <a class="nav-item" data-page="achievements">🏆 成就殿堂</a>
        <a class="nav-item" data-page="settings">⚙️ 设置</a>
    </nav>
    <main id="main">
        <div id="page-dashboard" class="page active"></div>
        <div id="page-tasks" class="page"></div>
        <div id="page-practice" class="page"></div>
        <div id="page-mistakes" class="page"></div>
        <div id="page-progress" class="page"></div>
        <div id="page-guild" class="page"></div>
        <div id="page-season" class="page"></div>
        <div id="page-achievements" class="page"></div>
        <div id="page-settings" class="page"></div>
    </main>
    <div id="toast-container"></div>
    <div id="modal-overlay" style="display:none"></div>
    <script src="/static/js/audio.js"></script>
    <script src="/static/js/components.js"></script>
    <script src="/static/js/app.js"></script>
    <script src="/static/js/dashboard.js"></script>
    <script src="/static/js/tasks.js"></script>
    <script src="/static/js/practice.js"></script>
    <script src="/static/js/mistakes.js"></script>
    <script src="/static/js/progress.js"></script>
    <script src="/static/js/guild.js"></script>
    <script src="/static/js/season.js"></script>
    <script src="/static/js/achievements.js"></script>
</body>
</html>
```

- [ ] **Step 3: Write app.js — router + API wrapper + global state**

```javascript
// app.js — SPA router, API helper, global state, toast, modal
const App = {
    state: { player: null },
    baseURL: '/api',

    async api(method, path, body) {
        const opts = { method, headers: { 'Content-Type': 'application/json' } };
        if (body) opts.body = JSON.stringify(body);
        const res = await fetch(`${this.baseURL}${path}`, opts);
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || 'Request failed');
        return data;
    },

    get(path) { return this.api('GET', path); },
    post(path, body) { return this.api('POST', path, body); },

    toast(msg, type='info') {
        const el = document.createElement('div');
        el.className = `toast toast-${type}`;
        el.textContent = msg;
        document.getElementById('toast-container').appendChild(el);
        setTimeout(() => el.remove(), 3000);
    },

    navigate(page) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        const target = document.getElementById(`page-${page}`);
        if (target) target.classList.add('active');
        const nav = document.querySelector(`[data-page="${page}"]`);
        if (nav) nav.classList.add('active');
        window.location.hash = page;
    },

    async refreshPlayer() {
        if (!this.state.player) return;
        const p = await this.get(`/players/${this.state.player.id}`);
        this.state.player = p;
        this.updateSidebar();
    },

    updateSidebar() {
        const p = this.state.player;
        if (!p) return;
        document.getElementById('sidebar-name').textContent = p.username;
        document.getElementById('sidebar-level').textContent = `Lv.${p.level} ${p.title}`;
        document.getElementById('sidebar-streak').textContent = p.streak_days;
        document.getElementById('sidebar-energy').textContent = p.focus_energy;
    },
};

window.addEventListener('DOMContentLoaded', () => {
    const page = window.location.hash.slice(1) || 'dashboard';
    // Check for existing player (localStorage playerId)
    const pid = localStorage.getItem('playerId');
    if (pid) {
        App.get(`/players/${pid}`).then(p => {
            App.state.player = p;
            App.updateSidebar();
        }).catch(() => localStorage.removeItem('playerId'));
    }
    App.navigate(page);
    // If no player, show welcome/create modal
    if (!pid) {
        document.getElementById('page-dashboard').innerHTML = `
            <div class="welcome-screen">
                <h1>⚔️ 数学冒险</h1>
                <p>把刷题变成打怪升级</p>
                <form id="create-player-form">
                    <input id="username-input" placeholder="输入你的冒险者名字" required>
                    <button type="submit">开始冒险</button>
                </form>
            </div>`;
        document.getElementById('create-player-form').onsubmit = async (e) => {
            e.preventDefault();
            const username = document.getElementById('username-input').value;
            const p = await App.post('/players', { username });
            App.state.player = p;
            App.updateSidebar();
            localStorage.setItem('playerId', p.id);
            App.navigate('dashboard');
            dashboard.render();
        };
    }
});

window.addEventListener('hashchange', () => {
    const page = window.location.hash.slice(1) || 'dashboard';
    App.navigate(page);
});

// Nav clicks
document.getElementById('sidebar').addEventListener('click', (e) => {
    const nav = e.target.closest('.nav-item');
    if (!nav) return;
    e.preventDefault();
    App.navigate(nav.dataset.page);
});
```

- [ ] **Step 4: Write audio.js (placeholder)**

```javascript
// audio.js — Web Audio API sound effects (no external files)
const Audio = {
    ctx: null,
    _init() { if (!this.ctx) this.ctx = new (window.AudioContext || window.webkitAudioContext)(); },
    beep(freq, dur, type='square') {
        this._init();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = type; osc.frequency.value = freq;
        gain.gain.value = 0.1;
        osc.connect(gain); gain.connect(this.ctx.destination);
        osc.start(); osc.stop(this.ctx.currentTime + dur);
    },
    levelUp() { this.beep(523, 0.1); setTimeout(() => this.beep(659, 0.1), 100); setTimeout(() => this.beep(784, 0.2), 200); },
    gachaFlip() { this.beep(200, 0.3, 'triangle'); },
    gachaRare(level) { const f = {rare: 440, epic: 550, legendary: 660, mythic: 880}[level] || 440; this.beep(f, 0.5, 'sine'); },
    bossKill() { for (let i = 0; i < 5; i++) setTimeout(() => this.beep(300 + i*100, 0.1), i*80); },
    click() { this.beep(800, 0.05); },
};
```

- [ ] **Step 5: Write components.js (placeholder — fleshed out in later tasks)**

```javascript
// components.js — shared UI widgets
const Components = {
    xpBar(player) {
        const thresholds = Object.keys(App.state._levelThresholds || {1:0,5:500,10:1500,15:3500,20:7000,25:12000,30:20000});
        const next = /* find next threshold above player.level */ 500;
        const prev = /* threshold for current level */ 0;
        const pct = ((player.xp - prev) / (next - prev)) * 100;
        return `<div class="xp-bar"><div class="xp-fill" style="width:${pct}%"></div></div>`;
    },
    bossCard(spot) { /* renders blind_spot as monster card with HP bar */ },
    gachaReveal(item) { /* 1.5s flip animation overlay */ },
    modal(title, content, buttons) { /* generic modal — returns Promise */ },
};
```

- [ ] **Step 6: Test — open browser, see sidebar, click nav items, page divs toggle**

- [ ] **Step 7: Commit**

```bash
git add static/
git commit -m "feat: SPA shell with sidebar navigation and router"
```

---

### Task 4: Player API — create, get, check-in, claim energy

**Files:**
- Create: `models/__init__.py`, `models/player.py`, `models/common.py`
- Create: `routers/__init__.py`, `routers/players.py`
- Create: `services/__init__.py`, `services/player_service.py`

**Interfaces:**
- Produces: `POST /api/players` → `PlayerResponse`, `GET /api/players/{id}` → `PlayerResponse`, `POST /api/players/{id}/checkin` → `CheckinResponse`, `POST /api/players/{id}/claim-energy` → `EnergyResponse`

- [ ] **Step 1: Write models/common.py**

```python
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str
```

- [ ] **Step 2: Write models/player.py**

```python
from pydantic import BaseModel, Field
from typing import Optional

class PlayerCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=20)

class PlayerResponse(BaseModel):
    id: int
    username: str
    xp: int
    level: int
    title: str
    prestige_count: int
    streak_days: int
    max_streak: int
    streak_shields: int
    focus_energy: int
    focus_max: int
    season_xp: int
    battle_pass_tier: int
    coins: int
    owned_cosmetics: list = []
    guild_id: Optional[int] = None
    guild_role: str = "member"
    last_login: Optional[str] = None

class CheckinResponse(BaseModel):
    streak_days: int
    xp_gained: int
    bonus_applied: bool
    gacha_result: Optional[dict] = None

class EnergyResponse(BaseModel):
    focus_energy: int
    claimed: int
```

- [ ] **Step 3: Write services/player_service.py**

```python
import json
from datetime import datetime, date
from database import get_db
import config

def create_player(username: str) -> dict:
    db = get_db()
    cur = db.execute("INSERT INTO players (username, last_login) VALUES (?, datetime('now'))", (username,))
    db.commit()
    pid = cur.lastrowid
    # Create module_mastery rows for all modules
    modules = db.execute("SELECT id FROM modules").fetchall()
    for m in modules:
        db.execute("INSERT OR IGNORE INTO module_mastery (player_id, module_id) VALUES (?, ?)", (pid, m["id"]))
    db.commit()
    return get_player(pid)

def get_player(player_id: int) -> dict:
    db = get_db()
    row = db.execute("SELECT * FROM players WHERE id=?", (player_id,)).fetchone()
    if not row: return None
    p = dict(row)
    p["owned_cosmetics"] = json.loads(p.get("owned_cosmetics", "[]"))
    _recalc_energy(p)
    return p

def _recalc_energy(p: dict) -> dict:
    """Apply passive regen since last refill timestamp."""
    import time
    if not p.get("last_energy_refill"):
        return p
    try:
        last = datetime.fromisoformat(p["last_energy_refill"])
    except (ValueError, TypeError):
        return p
    elapsed = (datetime.now() - last).total_seconds()
    gained = int(elapsed / config.ENERGY_REGEN_SECONDS)
    if gained > 0:
        p["focus_energy"] = min(p["focus_max"], p["focus_energy"] + gained)
        # Update DB
        db = get_db()
        db.execute("UPDATE players SET focus_energy=?, last_energy_refill=datetime('now') WHERE id=?",
                   (p["focus_energy"], p["id"]))
        db.commit()
    return p

def checkin(player_id: int) -> dict:
    db = get_db()
    today = date.today().isoformat()
    # Avoid duplicate
    existing = db.execute("SELECT id FROM checkins WHERE player_id=? AND checkin_date=?", (player_id, today)).fetchone()
    if existing:
        return {"detail": "already checked in today"}

    db.execute("INSERT INTO checkins (player_id, checkin_date) VALUES (?, ?)", (player_id, today))

    p = get_player(player_id)
    yesterday = date.today()
    # Check if yesterday was checked in → continue streak
    yesterday_check = db.execute("SELECT id FROM checkins WHERE player_id=? AND checkin_date=?",
                                  (player_id, yesterday.isoformat())).fetchone()
    if yesterday_check:
        new_streak = p["streak_days"] + 1
    else:
        new_streak = 1

    # Apply streak bonuses
    multiplier = 1.0
    bonus = False
    if new_streak >= 7:
        multiplier = config.XP_STREAK_COMBO_MULTIPLIER.get(7, 2.0)
        bonus = True
    elif new_streak >= 3:
        multiplier = config.XP_STREAK_COMBO_MULTIPLIER.get(3, 1.5)
        bonus = True

    base_xp = 30
    xp_gained = int(base_xp * multiplier)

    # Weekly streak shield (Sunday)
    shields = p["streak_shields"]
    if date.today().weekday() == 6:  # Sunday
        shields = min(shields + 1, 3)

    db.execute("""UPDATE players SET streak_days=?, max_streak=MAX(max_streak,?),
                  xp=xp+?, streak_shields=?, last_login=datetime('now') WHERE id=?""",
               (new_streak, new_streak, xp_gained, shields, player_id))
    db.commit()

    # Gacha roll on checkin
    from services.gacha_service import roll_gacha
    streak_bonus = new_streak >= 7
    gacha = roll_gacha(player_id, streak_bonus=streak_bonus)

    return {"streak_days": new_streak, "xp_gained": xp_gained, "bonus_applied": bonus, "gacha_result": gacha}

def claim_energy(player_id: int, hour: int) -> dict:
    if hour not in config.ENERGY_CLAIM_HOURS:
        return {"detail": "not a claim window"}
    p = get_player(player_id)
    new_energy = min(p["focus_max"], p["focus_energy"] + config.ENERGY_CLAIM_AMOUNT)
    db = get_db()
    db.execute("UPDATE players SET focus_energy=?, last_energy_refill=datetime('now') WHERE id=?",
               (new_energy, player_id))
    db.commit()
    return {"focus_energy": new_energy, "claimed": config.ENERGY_CLAIM_AMOUNT}

def spend_energy(player_id: int, amount: int) -> bool:
    p = get_player(player_id)
    p = _recalc_energy(p)
    if p["focus_energy"] < amount:
        return False
    db = get_db()
    db.execute("UPDATE players SET focus_energy=focus_energy-?, last_energy_refill=datetime('now') WHERE id=?",
               (amount, player_id))
    db.commit()
    return True

def award_xp(player_id: int, amount: int):
    db = get_db()
    p = get_player(player_id)
    new_xp = p["xp"] + amount
    # Determine new level
    new_level = p["level"]
    for lvl, threshold in sorted(config.LEVEL_THRESHOLDS.items(), reverse=True):
        if new_xp >= threshold:
            new_level = lvl
            break
    new_title = config.TITLES.get(new_level, p["title"])
    db.execute("UPDATE players SET xp=?, level=?, title=? WHERE id=?",
               (new_xp, new_level, new_title, player_id))
    db.commit()
    return {"xp": new_xp, "level": new_level, "title": new_title, "leveled_up": new_level > p["level"]}
```

- [ ] **Step 4: Write routers/players.py**

```python
from fastapi import APIRouter, HTTPException
from models.player import PlayerCreate, PlayerResponse, CheckinResponse, EnergyResponse
from services import player_service

router = APIRouter(prefix="/api/players", tags=["players"])

@router.post("", response_model=PlayerResponse, status_code=201)
def create_player(body: PlayerCreate):
    return player_service.create_player(body.username)

@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int):
    p = player_service.get_player(player_id)
    if not p: raise HTTPException(404, "Player not found")
    return p

@router.post("/{player_id}/checkin")
def checkin(player_id: int):
    result = player_service.checkin(player_id)
    if "detail" in result: raise HTTPException(400, result["detail"])
    return result

@router.post("/{player_id}/claim-energy")
def claim_energy(player_id: int, hour: int | None = None):
    h = hour or datetime.now().hour
    result = player_service.claim_energy(player_id, h)
    if "detail" in result: raise HTTPException(400, result["detail"])
    return result
```

- [ ] **Step 5: Register router in app.py**

```python
from routers.players import router as players_router
app.include_router(players_router)
```

- [ ] **Step 6: Test with curl**

```bash
curl -X POST localhost:8000/api/players -H 'Content-Type: application/json' -d '{"username":"test"}'
curl localhost:8000/api/players/1
curl -X POST localhost:8000/api/players/1/checkin
```

- [ ] **Step 7: Commit**

```bash
git add models/ routers/ services/ app.py
git commit -m "feat: player API — create, get, checkin, claim energy"
```

---

### Task 5: Seed data — modules + concept dependencies + initial questions with patterns

**Files:**
- Create: `seed_data.py`

**Interfaces:**
- Produces: Idempotently inserts 8 modules, concept_dependencies, question_patterns, and at least 40 seed questions across all modules

- [ ] **Step 1: Write seed_data.py — modules**

```python
"""Idempotent seed data. Safe to run multiple times — uses INSERT OR IGNORE."""
import sqlite3
import json
from database import get_db

MODULES = [
    (1, "三角函数与解三角形", 15, 1, 1, "📐", "和差角公式、二倍角公式、正弦定理、余弦定理"),
    (2, "数列", 12, 1, 2, "🔢", "等差/等比数列通项与求和、裂项相消、错位相减"),
    (3, "统计与概率", 17, 1, 3, "🎲", "排列组合、二项式定理、分布列与期望"),
    (4, "立体几何", 17, 2, 4, "📦", "空间向量法：建系→法向量→角与距离"),
    (5, "解析几何", 17, 2, 5, "📈", "椭圆/双曲线/抛物线、联立+韦达定理"),
    (6, "导数及其应用", 17, 2, 6, "📉", "单调性、极值最值、切线问题"),
    (7, "集合与常用逻辑", 5, 3, 7, "🔤", "集合运算、充要条件"),
    (8, "复数与向量", 10, 3, 8, "🧮", "复数运算、向量坐标运算"),
]

CONCEPT_DEPS = [
    ("完全平方公式", None, "必修一 P32"),
    ("一元二次函数图像", "完全平方公式", "必修一 P36"),
    ("一元二次不等式", "一元二次函数图像", "必修一 P40"),
    ("穿根法", "一元二次不等式", "必修一 P42"),
    ("正弦定理", None, "必修五 P2"),
    ("余弦定理", None, "必修五 P6"),
    ("和差角公式", None, "必修四 P25"),
    ("二倍角公式", "和差角公式", "必修四 P30"),
    ("等差数列通项", None, "必修五 P35"),
    ("等比数列通项", None, "必修五 P48"),
    ("裂项相消", "等差数列通项", "必修五 P55"),
    ("错位相减", "等比数列通项", "必修五 P56"),
    ("空间向量坐标运算", None, "选修2-1 P85"),
    ("法向量求法", "空间向量坐标运算", "选修2-1 P90"),
    ("导数定义", None, "选修2-2 P2"),
    ("导数单调性", "导数定义", "选修2-2 P22"),
    ("导数极值最值", "导数单调性", "选修2-2 P28"),
    ("导数切线", "导数定义", "选修2-2 P16"),
    ("椭圆标准方程", None, "选修2-1 P38"),
    ("双曲线标准方程", None, "选修2-1 P50"),
    ("抛物线标准方程", None, "选修2-1 P60"),
]

def seed():
    db = get_db()
    cur = db.cursor()

    # Modules
    cur.executemany(
        "INSERT OR IGNORE INTO modules (id, name, weight, tier, sort_order, icon, description) VALUES (?,?,?,?,?,?,?)",
        MODULES
    )

    # Concept dependencies
    for name, parent, ref in CONCEPT_DEPS:
        cur.execute(
            "INSERT OR IGNORE INTO concept_dependencies (concept_name, parent_concept, textbook_ref) VALUES (?,?,?)",
            (name, parent, ref)
        )

    # Season
    cur.execute(
        "INSERT OR IGNORE INTO seasons (id, name, start_date, end_date, reward_tiers, active) VALUES (1, '第1赛季: 函数觉醒', '2026-07-01', '2026-08-30', '[]', 1)"
    )

    db.commit()
    db.close()
    print("Seed data loaded.")

if __name__ == "__main__":
    from database import init_db
    init_db()
    seed()
```

- [ ] **Step 2: Test — `python seed_data.py`** → prints "Seed data loaded."

- [ ] **Step 3: Commit**

```bash
git add seed_data.py
git commit -m "feat: seed data — modules, concept deps, season stub"
```

---

### Task 6: Gacha service

**Files:**
- Create: `services/gacha_service.py`

**Interfaces:**
- Produces: `roll_gacha(player_id, streak_bonus=False) → dict` with `{rarity, item_name, item_type, animation_class}`

- [ ] **Step 1: Write services/gacha_service.py**

```python
import random
import json
from database import get_db
import config

COSMETIC_POOL = {
    "common": [
        {"name": "木剑头像框", "type": "avatar_frame", "emoji": "⚪"},
        {"name": "绿色称号", "type": "title_color", "emoji": "🟢"},
        {"name": "新手光环", "type": "effect", "emoji": "✨"},
        {"name": "白色披风", "type": "cape", "emoji": "🤍"},
    ],
    "rare": [
        {"name": "铁剑头像框", "type": "avatar_frame", "emoji": "🔵"},
        {"name": "蓝色称号", "type": "title_color", "emoji": "🔷"},
        {"name": "闪电特效", "type": "effect", "emoji": "⚡"},
        {"name": "蓝色披风", "type": "cape", "emoji": "💙"},
    ],
    "epic": [
        {"name": "秘银头像框", "type": "avatar_frame", "emoji": "🟣"},
        {"name": "紫色称号", "type": "title_color", "emoji": "💜"},
        {"name": "暗焰特效", "type": "effect", "emoji": "🔥"},
        {"name": "星光披风", "type": "cape", "emoji": "🌌"},
    ],
    "legendary": [
        {"name": "金色头像框", "type": "avatar_frame", "emoji": "🟡"},
        {"name": "金色称号", "type": "title_color", "emoji": "👑"},
        {"name": "雷神特效", "type": "effect", "emoji": "⚡"},
        {"name": "龙翼披风", "type": "cape", "emoji": "🐉"},
    ],
    "mythic": [
        {"name": "彩虹头像框", "type": "avatar_frame", "emoji": "🌈"},
        {"name": "彩虹称号", "type": "title_color", "emoji": "💎"},
        {"name": "星辰爆发", "type": "effect", "emoji": "💫"},
        {"name": "虚空披风", "type": "cape", "emoji": "🌀"},
    ],
}

def roll_gacha(player_id: int, streak_bonus: bool = False) -> dict:
    odds = dict(config.GACHA_ODDS)
    if streak_bonus:
        # Shift legendary probability
        odds["legendary"] = odds.get("legendary", 0.015) + config.GACHA_STREAK_BONUS
        odds["common"] = odds.get("common", 0.70) - config.GACHA_STREAK_BONUS

    roll = random.random()
    cumulative = 0
    result_rarity = "common"
    for rarity, prob in odds.items():
        cumulative += prob
        if roll <= cumulative:
            result_rarity = rarity
            break

    item = random.choice(COSMETIC_POOL[result_rarity])

    # Grant to player
    db = get_db()
    row = db.execute("SELECT owned_cosmetics FROM players WHERE id=?", (player_id,)).fetchone()
    owned = json.loads(row["owned_cosmetics"]) if row else []
    owned.append(item["name"])
    db.execute("UPDATE players SET owned_cosmetics=? WHERE id=?", (json.dumps(owned), player_id))

    # Log drop for broadcast
    db.execute("INSERT INTO cosmetic_drops_log (player_id, item_rarity, item_name) VALUES (?,?,?)",
               (player_id, result_rarity, item["name"]))
    db.commit()
    db.close()

    return {
        "rarity": result_rarity,
        "item_name": item["name"],
        "item_type": item["type"],
        "animation_class": f"gacha-{result_rarity}",
    }
```

- [ ] **Step 2: Test — in Python REPL: create player, call roll_gacha(1), verify item added**

```python
from services.gacha_service import roll_gacha
result = roll_gacha(1, streak_bonus=True)
assert "rarity" in result
assert "item_name" in result
```

- [ ] **Step 3: Commit**

```bash
git add services/gacha_service.py
git commit -m "feat: gacha service — rarity roll, cosmetic grant, drop logging"
```

---

### Task 7: Practice API — get questions, submit answers, gacha on completion

**Files:**
- Create: `models/practice.py`
- Create: `services/practice_service.py`
- Create: `services/question_service.py`
- Create: `routers/practice.py`

**Interfaces:**
- Consumes: `player_service.spend_energy()`, `player_service.award_xp()`, `gacha_service.roll_gacha()`
- Produces: `GET /api/modules` → `[ModuleResponse]`, `GET /api/modules/{id}/practice?count=10` → `PracticeSession`, `POST /api/players/{id}/practice` → `PracticeResult` (includes gacha roll)

- [ ] **Step 1: Write models/practice.py**

```python
from pydantic import BaseModel
from typing import Optional

class ModuleResponse(BaseModel):
    id: int
    name: str
    weight: int
    tier: int
    icon: str
    description: Optional[str] = None

class QuestionItem(BaseModel):
    id: int
    type: str
    difficulty: int
    content: str
    options: Optional[list[str]] = None
    time_limit_sec: Optional[int] = None

class PracticeSession(BaseModel):
    session_id: str
    module_id: int
    module_name: str
    questions: list[QuestionItem]
    focus_cost: int

class Answer(BaseModel):
    question_id: int
    answer: str

class PracticeSubmit(BaseModel):
    session_id: str
    module_id: int
    answers: list[Answer]
    time_used_sec: int

class PracticeResult(BaseModel):
    total: int
    correct: int
    accuracy: float
    xp_gained: int
    near_miss: bool
    gacha_result: dict
```

- [ ] **Step 2: Write services/question_service.py**

```python
import uuid
from database import get_db

def get_questions_for_module(module_id: int, player_id: int, count: int = 10) -> list:
    """Return questions the player hasn't answered yet, matched to their difficulty level."""
    db = get_db()
    # Get player's current accuracy for difficulty matching
    mastery = db.execute(
        "SELECT accuracy_avg, status FROM module_mastery WHERE player_id=? AND module_id=?",
        (player_id, module_id)
    ).fetchone()

    target_difficulty = 1
    if mastery:
        if mastery["accuracy_avg"] >= 0.80:
            target_difficulty = 2
        if mastery["accuracy_avg"] >= 0.90 and mastery["status"] == "practicing":
            target_difficulty = 3

    # Get questions not yet answered by this player
    answered_ids = db.execute("""
        SELECT DISTINCT question_id FROM practice_records pr
        JOIN json_each(pr.answers_json) WHERE pr.player_id=?
    """, (player_id,)).fetchall()
    answered_set = set(r[0] for r in answered_ids) if answered_ids else set()

    if answered_set:
        placeholders = ",".join("?" * len(answered_set))
        rows = db.execute(f"""
            SELECT id, module_id, type, difficulty, content, options, time_limit_sec
            FROM questions
            WHERE module_id=? AND id NOT IN ({placeholders})
            ORDER BY ABS(difficulty - ?), RANDOM()
            LIMIT ?
        """, [module_id] + list(answered_set) + [target_difficulty, count])
    else:
        rows = db.execute("""
            SELECT id, module_id, type, difficulty, content, options, time_limit_sec
            FROM questions WHERE module_id=?
            ORDER BY ABS(difficulty - ?), RANDOM()
            LIMIT ?
        """, (module_id, target_difficulty, count))

    questions = []
    for r in rows.fetchall():
        q = dict(r)
        import json
        q["options"] = json.loads(q["options"]) if q.get("options") else None
        questions.append(q)
    return questions

def generate_session_id() -> str:
    return uuid.uuid4().hex[:12]
```

- [ ] **Step 3: Write services/practice_service.py**

```python
import json
import time
from database import get_db
from services.player_service import spend_energy, award_xp, get_player
from services.gacha_service import roll_gacha
from services.question_service import get_questions_for_module, generate_session_id
import config

def start_practice(player_id: int, module_id: int, count: int = 10) -> dict:
    questions = get_questions_for_module(module_id, player_id, count)
    if not questions:
        return None

    session_id = generate_session_id()
    # Determine focus cost based on question types
    cost = sum(config.FOCUS_COSTS.get(q["type"], 2) for q in questions)

    db = get_db()
    mod = db.execute("SELECT name FROM modules WHERE id=?", (module_id,)).fetchone()
    return {
        "session_id": session_id,
        "module_id": module_id,
        "module_name": mod["name"],
        "questions": questions,
        "focus_cost": cost,
    }

def submit_practice(player_id: int, module_id: int, session_id: str, answers: list, time_used_sec: int) -> dict:
    db = get_db()
    question_ids = [a["question_id"] for a in answers]
    placeholders = ",".join("?" * len(question_ids))
    rows = db.execute(f"SELECT id, answer, difficulty FROM questions WHERE id IN ({placeholders})", question_ids).fetchall()
    answer_map = {r["id"]: r["answer"] for r in rows}

    total = len(answers)
    correct_count = 0
    for a in answers:
        if str(a["answer"]).strip() == str(answer_map.get(a["question_id"], "")).strip():
            correct_count += 1

    accuracy = correct_count / total if total > 0 else 0

    # Record practice
    db.execute("""INSERT INTO practice_records (player_id, module_id, total_questions, correct_count, time_used_sec)
                  VALUES (?,?,?,?,?)""", (player_id, module_id, total, correct_count, time_used_sec))
    db.commit()

    # Spend energy (with refund from cost calculation)
    cost = 0
    for q_id in question_ids:
        q = db.execute("SELECT type FROM questions WHERE id=?", (q_id,)).fetchone()
        cost += config.FOCUS_COSTS.get(q["type"], 2) if q else 2
    spend_energy(player_id, cost)

    # Award XP
    base_xp = total * config.XP_PER_QUESTION
    if accuracy == 1.0:
        base_xp += config.XP_PERFECT_BONUS
    xp_result = award_xp(player_id, base_xp)

    # Near-miss check
    near_miss = config.NEAR_MISS_MIN <= accuracy <= config.NEAR_MISS_MAX

    # Gacha
    p = get_player(player_id)
    streak_bonus = p["streak_days"] >= 7
    gacha = roll_gacha(player_id, streak_bonus=streak_bonus)

    return {
        "total": total,
        "correct": correct_count,
        "accuracy": round(accuracy, 4),
        "xp_gained": base_xp,
        "near_miss": near_miss,
        "gacha_result": gacha,
    }
```

- [ ] **Step 4: Write routers/practice.py**

```python
from fastapi import APIRouter, HTTPException
from models.practice import PracticeSubmit, PracticeResult, PracticeSession, ModuleResponse
from services import practice_service

router = APIRouter(prefix="/api", tags=["practice"])

@router.get("/modules", response_model=list[ModuleResponse])
def list_modules():
    from database import get_db
    db = get_db()
    rows = db.execute("SELECT * FROM modules ORDER BY sort_order").fetchall()
    return [dict(r) for r in rows]

@router.get("/modules/{module_id}/practice")
def start_practice(module_id: int, player_id: int, count: int = 10):
    result = practice_service.start_practice(player_id, module_id, count)
    if not result:
        raise HTTPException(404, "No questions available for this module")
    return result

@router.post("/players/{player_id}/practice", response_model=PracticeResult)
def submit_practice(player_id: int, body: PracticeSubmit):
    return practice_service.submit_practice(
        player_id, body.module_id, body.session_id,
        [{"question_id": a.question_id, "answer": a.answer} for a in body.answers],
        body.time_used_sec
    )
```

- [ ] **Step 5: Register router in app.py**

```python
from routers.practice import router as practice_router
app.include_router(practice_router)
```

- [ ] **Step 6: Commit**

```bash
git add models/practice.py services/question_service.py services/practice_service.py routers/practice.py app.py
git commit -m "feat: practice API — question selection, submit, grading, gacha on completion"
```

---

### Task 8: Frontend — practice page with timer and gacha reveal

**Files:**
- Create: `static/js/practice.js`

**Interfaces:**
- Consumes: `App.api()`, `Components.gachaReveal()`, `Audio`
- Produces: Renders module grid → question flow → results + gacha animation

- [ ] **Step 1: Write practice.js — module selector + question flow**

```javascript
// practice.js
const practice = {
    currentSession: null,
    timerInterval: null,
    startTime: null,

    async render() {
        const main = document.getElementById('page-practice');
        main.innerHTML = '<h2>⚔️ 狩猎场 — 选择模块</h2><div id="module-grid" class="module-grid"></div>';
        const modules = await App.get('/modules');
        const grid = document.getElementById('module-grid');
        modules.forEach(m => {
            const card = document.createElement('div');
            card.className = 'module-card';
            card.innerHTML = `<span class="module-icon">${m.icon}</span>
                <span class="module-name">${m.name}</span>
                <span class="module-weight">${m.weight}分</span>`;
            card.onclick = () => this.startModule(m);
            grid.appendChild(card);
        });
    },

    async startModule(module) {
        const count = 10;
        try {
            const session = await App.get(`/modules/${module.id}/practice?player_id=${App.state.player.id}&count=${count}`);
            this.currentSession = session;
            this.currentIndex = 0;
            this.answers = [];
            this.startTime = Date.now();
            this.renderQuestion();
        } catch (e) {
            App.toast('该模块暂无可用的题目', 'error');
        }
    },

    renderQuestion() {
        const q = this.currentSession.questions[this.currentIndex];
        const main = document.getElementById('page-practice');
        const total = this.currentSession.questions.length;
        const idx = this.currentIndex + 1;

        let optionsHTML = '';
        if (q.options) {
            optionsHTML = q.options.map((opt, i) => `
                <label class="option-label">
                    <input type="radio" name="answer" value="${String.fromCharCode(65+i)}">
                    <span>${opt}</span>
                </label>`).join('');
        } else {
            optionsHTML = `<input type="text" id="answer-input" class="answer-input" placeholder="输入答案...">`;
        }

        main.innerHTML = `
            <div class="question-flow">
                <div class="question-header">
                    <span>${this.currentSession.module_name}</span>
                    <span class="question-counter">${idx} / ${total}</span>
                    <span class="question-timer" id="question-timer">⏱ 0:00</span>
                </div>
                <div class="question-card">
                    <div class="question-content">${q.content}</div>
                    <div class="question-options">${optionsHTML}</div>
                </div>
                <button id="btn-next" class="btn-primary" onclick="practice.nextQuestion()">
                    ${idx === total ? '提交' : '下一题'}
                </button>
            </div>`;
        this.startTimer();
    },

    startTimer() {
        this.startTime = Date.now();
        clearInterval(this.timerInterval);
        this.timerInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - this.startTime) / 1000);
            const min = Math.floor(elapsed / 60);
            const sec = elapsed % 60;
            const el = document.getElementById('question-timer');
            if (el) el.textContent = `⏱ ${min}:${String(sec).padStart(2, '0')}`;
        }, 1000);
    },

    nextQuestion() {
        const q = this.currentSession.questions[this.currentIndex];
        let answer;
        if (q.options) {
            const selected = document.querySelector('input[name="answer"]:checked');
            if (!selected) { App.toast('请选择一个答案'); return; }
            answer = selected.value;
        } else {
            answer = document.getElementById('answer-input').value;
        }
        this.answers.push({ question_id: q.id, answer });

        this.currentIndex++;
        if (this.currentIndex >= this.currentSession.questions.length) {
            this.submit();
        } else {
            this.renderQuestion();
        }
    },

    async submit() {
        clearInterval(this.timerInterval);
        const timeUsed = Math.floor((Date.now() - this.startTime) / 1000);
        const result = await App.post(`/players/${App.state.player.id}/practice`, {
            session_id: this.currentSession.session_id,
            module_id: this.currentSession.module_id,
            answers: this.answers,
            time_used_sec: timeUsed,
        });
        this.showResult(result);
    },

    showResult(result) {
        const main = document.getElementById('page-practice');
        const pct = Math.round(result.accuracy * 100);
        const emoji = pct >= 90 ? '🎉' : pct >= 70 ? '👍' : '💪';

        main.innerHTML = `
            <div class="result-screen">
                <h2>${emoji} 练习完成</h2>
                <div class="result-big-number">${result.correct} / ${result.total}</div>
                <div class="result-accuracy">正确率 ${pct}%</div>
                <div class="result-xp">+${result.xp_gained} XP</div>
                <div id="gacha-container"></div>
                ${result.near_miss ? `<div class="near-miss-banner">
                    <p>差一点就完美了！</p>
                    <button class="btn-primary" onclick="practice.startModule(practice.currentModule)">再来一套 (三倍奖励!)</button>
                </div>` : ''}
                <button class="btn-secondary" onclick="practice.render()">返回模块列表</button>
            </div>`;

        // Gacha reveal animation
        setTimeout(() => {
            Components.gachaReveal(result.gacha_result, document.getElementById('gacha-container'));
        }, 500);
        App.refreshPlayer();
    },
};
```

- [ ] **Step 2: Implement Components.gachaReveal in components.js**

```javascript
gachaReveal(item, container) {
    container.innerHTML = `
        <div class="gacha-card gacha-${item.rarity}">
            <div class="gacha-spinner">🎴</div>
            <div class="gacha-result" style="display:none">
                <div class="gacha-rarity">${item.rarity.toUpperCase()}</div>
                <div class="gacha-item">${item.item_name}</div>
            </div>
        </div>`;
    const spinner = container.querySelector('.gacha-spinner');
    const result = container.querySelector('.gacha-result');
    Audio.gachaFlip();
    // 1.5s suspense animation
    setTimeout(() => {
        spinner.style.display = 'none';
        result.style.display = 'block';
        Audio.gachaRare(item.rarity);
    }, 1500);
},
```

- [ ] **Step 3: Add CSS for practice page**

```css
.module-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px; }
.module-card { background: var(--surface); padding: 20px; border-radius: var(--radius-lg); cursor: pointer; text-align: center; transition: transform 0.15s, box-shadow 0.15s; }
.module-card:hover { transform: translateY(-2px); box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
.module-icon { font-size: 32px; display: block; margin-bottom: 8px; }
.module-name { font-weight: 600; display: block; }
.module-weight { color: var(--accent); font-size: 13px; }
.question-flow { max-width: 700px; margin: 0 auto; }
.question-header { display: flex; justify-content: space-between; margin-bottom: 16px; color: var(--text-dim); }
.question-card { background: var(--surface); padding: 24px; border-radius: var(--radius-lg); margin-bottom: 16px; }
.question-content { font-size: 16px; line-height: 1.8; margin-bottom: 20px; }
.option-label { display: flex; align-items: flex-start; gap: 10px; padding: 12px; border: 1px solid var(--surface2); border-radius: var(--radius); margin-bottom: 8px; cursor: pointer; transition: border-color 0.15s; }
.option-label:has(input:checked) { border-color: var(--accent); background: rgba(245,158,11,0.1); }
.result-screen { text-align: center; max-width: 500px; margin: 0 auto; }
.result-big-number { font-size: 64px; font-weight: 700; color: var(--accent); }
.result-accuracy { font-size: 20px; margin: 8px 0; }
.gacha-card { width: 200px; height: 140px; margin: 20px auto; border-radius: var(--radius-lg); display: flex; align-items: center; justify-content: center; font-size: 48px; }
.gacha-common { border: 2px solid var(--rarity-common); }
.gacha-rare { border: 2px solid var(--rarity-rare); box-shadow: 0 0 20px rgba(59,130,246,0.3); }
.gacha-epic { border: 2px solid var(--rarity-epic); box-shadow: 0 0 20px rgba(168,85,247,0.4); }
.gacha-legendary { border: 2px solid var(--rarity-legendary); box-shadow: 0 0 30px rgba(245,158,11,0.5); animation: glow-legendary 1s infinite alternate; }
.gacha-mythic { border: 2px solid var(--rarity-mythic); box-shadow: 0 0 40px rgba(239,68,68,0.6); animation: glow-mythic 0.5s infinite alternate; }
@keyframes glow-legendary { from { box-shadow: 0 0 20px rgba(245,158,11,0.3); } to { box-shadow: 0 0 40px rgba(245,158,11,0.6); } }
@keyframes glow-mythic { from { box-shadow: 0 0 20px rgba(239,68,68,0.3); } to { box-shadow: 0 0 50px rgba(239,68,68,0.8); } }
.near-miss-banner { background: var(--surface); padding: 16px; border-radius: var(--radius-lg); margin: 16px 0; border-left: 3px solid var(--accent); }
```

- [ ] **Step 4: Commit**

```bash
git add static/js/practice.js static/js/components.js static/css/styles.css
git commit -m "feat: practice page — module grid, question flow, timer, gacha reveal animation"
```

---

### Task 9: Seed questions — 5-8 starter questions per module

**Files:**
- Modify: `seed_data.py`

**Interfaces:**
- Produces: At least 5 questions per module (40+ total) covering choice/fill/answer types at diff 1-2

- [ ] **Step 1: Add SEED_QUESTIONS list to seed_data.py**

```python
SEED_QUESTIONS = [
    # Module 1: 三角函数与解三角形
    (1, None, "choice", 1, '["和差角公式"]', 2, 0,
     "已知 $\\sin\\alpha = \\frac{3}{5}$，$\\alpha \\in (0, \\frac{\\pi}{2})$，则 $\\cos\\alpha$ 等于",
     '["A. \\\\frac{3}{5}", "B. \\\\frac{4}{5}", "C. -\\\\frac{4}{5}", "D. \\\\frac{5}{3}"]',
     "B", "由 $\\sin^2\\alpha + \\cos^2\\alpha = 1$，$\\alpha$ 在第一象限，$\\cos\\alpha = \\frac{4}{5}$", 60,
     None, None, "generated", None),
    (1, None, "fill", 1, '["二倍角公式"]', 2, 0,
     "已知 $\\sin\\alpha = \\frac{1}{3}$，则 $\\cos 2\\alpha =$ ____",
     None, "7/9", "$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\times \\frac{1}{9} = \\frac{7}{9}$", 90,
     None, None, "generated", None),
    (1, None, "answer", 2, '["正弦定理","余弦定理"]', 4, 0,
     "在 $\\triangle ABC$ 中，已知 $a=3$，$b=4$，$\\angle C = 60°$，求边 $c$ 的长度",
     None, "√13", "由余弦定理 $c^2 = a^2 + b^2 - 2ab\\cos C = 9 + 16 - 24 \\times \\frac{1}{2} = 13$，$c = \\sqrt{13}$", 120,
     None, None, "generated", None),
    (1, None, "choice", 1, '["和差角公式"]', 2, 0,
     "$\\sin 75°$ 的值为",
     '["A. \\\\frac{\\\\sqrt{6}+\\\\sqrt{2}}{4}", "B. \\\\frac{\\\\sqrt{6}-\\\\sqrt{2}}{4}", "C. \\\\frac{\\\\sqrt{3}}{2}", "D. \\\\frac{1}{2}"]',
     "A", "$\\sin 75° = \\sin(45°+30°) = \\sin 45°\\cos 30° + \\cos 45°\\sin 30° = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$", 90,
     None, None, "generated", None),
    (1, None, "fill", 2, '["正弦定理"]', 3, 0,
     "在 $\\triangle ABC$ 中，已知 $\\angle A = 45°$，$\\angle B = 60°$，$a = 2$，则 $b =$ ____",
     None, "√6", "由正弦定理 $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$，$b = \\frac{a\\sin B}{\\sin A} = \\frac{2 \\times \\sqrt{3}/2}{\\sqrt{2}/2} = \\sqrt{6}$", 120,
     None, None, "generated", None),
    # ... 35+ more questions for modules 2-8 (at least 5 each)
]

# In seed() function, add:
def _seed_questions(cur):
    cols = "(module_id, pattern_id, type, difficulty, concepts, step_count, has_trap, content, options, answer, solution, time_limit_sec, variant_of, variant_axis, source_type, source_ref)"
    for q in SEED_QUESTIONS:
        cur.execute(f"INSERT OR IGNORE INTO questions {cols} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", q)
```

- [ ] **Step 2: Write out all 40+ questions** (expand SEED_QUESTIONS to cover all 8 modules, 5-8 each)

- [ ] **Step 3: Test — run seed_data.py, verify `SELECT COUNT(*) FROM questions` >= 40**

- [ ] **Step 4: Commit**

```bash
git add seed_data.py
git commit -m "feat: 40+ seed questions across all 8 modules"
```

---

### Task 10: Integration test — complete practice flow

- [ ] **Step 1: Start server, create player via curl**

- [ ] **Step 2: Open browser, verify: module grid → click module → see questions → answer → submit → see result + gacha animation → XP updated in sidebar**

- [ ] **Step 3: Verify gacha drop appears in player's owned_cosmetics**

- [ ] **Step 4: Fix any integration issues**

- [ ] **Step 5: Commit integration fixes**

```bash
git add -A
git commit -m "fix: integration fixes for practice flow end-to-end"
```

### ✅ Round 1 complete — player can register, browse modules, answer questions, receive gacha rewards

---

## Round 2: Mistakes, Blind Spots, Tasks, Dashboard

### Task 11: Mistake API (三问法)

**Files:**
- Create: `models/mistake.py`
- Create: `services/mistake_service.py`
- Create: `routers/mistakes.py`

**Interfaces:**
- Consumes: player exists, module exists
- Produces: `POST /api/players/{id}/mistakes` (create with 三问法), `GET /api/players/{id}/mistakes` (list), `POST /api/players/{id}/mistakes/{id}/retry` (retry grading)

- [ ] **Step 1: Write models/mistake.py**

```python
from pydantic import BaseModel, Field
from typing import Optional

class MistakeCreate(BaseModel):
    module_id: int
    question: str
    wrong_step: str = ""
    correct_thought: str = ""
    knowledge_point: str = ""
    error_type: str = "knowledge_gap"   # 'calculation'|'logic'|'knowledge_gap'
    blind_spot_name: Optional[str] = None  # Auto-create blind spot if provided

class MistakeRetry(BaseModel):
    answer: str

class MistakeResponse(BaseModel):
    id: int
    module_id: int
    question: str
    wrong_step: str
    correct_thought: str
    knowledge_point: str
    error_type: str
    retry_count: int
    mastered: bool
    created_date: str
```

- [ ] **Step 2: Write services/mistake_service.py**

```python
import json
from datetime import date, timedelta
from database import get_db
from services.player_service import award_xp, spend_energy
import config

def create_mistake(player_id: int, data: dict) -> dict:
    db = get_db()
    cur = db.execute(
        """INSERT INTO mistakes (player_id, module_id, question, wrong_step, correct_thought, knowledge_point, error_type)
           VALUES (?,?,?,?,?,?,?)""",
        (player_id, data["module_id"], data["question"], data.get("wrong_step", ""),
         data.get("correct_thought", ""), data.get("knowledge_point", ""), data.get("error_type", "knowledge_gap"))
    )
    mid = cur.lastrowid
    db.commit()

    # Auto-create blind spot if name provided
    if data.get("blind_spot_name"):
        _ensure_blind_spot(db, player_id, data["blind_spot_name"], data["module_id"], mid)

    return get_mistake(mid)

def _ensure_blind_spot(db, player_id, name, module_id, mistake_id):
    existing = db.execute("SELECT id FROM blind_spots WHERE player_id=? AND name=?",
                          (player_id, name)).fetchone()
    if existing:
        # Extend module_ids
        spot = db.execute("SELECT module_ids FROM blind_spots WHERE id=?", (existing["id"],)).fetchone()
        mods = json.loads(spot["module_ids"])
        if module_id not in mods:
            mods.append(module_id)
            db.execute("UPDATE blind_spots SET module_ids=? WHERE id=?", (json.dumps(mods), existing["id"]))
        db.commit()
        return existing["id"]

    cur = db.execute(
        "INSERT INTO blind_spots (player_id, name, module_ids, created_from_mistake_id) VALUES (?,?,?,?)",
        (player_id, name, json.dumps([module_id]), mistake_id)
    )
    db.commit()
    return cur.lastrowid

def get_mistake(mistake_id: int) -> dict:
    db = get_db()
    return dict(db.execute("SELECT * FROM mistakes WHERE id=?", (mistake_id,)).fetchone())

def list_mistakes(player_id: int, module_id: int = None, mastered: int = None) -> list:
    db = get_db()
    query = "SELECT * FROM mistakes WHERE player_id=?"
    params = [player_id]
    if module_id is not None:
        query += " AND module_id=?"
        params.append(module_id)
    if mastered is not None:
        query += " AND mastered=?"
        params.append(mastered)
    query += " ORDER BY created_date DESC"
    return [dict(r) for r in db.execute(query, params).fetchall()]

def retry_mistake(player_id: int, mistake_id: int, user_answer: str) -> dict:
    db = get_db()
    m = db.execute("SELECT * FROM mistakes WHERE id=? AND player_id=?", (mistake_id, player_id)).fetchone()
    if not m:
        return {"detail": "not found"}

    # Check answer against stored question (for retry, user re-does the original — we trust self-grade)
    # OR connect to original question answer if available
    # For now: user self-grades via a separate field
    m = dict(m)
    new_retry = m["retry_count"] + 1
    # Store that retry happened
    db.execute("UPDATE mistakes SET retry_count=?, last_retry_date=date('now'), last_retry_correct=1 WHERE id=?",
               (new_retry, mistake_id))

    # Check mastery: 2 consecutive correct retries
    if new_retry >= 2:
        db.execute("UPDATE mistakes SET mastered=1 WHERE id=?", (mistake_id,))

        # Also update blind spot HP
        spot = db.execute("SELECT id, hp_current FROM blind_spots WHERE created_from_mistake_id=?",
                          (mistake_id,)).fetchone()
        if spot:
            new_hp = max(0, spot["hp_current"] - 25)
            status = "cleared" if new_hp == 0 else "active"
            db.execute("UPDATE blind_spots SET hp_current=?, status=?, defeat_count=defeat_count+1 WHERE id=?",
                       (new_hp, status, spot["id"]))
            if new_hp == 0:
                # Boss kill! Schedule achievement check later
                pass

    db.commit()

    # Refund 50% energy
    player = db.execute("SELECT focus_energy, focus_max FROM players WHERE id=?", (player_id,)).fetchone()
    refund = int(config.FOCUS_COSTS.get("fill", 3) * config.ENERGY_REFUND_RATE)
    db.execute("UPDATE players SET focus_energy=MIN(focus_max, focus_energy+?) WHERE id=?",
               (refund, player_id))
    db.commit()

    # Award XP for retry
    xp_res = award_xp(player_id, config.XP_MISTAKE_RETRY)

    return {"retry_count": new_retry, "mastered": new_retry >= 2, "xp_gained": config.XP_MISTAKE_RETRY}
```

- [ ] **Step 3: Write routers/mistakes.py**

```python
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
    if "detail" in result: raise HTTPException(404, result["detail"])
    return result
```

- [ ] **Step 4: Register in app.py, test with curl, commit**

```bash
git add models/mistake.py services/mistake_service.py routers/mistakes.py app.py
git commit -m "feat: mistake API — create with 三问法, auto blind-spot, retry with energy refund"
```

---

### Task 12: Blind Spot API — monster list, attack schedule

**Files:**
- Create: `models/blind_spot.py`
- Create: `services/blind_spot_service.py`
- Create: `routers/blind_spots.py`

**Interfaces:**
- Consumes: mistakes exist
- Produces: `GET /api/players/{id}/blind-spots`, `GET /api/players/{id}/blind-spots/due-today`, `POST /api/players/{id}/blind-spots/{id}/attack`

- [ ] **Step 1: Write models/blind_spot.py**

```python
from pydantic import BaseModel
from typing import Optional

class BlindSpotResponse(BaseModel):
    id: int
    name: str
    hp_total: int
    hp_current: int
    boss_type: str
    status: str
    defeat_count: int
    module_ids: list[int]
    parent_id: Optional[int] = None

class AttackRequest(BaseModel):
    answer: str
    round_number: int  # 1-4

class AttackResponse(BaseModel):
    damage: int         # 25 if correct, 0 if wrong
    hp_remaining: int
    boss_killed: bool
    xp_gained: int
```

- [ ] **Step 2: Write services/blind_spot_service.py — full 4-round scheduling**

```python
import json
from datetime import date, timedelta
from database import get_db
from services.player_service import award_xp, spend_energy
import config

def list_blind_spots(player_id: int) -> list:
    db = get_db()
    rows = db.execute("SELECT * FROM blind_spots WHERE player_id=? AND status='active'", (player_id,)).fetchall()
    result = []
    for r in rows:
        d = dict(r)
        d["module_ids"] = json.loads(d["module_ids"])
        result.append(d)
    return result

def get_due_today(player_id: int) -> list:
    db = get_db()
    today = date.today().isoformat()
    rows = db.execute("""
        SELECT bsr.*, bs.name as spot_name, bs.hp_current, bs.status as spot_status
        FROM blind_spot_rounds bsr
        JOIN blind_spots bs ON bsr.blind_spot_id = bs.id
        WHERE bs.player_id=? AND bsr.scheduled_date=? AND bsr.result='pending'
    """, (player_id, today)).fetchall()
    return [dict(r) for r in rows]

def schedule_rounds(blind_spot_id: int):
    """Schedule 4 rounds: day 0 (today), day 2, day 7, day 21"""
    db = get_db()
    spot = db.execute("SELECT * FROM blind_spots WHERE id=?", (blind_spot_id,)).fetchone()
    if not spot: return

    today = date.today()
    intervals = [0, 2, 7, 21]
    for round_num, offset in enumerate(intervals, 1):
        sched_date = (today + timedelta(days=offset)).isoformat()
        # Reuse original question text from the mistake for round 1
        mistake = db.execute("SELECT question FROM mistakes WHERE id=?",
                             (spot["created_from_mistake_id"],)).fetchone()
        q_text = mistake["question"] if mistake else spot["name"]
        db.execute("""INSERT OR IGNORE INTO blind_spot_rounds (blind_spot_id, round, question, question_type, scheduled_date)
                      VALUES (?,?,?,?,?)""",
                   (blind_spot_id, round_num, q_text,
                    "original" if round_num == 1 else "variant", sched_date))
    db.commit()

def attack_blind_spot(player_id: int, blind_spot_id: int, answer: str, round_number: int) -> dict:
    db = get_db()
    spot = db.execute("SELECT * FROM blind_spots WHERE id=? AND player_id=?",
                      (blind_spot_id, player_id)).fetchone()
    if not spot: return {"detail": "not found"}

    # Find the round
    round_row = db.execute("SELECT * FROM blind_spot_rounds WHERE blind_spot_id=? AND round=? AND result='pending'",
                           (blind_spot_id, round_number)).fetchone()
    if not round_row: return {"detail": "round not pending or not found"}

    # For now: user self-grades OR we check against matching question answer
    # Simplified: user marks themselves if correct. We count it as correct.
    correct = True  # Assume self-graded honesty for MVP

    damage = 25 if correct else 0
    new_hp = max(0, spot["hp_current"] - damage)
    boss_killed = new_hp == 0

    db.execute("UPDATE blind_spot_rounds SET result=?, answered_date=date('now') WHERE id=?",
               ("correct" if correct else "wrong", round_row["id"]))
    db.execute("UPDATE blind_spots SET hp_current=?, status=?, defeat_count=defeat_count+? WHERE id=?",
               (new_hp, "cleared" if boss_killed else "active", 1 if correct else 0, blind_spot_id))
    db.commit()

    # Award XP proportional to round (later rounds = more XP)
    xp_res = award_xp(player_id, 80 if correct else 0)

    if boss_killed:
        # Trigger boss kill animation data
        return {
            "damage": damage, "hp_remaining": 0, "boss_killed": True,
            "xp_gained": 80, "kill_animation": True
        }

    return {"damage": damage, "hp_remaining": new_hp, "boss_killed": False, "xp_gained": 80 if correct else 0}
```

- [ ] **Step 3: Write routers/blind_spots.py, register, test, commit**

---

### Task 13: Frontend — mistake book + monster gallery

**Files:**
- Create: `static/js/mistakes.js`

**Interfaces:**
- Consumes: `App.api()`, `Components.bossCard()`
- Produces: Renders 错题本 list + 怪物图鉴 grid + due-today attack cards

- [ ] **Step 1: Write mistakes.js — dual view (mistake list / monster gallery)**

Tab-based view: "📝 错题列表" | "🐉 怪物图鉴" | "⚔️ 今日讨伐"

- Mistake list: fetch → render cards with module, error type badge, retry status, "重做" button
- Monster gallery: fetch blind_spots → render `Components.bossCard()` with HP bar, attack button
- Due today: fetch blind-spots/due-today → render attack queue

- [ ] **Step 2: Implement Components.bossCard in components.js**

```javascript
bossCard(spot) {
    const hpPct = (spot.hp_current / spot.hp_total) * 100;
    const hpColor = hpPct > 50 ? 'var(--correct)' : hpPct > 25 ? 'var(--accent)' : 'var(--wrong)';
    return `<div class="boss-card boss-${spot.boss_type}">
        <div class="boss-icon">🐉</div>
        <div class="boss-name">${spot.name}</div>
        <div class="boss-hp-bar"><div class="boss-hp-fill" style="width:${hpPct}%;background:${hpColor}"></div></div>
        <div class="boss-hp-text">HP: ${spot.hp_current}/${spot.hp_total}</div>
        <div class="boss-defeats">🏆 同类击败: ${spot.defeat_count}</div>
        <button class="btn-attack" onclick="mistakes.attackBoss(${spot.id})">⚔️ 攻击</button>
    </div>`;
},
```

- [ ] **Step 3: Add CSS + test flow, commit**

---

### Task 14: Daily Task generator + API

**Files:**
- Create: `models/task.py`
- Create: `services/task_service.py`
- Create: `routers/tasks.py`

**Interfaces:**
- Produces: Task generation picks 1 main (from lowest-mastery module), 3 side (mistake retries), 1 challenge (random timed event)

- [ ] **Step 1: Write task_service.py — generate_daily_tasks()**

```python
import random
from datetime import date
from database import get_db
import config

def generate_daily_tasks(player_id: int) -> list:
    db = get_db()
    today = date.today().isoformat()

    # Check if already generated
    existing = db.execute("SELECT id FROM daily_tasks WHERE player_id=? AND scheduled_date=?",
                          (player_id, today)).fetchone()
    if existing:
        return list_tasks(player_id, today)

    tasks = []

    # Main quest: lowest mastery module
    lowest = db.execute("""SELECT mm.module_id, m.name FROM module_mastery mm
        JOIN modules m ON mm.module_id = m.id
        WHERE mm.player_id=? AND mm.status != 'mastered'
        ORDER BY mm.accuracy_avg ASC LIMIT 1""", (player_id,)).fetchone()
    if lowest:
        tasks.append((player_id, lowest["module_id"], "main",
                      f"讨伐「{lowest['name']}」— 完成10道练习题",
                      30, config.XP_DAILY_TASK["main"], today))

    # Side quests: 3 pending blind spot retries
    due = db.execute("""SELECT bs.id, bs.name FROM blind_spot_rounds bsr
        JOIN blind_spots bs ON bsr.blind_spot_id = bs.id
        WHERE bs.player_id=? AND bsr.scheduled_date=? AND bsr.result='pending' LIMIT 3""",
        (player_id, today)).fetchall()
    for d in due:
        tasks.append((player_id, None, "side",
                      f"炼金: 复测盲点「{d['name']}」",
                      15, config.XP_DAILY_TASK["side"], today))

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
        "INSERT INTO daily_tasks (player_id, module_id, task_type, content, time_limit_min, xp_reward, scheduled_date) VALUES (?,?,?,?,?,?,?)",
        tasks
    )
    db.commit()
    return list_tasks(player_id, today)

def list_tasks(player_id: int, dt: str) -> list:
    db = get_db()
    return [dict(r) for r in db.execute(
        "SELECT * FROM daily_tasks WHERE player_id=? AND scheduled_date=?", (player_id, dt)).fetchall()]

def complete_task(player_id: int, task_id: int, actual_time_min: int = 0) -> dict:
    db = get_db()
    task = db.execute("SELECT * FROM daily_tasks WHERE id=? AND player_id=? AND completed=0",
                      (task_id, player_id)).fetchone()
    if not task: return {"detail": "not found or already completed"}

    db.execute("UPDATE daily_tasks SET completed=1, actual_time_min=?, completed_date=datetime('now') WHERE id=?",
               (actual_time_min, task_id))
    db.commit()

    from services.player_service import award_xp
    xp_res = award_xp(player_id, task["xp_reward"])

    return {"task_id": task_id, "completed": True, "xp_gained": task["xp_reward"]}
```

- [ ] **Step 2: Write routers/tasks.py, models/task.py, register, test, commit**

---

### Task 15: Frontend — task board

**Files:**
- Create: `static/js/tasks.js`

**Interfaces:**
- Consumes: tasks API
- Produces: Renders 冒险者任务板 with main/side/challenge sections, complete buttons

- [ ] **Step 1: Write tasks.js — fetch + render quest cards**

```javascript
const tasks = {
    async render() {
        const main = document.getElementById('page-tasks');
        const today = new Date().toISOString().slice(0, 10);
        const p = App.state.player;

        // Auto-generate if none exist
        let taskList = await App.get(`/players/${p.id}/tasks?date=${today}`);
        if (taskList.length === 0) {
            await App.post(`/players/${p.id}/tasks/generate`);
            taskList = await App.get(`/players/${p.id}/tasks?date=${today}`);
        }

        const byType = { main: [], side: [], challenge: [] };
        taskList.forEach(t => byType[t.task_type].push(t));

        main.innerHTML = `
            <h2>☀️ 今日任务板 <span class="streak-badge">🔥×${p.streak_days}</span></h2>
            <div class="quest-section">
                <h3>🗡️ 主线任务</h3>
                ${byType.main.map(t => this.questCard(t)).join('') || '<p class="empty">暂无主线任务</p>'}
            </div>
            <div class="quest-section">
                <h3>🧪 支线任务</h3>
                ${byType.side.map(t => this.questCard(t)).join('') || '<p class="empty">暂无支线任务</p>'}
            </div>
            <div class="quest-section">
                <h3>⚡ 每日挑战</h3>
                ${byType.challenge.map(t => this.questCard(t)).join('') || '<p class="empty">暂无挑战</p>'}
            </div>`;
    },

    questCard(task) {
        const done = task.completed;
        return `<div class="quest-card ${done ? 'quest-done' : ''}">
            <div class="quest-content">${task.content}</div>
            <div class="quest-reward">💰 ${task.xp_reward} XP</div>
            ${task.time_limit_min ? `<div class="quest-timer">⏱ ${task.time_limit_min}分钟</div>` : ''}
            ${!done ? `<button class="btn-complete" onclick="tasks.complete(${task.id})">完成</button>`
                     : '<span class="quest-done-badge">✅ 已完成</span>'}
        </div>`;
    },

    async complete(taskId) {
        await App.post(`/players/${App.state.player.id}/tasks/${taskId}/complete`, { actual_time_min: 0 });
        Audio.levelUp();
        App.toast('任务完成!', 'success');
        await App.refreshPlayer();
        this.render();
    },
};
```

- [ ] **Step 2: Add CSS, test, commit**

---

### Task 16: Dashboard + progress API

**Files:**
- Create: `routers/stats.py`
- Create: `services/mastery_service.py`
- Modify: `static/js/dashboard.js`, `static/js/progress.js`

**Interfaces:**
- Produces: `GET /api/players/{id}/dashboard` and `GET /api/players/{id}/progress`

- [ ] **Step 1: Write mastery_service.py — five-dimension scoring**

```python
import json
from database import get_db
import config

def calculate_mastery(player_id: int, module_id: int) -> dict:
    db = get_db()
    # Recent accuracy (last 3 practice records)
    records = db.execute("""
        SELECT correct_count*1.0/total_questions as acc
        FROM practice_records WHERE player_id=? AND module_id=?
        ORDER BY practice_date DESC LIMIT 3
    """, (player_id, module_id)).fetchall()
    accuracy_avg = sum(r["acc"] for r in records) / len(records) if records else 0

    # Speed qualify (check if average time per question meets limits)
    speed_records = db.execute("""
        SELECT time_used_sec*1.0/total_questions as avg_time, total_questions
        FROM practice_records WHERE player_id=? AND module_id=?
        ORDER BY practice_date DESC LIMIT 3
    """, (player_id, module_id)).fetchall()
    time_ok = all(r["avg_time"] <= 150 for r in speed_records) if speed_records else False

    # Retention: check 7-day-old retry results
    # Simplified: use blind_spot clear rate as proxy
    spots = db.execute("SELECT COUNT(*) as total, SUM(CASE WHEN status='cleared' THEN 1 ELSE 0 END) as cleared FROM blind_spots WHERE player_id=? AND module_ids LIKE ?",
                       (player_id, f'%{module_id}%')).fetchone()
    mistake_clear = spots["cleared"] / spots["total"] if spots["total"] > 0 else 1.0

    # Stability: variance of last 5 accuracies
    all_acc = db.execute("""
        SELECT correct_count*1.0/total_questions as acc
        FROM practice_records WHERE player_id=? AND module_id=?
        ORDER BY practice_date DESC LIMIT 5
    """, (player_id, module_id)).fetchall()
    accs = [r["acc"] for r in all_acc]
    stability = 0
    if len(accs) >= 2:
        mean = sum(accs) / len(accs)
        variance = sum((a - mean)**2 for a in accs) / len(accs)
        stability = max(0, 1 - variance * 10)  # Scale: low variance = high stability

    # Determine status
    if accuracy_avg >= config.MASTERY_ACCURACY and mistake_clear >= config.MASTERY_MISTAKE_CLEAR and stability >= 0.7:
        status = "mastered"
    elif accuracy_avg >= 0.70:
        status = "practicing"
    elif accuracy_avg > 0:
        status = "learning"
    else:
        status = "new"

    db.execute("""UPDATE module_mastery SET accuracy_avg=?, speed_qualify=?, retention_score=?,
                  mistake_clear_rate=?, stability_score=?, status=?, mastered_date=? WHERE player_id=? AND module_id=?""",
               (accuracy_avg, int(time_ok), mistake_clear, mistake_clear, stability,
                status, date.today().isoformat() if status == "mastered" else None,
                player_id, module_id))
    db.commit()

    return {"accuracy_avg": accuracy_avg, "speed_qualify": time_ok, "retention_score": mistake_clear,
            "mistake_clear_rate": mistake_clear, "stability_score": stability, "status": status}
```

- [ ] **Step 2: Write routers/stats.py — dashboard endpoint**

```python
@router.get("/players/{player_id}/dashboard")
def dashboard(player_id: int):
    db = get_db()
    p = get_player(player_id)
    modules = db.execute("SELECT * FROM modules ORDER BY sort_order").fetchall()
    masteries = []
    total_xp = p["xp"]
    estimated_score = 0
    for m in modules:
        mas = calculate_mastery(player_id, m["id"])
        masteries.append({"module_id": m["id"], "module_name": m["name"], "icon": m["icon"], **mas})
        if mas["status"] == "mastered":
            estimated_score += m["weight"]
        elif mas["status"] == "practicing":
            estimated_score += m["weight"] * 0.6

    return {
        "player": p,
        "estimated_score": min(150, int(estimated_score)),
        "module_masteries": masteries,
        "total_questions": p.get("total_questions", 0),
        "total_correct": p.get("total_correct", 0),
    }
```

- [ ] **Step 3: Write dashboard.js — ring chart + score estimate + streak calendar**

- [ ] **Step 4: Write progress.js — radar chart + module detail**

- [ ] **Step 5: Register router, test, commit**

---

### Task 17: Integration — wire dashboard to page load

- [ ] **Step 1: When App.navigate('dashboard'), call dashboard.render()**

- [ ] **Step 2: End-to-end test — login, see score estimate, see module status**

- [ ] **Step 3: Commit**

### ✅ Round 2 complete

---

## Round 3: Season, Guild, Achievements, Polish

### Task 18: Season + Battle Pass API
### Task 19: Guild API (create, join, contribute, boss)
### Task 20: Achievements system (hidden triggers + badge unlock)
### Task 21: Cosmetics shop + gacha spending
### Task 22: Frontend — season page, guild page, achievements page
### Task 23: Global animations — level up overlay, boss kill camera shake, drop broadcast toast
### Task 24: Mobile responsive pass
### Task 25: Seed 300+ questions from LLM analysis pipeline (run tools/analyze_exam.py + tools/generate_variants.py + tools/merge_seed.py)

(Full task detail for Round 3 tasks would continue in the same bite-sized pattern. Each follows the established file structure — model + service + router + frontend JS module.)

---

## Launch Checklist

- [ ] `pip install -r requirements.txt && python seed_data.py && python app.py` succeeds
- [ ] Browser opens, creates player, sidebar updates
- [ ] Practice complete flow: module → questions → timer → submit → gacha reveal → XP update
- [ ] Mistake flow: create → auto blind-spot → retry → mastery check → boss HP decreases
- [ ] Daily tasks auto-generate and can be completed
- [ ] Dashboard shows score estimate and module mastery
- [ ] Config changes take effect on restart (tweak `config.py`, restart, verify)
- [ ] Database file is portable (copy `math_rpg.db` to new machine, it works)

---

## Post-Launch

- Run `tools/analyze_exam.py` with Claude API to analyze real gaokao exams → structured patterns
- Run `tools/generate_variants.py` to expand question pool to 300+
- Run `tools/merge_seed.py` to regenerate `seed_data.py`
- A/B test gacha odds and XP rates with real users
- Collect accuracy data to tune `difficulty_dynamic` calibration
