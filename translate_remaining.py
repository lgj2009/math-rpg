"""
Translate remaining questions 51-72 using Google Translate API.
Keeps ALL LaTeX intact. Only translates Chinese text.
"""
import sqlite3, json, re, time, sys
from googletrans import Translator

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"
sys.stdout.reconfigure(encoding='utf-8')

def extract_latex(text):
    if not text: return text, {}
    placeholders = {}
    def rep(m):
        idx = len(placeholders)
        ph = f'__LX_{idx}__'
        placeholders[ph] = m.group(0)
        return ph
    text = re.sub(r'\$\$(.*?)\$\$', rep, text, flags=re.DOTALL)
    text = re.sub(r'\$(.*?)\$', rep, text)
    return text, placeholders

def restore_latex(text, placeholders):
    if not text: return text
    for ph, orig in placeholders.items():
        text = text.replace(ph, orig)
    return text

def translate_text(t, text, lang, retries=3):
    if not text or not text.strip(): return text
    protected, placeholders = extract_latex(text)
    if not protected.strip(): return text
    for attempt in range(retries):
        try:
            result = t.translate(protected, dest=lang, src='zh-cn')
            if result and result.text:
                return restore_latex(result.text, placeholders)
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(3)
            else:
                print(f"  Error: {e}", file=sys.stderr); return text
    return text

def translate_options(t, opt_json, lang):
    if not opt_json: return None
    try:
        opts = json.loads(opt_json)
    except json.JSONDecodeError:
        return opt_json
    return json.dumps([translate_text(t, o, lang) for o in opts], ensure_ascii=False)

def has_cn(text):
    return bool(text and re.search(r'[\u4e00-\u9fff]', str(text)))

def main():
    translator = Translator()
    conn = sqlite3.connect(DB_PATH)
    conn.text_factory = lambda x: str(x, 'utf-8', errors='replace')
    cur = conn.cursor()

    cur.execute('SELECT id, content, options, answer, solution FROM questions WHERE id BETWEEN 51 AND 72 AND content_en IS NULL ORDER BY id')
    rows = cur.fetchall()
    print(f'Found {len(rows)} remaining questions to translate (51-72)')

    if not rows:
        print('All questions 51-72 are already translated!')
        conn.close()
        return

    updated = 0
    for row in rows:
        qid, content, options, answer, solution = row
        print(f'\n--- Q{qid} ---')
        print(f'  CN: {content[:90]}{"..." if len(content)>90 else ""}')

        content_en = translate_text(translator, content, 'en') if has_cn(content) else content
        content_vi = translate_text(translator, content, 'vi') if has_cn(content) else content
        print(f'  EN: {content_en[:90]}{"..." if len(content_en)>90 else ""}')
        print(f'  VI: {content_vi[:90]}{"..." if len(content_vi)>90 else ""}')

        options_en = options_vi = None
        if options:
            try:
                ol = json.loads(options)
                if any(has_cn(o) for o in ol):
                    options_en = translate_options(translator, options, 'en')
                    options_vi = translate_options(translator, options, 'vi')
                else:
                    options_en = options_vi = options
            except json.JSONDecodeError as e:
                print(f"  Options parse error: {e}")
                options_en = options_vi = options

        answer_en = answer_vi = answer
        if has_cn(answer):
            answer_en = translate_text(translator, answer, 'en')
            answer_vi = translate_text(translator, answer, 'vi')

        solution_en = solution_vi = solution
        if has_cn(solution):
            solution_en = translate_text(translator, solution, 'en')
            solution_vi = translate_text(translator, solution, 'vi')

        cur.execute('''UPDATE questions SET content_en=?,content_vi=?,options_en=?,options_vi=?,
            answer_en=?,answer_vi=?,solution_en=?,solution_vi=? WHERE id=?''',
            (content_en, content_vi, options_en, options_vi, answer_en, answer_vi, solution_en, solution_vi, qid))
        conn.commit()
        updated += 1
        print(f'  => Updated Q{qid}')
        time.sleep(1.5)

    conn.close()
    print(f'\nDone! Updated {updated} remaining questions.')

if __name__ == '__main__':
    main()
