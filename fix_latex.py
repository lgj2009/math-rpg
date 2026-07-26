#!/usr/bin/env python3
"""Fix corrupted LaTeX in the database translations."""

import sqlite3

DB_PATH = 'd:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

conn = sqlite3.connect(DB_PATH)
conn.text_factory = str
cursor = conn.cursor()

# Check current state of ID 54 solution
cursor.execute('SELECT solution_en FROM questions WHERE id=54')
current = cursor.fetchone()[0]
print(f"Current ID 54 solution:\n{repr(current)}\n")

# The correct solution - use raw strings to avoid Python escape issues
correct = (r"$f'(x)=3x^2-1$, critical points at $x=\pm\frac{1}{\sqrt{3}}$."
           r" $f(-2)=-5$, $f(-\frac{1}{\sqrt{3}})\approx1.38$, $f(\frac{1}{\sqrt{3}})\approx0.62$, $f(2)=7$."
           r" Max value is 7, min value is -5, their sum is 4.")

cursor.execute('UPDATE questions SET solution_en=? WHERE id=?', (correct, 54))
conn.commit()
print(f"Updated to:\n{repr(correct)}\n")

# Verify
cursor.execute('SELECT solution_en FROM questions WHERE id=54')
updated = cursor.fetchone()[0]
print(f"Verified:\n{repr(updated)}")

# Check that backslashes are intact
if '\\frac' in updated and '\\sqrt' in updated:
    print("SUCCESS: LaTeX backslashes are preserved!")
else:
    print("WARNING: LaTeX backslashes may still be corrupted!")

conn.close()
