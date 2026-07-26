"""Learning hall — module-organized concepts with explanations, formulas, and examples."""
from database import get_db

# Which concepts belong to which module
MODULE_CONCEPTS = {
    1: ["和差角公式", "二倍角公式", "正弦定理", "余弦定理"],
    2: ["等差数列通项", "等比数列通项", "裂项相消", "错位相减"],
    3: ["排列组合", "二项式定理", "概率"],
    4: ["空间向量坐标运算", "法向量求法"],
    5: ["椭圆标准方程", "抛物线标准方程", "双曲线标准方程"],
    6: ["导数定义", "导数单调性", "导数极值最值", "导数切线"],
    7: [],
    8: ["复数运算"],
}

# Learning content for each concept
CONCEPT_LESSONS = {
    "正弦定理": {
        "summary": "在任意三角形中，各边与其对角的正弦值之比相等，且等于外接圆直径。",
        "formula": "\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R",
        "explanation": "正弦定理揭示了三角形中**边与角**的定量关系。\n\n- $a,b,c$ 分别是角 $A,B,C$ 的对边\n- $R$ 是三角形外接圆的半径\n- 已知两角一边，或两边一对角时，用正弦定理",
        "example": {
            "question": "在 $\\triangle ABC$ 中，已知 $A=30\\degree$，$B=45\\degree$，$a=10$，求边 $b$。",
            "solution": "由正弦定理：$\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$\n\n$b = \\frac{a \\cdot \\sin B}{\\sin A} = \\frac{10 \\times \\frac{\\sqrt{2}}{2}}{\\frac{1}{2}} = 10\\sqrt{2}$",
            "answer": "$b = 10\\sqrt{2}$"
        },
        "traps": ["正弦定理中 $\\frac{a}{\\sin A} = 2R$，不要写成 $\\frac{\\sin A}{a}$（分子分母反了）",
                  "注意锐角/钝角情况：$\\sin\\theta = \\sin(180\\degree-\\theta)$，可能有两解"]
    },
    "余弦定理": {
        "summary": "三角形的任意一边的平方，等于其他两边的平方和减去这两边与夹角余弦乘积的两倍。",
        "formula": "a^2 = b^2 + c^2 - 2bc\\cos A",
        "explanation": "余弦定理是**勾股定理的推广**。\n\n- 当 $A=90\\degree$ 时，$\\cos A=0$，退化为 $a^2=b^2+c^2$（勾股定理）\n- 已知两边及夹角，或已知三边时，用余弦定理\n- 也可以反过来求角：$\\cos A = \\frac{b^2+c^2-a^2}{2bc}$",
        "example": {
            "question": "在 $\\triangle ABC$ 中，$a=7$，$b=8$，$c=9$，求 $\\cos A$。",
            "solution": "$\\cos A = \\frac{b^2+c^2-a^2}{2bc} = \\frac{64+81-49}{2 \\times 8 \\times 9} = \\frac{96}{144} = \\frac{2}{3}$",
            "answer": "$\\cos A = \\frac{2}{3}$"
        },
        "traps": ["别忘记公式里的系数 2：$a^2 = b^2 + c^2 - \\mathbf{2}bc\\cos A$",
                  "求角时注意 $\\cos A$ 的正负对应锐角/钝角"]
    },
    "和差角公式": {
        "summary": "两个角的和或差的三角函数，可以用这两个角的三角函数表示。",
        "formula": "\\sin(\\alpha\\pm\\beta) = \\sin\\alpha\\cos\\beta \\pm \\cos\\alpha\\sin\\beta \\\\\n\\cos(\\alpha\\pm\\beta) = \\cos\\alpha\\cos\\beta \\mp \\sin\\alpha\\sin\\beta \\\\\n\\tan(\\alpha\\pm\\beta) = \\frac{\\tan\\alpha \\pm \\tan\\beta}{1 \\mp \\tan\\alpha\\tan\\beta}",
        "explanation": "和差角公式是三角恒等变换的**基石**。\n\n- $\\sin$ 是 \"异名同号\"：sin·cos ± cos·sin\n- $\\cos$ 是 \"同名异号\"：cos·cos ∓ sin·sin（注意符号反了！）\n- $\\tan$ 是 \"分子加减，分母减加\"",
        "example": {
            "question": "求 $\\sin 75\\degree$ 的值。",
            "solution": "$\\sin 75\\degree = \\sin(45\\degree+30\\degree)$\n\n$= \\sin45\\degree\\cos30\\degree + \\cos45\\degree\\sin30\\degree$\n\n$= \\frac{\\sqrt{2}}{2} \\times \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{2}}{2} \\times \\frac{1}{2}$\n\n$= \\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
            "answer": "$\\frac{\\sqrt{6}+\\sqrt{2}}{4}$"
        },
        "traps": ["余弦和角公式符号是减号：$\\cos(\\alpha+\\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$",
                  "正切公式分母是 $1 \\mp \\tan\\alpha\\tan\\beta$，别忘写 1"]
    },
    "二倍角公式": {
        "summary": "二倍角公式是和差角公式的特例（令 $\\beta=\\alpha$）。",
        "formula": "\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha \\\\\n\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha = 2\\cos^2\\alpha - 1 = 1 - 2\\sin^2\\alpha \\\\\n\\tan 2\\alpha = \\frac{2\\tan\\alpha}{1-\\tan^2\\alpha}",
        "explanation": "二倍角公式有三个常用变形，$\\cos 2\\alpha$ 有三种写法：\n\n- **升幂**：$\\cos 2\\alpha = 2\\cos^2\\alpha - 1$\n- **降幂**：$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$\n- 降幂公式反写：$\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$，$\\cos^2\\alpha = \\frac{1+\\cos 2\\alpha}{2}$",
        "example": {
            "question": "已知 $\\sin\\alpha = \\frac{3}{5}$，$\\alpha$ 为锐角，求 $\\cos 2\\alpha$。",
            "solution": "$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha$\n\n$= 1 - 2 \\times (\\frac{3}{5})^2 = 1 - 2 \\times \\frac{9}{25} = 1 - \\frac{18}{25} = \\frac{7}{25}$",
            "answer": "$\\frac{7}{25}$"
        },
        "traps": ["不要和 $\\sin 2\\alpha = 2\\sin\\alpha$ 混淆——必须有 $\\cos\\alpha$！",
                  "已知 $\\sin\\alpha$ 或 $\\cos\\alpha$ 时用 $\\cos 2\\alpha = 1-2\\sin^2\\alpha$ 或 $2\\cos^2\\alpha-1$"]
    },
    "等差数列通项": {
        "summary": "等差数列每项与前一项的差为常数（公差 $d$），通项公式是一次函数。",
        "formula": "a_n = a_1 + (n-1)d",
        "explanation": "- $a_1$ 是首项，$d$ 是公差\n- $a_n$ 是第 $n$ 项（$n$ 为正整数）\n- 等差数列的本质：每一项 = 首项 + (项数-1)×公差\n- 也可以写成：$a_n = a_m + (n-m)d$（从任意一项出发）",
        "example": {
            "question": "等差数列中，$a_3=7$，$a_7=19$，求通项公式。",
            "solution": "$a_7 = a_3 + 4d$，$19 = 7 + 4d$，$d=3$\n$a_3 = a_1 + 2d$，$7 = a_1 + 6$，$a_1=1$\n通项：$a_n = 1 + (n-1) \\times 3 = 3n-2$",
            "answer": "$a_n = 3n-2$"
        },
        "traps": ["通项公式是 $n-1$ 不是 $n$：$a_n = a_1 + \\mathbf{(n-1)}d$",
                  "首项是 $a_1$，不是 $a_0$"]
    },
    "等比数列通项": {
        "summary": "等比数列每项与前一项的比为常数（公比 $q$），通项公式是指数函数。",
        "formula": "a_n = a_1 \\cdot q^{n-1}",
        "explanation": "- $a_1$ 是首项，$q$ 是公比（$q \\neq 0$）\n- 当 $|q|<1$ 时，数列趋近于 0\n- 当 $|q|>1$ 时，数列趋于无穷\n- 也可以写成：$a_n = a_m \\cdot q^{n-m}$",
        "example": {
            "question": "等比数列中，$a_2=6$，$a_5=48$，求通项公式。",
            "solution": "$a_5 = a_2 \\cdot q^3$，$48 = 6q^3$，$q^3=8$，$q=2$\n$a_2 = a_1q$，$6 = 2a_1$，$a_1=3$\n通项：$a_n = 3 \\times 2^{n-1}$",
            "answer": "$a_n = 3 \\times 2^{n-1}$"
        },
        "traps": ["指数是 $n-1$ 不是 $n$：$a_n = a_1 \\cdot q^{\\mathbf{n-1}}$",
                  "公比 $q$ 可以是负数或分数"]
    },
    "裂项相消": {
        "summary": "将分式拆成两个分式的差，求和时中间项互相抵消，是数列求和的核心技巧。",
        "formula": "\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1} \\\\\n\\frac{1}{n(n+k)} = \\frac{1}{k}(\\frac{1}{n} - \\frac{1}{n+k})",
        "explanation": "裂项的核心思路：**把一个复杂的分式，拆成两个简单的分式之差**。\n\n然后纵向求和时首尾相消，只留头尾两项：\n$S_n = (1-\\frac{1}{2}) + (\\frac{1}{2}-\\frac{1}{3}) + ... + (\\frac{1}{n}-\\frac{1}{n+1}) = 1 - \\frac{1}{n+1}$",
        "example": {
            "question": "求数列 $\\{\\frac{1}{n(n+2)}\\}$ 的前 $n$ 项和。",
            "solution": "$\\frac{1}{n(n+2)} = \\frac{1}{2}(\\frac{1}{n} - \\frac{1}{n+2})$\n\n$S_n = \\frac{1}{2}[(1-\\frac{1}{3}) + (\\frac{1}{2}-\\frac{1}{4}) + (\\frac{1}{3}-\\frac{1}{5}) + ...]$\n\n消去中间项得 $S_n = \\frac{1}{2}(1+\\frac{1}{2}-\\frac{1}{n+1}-\\frac{1}{n+2})$",
            "answer": "$S_n = \\frac{3}{4} - \\frac{2n+3}{2(n+1)(n+2)}$"
        },
        "traps": ["分母相差 $k$ 时，前面要乘以 $\\frac{1}{k}$",
                  "消去后留下的不是第1项和第n项，而是第1、2项和最后2项"]
    },
    "错位相减": {
        "summary": "等差数列乘以等比数列的求和，用错位相减法——乘以公比后错位对齐，相减消去大量项。",
        "formula": "若 $a_n = (An+B)q^{n-1}$（等差×等比），则 $S_{n+1} = qS_n + 等差$",
        "explanation": "错位相减的操作步骤：\n1. 写出 $S_n$（各项展开）\n2. 两边同乘公比 $q$\n3. 将两个等式对齐（错开一位）\n4. 相减消去中间大量重复项\n5. 用等比数列求和公式求剩余",
        "example": {
            "question": "求 $S_n = 1\\cdot2 + 2\\cdot2^2 + 3\\cdot2^3 + ... + n\\cdot2^n$。",
            "solution": "① $S_n = 1\\cdot2 + 2\\cdot4 + 3\\cdot8 + ... + n\\cdot2^n$\n② $2S_n = 1\\cdot4 + 2\\cdot8 + ... + (n-1)2^n + n\\cdot2^{n+1}$\n\n①-②：$-S_n = 2 + 4 + 8 + ... + 2^n - n\\cdot2^{n+1}$\n\n前 $n$ 项等比求和：$2+4+...+2^n = 2(2^n-1)$\n\n$-S_n = 2(2^n-1) - n\\cdot2^{n+1}$\n$S_n = (n-1)2^{n+1} + 2$",
            "answer": "$S_n = (n-1)2^{n+1}+2$"
        },
        "traps": ["乘以公比后第一项要对齐原式的第二项（错一位）",
                  "相减后的等比数列项数是 $n-1$ 不是 $n$"]
    },
    "导数定义": {
        "summary": "导数描述函数在某点的瞬时变化率，是切线的斜率。",
        "formula": "f'(x_0) = \\lim_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x) - f(x_0)}{\\Delta x}",
        "explanation": "- 几何意义：曲线 $y=f(x)$ 在点 $(x_0, f(x_0))$ 处切线的斜率\n- 物理意义：位移的导数是速度，速度的导数是加速度\n- 基本公式：$(x^n)' = nx^{n-1}$，$(e^x)' = e^x$，$(\\ln x)' = \\frac{1}{x}$",
        "example": {
            "question": "用定义求 $f(x)=x^2$ 在 $x=1$ 处的导数。",
            "solution": "$f'(1) = \\lim_{\\Delta x \\to 0} \\frac{(1+\\Delta x)^2 - 1^2}{\\Delta x}$\n\n$= \\lim_{\\Delta x \\to 0} \\frac{1+2\\Delta x+(\\Delta x)^2 - 1}{\\Delta x}$\n\n$= \\lim_{\\Delta x \\to 0} (2 + \\Delta x) = 2$",
            "answer": "$f'(1) = 2$"
        },
        "traps": ["$f'(x_0)$ 是一个数（切线斜率），$f'(x)$ 是一个函数（导函数）",
                  "$(x^n)' = nx^{n-1}$ 对 $n$ 是实数都成立，不仅仅是整数"]
    },
    "导数单调性": {
        "summary": "导数的正负决定了原函数的增减。这是导数最重要的应用。",
        "formula": "f'(x) > 0 \\Rightarrow f(x) \\text{ 单调递增} \\\\\nf'(x) < 0 \\Rightarrow f(x) \\text{ 单调递减} \\\\\nf'(x) = 0 \\Rightarrow f(x) \\text{ 可能有极值点}",
        "explanation": "判单调三步法：\n1. 求导 $f'(x)$\n2. 解 $f'(x)=0$ 得驻点\n3. 列表，在各区间取测试点，判断 $f'(x)$ 正负\n\n$f'(x)>0$ → 函数上升 ↑\n$f'(x)<0$ → 函数下降 ↓",
        "example": {
            "question": "讨论 $f(x)=x^3-3x$ 的单调性。",
            "solution": "$f'(x)=3x^2-3=3(x-1)(x+1)$\n驻点：$x=-1$，$x=1$\n\n测试区间：\n$x<-1$：$f'(x)>0$，递增 ↑\n$-1<x<1$：$f'(x)<0$，递减 ↓\n$x>1$：$f'(x)>0$，递增 ↑\n\n递增区间：$(-\\infty,-1)$ 和 $(1,+\\infty)$\n递减区间：$(-1,1)$",
            "answer": "在 $(-\\infty,-1)$ 递增，$(-1,1)$ 递减，$(1,+\\infty)$ 递增"
        },
        "traps": ["$f'(x)=0$ 只是可能的极值点，不一定真的是极值（如 $f(x)=x^3$ 在 $x=0$）",
                  "列表时一定要取区间内的点，不要取端点"]
    },
    "导数极值最值": {
        "summary": "极值是局部概念，最值是全局概念。开区间无极值点不意味无最值。",
        "formula": "极值点必要条件: f'(x_0) = 0 \\\\\n充分条件: f'(x) 在 x_0 左右变号",
        "explanation": "求极值/最值步骤：\n1. 求导，令 $f'(x)=0$，得驻点\n2. 判断每个驻点左右导数符号是否变号\n3. 对闭区间，还要算端点值\n4. 比较所有驻点值和端点值，得最值",
        "example": {
            "question": "求 $f(x)=x^3-3x^2+1$ 在 $[-1,3]$ 上的最大值和最小值。",
            "solution": "$f'(x)=3x^2-6x=3x(x-2)$，驻点 $x=0,2$\n\n比较函数值：$f(-1)=-3$，$f(0)=1$，$f(2)=-3$，$f(3)=1$\n\n最大值 $=1$（$x=0$ 或 $x=3$），最小值 $=-3$（$x=-1$ 或 $x=2$）",
            "answer": "最大值 1，最小值 -3"
        },
        "traps": ["闭区间求最值一定要算端点！",
                  "极值点是横坐标 $x$ 的值，极值是函数值 $f(x)$"]
    },
    "导数切线": {
        "summary": "函数在某点的切线斜率等于该点的导数，切线方程用点斜式。",
        "formula": "y - f(x_0) = f'(x_0)(x - x_0)",
        "explanation": "切线问题的三个层次：\n1. **已知切点求切线**：直接用公式\n2. **已知斜率求切线**：令 $f'(x_0)=k$，解出 $x_0$\n3. **过曲线外一点求切线**：设切点 $(x_0,f(x_0))$，写出切线方程，代入外点解 $x_0$",
        "example": {
            "question": "求曲线 $y=x^2$ 在点 $(1,1)$ 处的切线方程。",
            "solution": "$y'=2x$，$k=2 \\times 1 = 2$\n切线：$y-1 = 2(x-1)$\n即 $y = 2x - 1$",
            "answer": "$y = 2x - 1$"
        },
        "traps": ["先求导再代入：$f'(x_0)$ 而不是 $[f(x_0)]'$（后者恒为0）",
                  "切线是直线，过切点斜率为 $f'(x_0)$，不是 $f(x_0)$"]
    },
    "椭圆标准方程": {
        "summary": "椭圆是到两个焦点距离之和为常数的点的轨迹。",
        "formula": "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\quad (a>b>0) \\\\\nc^2 = a^2 - b^2, \\quad e = \\frac{c}{a}",
        "explanation": "- $a$ 是长半轴，$b$ 是短半轴，$c$ 是半焦距\n- 焦点在 $x$ 轴上：$F_1(-c,0), F_2(c,0)$\n- 焦点在 $y$ 轴上：$F_1(0,-c), F_2(0,c)$（此时 $a$ 在分母 $y^2$ 下）\n- $e$ 是离心率，$0<e<1$，$e$ 越接近 1 越扁",
        "example": {
            "question": "已知椭圆长轴长 $10$，短轴长 $6$，焦点在 $x$ 轴，求椭圆方程。",
            "solution": "$2a=10$，$a=5$；$2b=6$，$b=3$\n$c = \\sqrt{a^2-b^2} = \\sqrt{25-9} = 4$\n椭圆方程：$\\frac{x^2}{25} + \\frac{y^2}{9} = 1$",
            "answer": "$\\frac{x^2}{25} + \\frac{y^2}{9} = 1$"
        },
        "traps": ["$a$ 永远是大的那个（$a>b$），焦点在哪 $a^2$ 就在哪个分母",
                  "椭圆上任意点到两焦点的距离之和 $=2a$（定义）"]
    },
    "抛物线标准方程": {
        "summary": "抛物线是到焦点和到准线距离相等的点的轨迹。",
        "formula": "y^2 = 2px \\text{（焦点在x轴）} \\quad \\text{焦点}(\\frac{p}{2},0), \\text{准线} x=-\\frac{p}{2} \\\\\nx^2 = 2py \\text{（焦点在y轴）} \\quad \\text{焦点}(0,\\frac{p}{2}), \\text{准线} y=-\\frac{p}{2}",
        "explanation": "- $p$ 是焦点到准线的距离\n- $p>0$ 时开口向右（$y^2=2px$）或向上（$x^2=2py$）\n- 抛物线上任意点到焦点的距离 = 到准线的距离（定义）",
        "example": {
            "question": "求抛物线 $y^2=8x$ 的焦点坐标和准线方程。",
            "solution": "$2p=8$，$p=4$\n焦点：$(\\frac{p}{2}, 0) = (2, 0)$\n准线：$x = -\\frac{p}{2} = -2$",
            "answer": "焦点 $(2,0)$，准线 $x=-2$"
        },
        "traps": ["不要把 $p$ 当成焦点坐标：焦点是 $(\\frac{p}{2}, 0)$ 不是 $(p,0)$",
                  "$y^2=2px$ 开口朝右，$y^2=-2px$ 开口朝左"]
    },
    "双曲线标准方程": {
        "summary": "双曲线是到两个焦点距离之差的绝对值为常数的点的轨迹。",
        "formula": "\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1 \\\\\nc^2 = a^2 + b^2, \\quad e = \\frac{c}{a} > 1 \\\\\n\\text{渐近线：} y = \\pm\\frac{b}{a}x",
        "explanation": "- 双曲线有两个分支，$e>1$\n- 渐近线是双曲线无限趋近但永不相交的直线\n- 等轴双曲线：$a=b$，渐近线 $y=\\pm x$，离心率 $e=\\sqrt{2}$",
        "example": {
            "question": "求双曲线 $\\frac{x^2}{9} - \\frac{y^2}{16} = 1$ 的渐近线和离心率。",
            "solution": "$a=3,b=4$，$c=\\sqrt{9+16}=5$\n渐近线：$y = \\pm\\frac{4}{3}x$\n离心率：$e = \\frac{5}{3}$",
            "answer": "渐近线 $y=\\pm\\frac{4}{3}x$，离心率 $e=\\frac{5}{3}$"
        },
        "traps": ["双曲线 $c^2=a^2+b^2$（注意是加号！椭圆是减号）",
                  "焦点永远在 $a$ 所在的轴上"]
    },
    "排列组合": {
        "summary": "排列有序，组合无序。排列数 $A_n^m$ 考虑顺序，组合数 $C_n^m$ 不考虑。",
        "formula": "A_n^m = n(n-1)\\cdots(n-m+1) = \\frac{n!}{(n-m)!} \\\\\nC_n^m = \\frac{A_n^m}{m!} = \\frac{n!}{m!(n-m)!}",
        "explanation": "判排列还是组合的关键问题：交换两个元素的位置，是否产生新的情况？\n\n- 是 → 排列（如排队、密码）\n- 否 → 组合（如选人、抽奖）",
        "example": {
            "question": "从5本不同的书中选3本送给3位同学，每人1本，有多少种送法？",
            "solution": "先选3本书有 $C_5^3=10$ 种，再排列 $3!=6$ 种。\n等价于 $A_5^3 = 5 \\times 4 \\times 3 = 60$ 种。",
            "answer": "60 种"
        },
        "traps": ["$C_n^0 = C_n^n = 1$",
                  "$C_n^m = C_n^{n-m}$（选 m 个等于排除 n-m 个）"]
    },
    "二项式定理": {
        "summary": "$(a+b)^n$ 的展开式中每一项的系数由组合数给出。",
        "formula": "(a+b)^n = \\sum_{k=0}^{n} C_n^k \\cdot a^{n-k} \\cdot b^k",
        "explanation": "- 第 $k+1$ 项（通项）：$T_{k+1} = C_n^k a^{n-k} b^k$\n- 二项式系数之和：$C_n^0 + C_n^1 + ... + C_n^n = 2^n$\n- 奇数项系数和 = 偶数项系数和 = $2^{n-1}$",
        "example": {
            "question": "求 $(x+\\frac{1}{x})^6$ 的展开式中的常数项。",
            "solution": "通项：$T_{k+1} = C_6^k x^{6-k}(\\frac{1}{x})^k = C_6^k x^{6-2k}$\n令 $6-2k=0$，$k=3$\n常数项 $= C_6^3 = 20$",
            "answer": "20"
        },
        "traps": ["通项公式的指数：$a$ 的指数是 $n-k$，$b$ 的指数是 $k$",
                  "求常数项时令 $x$ 的指数为 0 解出 $k$"]
    },
    "空间向量坐标运算": {
        "summary": "空间向量的数量积、向量积和坐标运算，用于求角、距离和面积。",
        "formula": "\\vec{a}\\cdot\\vec{b} = x_1x_2 + y_1y_2 + z_1z_2 \\\\\n|\\vec{a}| = \\sqrt{x_1^2+y_1^2+z_1^2} \\\\\n\\cos\\theta = \\frac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}",
        "explanation": "空间向量三步法：\n1. **建系**：选原点，标坐标\n2. **写向量**：终点减起点\n3. **套公式**：数量积求角，向量积求面积/法向量",
        "example": {
            "question": "已知 $\\vec{a}=(1,2,-1)$，$\\vec{b}=(2,-1,1)$，求夹角余弦。",
            "solution": "$\\vec{a}\\cdot\\vec{b}=2-2-1=-1$\n$|\\vec{a}|=\\sqrt{6}$，$|\\vec{b}|=\\sqrt{6}$\n$\\cos\\theta = \\frac{-1}{6}$",
            "answer": "$\\cos\\theta = -\\frac{1}{6}$"
        },
        "traps": ["$\\vec{a}\\cdot\\vec{b}=0$ 是垂直的充要条件",
                  "$\\vec{a}\\parallel\\vec{b}$ 等价于对应坐标成比例"]
    },
    "法向量求法": {
        "summary": "法向量垂直于平面内的所有直线，通过两个不共线向量的叉积求得。",
        "formula": "\\vec{n} = \\vec{AB} \\times \\vec{AC} = \n\\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ x_1 & y_1 & z_1 \\\\ x_2 & y_2 & z_2 \\end{vmatrix}",
        "explanation": "求法向量步骤：\n1. 在平面上找两个不共线的向量（如 $\\vec{AB}$ 和 $\\vec{AC}$）\n2. 算叉积得到法向量\n3. 可以约简（同乘除一个数后仍是法向量）\n\n用法向量可以求：二面角、线面角、点到面距离",
        "example": {
            "question": "已知三点 $A(1,0,0),B(0,1,0),C(0,0,1)$，求平面 ABC 的法向量。",
            "solution": "$\\vec{AB}=(-1,1,0)$，$\\vec{AC}=(-1,0,1)$\n$\\vec{n} = \\vec{AB} \\times \\vec{AC} = (1,1,1)$\n可以取 $\\vec{n} = (1,1,1)$",
            "answer": "$\\vec{n} = (1,1,1)$"
        },
        "traps": ["法向量方向可以相反——$\\vec{n}$ 和 $-\\vec{n}$ 都是法向量",
                  "二面角要看法向量夹角是锐角还是钝角来判断大小"]
    },
    "复数运算": {
        "summary": "复数 $a+bi$ 的加减乘除和模长计算，$i^2=-1$。",
        "formula": "|z| = \\sqrt{a^2+b^2}, \\quad \\bar{z} = a-bi \\\\\nz_1 \\cdot z_2 = (a_1a_2-b_1b_2) + (a_1b_2+a_2b_1)i \\\\\n\\frac{z_1}{z_2} = \\frac{z_1\\bar{z_2}}{|z_2|^2}",
        "explanation": "- $i^2=-1$，$i^3=-i$，$i^4=1$（周期为4）\n- 复数相除：分子分母同乘分母的共轭\n- 模长 $|z|$ 表示复数在复平面上到原点距离\n- $z\\cdot\\bar{z} = |z|^2 = a^2+b^2$",
        "example": {
            "question": "计算 $\\frac{1+i}{1-i}$。",
            "solution": "分子分母同乘 $1+i$：\n$\\frac{(1+i)^2}{(1-i)(1+i)} = \\frac{1+2i+i^2}{1-i^2} = \\frac{2i}{2} = i$",
            "answer": "$i$"
        },
        "traps": ["$i^2=-1$，不要和 $(-i)^2=-1$ 混淆",
                  "共轭复数的乘积是实数：$(a+bi)(a-bi)=a^2+b^2$"]
    },
    "概率": {
        "summary": "古典概型中概率 = 有利情况数 / 总情况数。独立事件概率相乘，互斥事件概率相加。",
        "formula": "P(A) = \\frac{n(A)}{n(\\Omega)} \\\\\nP(AB) = P(A) \\cdot P(B) \\text{（独立）} \\\\\nP(A \\cup B) = P(A) + P(B) - P(AB)",
        "explanation": "概率三公式：\n- **加法公式**：$P(A\\cup B) = P(A)+P(B)-P(AB)$（容斥原理）\n- **乘法公式**：$P(AB)=P(A)P(B|A)$（条件概率）\n- **全概率**：$P(B)=\\sum P(A_i)P(B|A_i)$",
        "example": {
            "question": "掷一枚骰子两次，两次点数之和为7的概率是多少？",
            "solution": "总情况数：$6 \\times 6 = 36$\n和为7的组合：$(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)$ 共6种\n$P = \\frac{6}{36} = \\frac{1}{6}$",
            "answer": "$\\frac{1}{6}$"
        },
        "traps": ["古典概型要求每个基本事件等可能",
                  "独立 ≠ 互斥：独立事件可以同时发生，互斥事件不能"]
    },
}

