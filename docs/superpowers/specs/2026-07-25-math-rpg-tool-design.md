# 高中数学 RPG 提分工具 — 设计规格

## 概述

一个 Web 应用，将高中数学备考方案与 RPG 游戏机制深度融合。把"刷题提分"变成"打怪升级"——用变量奖励、赛季通行证、公会协作等公认最有效的成瘾机制，降低学习抵触感，让用户持续使用直到高考。

**目标用户**：高中数学在 70-100 分段，希望短时间冲到 120+ 的学生。

**核心指标**：用户连续使用 60 天后，模考成绩稳定 120+。

---

## 设计原则

1. **一切皆可配**：概率表、体力回复速率、等级阈值、赛季周期等游戏参数全部抽到 `config.py`，改一个数就生效，不用翻代码
2. **模块热插拔**：每个功能模块独立路由 + 独立 service + 独立前端 JS，增删改一个模块不影响其他
3. **数据驱动**：题目难度、知识点标签、变式规则全部走数据库和数据文件，不硬编码逻辑
4. **前端无状态**：所有状态在服务端，前端只做渲染，刷新页面不丢数据
5. **单文件启动**：`pip install -r requirements.txt && python app.py`，然后浏览器打开

---

## 技术栈

| 层 | 选型 | 理由 |
|---|------|------|
| 后端 | Python FastAPI | REST API，异步支持好 |
| 前端 | 原生 HTML/CSS/JS (SPA) | 无框架依赖，交互自由 |
| 数据库 | SQLite | 单文件、零配置、Python 内置 |
| 图表 | Chart.js (CDN) | 仪表盘可视化 |
| 部署 | `python app.py` 一键启动 | 单命令启动 |

---

## 页面结构

```
┌──────── 侧边栏 (240px) ────────┐  ┌──── 主内容区 ────────────────────┐
│                                 │  │                                  │
│  👤 角色头像 + 等级 + XP条      │  │   根据导航切换渲染                │
│  🔥 连击:N天  ⚡ 体力:N/100     │  │                                  │
│  ───────────────────────        │  │                                  │
│  📊 冒险大厅 (仪表盘)           │  │                                  │
│  📋 任务板 (每日任务)           │  │                                  │
│  ⚔️ 狩猎场 (专项刷题)           │  │                                  │
│  🐉 怪物图鉴 (错题/盲点)        │  │                                  │
│  📈 修炼进度                     │  │                                  │
│  🏰 公会                         │  │                                  │
│  🏁 赛季通行证                   │  │                                  │
│  🏆 成就殿堂                     │  │                                  │
│  ⚙️ 设置                         │  │                                  │
│                                 │  │                                  │
└─────────────────────────────────┘  └──────────────────────────────────┘
```

---

## 数据模型

### players
```sql
CREATE TABLE players (
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
    owned_cosmetics TEXT DEFAULT '[]',       -- JSON array
    guild_id INTEGER,
    guild_role TEXT DEFAULT 'member',
    last_login TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);
```

### modules (知识模块)
```sql
CREATE TABLE modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,                       -- e.g. '三角函数与解三角形'
    weight INTEGER NOT NULL DEFAULT 10,       -- 高考分值权重
    tier INTEGER NOT NULL DEFAULT 1,          -- 1=第一梯队, 2=第二梯队, 3=第三梯队
    sort_order INTEGER NOT NULL DEFAULT 0,
    icon TEXT DEFAULT '📐',
    description TEXT
);
```

### module_mastery (模块掌握度)
```sql
CREATE TABLE module_mastery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    accuracy_avg REAL DEFAULT 0,              -- 最近3次正确率均值
    speed_qualify INTEGER DEFAULT 0,          -- 0/1 速度是否达标
    retention_score REAL DEFAULT 0,           -- 7天复测得分
    mistake_clear_rate REAL DEFAULT 0,        -- 错题消灭率 0.0-1.0
    stability_score REAL DEFAULT 0,           -- 稳定性(方差)
    status TEXT DEFAULT 'new',                -- 'new'|'learning'|'practicing'|'mastered'
    mastered_date TEXT,
    UNIQUE(player_id, module_id)
);
```

### daily_tasks (每日任务)
```sql
CREATE TABLE daily_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    module_id INTEGER,
    task_type TEXT NOT NULL,                  -- 'main'|'side'|'challenge'
    content TEXT NOT NULL,
    time_limit_min INTEGER,
    xp_reward INTEGER DEFAULT 30,
    completed INTEGER DEFAULT 0,
    actual_time_min INTEGER,
    scheduled_date TEXT NOT NULL,
    completed_date TEXT
);
```

