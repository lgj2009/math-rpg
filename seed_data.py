"""Idempotent seed data. Safe to run multiple times — uses INSERT OR IGNORE."""
import sqlite3
import json
from database import get_db

MODULES = [
    (1, "三角函数与解三角形", 15, 1, 1, "📐", "和差角公式、二倍角公式、正弦定理、余弦定理"),
    (2, "数列", 12, 1, 2, "🔢", "等差/等比数列通项与求和、裂项相消、错位相减"),
    (3, "统计与概率", 17, 1, 3, "🎲", "排列组合、二项式定理、分布列与期望"),
    (4, "立体几何", 17, 2, 4, "📦", "空间向量法：建系→法向量→角与距离"),
    (5, "解析几何", 17, 2, 5, "📈", "椭圆/双曲线/抛物线、联立+韦达定理"),
    (6, "导数及其应用", 17, 2, 6, "📉", "单调性、极值最值、切线问题"),
    (7, "集合与常用逻辑", 5, 3, 7, "🔤", "集合运算、充要条件"),
    (8, "复数与向量", 10, 3, 8, "🧮", "复数运算、向量坐标运算"),
]

CONCEPT_DEPS = [
    ("完全平方公式", None, "必修一 P32"),
    ("一元二次函数图像", "完全平方公式", "必修一 P36"),
    ("一元二次不等式", "一元二次函数图像", "必修一 P40"),
    ("穿根法", "一元二次不等式", "必修一 P42"),
    ("正弦定理", None, "必修五 P2"),
    ("余弦定理", None, "必修五 P6"),
    ("和差角公式", None, "必修四 P25"),
    ("二倍角公式", "和差角公式", "必修四 P30"),
    ("等差数列通项", None, "必修五 P35"),
    ("等比数列通项", None, "必修五 P48"),
    ("裂项相消", "等差数列通项", "必修五 P55"),
    ("错位相减", "等比数列通项", "必修五 P56"),
    ("空间向量坐标运算", None, "选修2-1 P85"),
    ("法向量求法", "空间向量坐标运算", "选修2-1 P90"),
    ("导数定义", None, "选修2-2 P2"),
    ("导数单调性", "导数定义", "选修2-2 P22"),
    ("导数极值最值", "导数单调性", "选修2-2 P28"),
    ("导数切线", "导数定义", "选修2-2 P16"),
    ("椭圆标准方程", None, "选修2-1 P38"),
    ("双曲线标准方程", None, "选修2-1 P50"),
    ("抛物线标准方程", None, "选修2-1 P60"),
    ("圆的标准方程", None, "必修二 P10"),
    ("两点间距离公式", None, "必修二 P105"),
]