def get_learn_modules():
    """Return modules with their concepts for the learning hall."""
    db = get_db()
    modules = db.execute("SELECT id, name, icon, weight, tier FROM modules ORDER BY sort_order").fetchall()
    result = []
    for m in modules:
        mid = m["id"]
        concept_names = MODULE_CONCEPTS.get(mid, [])
        concepts = []
        for name in concept_names:
            concepts.append({
                "name": name,
                "has_lesson": name in CONCEPT_LESSONS,
            })
        result.append({
            "id": mid,
            "name": m["name"],
            "icon": m["icon"],
            "weight": m["weight"],
            "concepts": concepts,
            "concept_count": len(concepts),
        })
    return result


def get_concept_tree():
    """Return all concepts organized by dependency hierarchy."""
    db = get_db()
    rows = db.execute(
        "SELECT concept_name, parent_concept, textbook_ref FROM concept_dependencies ORDER BY concept_name"
    ).fetchall()

    concepts = {}
    roots = []
    for r in rows:
        name = r["concept_name"]
        parent = r["parent_concept"]
        concepts[name] = {
            "name": name,
            "parent": parent,
            "textbook_ref": r["textbook_ref"],
            "has_lesson": name in CONCEPT_LESSONS,
            "children": [],
        }

    # Build tree
    for name, c in concepts.items():
        if c["parent"] and c["parent"] in concepts:
            concepts[c["parent"]]["children"].append(c)
        elif not c["parent"]:
            roots.append(c)

    return {"roots": roots, "all": list(concepts.keys())}