### mistakes (错题本)
```sql
CREATE TABLE mistakes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    question TEXT NOT NULL,                   -- 题目描述或图片路径
    wrong_step TEXT,                          -- 错在哪一步
    correct_thought TEXT,                     -- 正确思路
    knowledge_point TEXT,                     -- 考点
    error_type TEXT,                          -- 'calculation'|'logic'|'knowledge_gap'
    retry_count INTEGER DEFAULT 0,
    last_retry_date TEXT,
    last_retry_correct INTEGER DEFAULT 0,
    mastered INTEGER DEFAULT 0,              -- 连续2次重做正确 → 1
    created_date TEXT DEFAULT (datetime('now'))
);
```

### blind_spots (知识盲点 → 怪物)
```sql
CREATE TABLE blind_spots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    name TEXT NOT NULL,                       -- e.g. '完全平方公式'
    parent_id INTEGER,                        -- 依赖的前置知识点
    textbook_ref TEXT,                        -- e.g. '必修一 P32'
    module_ids TEXT NOT NULL DEFAULT '[]',    -- JSON array of module IDs
    hp_total INTEGER DEFAULT 100,
    hp_current INTEGER DEFAULT 100,
    boss_type TEXT DEFAULT 'normal',          -- 'normal'|'elite'|'world_boss'
    guild_id INTEGER,                         -- if world boss
    status TEXT DEFAULT 'active',             -- 'active'|'cleared'
    defeat_count INTEGER DEFAULT 0,           -- 同类击败数
    created_from_mistake_id INTEGER,
    created_date TEXT DEFAULT (datetime('now'))
);
```

### blind_spot_rounds (盲点复测轮次)
```sql
CREATE TABLE blind_spot_rounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    blind_spot_id INTEGER NOT NULL,
    round INTEGER NOT NULL CHECK(round BETWEEN 1 AND 4),
    question TEXT NOT NULL,                    -- 题目内容
    question_type TEXT DEFAULT 'variant',     -- 'original'|'variant'|'comprehensive'
    scheduled_date TEXT NOT NULL,
    result TEXT DEFAULT 'pending',            -- 'pending'|'correct'|'wrong'
    answered_date TEXT
);
```

### practice_records (刷题记录)
```sql
CREATE TABLE practice_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    correct_count INTEGER NOT NULL,
    time_used_sec INTEGER,
    practice_date TEXT DEFAULT (datetime('now'))
);
```

### checkins (打卡)
```sql
CREATE TABLE checkins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    checkin_date TEXT NOT NULL,
    UNIQUE(player_id, checkin_date)
);
```

### achievements (成就)
```sql
CREATE TABLE achievements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    badge_key TEXT NOT NULL,
    unlocked_date TEXT,
    displayed INTEGER DEFAULT 0,
    UNIQUE(player_id, badge_key)
);
```

### seasons (赛季)
```sql
CREATE TABLE seasons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    reward_tiers TEXT NOT NULL DEFAULT '[]',   -- JSON: [{tier, xp_required, reward}]
    active INTEGER DEFAULT 1
);
```

### guilds (公会)
```sql
CREATE TABLE guilds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    daily_xp INTEGER DEFAULT 0,
    weekly_xp INTEGER DEFAULT 0,
    members TEXT NOT NULL DEFAULT '[]',         -- JSON array of {player_id, role, contribution}
    created_date TEXT DEFAULT (datetime('now'))
);
```

### cosmetic_drops_log (掉落播报)
```sql
CREATE TABLE cosmetic_drops_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    item_rarity TEXT NOT NULL,                 -- 'common'|'rare'|'epic'|'legendary'|'mythic'
    item_name TEXT NOT NULL,
    module_name TEXT,
    timestamp TEXT DEFAULT (datetime('now'))
);
```

---

## API 设计

### 玩家
```
POST   /api/players             创建玩家
GET    /api/players/{id}        获取玩家状态
POST   /api/players/{id}/checkin  每日打卡
POST   /api/players/{id}/claim-energy  领取体力
```

### 任务
```
GET    /api/players/{id}/tasks?date=YYYY-MM-DD   获取今日任务
POST   /api/players/{id}/tasks/{task_id}/complete  完成任务
POST   /api/players/{id}/tasks/generate           生成明日任务
```

