import sqlite3
import json

DB_PATH = r'D:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

def check():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Count translated vs untranslated
    c.execute('SELECT COUNT(*) FROM questions WHERE content_en IS NULL')
    untranslated = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM questions WHERE content_en IS NOT NULL')
    translated = c.fetchone()[0]
    print(f"Translated: {translated}, Untranslated: {untranslated}")

    # Show sample translated
    c.execute('SELECT id, content_en FROM questions WHERE content_en IS NOT NULL ORDER BY id LIMIT 5')
    for r in c.fetchall():
        print(f"  ID {r[0]}: {r[1][:80]}")

    conn.close()

if __name__ == '__main__':
    check()
