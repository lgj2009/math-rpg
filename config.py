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