### 刷题
```
GET    /api/modules              获取所有模块
GET    /api/modules/{id}/practice  获取模块练习题
POST   /api/players/{id}/practice  提交练习结果 → 返回翻牌结果
```

### 错题/盲点
```
POST   /api/players/{id}/mistakes           录入错题 (含三问法 + 盲点标签)
GET    /api/players/{id}/mistakes           获取错题列表
POST   /api/players/{id}/mistakes/{id}/retry  重做错题
GET    /api/players/{id}/blind-spots         获取盲点怪物列表
POST   /api/players/{id}/blind-spots/{id}/attack  攻击盲点Boss (复测)
GET    /api/players/{id}/blind-spots/due-today   今日待复测
```

### 赛季/通行证
```
GET    /api/seasons/current               当前赛季信息
GET    /api/players/{id}/battle-pass      通行证进度
POST   /api/players/{id}/battle-pass/claim  领取通行证奖励
```

### 公会
```
POST   /api/guilds                   创建公会
POST   /api/guilds/{id}/join         加入公会
GET    /api/guilds/{id}              公会详情
POST   /api/guilds/{id}/contribute   贡献攻击
```

### 成就/装扮
```
GET    /api/players/{id}/achievements     成就列表
GET    /api/players/{id}/cosmetics        已拥有装扮
POST   /api/players/{id}/cosmetics/equip  装备装扮
GET    /api/cosmetics/shop                装扮商店
POST   /api/players/{id}/shop/buy         购买/抽卡
```

### 统计
```
GET    /api/players/{id}/dashboard         仪表盘数据
GET    /api/players/{id}/progress          进度数据
```

---

## 游戏化机制实现要点

### 变量奖励 (翻牌)
- 翻牌概率: 普通 70% / 稀有 20% / 史诗 8% / 传说 1.5% / 神话 0.5%
- 前端实现 1.5 秒悬念动画（翻牌 + 光芒颜色 + 音效模拟）
- 连击天数 ≥7 → 传说概率翻倍（1.5% → 3%）

### 连击保护
- 每天首次打卡即续连击
- 每周获得 1 个"连击护盾"，周末可用
- 3 次完美练习（100% 正确率）兑换 1 次补卡

### 接近胜利
- 正确率在 85%-94% 时触发"再来一套"对话框
- 提示"如果下一套全对 → 三倍奖励"

### 体力系统
- 上限 100，每 5 分钟回复 1 点（服务端计算）
- 8:00 / 12:00 / 20:00 三个时段各送 20 点（可累积但不超上限）
- 错题复测返还 50% 消耗

### 赛季
- 每两个月一赛季，匹配备考阶段
- 赛季结束后未领取奖励绝版
- 赛季经验来源：每日任务、消灭盲点、模考进步

### 公会
- 3-5 人小团体
- 每日总目标 300 XP → 全员额外翻牌
- 3 天无贡献 → 系统私下提醒
- 公会 Boss：超大 HP 盲点，全员攻击共享

---

## 前端交互细节

### 全局音效/动画
- 升级：光柱 + 音效
- 翻牌：1.5 秒悬念动画
- Boss 击杀：震屏 + 击杀动画
- 稀有掉落：屏幕边缘发光 + 左下角广播

### 响应式
- 优先桌面端（学习场景多为电脑）
- 移动端降级适配（查看进度、打卡）

---

## 项目结构