def get_lesson(concept_name: str) -> dict | None:
    """Return the full lesson for a concept, preferring rich lessons."""
    # Try rich lessons first, fall back to basic
    try:
        from services.rich_lessons import RICH_LESSONS
        if concept_name in RICH_LESSONS:
            lesson = RICH_LESSONS[concept_name]
            return _build_lesson_response(concept_name, lesson)
    except ImportError:
        pass

    lesson = CONCEPT_LESSONS.get(concept_name)
    if not lesson:
        return None
    return _build_lesson_response(concept_name, lesson)


def _build_lesson_response(name: str, lesson: dict) -> dict:
    """Build a unified lesson response from either rich or basic format."""
    db = get_db()
    children = db.execute(
        "SELECT concept_name FROM concept_dependencies WHERE parent_concept=?",
        (name,),
    ).fetchall()
    parent_row = db.execute(
        "SELECT parent_concept FROM concept_dependencies WHERE concept_name=?",
        (name,),
    ).fetchone()
    ref_row = db.execute(
        "SELECT textbook_ref FROM concept_dependencies WHERE concept_name=?",
        (name,),
    ).fetchone()

    return {
        "name": name,
        "parent": parent_row["parent_concept"] if parent_row else None,
        "children": [r["concept_name"] for r in children],
        "textbook_ref": ref_row["textbook_ref"] if ref_row else None,
        **lesson,
    }
