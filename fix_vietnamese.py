import sqlite3, re

DB = r"D:\编程\Python\stutdy\.claude\worktrees\math-rpg-implementation\math_rpg.db"

def fix_escapes(s):
    if not s:
        return s
    # Match literal \uXXXX in the stored text and replace with actual Unicode
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("SELECT id, content_vi, options_vi, answer_vi, solution_vi FROM questions WHERE id <= 50")
rows = cur.fetchall()
count = 0
for r in rows:
    qid = r[0]
    cv = fix_escapes(r[1])
    ov = fix_escapes(r[2]) if r[2] else r[2]
    av = fix_escapes(r[3]) if r[3] else r[3]
    sv = fix_escapes(r[4])
    cur.execute("UPDATE questions SET content_vi=?, options_vi=?, answer_vi=?, solution_vi=? WHERE id=?",
                (cv, ov, av, sv, qid))
    count += 1
conn.commit()

cur.execute("SELECT id, content_vi FROM questions WHERE id IN (1,7,12,34,50)")
for r in cur.fetchall():
    print(f"Q{r[0]}: {r[1]}")
    print(f"  has unicode: {any(ord(c)>127 for c in r[1])}")
    print()

conn.close()
print(f"Fixed {count} questions.")
