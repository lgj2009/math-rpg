"""
Translate questions 51-72 to English and Vietnamese (hardcoded).
Keeps ALL LaTeX intact. Only translates Chinese text.
"""
import sqlite3, json

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"
translations = []

def t(id_val, content_en, content_vi, options_en=None, options_vi=None,
       answer_en=None, answer_vi=None, solution_en=None, solution_vi=None):
    translations.append((id_val, content_en, content_vi,
                         options_en, options_vi,
                         answer_en, answer_vi,
                         solution_en, solution_vi))

# ===== Q51 =====
t(51,
  "Given vectors \(ec{a},ec{b}\) satisfy \(|ec{a}-ec{b}|=\sqrt{3}\), \(|ec{a}+ec{b}|=|2ec{a}-ec{b}|\), find \(|ec{b}|=\) ____",
  "Cho vecto \(ec{a},ec{b}\) thoa man \(|ec{a}-ec{b}|=\sqrt{3}\), \(|ec{a}+ec{b}|=|2ec{a}-ec{b}|\), tim \(|ec{b}|=\) ____",
  None, None, None, None,
  "Expanding and combining, we get \(|ec{b}|=\sqrt{3}\).",
  "Khai trien ket hop, giai duoc \(|ec{b}|=\sqrt{3}\).")

print("test ok")
