# Task 9: Seed Questions — Report

## Summary
Successfully seeded 41 questions across all 8 modules into the `questions` table.

## Count Per Module

| Module | Name | Count |
|--------|------|-------|
| 1 | 三角函数与解三角形 | 6 |
| 2 | 数列 | 5 |
| 3 | 统计与概率 | 5 |
| 4 | 立体几何 | 5 |
| 5 | 解析几何 | 5 |
| 6 | 导数及其应用 | 5 |
| 7 | 集合与常用逻辑 | 5 |
| 8 | 复数与向量 | 5 |
| **Total** | | **41** |

## Type Distribution
- choice: 18
- fill: 16
- answer: 7

## Difficulty Distribution
- difficulty 1: 17 questions
- difficulty 2: 24 questions
- difficulty 3: 0 (none required for this task)

## Question Accuracy Review

All questions were manually verified for mathematical correctness:

### Module 1 (三角函数与解三角形)
- Q1: sinα=3/5 → cosα=4/5 (Pythagorean identity, α in Q1) ✓
- Q2: sinα=1/3 → cos2α=7/9 (double-angle formula) ✓
- Q3: Triangle a=3,b=4,C=60° → c=√13 (cosine theorem) ✓
- Q4: sin75° = (√6+√2)/4 (sum-angle formula) ✓
- Q5: Triangle A=45°,B=60°,a=2 → b=√6 (sine theorem) ✓
- Q6: Triangle a=2,b=3,c=√7 → C=60° (cosine theorem, has trap: students may mistake angle for side) ✓

### Module 2 (数列)
- Q7: a₁=2,d=3 → a₅=14 (arithmetic) ✓
- Q8: a₁=1,q=2 → S₅=31 (geometric sum) ✓
- Q9: Sₙ=2n²+n → a₃=11 (Sₙ difference method) ✓
- Q10: a₂=2,a₅=16 → S₄=15 (geometric, has trap: find q first) ✓
- Q11: ∑1/(n(n+1)) from 1 to 100 = 100/101 (telescoping) ✓

### Module 3 (统计与概率)
- Q12: 5 books arrangement = 5! = 120 ✓
- Q13: Choose 2 from 10 = C(10,2) = 45 ✓
- Q14: Two dice sum 7 = 6/36 = 1/6 ✓
- Q15: (x+1)⁴, x² coefficient = C(4,2) = 6 ✓
- Q16: E(X) for die = 3.5 ✓

### Module 4 (立体几何)
- Q17: Cube side 2, diagonal = 2√3 ✓
- Q18: Sphere r=3, V=36π ✓
- Q19: Rectangular prism 3×4×5, diagonal-base angle tanθ=1 (has trap: 5/√(3²+4²)=1, not √2) ✓
- Q20: Pyramid square base 2, height 3, V=4 ✓
- Q21: Cone r=3, h=4, lateral area = 15π ✓

### Module 5 (解析几何)
- Q22: Circle x²+y²=4, r=2 ✓
- Q23: Distance (1,2)-(4,6) = 5 ✓
- Q24: Ellipse x²/9+y²/4=1, focal length = 2√5 ✓
- Q25: Parabola y²=8x, focus = (2,0) ✓
- Q26: Hyperbola x²/3-y²/4=1, asymptotes y=±(2/√3)x ✓

### Module 6 (导数及其应用)
- Q27: f(x)=x², f'(2)=4 ✓
- Q28: f(x)=sin x, f'(π/3)=1/2 ✓
- Q29: f(x)=x³-3x, local max = 2 (has trap: second derivative test needed) ✓
- Q30: f(x)=ln x, tangent at x=1: y=x-1 ✓
- Q31: f(x)=x³-6x²+9x+1, max on [0,4] = 5 (has trap: endpoints matter) ✓

### Module 7 (集合与常用逻辑)
- Q32: {1,2,3}∩{2,3,4}={2,3} ✓
- Q33: {x|x>2}∪{x|x≤5}=R ✓
- Q34: x=1 is sufficient but not necessary for x²=1 ✓
- Q35: |{1,2,3}| subsets = 8 ✓
- Q36: x>2 is sufficient but not necessary for x²>4 ✓

### Module 8 (复数与向量)
- Q37: (1+i)² = 2i ✓
- Q38: z²=-1 → z=±i ✓
- Q39: (1,2)·(3,4)=11 ✓
- Q40: |a|=2,|b|=3,angle=60°, a·b=3 ✓
- Q41: a=(1,2),b=(2,1), cosθ=4/5 ✓

## Files Modified
- `d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/seed_data.py` — Added `SEED_QUESTIONS` list (41 questions) and `_seed_questions(cur)` function; called from `seed()`

## How to Verify
```bash
cd <project_dir>
python seed_data.py
python -c "import sqlite3; c=sqlite3.connect('math_rpg.db'); print(c.execute('SELECT COUNT(*) FROM questions').fetchone()[0])"
```
Expected output: `41`

## P1 Fixes Applied (2026-07-25)

### P1-1: Wrong concepts on Q22 and Q23
- **Q22** (circle radius): concept changed from `["椭圆标准方程"]` to `["圆的标准方程"]`
- **Q23** (distance between points): concept changed from `["椭圆标准方程"]` to `["两点间距离公式"]`
- Added to CONCEPT_DEPS:
  - `("圆的标准方程", None, "必修二 P10")`
  - `("两点间距离公式", None, "必修二 P105")`

### P1-2: Duplicate option values in Q19
- Q19 option D: changed from `\frac{5}{5}` (= 1, same as option B) to `\frac{5}{4}` (distinct distractor)

### Files Changed
- `seed_data.py`: concept tags, CONCEPT_DEPS additions, Q19 option D value
- `database.py`: added `idx_questions_content` unique index for idempotency (also committed as part of this task)

Both fixes verified: `python seed_data.py` yields 41 rows, no duplicates, no encoding errors.