SEED_QUESTIONS = [
    # ==================== Module 1: 三角函数与解三角形 (6 questions) ====================
    # Q1: choice, diff 1, sin(x) given find cos(x)
    (1, None, "choice", 1, '["同角三角函数关系"]', 2, 0,
     "已知 $\\sin\\alpha = \\frac{3}{5}$，$\\alpha \\in (0, \\frac{\\pi}{2})$，则 $\\cos\\alpha$ 等于",
     '["A. \\\\frac{3}{5}", "B. \\\\frac{4}{5}", "C. -\\\\frac{4}{5}", "D. \\\\frac{5}{3}"]',
     "B", "由 $\\sin^2\\alpha + \\cos^2\\alpha = 1$，$\\alpha$ 在第一象限，$\\cos\\alpha = \\frac{4}{5}$", 60,
     None, None, "generated", None),

    # Q2: fill, diff 1, double-angle formula
    (1, None, "fill", 1, '["二倍角公式"]', 2, 0,
     "已知 $\\sin\\alpha = \\frac{1}{3}$，则 $\\cos 2\\alpha =$ ____",
     None, "7/9", "$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\times \\frac{1}{9} = \\frac{7}{9}$", 90,
     None, None, "generated", None),

    # Q3: answer, diff 2, cosine theorem
    (1, None, "answer", 2, '["正弦定理","余弦定理"]', 4, 0,
     "在 $\\triangle ABC$ 中，已知 $a=3$，$b=4$，$\\angle C = 60\\degree$，求边 $c$ 的长度",
     None, "\\sqrt{13}", "由余弦定理 $c^2 = a^2 + b^2 - 2ab\\cos C = 9 + 16 - 24 \\times \\frac{1}{2} = 13$，$c = \\sqrt{13}$", 120,
     None, None, "generated", None),

    # Q4: choice, diff 1, sin 75 degrees
    (1, None, "choice", 1, '["和差角公式"]', 2, 0,
     "$\\sin 75\\degree$ 的值为",
     '["A. \\\\frac{\\\\sqrt{6}+\\\\sqrt{2}}{4}", "B. \\\\frac{\\\\sqrt{6}-\\\\sqrt{2}}{4}", "C. \\\\frac{\\\\sqrt{3}}{2}", "D. \\\\frac{1}{2}"]',
     "A", "$\\sin 75\\degree = \\sin(45\\degree+30\\degree) = \\sin 45\\degree\\cos 30\\degree + \\cos 45\\degree\\sin 30\\degree = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$", 90,
     None, None, "generated", None),

    # Q5: fill, diff 2, sine theorem
    (1, None, "fill", 2, '["正弦定理"]', 3, 0,
     "在 $\\triangle ABC$ 中，已知 $\\angle A = 45\\degree$，$\\angle B = 60\\degree$，$a = 2$，则 $b =$ ____",
     None, "\\sqrt{6}", "由正弦定理 $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$，$b = \\frac{a\\sin B}{\\sin A} = \\frac{2 \\times \\sqrt{3}/2}{\\sqrt{2}/2} = \\sqrt{6}$", 120,
     None, None, "generated", None),

    # Q6: choice, diff 2, cosine theorem find angle (has trap)
    (1, None, "choice", 2, '["余弦定理"]', 3, 1,
     "在 $\\triangle ABC$ 中，$a=2$，$b=3$，$c=\\sqrt{7}$，则角 $C$ 的度数为",
     '["A. 30\\u00b0", "B. 45\\u00b0", "C. 60\\u00b0", "D. 90\\u00b0"]',
     "C", "由余弦定理 $\\cos C = \\frac{a^2+b^2-c^2}{2ab} = \\frac{4+9-7}{2\\times2\\times3} = \\frac{1}{2}$，$C=60\\degree$", 90,
     None, None, "generated", None),

    # ==================== Module 2: 数列 (5 questions) ====================
    # Q7: choice, diff 1, arithmetic sequence
    (2, None, "choice", 1, '["等差数列通项"]', 1, 0,
     "已知等差数列 $\\{a_n\\}$ 的首项 $a_1=2$，公差 $d=3$，则 $a_5$ 等于",
     '["A. 11", "B. 12", "C. 13", "D. 14"]',
     "D", "$a_5 = a_1 + (5-1)d = 2 + 4 \\times 3 = 14$", 60,
     None, None, "generated", None),

    # Q8: fill, diff 1, geometric sequence sum
    (2, None, "fill", 1, '["等比数列通项"]', 2, 0,
     "已知等比数列 $\\{a_n\\}$ 的首项 $a_1=1$，公比 $q=2$，则前 $5$ 项和 $S_5 =$ ____",
     None, "31", "$S_5 = a_1 \\frac{q^5-1}{q-1} = 1 \\times \\frac{2^5-1}{2-1} = 31$", 90,
     None, None, "generated", None),

    # Q9: choice, diff 2, Sn formula to find term
    (2, None, "choice", 2, '["等差数列通项"]', 2, 0,
     "已知数列 $\\{a_n\\}$ 的前 $n$ 项和 $S_n = 2n^2 + n$，则 $a_3$ 等于",
     '["A. 9", "B. 10", "C. 11", "D. 12"]',
     "C", "$a_3 = S_3 - S_2 = (2\\times9+3) - (2\\times4+2) = 21 - 10 = 11$", 90,
     None, None, "generated", None),

    # Q10: fill, diff 2, geometric sequence find sum (has trap)
    (2, None, "fill", 2, '["等比数列通项"]', 3, 1,
     "在等比数列 $\\{a_n\\}$ 中，$a_2=2$，$a_5=16$，则前 $4$ 项和 $S_4 =$ ____",
     None, "15", "$q^3 = \\frac{a_5}{a_2} = \\frac{16}{2} = 8$，$q=2$，$a_1=\\frac{a_2}{q}=1$，$S_4 = \\frac{1\\times(2^4-1)}{2-1}=15$", 120,
     None, None, "generated", None),

    # Q11: answer, diff 2, telescoping sum
    (2, None, "answer", 2, '["裂项相消"]', 3, 0,
     "求 $\\sum\\limits_{n=1}^{100} \\frac{1}{n(n+1)}$ 的值",
     None, "100/101", "$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$，$\\sum_{n=1}^{100} \\frac{1}{n(n+1)} = 1 - \\frac{1}{101} = \\frac{100}{101}$", 120,
     None, None, "generated", None),

    # ==================== Module 3: 统计与概率 (5 questions) ====================
    # Q12: choice, diff 1, permutation 5!
    (3, None, "choice", 1, '["排列","计数原理"]', 1, 0,
     "将 $5$ 本不同的书排成一排，共有多少种不同的排法",
     '["A. 60", "B. 100", "C. 120", "D. 240"]',
     "C", "$5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$", 60,
     None, None, "generated", None),

    # Q13: fill, diff 1, combination C(10,2)
    (3, None, "fill", 1, '["组合"]', 1, 0,
     "从 $10$ 名学生中选出 $2$ 名参加比赛，共有____种不同的选法",
     None, "45", "$\\mathrm{C}_{10}^2 = \\frac{10\\times9}{2} = 45$", 60,
     None, None, "generated", None),

    # Q14: choice, diff 2, dice probability sum=7
    (3, None, "choice", 2, '["古典概型"]', 2, 0,
     "投掷两枚均匀骰子，点数之和为 $7$ 的概率是",
     '["A. \\\\frac{1}{6}", "B. \\\\frac{1}{4}", "C. \\\\frac{1}{3}", "D. \\\\frac{5}{36}"]',
     "A", "点数之和为7的基本事件有(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)共6种，总事件36种，$P=\\frac{6}{36}=\\frac{1}{6}$", 90,
     None, None, "generated", None),

    # Q15: fill, diff 2, binomial coefficient
    (3, None, "fill", 2, '["二项式定理"]', 2, 0,
     "$(x+1)^4$ 的展开式中 $x^2$ 项的系数为____",
     None, "6", "$T_{r+1} = \\mathrm{C}_4^r x^{4-r} \\cdot 1^r$，令 $4-r=2$ 得 $r=2$，系数为 $\\mathrm{C}_4^2 = 6$", 90,
     None, None, "generated", None),

    # Q16: answer, diff 2, expected value
    (3, None, "answer", 2, '["数学期望"]', 2, 0,
     "掷一枚均匀骰子，记点数为 $X$，求 $E(X)$",
     None, "3.5", "$E(X) = \\frac{1+2+3+4+5+6}{6} = 3.5$", 90,
     None, None, "generated", None),

    # ==================== Module 4: 立体几何 (5 questions) ====================
    # Q17: choice, diff 1, cube diagonal
    (4, None, "choice", 1, '["空间几何体"]', 1, 0,
     "棱长为 $2$ 的正方体的体对角线长度为",
     '["A. 2", "B. 2\\\\sqrt{3}", "C. 2\\\\sqrt{2}", "D. 4"]',
     "B", "体对角线 $= \\sqrt{2^2+2^2+2^2} = 2\\sqrt{3}$", 60,
     None, None, "generated", None),

    # Q18: fill, diff 1, sphere volume
    (4, None, "fill", 1, '["空间几何体"]', 1, 0,
     "半径为 $3$ 的球体积为____",
     None, "$36\\pi$", "$V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi \\times 27 = 36\\pi$", 60,
     None, None, "generated", None),

    # Q19: choice, diff 2, rectangular prism diagonal angle (has trap)
    (4, None, "choice", 2, '["空间几何体"]', 3, 1,
     "长方体的长、宽、高分别为 $3$、$4$、$5$，则体对角线与底面所成角的正切值为",
     '["A. \\\\frac{\\\\sqrt{2}}{2}", "B. 1", "C. \\\\sqrt{2}", "D. \\\\frac{5}{4}"]',
     "B", "底面对角线 $= \\sqrt{3^2+4^2}=5$，高 $=5$，$\\tan\\theta = \\frac{5}{5} = 1$", 120,
     None, None, "generated", None),

    # Q20: fill, diff 2, pyramid volume
    (4, None, "fill", 2, '["空间几何体"]', 2, 0,
     "底面为边长为 $2$ 的正方形、高为 $3$ 的棱锥体积为____",
     None, "4", "$V = \\frac{1}{3}Sh = \\frac{1}{3} \\times 4 \\times 3 = 4$", 90,
     None, None, "generated", None),

    # Q21: answer, diff 2, cone lateral area
    (4, None, "answer", 2, '["空间几何体"]', 2, 0,
     "圆锥底面半径为 $3$，高为 $4$，求其侧面积",
     None, "$15\\pi$", "母线 $l = \\sqrt{3^2+4^2}=5$，侧面积 $S = \\pi r l = \\pi \\times 3 \\times 5 = 15\\pi$", 120,
     None, None, "generated", None),

    # ==================== Module 5: 解析几何 (5 questions) ====================
    # Q22: choice, diff 1, circle radius
    (5, None, "choice", 1, '["圆的标准方程"]', 1, 0,
     "圆 $x^2 + y^2 = 4$ 的半径为",
     '["A. 1", "B. 2", "C. 4", "D. 16"]',
     "B", "圆的标准方程 $x^2+y^2=r^2$，$r^2=4$，$r=2$", 60,
     None, None, "generated", None),

    # Q23: fill, diff 1, distance between points
    (5, None, "fill", 1, '["两点间距离公式"]', 1, 0,
     "点 $(1,2)$ 到点 $(4,6)$ 的距离为____",
     None, "5", "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9+16}=5$", 60,
     None, None, "generated", None),

    # Q24: choice, diff 2, ellipse focal length
    (5, None, "choice", 2, '["椭圆标准方程"]', 2, 0,
     "椭圆 $\\frac{x^2}{9} + \\frac{y^2}{4} = 1$ 的焦距为",
     '["A. 2\\\\sqrt{5}", "B. \\\\sqrt{5}", "C. 2", "D. 5"]',
     "A", "$a^2=9$，$b^2=4$，$c^2 = a^2-b^2 = 5$，焦距 $2c = 2\\sqrt{5}$", 90,
     None, None, "generated", None),

    # Q25: fill, diff 2, parabola focus
    (5, None, "fill", 2, '["抛物线标准方程"]', 2, 0,
     "抛物线 $y^2 = 8x$ 的焦点坐标为 (____, 0)",
     None, "2", "$y^2 = 2px$，$2p=8$，$p=4$，焦点 $\\left(\\frac{p}{2}, 0\\right) = (2, 0)$", 90,
     None, None, "generated", None),

    # Q26: answer, diff 2, hyperbola asymptotes
    (5, None, "answer", 2, '["双曲线标准方程"]', 2, 0,
     "求双曲线 $\\frac{x^2}{3} - \\frac{y^2}{4} = 1$ 的渐近线方程",
     None, "y=\\pm(2/\\sqrt{3})x", "$a^2=3$，$b^2=4$，渐近线 $y = \\pm\\frac{b}{a}x = \\pm\\frac{2}{\\sqrt{3}}x$", 90,
     None, None, "generated", None),

    # ==================== Module 6: 导数及其应用 (5 questions) ====================
    # Q27: choice, diff 1, derivative at a point
    (6, None, "choice", 1, '["导数定义"]', 1, 0,
     "函数 $f(x)=x^2$ 在 $x=2$ 处的导数值为",
     '["A. 2", "B. 3", "C. 4", "D. 5"]',
     "C", "$f'(x)=2x$，$f'(2)=4$", 60,
     None, None, "generated", None),

    # Q28: fill, diff 1, derivative of sin
    (6, None, "fill", 1, '["导数定义"]', 1, 0,
     "函数 $f(x)=\\sin x$ 在 $x=\\frac{\\pi}{3}$ 处的导数值为____",
     None, "1/2", "$f'(x)=\\cos x$，$f'(\\frac{\\pi}{3})=\\cos\\frac{\\pi}{3}=\\frac{1}{2}$", 60,
     None, None, "generated", None),

    # Q29: choice, diff 2, local maximum of cubic (has trap)
    (6, None, "choice", 2, '["导数极值最值"]', 3, 1,
     "函数 $f(x)=x^3-3x$ 的极大值为",
     '["A. -2", "B. 0", "C. 2", "D. 4"]',
     "C", "$f'(x)=3x^2-3=0$，$x=\\pm1$，$f''(x)=6x$，$f''(-1)=-6<0$ 为极大值点，$f(-1)=-1+3=2$", 90,
     None, None, "generated", None),

    # Q30: fill, diff 2, tangent line
    (6, None, "fill", 2, '["导数切线"]', 2, 0,
     "曲线 $f(x)=\\ln x$ 在 $x=1$ 处的切线方程为 $y =$ ____",
     None, "x-1", "$f'(x)=\\frac{1}{x}$，$f'(1)=1$，$f(1)=0$，切线 $y = 1\\times(x-1)+0 = x-1$", 90,
     None, None, "generated", None),

    # Q31: answer, diff 2, max on closed interval (has trap)
    (6, None, "answer", 2, '["导数极值最值"]', 4, 1,
     "求函数 $f(x)=x^3-6x^2+9x+1$ 在区间 $[0,4]$ 上的最大值",
     None, "5", "$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0$，$x=1,3$。$f(0)=1$，$f(1)=5$，$f(3)=1$，$f(4)=5$，最大值为$5$", 120,
     None, None, "generated", None),

    # ==================== Module 7: 集合与常用逻辑 (5 questions) ====================
    # Q32: choice, diff 1, set intersection
    (7, None, "choice", 1, '["集合运算"]', 1, 0,
     "已知集合 $A=\\{1,2,3\\}$，$B=\\{2,3,4\\}$，则 $A\\cap B$ 等于",
     '["A. \\\\{1,2,3,4\\\\}", "B. \\\\{2,3\\\\}", "C. \\\\{1,4\\\\}", "D. \\\\{1,2,3\\\\}"]',
     "B", "$A\\cap B = \\{2,3\\}$", 60,
     None, None, "generated", None),

    # Q33: fill, diff 1, set union
    (7, None, "fill", 1, '["集合运算"]', 1, 0,
     "已知集合 $A=\\{x\\mid x>2\\}$，$B=\\{x\\mid x\\le 5\\}$，则 $A\\cup B =$ ____（答案填R即可）",
     None, "R", "结合数轴，$A\\cup B$ 覆盖全体实数，结果为 $\\mathbb{R}$", 60,
     None, None, "generated", None),

    # Q34: choice, diff 2, sufficient condition
    (7, None, "choice", 2, '["充分条件","必要条件"]', 2, 0,
     '设 $x\\in\\mathbb{R}$，则 "$x=1$" 是 "$x^2=1$" 的',
     '["A. 充分必要条件", "B. 充分不必要条件", "C. 必要不充分条件", "D. 既不充分也不必要条件"]',
     "B", "$x=1\\Rightarrow x^2=1$，但 $x^2=1\\Rightarrow x=\\pm1$，故充分不必要", 90,
     None, None, "generated", None),

    # Q35: fill, diff 2, number of subsets
    (7, None, "fill", 2, '["集合运算"]', 1, 0,
     "集合 $\\{1,2,3\\}$ 的子集个数为____",
     None, "8", "$2^3 = 8$，分别为 $\\emptyset,\\{1\\},\\{2\\},\\{3\\},\\{1,2\\},\\{1,3\\},\\{2,3\\},\\{1,2,3\\}$", 60,
     None, None, "generated", None),

    # Q36: choice, diff 2, sufficient condition
    (7, None, "choice", 2, '["充分条件","必要条件"]', 2, 0,
     '设 $x\\in\\mathbb{R}$，则 "$x>2$" 是 "$x^2>4$" 的',
     '["A. 充分必要条件", "B. 充分不必要条件", "C. 必要不充分条件", "D. 既不充分也不必要条件"]',
     "B", "$x>2\\Rightarrow x^2>4$，但 $x^2>4\\Rightarrow x<-2$ 或 $x>2$，故充分不必要", 90,
     None, None, "generated", None),

    # ==================== Module 8: 复数与向量 (5 questions) ====================
    # Q37: choice, diff 1, (1+i)^2
    (8, None, "choice", 1, '["复数运算"]', 1, 0,
     "$(1+i)^2$ 等于",
     '["A. 0", "B. 2i", "C. 2", "D. 1+i"]',
     "B", "$(1+i)^2 = 1+2i+i^2 = 1+2i-1 = 2i$", 60,
     None, None, "generated", None),

    # Q38: fill, diff 1, solve z^2 = -1
    (8, None, "fill", 1, '["复数运算"]', 1, 0,
     "方程 $z^2 = -1$ 的解为 $z =$ ____（用 $i$ 表示）",
     None, "\\pm i", "由 $i^2=-1$，$(-i)^2=-1$，故 $z=\\pm i$", 60,
     None, None, "generated", None),

    # Q39: choice, diff 2, dot product
    (8, None, "choice", 2, '["空间向量坐标运算"]', 1, 0,
     "已知向量 $\\vec{a}=(1,2)$，$\\vec{b}=(3,4)$，则 $\\vec{a}\\cdot\\vec{b}$ 等于",
     '["A. 10", "B. 11", "C. 12", "D. 13"]',
     "B", "$\\vec{a}\\cdot\\vec{b} = 1\\times3 + 2\\times4 = 11$", 60,
     None, None, "generated", None),

    # Q40: fill, diff 2, dot product with angle
    (8, None, "fill", 2, '["空间向量坐标运算"]', 1, 0,
     "已知 $|\\vec{a}|=2$，$|\\vec{b}|=3$，$\\vec{a}$ 与 $\\vec{b}$ 夹角为 $60\\degree$，则 $\\vec{a}\\cdot\\vec{b} =$ ____",
     None, "3", "$\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos 60\\degree = 2\\times3\\times\\frac{1}{2} = 3$", 60,
     None, None, "generated", None),

    # Q41: answer, diff 2, cosine of angle between vectors
    (8, None, "answer", 2, '["空间向量坐标运算"]', 2, 0,
     "已知向量 $\\vec{a}=(1,2)$，$\\vec{b}=(2,1)$，求 $\\vec{a}$ 与 $\\vec{b}$ 夹角 $\\theta$ 的余弦值",
     None, "4/5", "$\\vec{a}\\cdot\\vec{b}=1\\times2+2\\times1=4$，$|\\vec{a}|=|\\vec{b}|=\\sqrt{5}$，$\\cos\\theta=\\frac{4}{\\sqrt{5}\\cdot\\sqrt{5}}=\\frac{4}{5}$", 90,
     None, None, "generated", None),
]