```
math-rpg/
├── app.py                    # FastAPI 入口
├── config.py                 # 配置（体力回复速率、概率表等）
├── database.py               # SQLite 初始化 + 连接管理
├── models/                   # Pydantic models
│   ├── player.py
│   ├── task.py
│   ├── mistake.py
│   ├── blind_spot.py
│   ├── practice.py
│   └── guild.py
├── routers/                  # API 路由
│   ├── players.py
│   ├── tasks.py
│   ├── practice.py
│   ├── mistakes.py
│   ├── blind_spots.py
│   ├── seasons.py
│   ├── guilds.py
│   ├── achievements.py
│   └── stats.py
├── services/                 # 业务逻辑
│   ├── player_service.py
│   ├── task_service.py
│   ├── practice_service.py
│   ├── mistake_service.py
│   ├── blind_spot_service.py
│   ├── season_service.py
│   ├── guild_service.py
│   ├── gacha_service.py      # 翻牌/抽卡逻辑
│   ├── mastery_service.py    # 掌握度五维评分
│   ├── difficulty_service.py # 动态难度校准
│   └── question_service.py   # 题目匹配/变式推荐
├── seed_data.py              # 初始化预设数据（模块、成就、赛季、题目、模式、知识点图）
├── tools/                    # 开发阶段一次性脚本（离线AI分析用）
│   ├── analyze_exam.py       # LLM 分析真题 → 结构化JSON
│   ├── generate_variants.py  # LLM 批量生成变式题
│   └── merge_seed.py         # 合并所有数据 → seed_data.py
├── static/
│   ├── index.html            # SPA 入口
│   ├── css/
│   │   └── styles.css
│   └── js/
│       ├── app.js            # 路由 + 全局状态
│       ├── dashboard.js      # 仪表盘
│       ├── tasks.js          # 任务板
│       ├── practice.js       # 狩猎场（刷题）
│       ├── mistakes.js       # 怪物图鉴（错题/盲点）
│       ├── progress.js       # 修炼进度
│       ├── guild.js          # 公会
│       ├── season.js         # 赛季通行证
│       ├── achievements.js   # 成就殿堂
│       ├── components.js     # 共用组件（翻牌动画、XP条、体力条...）
│       └── audio.js          # 音效管理
└── math_rpg.db               # SQLite 数据库文件 (auto-generated)
```

---

## 智能题库系统

### 核心思路：真题驱动 + AI 分析 + 自动变式

```
历年高考真题 ─┐
              ├──→ LLM 分析引擎 ──→ 出题模式库 ──→ 智能生成引擎 ──→ 题目池
网络学习资料 ─┘                            │
                                           ├── 难度模型（知识点数 / 推导步数 / 易错陷阱）
                                           ├── 变式模板（改数 / 改条件 / 反向 / 跨模块综合）
                                           └── 知识点依赖图谱

用户录入错题 ──→ 盲点标签 ──→ 系统匹配同类变式题 ──↗
```

**关键设计**：所有 AI 工作在开发阶段离线完成，运行时纯本地，零 API 成本。

### 三引擎架构

**引擎一：真题解析（离线 · 开发阶段跑一次）**

收集 2019-2025 高考真题 + 经典模拟卷，用 LLM 对每道题输出结构化分析：

```json
{
  "module": "三角函数",
  "sub_topics": ["和差角公式", "二倍角公式"],
  "difficulty": 2,
  "difficulty_factors": {
    "concept_count": 2,
    "step_count": 4,
    "has_trap": false,
    "computation_complexity": "medium"
  },
  "pattern": "已知A求B型",
  "pattern_template": "已知 {条件1} 和 {条件2}，求 {目标表达式} 的值",
  "variant_axes": [
    "替换条件1的数值",
    "更换函数类型",
    "增加中间步骤",
    "反向：已知结果求条件"
  ]
}
```

**引擎二：难度自适应（运行时动态校准）**

```
初始标注（规则驱动）:
├── 难度1: 单一知识点 + 直接套公式 + ≤2步推导
├── 难度2: 2-3知识点 + 需要转化 + 3-5步推导
└── 难度3: 多知识点综合 + 需要构造 + ≥5步 或 含陷阱

运行时校准:
├── 某题标注难度2，但用户正确率仅40% → 动态难度上调为3
├── 每100次作答自动重新评估难度标签
└── 用户当前水平与题目难度匹配度 → 决定是否出这道题
```

**引擎三：变式生成（离线批量 + 用户错题驱动）**

```
原题: sinα=3/5, α∈(0,π/2)，求 cosα

变式维度:
├── 数值变更: sinα=5/13 → cosα
├── 条件增强: 追一步二倍角 → sin2α
├── 反向设问: 已知 sinα+cosα=7/5，求 sinα·cosα
├── 跨模块: △ABC中用正弦定理
└── 陷阱版: α是三角形内角 → 需判断象限

每个变式自动标注:
├── 难度变化 (原题难度 ± 0~1)
├── 涉及知识点列表
└── 做错时可拆解回盲点标签
```

### 新增数据表

