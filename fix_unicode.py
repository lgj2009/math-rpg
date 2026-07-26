import sqlite3

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"


def remove_stray_backslashes(text):
    """Remove backslashes that appear before actual Unicode characters
    (which were originally backslash-uXXXX sequences where the conversion
    left the backslash)."""
    if text is None:
        return None
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        # If current char is \, look ahead for a non-ASCII char
        if ch == '\\' and i + 1 < len(text):
            # Check if next char is non-ASCII (was a converted \uXXXX)
            next_ch = text[i + 1]
            if ord(next_ch) > 127:
                # This is a stray backslash before a Unicode character
                # Skip it, keep the Unicode character
                i += 1
                continue
            # Also handle the case where \uXXXX was only partially converted
            # (e.g., \u0110 -> \Đ where \ was left)
        result.append(ch)
        i += 1
    return ''.join(result)


def fix_unicode_correctly(text):
    """Convert literal \uXXXX sequences to actual Unicode characters."""
    if text is None:
        return None
    result = []
    i = 0
    while i < len(text):
        ch = text[i]
        # Look for \uXXXX where XXXX is 4 hex digits
        if (ch == '\\' and i + 5 < len(text) and text[i+1] == 'u' and
            all(c in '0123456789abcdefABCDEF' for c in text[i+2:i+6])):
            hex_val = int(text[i+2:i+6], 16)
            result.append(chr(hex_val))
            i += 6
        else:
            result.append(ch)
            i += 1
    return ''.join(result)


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    fields = ['content_vi', 'options_vi', 'answer_vi', 'solution_vi']
    fixed_count = 0

    for qid in range(1, 51):
        updates = []
        params = []
        for field in fields:
            c.execute(f'SELECT {field} FROM questions WHERE id=?', (qid,))
            val = c.fetchone()[0]
            if val is None:
                updates.append(f'{field}=?')
                params.append(None)
            else:
                # First pass: convert remaining \uXXXX to Unicode chars
                val1 = fix_unicode_correctly(val)
                # Second pass: remove stray backslashes before Unicode chars
                val2 = remove_stray_backslashes(val1)
                if val2 != val:
                    fixed_count += 1
                updates.append(f'{field}=?')
                params.append(val2)

        sql = f'UPDATE questions SET {", ".join(updates)} WHERE id=?'
        params.append(qid)
        c.execute(sql, params)

    conn.commit()
    conn.close()
    print(f'Fixed {fixed_count} modified fields across questions 1-50.')


if __name__ == '__main__':
    main()
