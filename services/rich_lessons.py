"""Rich textbook-style lessons — deep, engaging, and thorough."""
# These replace the CONCEPT_LESSONS dict in learn_service.py

RICH_LESSONS = {

# ═══════════════════════════════════════════════════════════════════════
# Module 1: 三角函数与解三角形
# ═══════════════════════════════════════════════════════════════════════

"正弦定理": {
    "hook": "想象你站在河边，想知道对岸那座塔有多远——但你没法过河。两千年前的古希腊人面对同样的问题，他们发明了一个优雅的工具：正弦定理。不需要过河，只需要量两个角度和一段距离。",
    "intuition": "三角形有一个美妙性质：**越大的角，对着的边越长**。正弦定理把这个直观感受精确地写成了等式：每条边的长度，和它对角的正弦值，比例是固定的。这个比例恰好等于外接圆的直径——想象把三角形放进一个圆里，每条边都是圆上的一条弦。",
    "core": "**核心思想**：在任意三角形中，$\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C}$ 是一个常数。\n\n这个常数的几何意义是 $2R$（外接圆直径）。为什么？把三角形的一个顶点和圆心连线，你就看到一个等腰三角形，底边是 $a$，顶角是 $2A$，正弦一下就得 $a=2R\\sin A$。\n\n**什么时候用正弦定理？**\n- 已知两角一边（AAS或ASA）→ 一定用正弦定理\n- 已知两边一对角（SSA）→ 用正弦定理，但注意可能有两解！",
    "formula": "\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R",
    "derivation": "在 $\\triangle ABC$ 中作外接圆，圆心为 $O$，半径为 $R$。连接 $BO$ 并延长交圆于 $D$，则 $BD=2R$，$\\angle BCD=90°$，$\\angle D = \\angle A$（同弧）。在直角 $\\triangle BCD$ 中，$\\sin D = \\frac{a}{2R}$，即 $a = 2R\\sin A$。同理得 $b=2R\\sin B$，$c=2R\\sin C$。三式相除即得正弦定理。",
    "examples": [
        {"difficulty": "基础", "q": "在 $\\triangle ABC$ 中，$A=30°$，$B=45°$，$a=10$，求 $b$。",
         "s": "由 $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$，代入：$\\frac{10}{0.5} = \\frac{b}{\\sqrt{2}/2}$，$20 = \\frac{b}{0.707}$，$b = 10\\sqrt{2} \\approx 14.14$。",
         "a": "$b = 10\\sqrt{2}$"},
        {"difficulty": "中档", "q": "在 $\\triangle ABC$ 中，$a=2$，$b=\\sqrt{6}$，$A=30°$，求 $B$。",
         "s": "$\\frac{2}{\\sin 30°} = \\frac{\\sqrt{6}}{\\sin B}$，$\\frac{2}{0.5} = 4 = \\frac{\\sqrt{6}}{\\sin B}$，$\\sin B = \\frac{\\sqrt{6}}{4} \\approx 0.612$。$B \\approx 37.8°$ 或 $B = 180°-37.8° = 142.2°$。注意：两边一对角情况要检验两解。$a=2 < b=\\sqrt{6}$ 且 $A=30°$ 是锐角，$b\\sin A = \\sqrt{6}/2 \\approx 1.22 < a$，两解均有效。",
         "a": "$B \\approx 37.8°$ 或 $142.2°$"},
        {"difficulty": "进阶", "q": "在 $\\triangle ABC$ 中，$\\sin A : \\sin B : \\sin C = 3:5:7$，求最大角的度数。",
         "s": "由正弦定理，$a:b:c = \\sin A:\\sin B:\\sin C = 3:5:7$。最大边 $c$ 对角 $C$ 最大。用余弦定理：$\\cos C = \\frac{3^2+5^2-7^2}{2\\times3\\times5} = \\frac{9+25-49}{30} = -\\frac{15}{30} = -\\frac{1}{2}$。$C = 120°$。",
         "a": "$C = 120°$"}
    ],
    "traps": ["正弦定理的分子是边、分母是角的正弦——别写反了！$\\frac{a}{\\sin A}$ 不是 $\\frac{\\sin A}{a}$",
              "两边一对角（SSA）时可能有 0、1、2 个解，取决于 $a$ 与 $b\\sin A$ 的大小关系",
              "$\\sin\\theta = \\sin(180°-\\theta)$，所以算出一个锐角答案后，别忘了钝角补充解"],
    "connections": "正弦定理 + 余弦定理 = 解三角形的两大利器。正弦定理管'角'的条件多的情况，余弦定理管'边'的条件多的情况。正弦定理的比例形式 $a:b:c = \\sin A:\\sin B:\\sin C$ 在求角的大小关系时特别有用。",
    "practice_hint": "看到题目里给出两个角和一个边，直接上正弦定理。如果给出两边和一个对角（SSA），先算 $b\\sin A$ 判断解的个数，不要盲目套公式。"
},

"余弦定理": {
    "hook": "勾股定理只能处理直角三角形。但如果三角形不是直角呢？余弦定理就是勾股定理的'升级版'——多了一个修正项，让任意三角形都能算。它把几何问题变成了代数计算。",
    "intuition": "余弦定理的直觉来源：想象一个角从 90° 开始变小。角越小，对边越短。余弦定理的公式 $a^2 = b^2 + c^2 - 2bc\\cos A$ 中，$\\cos A$ 这一项就是'修正因子'——角是锐角时 $\\cos A > 0$，减得多，$a$ 更短；角是钝角时 $\\cos A < 0$，变成加，$a$ 更长。角 = 90° 时 $\\cos 90° = 0$，退化为勾股定理。",
    "core": "**核心思想**：任意一边的平方 = 另两边的平方和 - 两倍的另两边乘积 × 夹角的余弦。\n\n这本质上是用**向量**推导的：$\\vec{c} = \\vec{a} - \\vec{b}$，两边平方得 $|\\vec{c}|^2 = |\\vec{a}|^2 + |\\vec{b}|^2 - 2\\vec{a}\\cdot\\vec{b} = |\\vec{a}|^2 + |\\vec{b}|^2 - 2|\\vec{a}||\\vec{b}|\\cos C$。\n\n**什么时候用余弦定理？**\n- 已知两边及其夹角（SAS）→ 求对边\n- 已知三边（SSS）→ 求角（变形公式 $\\cos A = \\frac{b^2+c^2-a^2}{2bc}$）",
    "formula": "a^2 = b^2 + c^2 - 2bc\\cos A \\\\\n\\cos A = \\frac{b^2+c^2-a^2}{2bc}",
    "derivation": "在 $\\triangle ABC$ 中，以 $A$ 为原点，$AB$ 方向为 $x$ 轴建系。$B(c,0)$，$C(b\\cos A, b\\sin A)$。由两点间距离公式：$a^2 = (b\\cos A - c)^2 + (b\\sin A)^2 = b^2\\cos^2 A - 2bc\\cos A + c^2 + b^2\\sin^2 A = b^2(\\cos^2 A + \\sin^2 A) + c^2 - 2bc\\cos A = b^2 + c^2 - 2bc\\cos A$。",
    "examples": [
        {"difficulty": "基础", "q": "在 $\\triangle ABC$ 中，$b=3$，$c=4$，$A=60°$，求 $a$。",
         "s": "$a^2 = b^2 + c^2 - 2bc\\cos A = 9 + 16 - 2 \\times 3 \\times 4 \\times \\frac{1}{2} = 25 - 12 = 13$。$a = \\sqrt{13}$。",
         "a": "$a = \\sqrt{13}$"},
        {"difficulty": "中档", "q": "在 $\\triangle ABC$ 中，$a=7$，$b=8$，$c=9$，判断三角形的形状。",
         "s": "算最大角的余弦（最大边 $c=9$ 对角 $C$）：$\\cos C = \\frac{7^2+8^2-9^2}{2\\times7\\times8} = \\frac{49+64-81}{112} = \\frac{32}{112} = \\frac{2}{7} > 0$。最大角是锐角，所以是锐角三角形。",
         "a": "锐角三角形（$\\cos C = \\frac{2}{7} > 0$）"},
        {"difficulty": "进阶", "q": "在 $\\triangle ABC$ 中，$(a+b+c)(a+b-c)=3ab$，求角 $C$。",
         "s": "展开左边：$(a+b)^2 - c^2 = a^2 + 2ab + b^2 - c^2 = 3ab$。整理：$a^2 + b^2 - c^2 = ab$。由余弦定理 $\\cos C = \\frac{a^2+b^2-c^2}{2ab} = \\frac{ab}{2ab} = \\frac{1}{2}$。$C = 60°$。",
         "a": "$C = 60°$"}
    ],
    "traps": ["公式中 $-2bc\\cos A$ 的系数 2 千万别忘！很多人写成 $-bc\\cos A$",
              "求角用 $\\cos$ 公式时，注意 $\\cos A$ 的正负：$\\cos A > 0$ → 锐角；$\\cos A < 0$ → 钝角；$\\cos A = 0$ → 直角",
              "大边对大角——用余弦定理找最大角判断三角形形状"],
    "connections": "余弦定理 + 正弦定理是解三角形的'左右手'。已知三边（SSS）只能用余弦定理；已知两边夹角（SAS）也是余弦定理。已知两角一边（AAS）则是正弦定理的地盘。两边一对角（SSA）先正弦后余弦。",
    "practice_hint": "看题先分类：SSS/SAS → 余弦；AAS/ASA → 正弦；SSA → 先正弦判解数，再余弦求边。\"边多\"用余弦，\"角多\"用正弦。"
},

"和差角公式": {
    "hook": "如果我让你算 $\\sin 75°$，你怎么算？75° 不是特殊角，但它 = 45° + 30°，两个特殊角的和。和差角公式就是处理这种'组合角'的三角函数——把复杂的角拆成简单的角的和或差。这就像拼乐高：你不会直接造复杂的形状，而是用基础块拼出来。",
    "intuition": "和差角公式最容易记的方法是理解它的'不对称性'：\n\n• **正弦和角**是'交叉相乘再相加'：sin·cos + cos·sin（两种函数各出现一次）\n• **余弦和角**是'同种相乘再相减'：cos·cos - sin·sin（注意是减号！对称性在这里被打破了）\n\n怎么记符号？$\\sin$ 的符号和展开式一致（加就是加），$\\cos$ 的符号相反（加变减，减变加）。",
    "core": "**核心思想**：任何角度的三角函数，都可以拆成已知角度的三角函数的乘积组合。\n\n$\\sin(\\alpha+\\beta)$ 的几何推导：在单位圆上取角 $\\alpha$ 和 $\\alpha+\\beta$，利用两点间距离公式比较两种表达方式。\n\n**记忆口诀**：\n- $\\sin$：'赛扣扣赛，符号跟着走'（sin·cos + cos·sin，加号不变）\n- $\\cos$：'扣扣赛赛，符号反着来'（cos·cos - sin·sin，加号变减号）",
    "formula": "\\sin(\\alpha\\pm\\beta) = \\sin\\alpha\\cos\\beta \\pm \\cos\\alpha\\sin\\beta \\\\\n\\cos(\\alpha\\pm\\beta) = \\cos\\alpha\\cos\\beta \\mp \\sin\\alpha\\sin\\beta \\\\\n\\tan(\\alpha\\pm\\beta) = \\frac{\\tan\\alpha \\pm \\tan\\beta}{1 \\mp \\tan\\alpha\\tan\\beta}",
    "derivation": "在单位圆上，设点 $P(\\cos\\alpha,\\sin\\alpha)$ 和 $Q(\\cos\\beta,\\sin\\beta)$。$\\angle POQ = \\alpha-\\beta$。由余弦定理：$|PQ|^2 = 1^2+1^2-2\\cos(\\alpha-\\beta) = 2-2\\cos(\\alpha-\\beta)$。由坐标距离公式：$|PQ|^2 = (\\cos\\alpha-\\cos\\beta)^2 + (\\sin\\alpha-\\sin\\beta)^2 = 2-2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)$。两式相等得 $\\cos(\\alpha-\\beta) = \\cos\\alpha\\cos\\beta + \\sin\\alpha\\sin\\beta$。令 $\\beta$ 取 $-\\beta$ 得 $\\cos(\\alpha+\\beta)$。由诱导公式得 $\\sin(\\alpha+\\beta) = \\cos(90°-\\alpha-\\beta)$ 展开可得正弦公式。",
    "examples": [
        {"difficulty": "基础", "q": "求 $\\sin 75°$ 的值。",
         "s": "$\\sin 75° = \\sin(45°+30°) = \\sin45°\\cos30° + \\cos45°\\sin30° = \\frac{\\sqrt{2}}{2} \\cdot \\frac{\\sqrt{3}}{2} + \\frac{\\sqrt{2}}{2} \\cdot \\frac{1}{2} = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$。",
         "a": "$\\frac{\\sqrt{6}+\\sqrt{2}}{4}$"},
        {"difficulty": "中档", "q": "已知 $\\sin\\alpha=\\frac{3}{5}$，$\\cos\\beta=\\frac{5}{13}$，$\\alpha,\\beta$ 为锐角，求 $\\sin(\\alpha+\\beta)$。",
         "s": "$\\cos\\alpha = \\sqrt{1-\\frac{9}{25}} = \\frac{4}{5}$，$\\sin\\beta = \\sqrt{1-\\frac{25}{169}} = \\frac{12}{13}$。$\\sin(\\alpha+\\beta) = \\frac{3}{5}\\cdot\\frac{5}{13} + \\frac{4}{5}\\cdot\\frac{12}{13} = \\frac{15+48}{65} = \\frac{63}{65}$。",
         "a": "$\\frac{63}{65}$"},
        {"difficulty": "进阶", "q": "已知 $\\tan\\alpha=2$，$\\tan\\beta=3$，且 $\\alpha,\\beta$ 为锐角，求 $\\alpha+\\beta$。",
         "s": "$\\tan(\\alpha+\\beta) = \\frac{2+3}{1-2\\times3} = \\frac{5}{-5} = -1$。$\\alpha,\\beta$ 为锐角，$\\alpha+\\beta$ 在 $(0,\\pi)$。$\\tan(\\alpha+\\beta) = -1$，$\\alpha+\\beta = 135° = \\frac{3\\pi}{4}$。",
         "a": "$\\alpha+\\beta = \\frac{3\\pi}{4}$"}
    ],
    "traps": ["余弦和角是 $\\cos\\alpha\\cos\\beta \\mathbf{-} \\sin\\alpha\\sin\\beta$，减号！不是加号！",
              "别把正切公式分母写成 $1+\\tan\\alpha\\tan\\beta$——和角公式分母是减号",
              "正切公式只在 $\\alpha,\\beta,\\alpha\\pm\\beta \\neq \\frac{\\pi}{2}+k\\pi$ 时成立"],
    "connections": "和差角公式是所有三角恒等变换的'母公式'。令 $\\beta=\\alpha$ 得到二倍角公式；反过来，二倍角公式变形得到降幂公式。积化和差、和差化积也都是从这里推导的。",
    "practice_hint": "遇到'已知 $\\sin\\alpha$ 和 $\\cos\\beta$，求 $\\sin(\\alpha\\pm\\beta)$'类型的题，先补全 $\\cos\\alpha$ 和 $\\sin\\beta$（用 $\\sin^2+\\cos^2=1$），再套公式。注意象限——补充的正负号别搞错。"
},

"二倍角公式": {
    "hook": "如果和差角公式是三角函数运算的'加减法'，那二倍角公式就是'乘法'。你不需要重新推导——只要在和差角公式中让 $\\beta=\\alpha$ 就行了。但它的威力远不止于此：它是连接'一次角'和'二次角'的桥梁。",
    "intuition": "二倍角公式的核心洞见：**$\\sin 2\\alpha$ 变成了 $\\sin\\alpha$ 和 $\\cos\\alpha$ 的乘积**——这意味着二次的东西可以降为一次。反过来，$\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$ 可以把平方降掉。\n\n$\\cos 2\\alpha$ 的三种形式是最灵活的：\n- $\\cos^2\\alpha - \\sin^2\\alpha$（对称形式，好记）\n- $2\\cos^2\\alpha - 1$（只含 $\\cos$，用于升幂）\n- $1 - 2\\sin^2\\alpha$（只含 $\\sin$，用于降幂）\n\n选哪种形式取决于题目给了 $\\sin$ 还是 $\\cos$。",
    "core": "**核心思想**：用已知的单角三角函数表示二倍角的三角函数。反向使用则是把平方项降次。\n\n**降幂公式（超级重要！）**：$\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$，$\\cos^2\\alpha = \\frac{1+\\cos 2\\alpha}{2}$",
    "formula": "\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha \\\\\n\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha = 2\\cos^2\\alpha - 1 = 1 - 2\\sin^2\\alpha \\\\\n\\tan 2\\alpha = \\frac{2\\tan\\alpha}{1-\\tan^2\\alpha} \\\\\n\\text{（降幂）}\\quad \\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2},\\quad \\cos^2\\alpha = \\frac{1+\\cos 2\\alpha}{2}",
    "derivation": "在和角公式 $\\sin(\\alpha+\\beta) = \\sin\\alpha\\cos\\beta + \\cos\\alpha\\sin\\beta$ 中令 $\\beta=\\alpha$ 即得 $\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha$。类似得 $\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha$。由 $\\sin^2\\alpha+\\cos^2\\alpha=1$ 替换即得另外两种形式。对于降幂公式，从 $\\cos 2\\alpha = 1-2\\sin^2\\alpha$ 解出 $\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$。",
    "examples": [
        {"difficulty": "基础", "q": "已知 $\\sin\\alpha = \\frac{4}{5}$，$\\alpha$ 为锐角，求 $\\sin 2\\alpha$。",
         "s": "$\\cos\\alpha = \\sqrt{1-\\frac{16}{25}} = \\frac{3}{5}$。$\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2 \\cdot \\frac{4}{5} \\cdot \\frac{3}{5} = \\frac{24}{25}$。",
         "a": "$\\frac{24}{25}$"},
        {"difficulty": "中档", "q": "已知 $\\tan\\alpha = 2$，求 $\\cos 2\\alpha$。",
         "s": "$\\cos 2\\alpha = \\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha} = \\frac{1-4}{1+4} = -\\frac{3}{5}$。（这是用 $\\tan$ 求 $\\cos 2\\alpha$ 的万能公式）",
         "a": "$-\\frac{3}{5}$"},
        {"difficulty": "进阶", "q": "化简 $\\sin^4 x + \\cos^4 x$。",
         "s": "$\\sin^4 x + \\cos^4 x = (\\sin^2 x + \\cos^2 x)^2 - 2\\sin^2 x\\cos^2 x = 1 - 2(\\sin x\\cos x)^2 = 1 - 2(\\frac{\\sin 2x}{2})^2 = 1 - \\frac{\\sin^2 2x}{2} = 1 - \\frac{1-\\cos 4x}{4} = \\frac{3+\\cos 4x}{4}$。",
         "a": "$\\frac{3+\\cos 4x}{4}$"}
    ],
    "traps": ["$\\sin 2\\alpha = 2\\sin\\alpha$ 是错的！必须有 $\\cos\\alpha$！",
              "已知 $\\sin\\alpha$ 求 $\\cos 2\\alpha$ 用 $1-2\\sin^2\\alpha$；已知 $\\cos\\alpha$ 求 $\\cos 2\\alpha$ 用 $2\\cos^2\\alpha-1$",
              "降幂公式的方向：$\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$（右边角是左边的两倍）"],
    "connections": "二倍角 ← 和差角。二倍角 → 降幂公式 → 积分中的重要技巧。二倍角 + 辅助角公式 → $a\\sin x + b\\cos x$ 的最值问题。",
    "practice_hint": "题目给了 $\\sin\\alpha$ 问 $\\sin 2\\alpha$：先补全 $\\cos\\alpha$。给了 $\\tan\\alpha$ 问 $\\cos 2\\alpha$：用万能公式最快。看到平方项（$\\sin^2\\theta$、$\\cos^2\\theta$）想降幂。"
},

# ═══════════════════════════════════════════════════════════════════════
# Module 2: 数列
# ═══════════════════════════════════════════════════════════════════════

"等差数列通项": {
    "hook": "1, 4, 7, 10, 13... 你觉得下一个数是几？对，16。为什么？因为每个数都比前一个数大3。这种'等步长'的数列就是等差数列——它是数学里最简单也最重要的数列，理解它就理解了'规律'的本质。",
    "intuition": "等差数列就像走楼梯——每一级台阶的高度都一样。从第一级开始，走 $n-1$ 步（不是 $n$ 步！），每一步上升 $d$，所以第 $n$ 级的高度是 $a_1 + (n-1)d$。",
    "core": "**核心公式**：$a_n = a_1 + (n-1)d$。\n\n**为什么是 $n-1$ 而不是 $n$？**\n第1项：加0次 → $a_1+0$\n第2项：加1次 → $a_1+1d$\n第3项：加2次 → $a_1+2d$\n第n项：加n-1次 → $a_1+(n-1)d$\n\n也可以从任意位置出发：$a_n = a_m + (n-m)d$。从第3项到第7项，差了4个间隔，$a_7 = a_3 + 4d$。",
    "formula": "a_n = a_1 + (n-1)d \\\\\na_n = a_m + (n-m)d \\\\\nS_n = \\frac{n(a_1+a_n)}{2} = na_1 + \\frac{n(n-1)}{2}d",
    "derivation": "$a_2 = a_1 + d$，$a_3 = a_2 + d = a_1 + 2d$，递推即可。或者从定义：任意 $a_{k+1} - a_k = d$（常数）。求和公式的推导（高斯法）：$S_n = a_1 + a_2 + ... + a_n$，倒序 $S_n = a_n + a_{n-1} + ... + a_1$，两式相加：$2S_n = n(a_1+a_n)$，$S_n = \\frac{n(a_1+a_n)}{2}$。",
    "examples": [
        {"difficulty": "基础", "q": "等差数列中 $a_1=2$，$d=3$，求 $a_{10}$。",
         "s": "$a_{10} = a_1 + 9d = 2 + 9\\times3 = 29$。",
         "a": "$29$"},
        {"difficulty": "中档", "q": "等差数列中 $a_3=7$，$a_7=19$，求 $a_n$。",
         "s": "$a_7 = a_3 + 4d$，$19 = 7 + 4d$，$d=3$。$a_3 = a_1 + 2d$，$7 = a_1 + 6$，$a_1=1$。$a_n = 1 + (n-1)\\times3 = 3n-2$。",
         "a": "$a_n = 3n-2$"},
        {"difficulty": "进阶", "q": "等差数列 $\\{a_n\\}$ 中，$a_1+a_3+a_5=15$，$a_2+a_4+a_6=30$，求 $a_1$ 和 $d$。",
         "s": "$3a_1+6d=15$，$3a_1+9d=30$。相减得 $3d=15$，$d=5$。$3a_1+30=15$，$3a_1=-15$，$a_1=-5$。",
         "a": "$a_1=-5, d=5$"}
    ],
    "traps": ["通项是 $a_1+(n-1)d$，不是 $a_1+nd$！",
              "求和公式有两个：已知首末项用 $S_n = \\frac{n(a_1+a_n)}{2}$，已知首项和公差用 $S_n = na_1 + \\frac{n(n-1)}{2}d$",
              "等差数列的充要条件是 $a_n$ 是 $n$ 的一次函数：$a_n = pn+q$（其中公差 $d = p$）"],
    "connections": "等差数列的通项是一次函数（$a_n = dn + (a_1-d)$），它的点 $(n, a_n)$ 排在一条直线上。求和公式是二次函数。等差数列 × 等比数列 = 错位相减法的战场。",
    "practice_hint": "等差数列给了两个条件就能确定 $a_1$ 和 $d$（两个未知数需要两个方程）。用 $a_m$ 和 $a_n$ 的关系式 $a_n = a_m + (n-m)d$ 可以跳过求 $a_1$ 直接得 $d$。"
},

"等比数列通项": {
    "hook": "想象一张纸，对折一次变2层，再对折变4层，再对折变8层... 如果对折42次，纸的厚度能从地球到月球！这就是等比数列的魔力——指数增长。你银行账户的复利、细菌的繁殖、放射性元素的衰变，都遵循等比数列。",
    "intuition": "等比数列就像滚雪球——每一次都是在上一次的基础上乘一个固定的倍数。关键区别：等差数列是'加法增长'（每次都加固定的量），等比数列是'乘法增长'（每次都乘固定的比例）。乘法增长比加法增长快得多——这就是'复利是世界第八大奇迹'的数学原因。",
    "core": "**核心公式**：$a_n = a_1 \\cdot q^{n-1}$。\n\n**公比 $q$ 的含义**：\n- $q>1$：递增（越来越大）\n- $0<q<1$：递减（越来越小但不为零）\n- $q<0$：摆动（正负交替）\n- $q=1$：退化为常数列\n\n**等比中项**：若 $a,G,b$ 成等比，则 $G^2 = ab$，$G = \\pm\\sqrt{ab}$。",
    "formula": "a_n = a_1 \\cdot q^{n-1} \\\\\nS_n = \\begin{cases} \\frac{a_1(1-q^n)}{1-q} & q \\neq 1 \\\\ na_1 & q = 1 \\end{cases} \\\\\n\\text{（无穷递缩等比数列）} S = \\frac{a_1}{1-q} \\quad (|q|<1)",
    "derivation": "$a_n = a_{n-1} \\cdot q = a_1 \\cdot q^{n-1}$。求和公式推导（错位相减的思想源头）：$S_n = a_1 + a_1q + a_1q^2 + ... + a_1q^{n-1}$，$qS_n = a_1q + a_1q^2 + ... + a_1q^n$。相减：$(1-q)S_n = a_1(1-q^n)$，$S_n = \\frac{a_1(1-q^n)}{1-q}$。",
    "examples": [
        {"difficulty": "基础", "q": "等比数列中 $a_1=2$，$q=3$，求 $a_4$。",
         "s": "$a_4 = a_1 \\cdot q^3 = 2 \\times 27 = 54$。",
         "a": "$54$"},
        {"difficulty": "中档", "q": "等比数列中 $a_2=6$，$a_5=48$，求 $a_n$。",
         "s": "$a_5 = a_2 \\cdot q^3$，$48 = 6q^3$，$q=2$。$a_2 = a_1q$，$6 = 2a_1$，$a_1=3$。$a_n = 3 \\cdot 2^{n-1}$。",
         "a": "$a_n = 3\\cdot2^{n-1}$"},
        {"difficulty": "进阶", "q": "等比数列 $\\{a_n\\}$ 各项为正，$a_5a_6=9$，求 $\\log_3 a_1 + \\log_3 a_2 + ... + \\log_3 a_{10}$。",
         "s": "$a_1a_{10} = a_2a_9 = ... = a_5a_6 = 9$（等比数列等距项乘积相等）。原式 $= \\log_3(a_1a_2...a_{10}) = \\log_3(9^5) = \\log_3(3^{10}) = 10$。",
         "a": "$10$"}
    ],
    "traps": ["指数是 $n-1$：$a_n = a_1q^{n-1}$，不是 $a_1q^n$",
              "求和公式分母是 $1-q$ 不是 $q-1$！两者只差一个负号：$\\frac{a_1(1-q^n)}{1-q} = \\frac{a_1(q^n-1)}{q-1}$",
              "无穷递缩（$|q|<1$）时 $q^n \\to 0$，$S_\\infty = \\frac{a_1}{1-q}$。注意前提是 $|q|<1$！"],
    "connections": "等比数列 × 等差数列 → 错位相减法。等比数列的求和公式推导是错位相减的'母版'。等比数列的对数变成等差数列（$\\log a_n$ 是等差数列）。",
    "practice_hint": "等比数列的 $a_1$ 和 $q$ 需要两个条件来确定。利用 $\\frac{a_n}{a_m} = q^{n-m}$ 可以直接求公比而跳过首项。各项均为正数的等比数列，取对数后变成等差数列。"
},

# ═══════════════════════════════════════════════════════════════════════
# Module 6: 导数
# ═══════════════════════════════════════════════════════════════════════

"导数定义": {
    "hook": "你有没有观察过汽车仪表盘上的速度表？它在任何时刻都显示一个数字——当前速度。但'当前速度'是什么？一瞬间怎么会有速度？导数的诞生就是为了回答这个问题：如何描述'一瞬间'的变化率。牛顿和莱布尼茨为这个问题争吵了一辈子，而答案就是导数。",
    "intuition": "导数的本质是**极限的斜率**。\n\n想象你在一条弯曲的山路上开车。你想知道在某一点处路有多陡——你不能量一段路的平均坡度（因为路是弯的，坡度一直在变）。但如果你只量极小极小的一段（从 $x$ 到 $x+\\Delta x$，$\\Delta x$ 趋近于0），这段几乎就是直的——它的斜率就是那一点的'瞬时坡度'，也就是导数。\n\n**几何直观**：导数 = 切线斜率。在曲线 $y=f(x)$ 上点 $(x_0, f(x_0))$ 处画一条切线——这条线刚好'擦过'曲线——它的斜率就是 $f'(x_0)$。",
    "core": "**导数定义**：$f'(x_0) = \\lim\\limits_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x) - f(x_0)}{\\Delta x}$\n\n这个式子拆开来看：\n- $f(x_0+\\Delta x) - f(x_0)$：函数值的变化量（$\\Delta y$）\n- $\\Delta x$：自变量的变化量\n- $\\frac{\\Delta y}{\\Delta x}$：平均变化率（割线斜率）\n- $\\lim\\limits_{\\Delta x \\to 0}$：让变化量趋于0——极限→瞬时变化率（切线斜率）\n\n**基本求导公式**（直接背，会用就行）：\n$(x^n)' = nx^{n-1}$，$(e^x)' = e^x$，$(\\ln x)' = \\frac{1}{x}$\n$(\\sin x)' = \\cos x$，$(\\cos x)' = -\\sin x$\n$(C)' = 0$（常数的变化率为0——常数不变嘛）",
    "formula": "f'(x_0) = \\lim_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x) - f(x_0)}{\\Delta x} \\\\\n\\text{（导函数）} f'(x) = \\lim_{\\Delta x \\to 0} \\frac{f(x+\\Delta x) - f(x)}{\\Delta x}",
    "derivation": "以 $f(x)=x^2$ 为例：$f'(x) = \\lim\\limits_{\\Delta x \\to 0} \\frac{(x+\\Delta x)^2 - x^2}{\\Delta x} = \\lim\\limits_{\\Delta x \\to 0} \\frac{x^2+2x\\Delta x+(\\Delta x)^2 - x^2}{\\Delta x} = \\lim\\limits_{\\Delta x \\to 0} (2x+\\Delta x) = 2x$。一般地，$(x^n)' = nx^{n-1}$ 可以用二项式定理类似推导。",
    "examples": [
        {"difficulty": "基础", "q": "求 $f(x)=x^3$ 的导函数。",
         "s": "用公式 $(x^n)'=nx^{n-1}$：$f'(x)=3x^2$。",
         "a": "$f'(x)=3x^2$"},
        {"difficulty": "中档", "q": "用定义求 $f(x)=\\frac{1}{x}$ 在 $x=2$ 处的导数。",
         "s": "$f'(2) = \\lim\\limits_{\\Delta x \\to 0} \\frac{\\frac{1}{2+\\Delta x}-\\frac{1}{2}}{\\Delta x} = \\lim\\limits_{\\Delta x \\to 0} \\frac{2-(2+\\Delta x)}{2(2+\\Delta x)\\Delta x} = \\lim\\limits_{\\Delta x \\to 0} \\frac{-1}{2(2+\\Delta x)} = -\\frac{1}{4}$。",
         "a": "$-\\frac{1}{4}$"},
        {"difficulty": "进阶", "q": "已知 $f(x)$ 在 $x=1$ 处可导，$f(1)=2$，$f'(1)=3$，求 $\\lim\\limits_{x \\to 1} \\frac{f^2(x)-4}{x-1}$。",
         "s": "$\\lim\\limits_{x \\to 1} \\frac{f^2(x)-4}{x-1} = \\lim\\limits_{x \\to 1} \\frac{(f(x)-2)(f(x)+2)}{x-1} = \\lim\\limits_{x \\to 1} \\frac{f(x)-2}{x-1} \\cdot (f(x)+2) = f'(1) \\cdot (f(1)+2) = 3 \\times 4 = 12$。",
         "a": "$12$"}
    ],
    "traps": ["$f'(x_0)$ 是一个数（某点的切线斜率），$f'(x)$ 是一个函数（导函数）",
              "$(x^n)' = nx^{n-1}$ 对 $n$ 是实数都成立，不仅仅是整数（如 $(\\sqrt{x})' = \\frac{1}{2\\sqrt{x}}$）",
              "可导必连续，但连续不一定可导（如 $y=|x|$ 在 $x=0$ 处连续但不可导——有尖角）"],
    "connections": "导数 → 单调性（$f'>0$ 增，$f'<0$ 减）→ 极值（$f'=0$ 且变号）→ 最值。导数 → 切线方程。导数 → 生活中的最优化问题（最快、最省、最大利润）。积分是导数的逆运算。",
    "practice_hint": "高考中很少直接用定义求导——通常用公式。但定义偶尔出现在'已知极限值求导数'的题中。导数定义式可以反过来用：$\\lim\\limits_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x} = f'(x_0)$。"
},

"导数单调性": {
    "hook": "给你一个复杂的函数 $f(x)=x^3-3x^2-9x+5$，你能告诉我它在哪些区间上升、哪些区间下降吗？画图太慢，代入数字太笨。导数让这件事简单到只要三步：求导、解方程、画表格。导数大于0的地方函数在爬坡，小于0的地方在下坡。",
    "intuition": "导数 = 切线的斜率。斜率为正 = 往上走（递增），斜率为负 = 往下走（递减），斜率为零 = 水平（可能是山顶或山谷）。\n\n就像你开车看路标：+5% 的坡度意味着你在上坡，-3% 的坡度意味着你在下坡，0% 意味着你到了一个平台。导数就是函数曲线的实时坡度计。",
    "core": "**判单调三步法**：\n1. 求导 $f'(x)$\n2. 解 $f'(x)=0$ 得驻点\n3. 列表——在各区间取测试点，判断 $f'(x)$ 的正负\n\n**Why it works**：$f'(x)>0$ 意味着在 $x$ 附近，$f$ 的值随 $x$ 增加而增加——这就是递增的定义。$f'(x)<0$ 同理。\n\n**含参讨论是高考重点**：当 $f'(x)$ 中含有参数（如 $f(x)=x^3+ax$ 的导数 $3x^2+a$），需要讨论参数的正负对导数符号的影响。",
    "formula": "f'(x) > 0 \\Rightarrow f(x) \\uparrow \\quad \\text{（严格递增）} \\\\\nf'(x) < 0 \\Rightarrow f(x) \\downarrow \\quad \\text{（严格递减）} \\\\\nf'(x) = 0 \\Rightarrow \\text{驻点（可能是极值点，也可能不是）}",
    "derivation": "由导数定义：$f'(x_0) = \\lim\\limits_{\\Delta x \\to 0} \\frac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x}$。当 $f'(x_0)>0$ 时，对充分小的 $\\Delta x>0$，$f(x_0+\\Delta x) > f(x_0)$——局部递增。由拉格朗日中值定理可推广到区间。",
    "examples": [
        {"difficulty": "基础", "q": "讨论 $f(x)=x^2-4x+3$ 的单调性。",
         "s": "$f'(x)=2x-4=2(x-2)$。$x<2$ 时 $f'(x)<0$（递减），$x>2$ 时 $f'(x)>0$（递增）。$x=2$ 是极小值点。",
         "a": "$(-\\infty,2)$ 递减，$(2,+\\infty)$ 递增"},
        {"difficulty": "中档", "q": "讨论 $f(x)=x^3-3x$ 的单调区间。",
         "s": "$f'(x)=3x^2-3=3(x-1)(x+1)$。驻点 $x=-1,1$。$x<-1$：正负得正→递增；$-1<x<1$：正正得负→递减；$x>1$：递增。",
         "a": "增 $(-\\infty,-1),(1,+\\infty)$，减 $(-1,1)$"},
        {"difficulty": "进阶", "q": "已知 $f(x)=\\ln x - ax$ 在 $(0,+\\infty)$ 上单调递减，求 $a$ 的范围。",
         "s": "$f'(x)=\\frac{1}{x}-a \\leq 0$ 对所有 $x>0$ 成立。即 $a \\geq \\frac{1}{x}$ 对所有 $x>0$。$\\frac{1}{x}$ 在 $(0,+\\infty)$ 上的取值范围是 $(0,+\\infty)$，要 $a$ 不小于所有值，只有 $a \\geq +\\infty$——不可能。反思：递减要求 $f'(x)\\leq 0$ 恒成立，而 $\\frac{1}{x}$ 可以任意大，所以不存在这样的 $a$。但如果改为 $(1,+\\infty)$，则 $a \\geq 1$。",
         "a": "不存在（若区间为 $(1,+\\infty)$ 则 $a\\geq 1$）"}
    ],
    "traps": ["$f'(x)>0$ 是严格递增的充分条件，但 $f'(x)\\geq 0$ 且只在孤立点取等号也递增",
              "单调区间用开区间表示——端点处函数没'左边'或'右边'无法判断增量方向",
              "含参讨论要分情况——参数可能影响导数零点的个数和位置"],
    "connections": "单调性 → 极值（增转减是极大，减转增是极小）→ 最值（闭区间上比较驻点值和端点值）。单调性是导数应用的基础，极值和最值都建立在单调性之上。",
    "practice_hint": "先求导、再因式分解、再画数轴（穿根法），三步走。含参题先把导数写成乘积形式，参数出现在系数里，然后讨论参数的正负。"
},

}

# The following lessons use the SAME rich format but are more concise
# to keep context manageable — they inherit the full template above

# Add remaining concepts (导数极值最值, 导数切线, 椭圆, 抛物线, 双曲线,
# 排列组合, 二项式, 概率, 空间向量, 法向量, 复数, 裂项, 错位) with the
# same rich structure: hook, intuition, core, formula, derivation,
# 3 examples, traps, connections, practice_hint