```sql
-- 出题模式（真题分析产物）
CREATE TABLE question_patterns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    name TEXT NOT NULL,                   -- e.g. '和差角求值-已知A求B型'
    template TEXT NOT NULL,
    difficulty_base INTEGER DEFAULT 1,
    variant_axes TEXT NOT NULL,           -- JSON: 可变式维度列表
    source_question TEXT                  -- 来源真题追溯
);

-- 题目（升级版）
CREATE TABLE questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    pattern_id INTEGER,                   -- 关联出题模式
    type TEXT NOT NULL,                   -- 'choice'|'fill'|'answer'
    difficulty INTEGER DEFAULT 1,
    difficulty_dynamic REAL,              -- 动态难度（答题数据校准）
    total_attempts INTEGER DEFAULT 0,
    total_correct INTEGER DEFAULT 0,
    concepts TEXT NOT NULL DEFAULT '[]',  -- JSON: 知识点列表
    step_count INTEGER DEFAULT 1,
    has_trap INTEGER DEFAULT 0,
    content TEXT NOT NULL,
    options TEXT,                         -- JSON (选择题)
    answer TEXT NOT NULL,
    solution TEXT,
    time_limit_sec INTEGER,
    variant_of INTEGER,                   -- 变式来源题ID
    variant_axis TEXT,                    -- 用了哪个变式维度
    source_type TEXT DEFAULT 'generated', -- 'real_exam'|'generated'|'user_submitted'
    source_ref TEXT                       -- e.g. '2023新高考I卷·T7'
);

-- 知识点依赖图（用于提示连锁影响）
CREATE TABLE concept_dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    concept_name TEXT NOT NULL,            -- e.g. '完全平方公式'
    parent_concept TEXT,                   -- 前置知识点
    textbook_ref TEXT                      -- e.g. '必修一 P32'
);
```

### 题目获取逻辑
- 练习时：优先返回该模块未做过 + 难度匹配用户当前水平的题
- 错题重做时：从 `mistakes` 关联原题
- 盲点复测：第1轮原题，第2-4轮匹配同 `concepts` 标签的变式题
- 变式题耗尽时：标记对应 pattern，提示用户补充新错题来驱动生成
- 用户录入错题时：自动匹配 `concepts`，无匹配则创建新盲点标签

### 题库准备流程（开发阶段）

| 步骤 | 内容 | 工具 |
|------|------|------|
| 0 | 抓取 2019-2025 全国卷+新高考卷数理化真题文本 | 公开资源 |
| 1 | LLM 逐题分析 → 结构化 JSON（模式/知识点/难度因子/变式维度） | Claude API |
| 2 | LLM 为每个模式批量生成 20 道变式题 | Claude API |
| 3 | 人工抽检 10%，过滤明显错误 | 人工 |
| 4 | 全部打包进 `seed_data.py`，含模块/模式/题目/知识点图 | 代码 |
| 5 | 运行时：动态难度校准 + 用户错题驱动的匹配出题 | 代码 |

---

## 里程碑

| 阶段 | 内容 | 优先级 |
|------|------|--------|
| **P0** | 题库准备：真题抓取 + LLM 分析出题模式 + 批量生成变式 → 打包 seed_data | 前置 |
| **M1** | 项目骨架：FastAPI + SQLite + HTML SPA 框架 + 侧边栏导航 + 初始化种子数据 | 第一轮 |
| **M2** | 刷题系统：模块列表 + 选题（难度匹配）+ 答题界面 + 计时器 + 提交判分 + 翻牌动画 | 第一轮 |
| **M3** | 玩家系统：XP / 等级 / 体力 / 连击 / 打卡 / 装扮装备 | 第一轮 |
| **M4** | 错题本 + 盲点：三问法录入 → 自动拆盲点标签 → 怪物卡片 → 4轮复测调度 | 第二轮 |
| **M5** | 每日任务：自动生成主线/支线/挑战 + 任务板 UI + 完成结算 | 第二轮 |
| **M6** | 仪表盘：总体进度环图 + 分数预估 + 模块掌握度五维雷达图 + 连击日历热力图 | 第二轮 |
| **M7** | 赛季通行证：赛季倒计时 + 等级奖励 + FOMO 绝版提示 | 第三轮 |
| **M8** | 公会：创建/加入 + 每日贡献 + 公会Boss共享HP + 掉落播报 | 第三轮 |
| **M9** | 成就 + 商店：隐藏成就触发 + 抽卡（消耗金币）+ 战绩卡生成 | 第三轮 |
| **M10** | 打磨：全局音效/动画 + 移动端降级适配 + 性能优化 | 收尾 |
