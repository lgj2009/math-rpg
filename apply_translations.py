"""
Read translations JSON and update the database.
"""
import sqlite3
import json

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"

# Load translations
with open('translations_51_72.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

print(f"Loaded translations for {len(translations)} questions")

conn = sqlite3.connect(DB_PATH)
conn.text_factory = lambda x: str(x, 'utf-8', errors='replace')
cur = conn.cursor()

updated = 0
for qid_str, data in sorted(translations.items()):
    qid = int(qid_str)
    cur.execute("""
        UPDATE questions
        SET content_en = ?, content_vi = ?,
            options_en = ?, options_vi = ?,
            answer_en = ?, answer_vi = ?,
            solution_en = ?, solution_vi = ?
        WHERE id = ?
    """, (
        data.get('content_en'),
        data.get('content_vi'),
        data.get('options_en'),
        data.get('options_vi'),
        data.get('answer_en'),
        data.get('answer_vi'),
        data.get('solution_en'),
        data.get('solution_vi'),
        qid
    ))
    updated += 1
    print(f"  Updated Q{qid}")

conn.commit()
conn.close()
print(f"\nDone! Updated {updated} questions.")