def _seed_questions(cur):
    """Seed 41 questions across all 8 modules."""
    cols = "(module_id, pattern_id, type, difficulty, concepts, step_count, has_trap, content, options, answer, solution, time_limit_sec, variant_of, variant_axis, source_type, source_ref)"
    for q in SEED_QUESTIONS:
        cur.execute(f"INSERT OR IGNORE INTO questions {cols} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", q)


def seed():
    db = get_db()
    cur = db.cursor()

    # Modules
    cur.executemany(
        "INSERT OR IGNORE INTO modules (id, name, weight, tier, sort_order, icon, description) VALUES (?,?,?,?,?,?,?)",
        MODULES
    )

    # Concept dependencies
    for name, parent, ref in CONCEPT_DEPS:
        cur.execute(
            "INSERT OR IGNORE INTO concept_dependencies (concept_name, parent_concept, textbook_ref) VALUES (?,?,?)",
            (name, parent, ref)
        )

    # Season
    cur.execute(
        "INSERT OR IGNORE INTO seasons (id, name, start_date, end_date, reward_tiers, active) VALUES (1, '\u7b2c1\u8d5b\u5b63: \u51fd\u6570\u89c9\u9192', '2026-07-01', '2026-08-30', '[]', 1)"
    )

    # Questions
    _seed_questions(cur)

    db.commit()
    db.close()
    print("Seed data loaded.")


if __name__ == "__main__":
    from database import init_db
    init_db()
    seed()
