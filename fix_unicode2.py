import sqlite3

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"

def fix_text(text):
    if text is None:
        return None
    # Remove stray backslashes before non-ASCII characters
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        nxt = text[i+1] if i+1 < len(text) else ''
        if ch == chr(92) and nxt and ord(nxt) > 127:
            i += 1
            continue
        result.append(ch)
        i += 1
    return ''.join(result)

def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    fields = ['content_vi', 'options_vi', 'answer_vi', 'solution_vi']
    fixed = 0
    for qid in range(1, 51):
        updates = []
        params = []
        for f in fields:
            c.execute(f'SELECT {f} FROM questions WHERE id=?', (qid,))
            val = c.fetchone()[0]
            if val is None:
                updates.append(f'{f}=?')
                params.append(None)
            else:
                new_val = fix_text(val)
                if new_val != val:
                    fixed += 1
                updates.append(f'{f}=?')
                params.append(new_val)
        sql = f'UPDATE questions SET {", ".join(updates)} WHERE id=?'
        params.append(qid)
        c.execute(sql, params)
    conn.commit()
    conn.close()
    print(f'Fixed {fixed} fields')

if __name__ == '__main__':
    main()
