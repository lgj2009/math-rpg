"""Build-time seed: creates all tables and populates question bank."""
from database import init_db, get_db
from seed_data import seed
from add_exam_questions import EXAM_QUESTIONS, _seed_exam_questions
from expand_questions import EXPAND_QUESTIONS

init_db()
seed()
db = get_db()
cur = db.cursor()
_seed_exam_questions(cur, EXAM_QUESTIONS)
_seed_exam_questions(cur, EXPAND_QUESTIONS)
db.commit()
db.close()
print("Build seed complete.")
