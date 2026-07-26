"""Extended rich lessons — all remaining chapters in deep format."""
# Import at bottom of rich_lessons.py: from services.rich_lessons_ext import EXT_LESSONS; RICH_LESSONS.update(EXT_LESSONS)

def _m(chapter, char, text="", expression=None, bg=None, music=None, html=None, choices=None, canvas=None, quiz=None):
    """Shorthand for building VN script lines."""
    line = {"char": char, "text": text}
    if expression: line["expression"] = expression
    if bg: line["bg"] = bg
    if music: line["music"] = music
    if html: line["html"] = html
    if choices: line["choices"] = choices
    if canvas: line["canvas"] = canvas
    if quiz: line["quiz"] = quiz
    return line

def _c(label, jump): return {"label": label, "jump": jump}

EXT_LESSONS = {

# ═══════════════════════════════════════════════════════════════════════
# 余弦定理
# ═══════════════════════════════════════════════════════════════════════
"余弦定理": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📐</div><div style='font-size:20px;font-weight:800'>第 4 章</div><div style='font-size:15px;color:var(--text-secondary)'>勾股定理的升级 · 余弦定理</div></div>", bg="dawn"),
        _m("sage", "你知道勾股定理只适用于直角三角形。但如果三角形不是直角呢？", expression="🧙", music="calm"),
        _m("sage", "假设你有一个三角形，三边分别是 3、4、6——不是直角三角形。你怎么算它的角？", expression="🤔"),
        _m("player", choices=[_c("用尺子量...不对，我需要公式", 3), _c("勾股定理不行，得找个更通用的", 3)]),
        _m("sage", "余弦定理就是勾股定理的'通用版'。勾股定理说 a²+b²=c² 当角C=90°。余弦定理加了一个修正项：a² = b² + c² - 2bc·cosA。", expression="✨", bg="night", music="mysterious"),
        _m("sage", "注意那个 -2bc·cosA。当 A=90° 时，cos90°=0，修正项消失——退化成勾股定理！这就是为什么余弦定理是勾股定理的推广。", expression="🧐"),
        _m("sage", "看后面的交互画布——拖动三角形顶点，看余弦定理在任意三角形中如何运作。", expression="🎉", music="upbeat"),
        _m("player", "原来勾股定理是余弦定理在直角时的特例。"),
        _m("sage", "正是。数学里很多东西都是这样——特殊情况的推广。好，第五章见。", expression="⚔️"),
    ],
    "layer1_title": "第一层：为什么需要余弦定理？",
    "layer1": "## 勾股定理的局限\n\n勾股定理：$a^2 + b^2 = c^2$（仅当 $C=90°$）\n\n但如果角 C 不是 90° 呢？比如一个三角形三边为 3、4、6——怎么算它的角？勾股定理帮不了你。\n\n**余弦定理**就是勾股定理的通用版：\n\n$$a^2 = b^2 + c^2 - 2bc\\cos A$$\n\n当 $A=90°$：$\\cos 90°=0$，修正项消失——$a^2=b^2+c^2$，退化为勾股定理。",
    "layer2_title": "第二层：修正因子的直觉",
    "layer2": "## 修正因子 $-2bc\\cos A$ 在说什么？\n\n- **锐角 A**：$\\cos A>0$，$-2bc\\cos A$ 为负 → $a$ 比勾股定理预测的短（锐角把对边'拉近了'）\n- **钝角 A**：$\\cos A<0$，$-2bc\\cos A$ 为正 → $a$ 比勾股定理预测的长（钝角把对边'推远了'）\n- **直角 A**：$\\cos 90°=0$ → 等于勾股定理\n\n这就是余弦定理的物理直觉：**角的张开程度通过余弦函数转化为边长的修正量。**",
    "layer3_title": "第三层：余弦定理的两种用法",
    "layer3": "## 正向：已知两边夹角，求对边\n\n$$a^2 = b^2 + c^2 - 2bc\\cos A$$\n\n## 反向：已知三边，求角\n\n$$\\cos A = \\frac{b^2+c^2-a^2}{2bc}$$\n\n## 什么时候用？\n- **SSS**（已知三边）→ 唯一选择是余弦定理\n- **SAS**（已知两边夹角）→ 余弦定理\n- **AAS/ASA**（已知两角一边）→ 正弦定理",
    "layer4_title": "第四层：在数学图景中的位置",
    "layer4": "## 余弦定理 + 正弦定理 = 解三角形完整工具箱\n\n任何一个三角形，只要知道三个独立条件（至少含一个边），就能用这两个定理解出所有未知量。\n\n**数学史上的趣事**：余弦定理的向量形式 $\\vec{c} = \\vec{a} - \\vec{b}$ 两边平方即是 $c^2 = a^2 + b^2 - 2ab\\cos C$——这说明余弦定理本质上是**向量的模长公式**！",
    "layer5_title": "第五层：解题策略",
    "layer5": "## 题目分类\n\n| 已知 | 工具 | 注意 |\n|------|------|------|\n| SSS | 余弦定理求角 | 先求最大角判断形状 |\n| SAS | 余弦定理求对边 | — |\n| 判断三角形形状 | 余弦定理求最大角余弦 | cos>0锐角，cos<0钝角 |\n\n## 陷阱：系数的 2！\n$$a^2 = b^2 + c^2 - \\mathbf{2}bc\\cos A$$",
    "formula": "a^2 = b^2 + c^2 - 2bc\\cos A \\\\\n\\cos A = \\frac{b^2+c^2-a^2}{2bc}",
    "examples": [
        {"difficulty": "基础", "q": "在 $\\triangle ABC$ 中，$b=3,c=4,A=60°$，求 $a$。",
         "s": "$a^2 = 9+16-2\\times3\\times4\\times0.5 = 25-12 = 13$，$a=\\sqrt{13}$。", "a": "$a=\\sqrt{13}$"},
        {"difficulty": "中档", "q": "$a=7,b=8,c=9$，判断三角形形状。",
         "s": "最大边 $c=9$：$\\cos C = \\frac{49+64-81}{112} = \\frac{32}{112} > 0$，锐角三角形。", "a": "锐角三角形"},
        {"difficulty": "进阶", "q": "$(a+b+c)(a+b-c)=3ab$，求 $C$。",
         "s": "展开得 $a^2+b^2-c^2=ab$。$\\cos C = \\frac{ab}{2ab} = \\frac{1}{2}$，$C=60°$。", "a": "$C=60°$"}
    ],
    "traps": ["$-2bc\\cos A$ 中的系数 2 别忘！", "求角时 $\\cos A$ 正负对应锐/钝角", "大边对大角——用余弦定理找最大角判断形状"],
    "connections": "余弦定理 + 正弦定理 = 解三角形完整工具箱。余弦定理的向量形式连接了几何和代数。",
    "practice_hint": "三边→余弦定理求角。两边夹角→余弦定理求对边。判断形状→求最大角的余弦。"
},

# ═══════════════════════════════════════════════════════════════════════
# 和差角公式
# ═══════════════════════════════════════════════════════════════════════
"和差角公式": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🧩</div><div style='font-size:20px;font-weight:800'>第 5 章</div><div style='font-size:15px;color:var(--text-secondary)'>三角乐高 · 和差角公式</div></div>", bg="dawn"),
        _m("sage", "如果我让你算 sin75°，你怎么算？75° 不是特殊角。但 75° = 45° + 30°——两个特殊角的和！", expression="🧙", music="calm"),
        _m("sage", "和差角公式就是把复杂角拆成简单角的工具。就像乐高——你不会造复杂形状，而是用基础块拼。", expression="😊"),
        _m("player", choices=[_c("所以 sin75° = sin45° + sin30°？", 3), _c("需要用某个公式把 sin(α+β) 展开", 3)]),
        _m("sage", "第一个答案是错的！sin(α+β) ≠ sinα + sinβ。别被直觉骗了——三角函数不'分配'。正确的公式是 sinα·cosβ + cosα·sinβ。", expression="🤔"),
        _m("sage", "注意这个交叉相乘的结构：正弦管异名，余弦管同名。符号也有规律——正弦和角符号跟着走，余弦和角符号反着来。", expression="✨", bg="night", music="mysterious"),
        _m("sage", "记住口诀：sin是'赛扣扣赛，符号跟'；cos是'扣扣赛赛，符号反'。", expression="🧐"),
        _m("player", "赛扣扣赛？扣扣赛赛？这是什么咒语吗..."),
        _m("sage", "哈哈哈！sin·cos + cos·sin 和 cos·cos - sin·sin。赛=sin，扣=cos。咒语背熟了，公式就永远不会忘。好了，后面有详细推导。", expression="😄", music="upbeat"),
    ],
    "layer1_title": "第一层：为什么不能 sin75° = sin45° + sin30°？",
    "layer1": "## 一个常见的错误\n\n很多人天然以为 $\\sin(\\alpha+\\beta) = \\sin\\alpha + \\sin\\beta$——就像乘法分配律一样。\n\n**但三角函数不是线性的。** 验证一下：\n\n$\\sin(45°+30°) = \\sin75° \\approx 0.966$\n\n$\\sin45° + \\sin30° = 0.707 + 0.5 = 1.207$\n\n**不相等！** 差了很多。三角函数不能简单地分配。\n\n正确的公式是：$\\sin(\\alpha+\\beta) = \\sin\\alpha\\cos\\beta + \\cos\\alpha\\sin\\beta$",
    "layer2_title": "第二层：和差角公式的直觉",
    "layer2": "## 交叉相乘的结构\n\n$$\\sin(\\alpha+\\beta) = \\sin\\alpha\\cos\\beta + \\cos\\alpha\\sin\\beta$$\n\nsin 的展开式里，sin 和 cos 各出现一次——\"交叉相乘再相加\"。\n\n$$\\cos(\\alpha+\\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$$\n\ncos 的展开式里，cos 出现两次、sin 出现两次——\"同名相乘再相减\"。注意是**减号**！\n\n## 记忆口诀\n\n- sin：赛扣扣赛，符号跟着走（sin·cos + cos·sin，加号不变）\n- cos：扣扣赛赛，符号反着来（cos·cos - sin·sin，加号变减号）",
    "layer3_title": "第三层：公式推导",
    "layer3": "## 从单位圆推导\n\n在单位圆上取两点 $P(\\cos\\alpha,\\sin\\alpha)$ 和 $Q(\\cos\\beta,\\sin\\beta)$。\n\n$\\angle POQ = \\alpha-\\beta$。两点间距离的两种算法：\n\n1. 余弦定理：$|PQ|^2 = 2 - 2\\cos(\\alpha-\\beta)$\n2. 坐标距离：$|PQ|^2 = 2 - 2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)$\n\n两式相等 → $\\cos(\\alpha-\\beta) = \\cos\\alpha\\cos\\beta + \\sin\\alpha\\sin\\beta$\n\n令 $\\beta$ 替换为 $-\\beta$ 得 $\\cos(\\alpha+\\beta)$。由诱导公式 $\\sin(\\alpha+\\beta) = \\cos(90°-\\alpha-\\beta)$ 展开得正弦公式。",
    "layer4_title": "第四层：和差角公式的威力",
    "layer4": "## 它是所有三角恒等变换的母公式\n\n- 令 $\\beta=\\alpha$ → 二倍角公式\n- 二倍角反解 → 降幂公式\n- 两式加减 → 积化和差\n- 变量替换 → 和差化积\n\n**学一个公式，推导出五个。** 这就是数学的结构之美。",
    "layer5_title": "第五层：怎么用",
    "layer5": "## 常见题型\n\n1. 求特殊角的组合：$\\sin75° = \\sin(45°+30°)$\n2. 已知 $\\sin\\alpha$ 和 $\\cos\\beta$，求 $\\sin(\\alpha\\pm\\beta)$——先补全 $\\cos\\alpha$ 和 $\\sin\\beta$\n3. 已知 $\\tan\\alpha$ 和 $\\tan\\beta$，求 $\\tan(\\alpha+\\beta)$——直接用正切和角公式",
    "formula": "\\sin(\\alpha\\pm\\beta) = \\sin\\alpha\\cos\\beta \\pm \\cos\\alpha\\sin\\beta \\\\\n\\cos(\\alpha\\pm\\beta) = \\cos\\alpha\\cos\\beta \\mp \\sin\\alpha\\sin\\beta \\\\\n\\tan(\\alpha\\pm\\beta) = \\frac{\\tan\\alpha \\pm \\tan\\beta}{1 \\mp \\tan\\alpha\\tan\\beta}",
    "examples": [
        {"difficulty": "基础", "q": "求 $\\sin75°$。", "s": "$\\sin(45°+30°) = \\sin45°\\cos30°+\\cos45°\\sin30° = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$。", "a": "$\\frac{\\sqrt{6}+\\sqrt{2}}{4}$"},
        {"difficulty": "中档", "q": "$\\sin\\alpha=\\frac{3}{5},\\cos\\beta=\\frac{5}{13}$，求 $\\sin(\\alpha+\\beta)$。", "s": "补全 $\\cos\\alpha=\\frac{4}{5},\\sin\\beta=\\frac{12}{13}$。$\\sin(\\alpha+\\beta) = \\frac{3}{5}\\cdot\\frac{5}{13}+\\frac{4}{5}\\cdot\\frac{12}{13} = \\frac{63}{65}$。", "a": "$\\frac{63}{65}$"},
        {"difficulty": "进阶", "q": "$\\tan\\alpha=2,\\tan\\beta=3$，求 $\\alpha+\\beta$。", "s": "$\\tan(\\alpha+\\beta) = \\frac{2+3}{1-6} = -1$，$\\alpha+\\beta=135°$。", "a": "$135°$"}
    ],
    "traps": ["余弦和角是减号：$\\cos(\\alpha+\\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$", "正切分母是 $1 \\mp \\tan\\alpha\\tan\\beta$"],
    "connections": "和差角→二倍角→降幂→积化和差→和差化积。一条链串起所有三角恒等变换。",
    "practice_hint": "已知 sinα 和 cosβ 时，先补全 cosα 和 sinβ（用 sin²+cos²=1），注意象限决定正负。"
},

# ═══════════════════════════════════════════════════════════════════════
# 二倍角公式
# ═══════════════════════════════════════════════════════════════════════
"二倍角公式": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🪞</div><div style='font-size:20px;font-weight:800'>第 6 章</div><div style='font-size:15px;color:var(--text-secondary)'>倍角之谜 · 二倍角公式</div></div>", bg="dawn"),
        _m("sage", "上一章我们学了和差角公式。如果让 β = α——两个相同的角相加——会发生什么？", expression="🧙", music="calm"),
        _m("sage", "和差角公式瞬间变成二倍角公式。sin2α = 2sinαcosα。cos2α 有三种写法——这就是二倍角公式最迷人的地方。", expression="✨"),
        _m("sage", "cos2α 的三个形式：cos²α-sin²α（对称），2cos²α-1（只有cos），1-2sin²α（只有sin）。选哪个取决于题目给了你什么。", expression="🧐", bg="night", music="mysterious"),
        _m("sage", "更重要的是——反过来用！sin²α = (1-cos2α)/2。这叫什么？降幂公式。把二次降到一次。积分、求极值时这个是神器。", expression="🎉", music="upbeat"),
        _m("player", "原来二倍角公式不只是'把角乘2'——它还能把平方降下来！"),
        _m("sage", "精确。一个公式，两种用法。这就是为什么二倍角公式是高考的宠儿。", expression="⚔️"),
    ],
    "layer1_title": "第一层：从和差角到二倍角",
    "layer1": "在和角公式 $\\sin(\\alpha+\\beta) = \\sin\\alpha\\cos\\beta + \\cos\\alpha\\sin\\beta$ 中令 $\\beta=\\alpha$：\n\n$$\\sin 2\\alpha = \\sin\\alpha\\cos\\alpha + \\cos\\alpha\\sin\\alpha = 2\\sin\\alpha\\cos\\alpha$$\n\n同理：$\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha$\n\n**二倍角公式就是和差角公式在 $\\beta=\\alpha$ 时的特例。**",
    "layer2_title": "第二层：cos2α 的三种面孔",
    "layer2": "$$\\cos 2\\alpha = \\cos^2\\alpha - \\sin^2\\alpha$$\n$$= 2\\cos^2\\alpha - 1 \\quad \\text{（只含 cos，用于升幂）}$$\n$$= 1 - 2\\sin^2\\alpha \\quad \\text{（只含 sin，用于降幂）}$$\n\n这三个等价形式来自 $\\sin^2+\\cos^2=1$ 的替换。选哪个？\n- 题目给了 sinα → 用 $1-2\\sin^2\\alpha$\n- 题目给了 cosα → 用 $2\\cos^2\\alpha-1$\n- 给了 tanα → 用万能公式 $\\cos 2\\alpha = \\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}$",
    "layer3_title": "第三层：降幂——二倍角的逆用",
    "layer3": "从 $\\cos 2\\alpha = 1-2\\sin^2\\alpha$ 解出 $\\sin^2\\alpha$：\n\n$$\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2}$$\n\n从 $\\cos 2\\alpha = 2\\cos^2\\alpha-1$ 解出 $\\cos^2\\alpha$：\n\n$$\\cos^2\\alpha = \\frac{1+\\cos 2\\alpha}{2}$$\n\n**这就是降幂公式。** 把 $\\sin^2$ 或 $\\cos^2$ 变成一次式——在积分中极其有用。",
    "layer4_title": "第四层：在高考中的位置",
    "layer4": "二倍角公式在高考中无处不在：\n- 三角化简求值\n- 求 $y = a\\sin^2 x + b\\sin x\\cos x + c\\cos^2 x$ 的最值\n- 解三角方程\n- 和辅助角公式联用",
    "layer5_title": "第五层：解题策略",
    "layer5": "## 看到平方想降幂\n\n$\\sin^2\\theta$ → $\\frac{1-\\cos 2\\theta}{2}$\n$\\cos^2\\theta$ → $\\frac{1+\\cos 2\\theta}{2}$\n\n## 万能公式\n\n已知 $\\tan\\alpha$ 时：$\\sin 2\\alpha = \\frac{2\\tan\\alpha}{1+\\tan^2\\alpha}$，$\\cos 2\\alpha = \\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}$",
    "formula": "\\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha \\\\\n\\cos 2\\alpha = \\cos^2\\alpha-\\sin^2\\alpha = 2\\cos^2\\alpha-1 = 1-2\\sin^2\\alpha \\\\\n\\sin^2\\alpha = \\frac{1-\\cos 2\\alpha}{2},\\quad \\cos^2\\alpha = \\frac{1+\\cos 2\\alpha}{2}",
    "examples": [
        {"difficulty": "基础", "q": "$\\sin\\alpha=\\frac{4}{5}$，求 $\\sin 2\\alpha$。", "s": "$\\cos\\alpha=\\frac{3}{5}$，$\\sin 2\\alpha = 2\\cdot\\frac{4}{5}\\cdot\\frac{3}{5} = \\frac{24}{25}$。", "a": "$\\frac{24}{25}$"},
        {"difficulty": "中档", "q": "$\\tan\\alpha=2$，求 $\\cos 2\\alpha$。", "s": "$\\cos 2\\alpha = \\frac{1-4}{1+4} = -\\frac{3}{5}$。", "a": "$-\\frac{3}{5}$"},
        {"difficulty": "进阶", "q": "化简 $\\sin^4 x + \\cos^4 x$。", "s": "= $(\\sin^2 x+\\cos^2 x)^2 - 2\\sin^2 x\\cos^2 x = 1 - \\frac{\\sin^2 2x}{2} = 1 - \\frac{1-\\cos 4x}{4}$。", "a": "$\\frac{3+\\cos 4x}{4}$"}
    ],
    "traps": ["$\\sin 2\\alpha \\neq 2\\sin\\alpha$！必须有 $\\cos\\alpha$", "降幂公式右边角是左边的两倍：$\\sin^2\\alpha$ 变成 $\\cos 2\\alpha$"],
    "connections": "和差角→二倍角→降幂→积化和差。一条链。",
    "practice_hint": "看到 $\\sin^2$ 或 $\\cos^2$ 想降幂。给了 $\\sin\\alpha$ 求 $\\cos 2\\alpha$ 用 $1-2\\sin^2\\alpha$。"
},

# ═══════════════════════════════════════════════════════════════════════
# 导数单调性
# ═══════════════════════════════════════════════════════════════════════
"导数单调性": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📈</div><div style='font-size:20px;font-weight:800'>第 7 章</div><div style='font-size:15px;color:var(--text-secondary)'>爬坡还是下坡 · 导数单调性</div></div>", bg="dawn"),
        _m("sage", "你学会了求导。现在我有一个函数 f(x) = x³-3x²-9x+5。告诉我——它在哪里上升？哪里下降？", expression="🧙", music="calm"),
        _m("player", choices=[_c("我画个图看看...", 2), _c("求导！导数>0上升，<0下降", 2)]),
        _m("sage", "对！导数告诉你函数的'坡度'。f'(x)>0 = 爬坡。f'(x)<0 = 下坡。f'(x)=0 = 水平。", expression="😊"),
        _m("sage", "三步法：求导 → 解 f'(x)=0 得驻点 → 列表判断每段符号。这就像给函数画了一张'路况地图'。", expression="✨", bg="night", music="mysterious"),
        _m("sage", "f(x)=x³-3x²-9x+5 的导数是 f'(x)=3x²-6x-9=3(x-3)(x+1)。驻点 x=-1 和 x=3。x<-1 时 f'>0 上升，-1<x<3 时 f'<0 下降，x>3 时 f'>0 上升。", expression="🧐"),
        _m("sage", "注意：含参数时——比如 f(x)=x³+ax——导数 f'(x)=3x²+a 的符号取决于 a。这就是高考最爱考的'含参讨论'。", expression="🎉", music="upbeat"),
    ],
    "layer1_title": "第一层：导数 > 0 = 上升",
    "layer1": "导数的几何意义是切线斜率。斜率为正 = 切线朝上 = 函数在上升。\n\n$$f'(x) > 0 \\Rightarrow f(x) \\text{ 严格递增}$$\n$$f'(x) < 0 \\Rightarrow f(x) \\text{ 严格递减}$$\n\n**就像一个实时坡度计**：正值 = 上坡，负值 = 下坡，零 = 平台。",
    "layer2_title": "第二层：三步判单调法",
    "layer2": "1. 求导 $f'(x)$\n2. 解 $f'(x)=0$ 得驻点\n3. 画数轴列表——在每个区间取测试点判断 $f'(x)$ 正负\n\n例：$f(x)=x^3-3x$，$f'(x)=3x^2-3=3(x-1)(x+1)$\n\n驻点 $x=-1,1$。三段：$(-\\infty,-1)$、$(-1,1)$、$(1,+\\infty)$。\n\n$x=-2$→$f'>0$ 增 | $x=0$→$f'<0$ 减 | $x=2$→$f'>0$ 增",
    "layer3_title": "第三层：含参讨论——高考最爱",
    "layer3": "当 $f'(x)$ 含参数时，需要讨论参数对导数符号的影响。\n\n例：$f(x)=x^3+ax$，$f'(x)=3x^2+a$\n\n- 若 $a \\geq 0$：$f'(x) \\geq 0$ 恒成立，$f$ 在 R 上递增\n- 若 $a < 0$：$f'(x)=0$ 有两个解 $x=\\pm\\sqrt{-a/3}$，分三段讨论\n\n**关键：先把导数写成因式分解形式，再讨论参数。**",
    "layer4_title": "第四层：单调性 → 极值 → 最值",
    "layer4": "单调性是根基：\n\n```\n导数符号 → 单调区间 → 增转减=极大值 → 减转增=极小值 → 比较得最值\n```\n\n整个导数应用体系都建立在单调性之上。",
    "layer5_title": "第五层：解题模板",
    "layer5": "三步走：**求导 → 因式分解 → 画数轴列表**\n\n含参题：先把导数写成乘积形式（因式分解），参数出现在系数里，然后讨论系数的正负。\n\n**陷阱**：$f'(x) \\geq 0$ 但只在孤立点取等号时也是严格递增——如 $f(x)=x^3$，$f'(0)=0$ 但整体递增。",
    "formula": "f'(x) > 0 \\Rightarrow f(x) \\uparrow \\\\\nf'(x) < 0 \\Rightarrow f(x) \\downarrow \\\\\nf'(x) = 0 \\Rightarrow \\text{驻点}",
    "examples": [
        {"difficulty": "基础", "q": "讨论 $f(x)=x^2-4x+3$ 的单调性。", "s": "$f'(x)=2x-4$。$x<2$ 减，$x>2$ 增。", "a": "$(-\\infty,2)$减，$(2,+\\infty)$增"},
        {"difficulty": "中档", "q": "讨论 $f(x)=x^3-3x$ 的单调性。", "s": "$f'(x)=3(x-1)(x+1)$。$x<-1$增，$-1<x<1$减，$x>1$增。", "a": "增 $(-\\infty,-1),(1,+\\infty)$，减 $(-1,1)$"},
        {"difficulty": "进阶", "q": "$f(x)=x^3+ax$ 在 R 上递增，求 $a$ 的范围。", "s": "$f'(x)=3x^2+a \\geq 0$ 恒成立 → $a \\geq 0$。", "a": "$a \\geq 0$"}
    ],
    "traps": ["$f'(x)>0$ 是严格递增的充分条件", "单调区间用开区间", "含参讨论要分情况"],
    "connections": "单调性 → 极值 → 最值。整个导数应用体系的基础。",
    "practice_hint": "求导→因式分解→画数轴列表。含参题先因式分解再讨论系数正负。"
},

# ═══════════════════════════════════════════════════════════════════════
# 导数极值最值
# ═══════════════════════════════════════════════════════════════════════
"导数极值最值": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>⛰️</div><div style='font-size:20px;font-weight:800'>第 8 章</div><div style='font-size:15px;color:var(--text-secondary)'>山顶与山谷 · 极值与最值</div></div>", bg="dawn"),
        _m("sage", "你学会了判断函数的上升和下降。现在问一个更实用的问题：这个函数的最大值在哪里？", expression="🧙", music="calm"),
        _m("sage", "导数不仅能告诉你'在爬坡'——它还能告诉你'山顶在哪'。山顶的特征是：爬坡结束，下坡开始。也就是说：导数从正变负。", expression="😊"),
        _m("sage", "导数为零 + 左右变号 = 极值点。所有的极值点加上区间端点——比较它们，最大的就是最大值，最小的就是最小值。", expression="✨", music="upbeat"),
        _m("sage", "这就是为什么企业用导数来找最大利润、最优生产量——不是在'做题'，是在'做决策'。", expression="🎉"),
    ],
    "layer1_title": "第一层：极值是局部的，最值是全局的",
    "layer1": "**极值**：在某个点附近最大/最小——局部冠军\n**最值**：在整个区间上最大/最小——全局冠军\n\n山脉里每个山顶都是极值点（局部最高）。但只有最高的那个是最值点（全局最高）。",
    "layer2_title": "第二层：找极值点——导数变号",
    "layer2": "极值点的特征：**$f'(x)=0$ 且导数左右变号**\n\n- 左正右负（增转减）→ 极大值\n- 左负右正（减转增）→ 极小值\n- 左右同号 → 不是极值（比如 $f(x)=x^3$ 在 $x=0$）",
    "layer3_title": "第三层：求最值——比较所有候选",
    "layer3": "闭区间 $[a,b]$ 上求最值：\n1. 求导得驻点（$f'(x)=0$）\n2. 算所有驻点值和端点值 $f(a), f(b)$\n3. 比较——最大的是最大值，最小的是最小值\n\n**别忘算端点！** 最值可能在端点取得。",
    "layer4_title": "第四层：实际应用",
    "layer4": "导数求最值 = 数学化的决策工具：\n- 利润最大化：利润函数求导 = 0\n- 成本最小化：成本函数求导 = 0\n- 面积/体积最值：几何量函数求导 = 0",
    "layer5_title": "第五层：解题策略",
    "layer5": "1. 求导 → 驻点\n2. 判断每个驻点是否极值（左右变号）\n3. 闭区间问题：比较所有驻点 + 端点\n4. 开区间问题：判断单调性确定最值",
    "formula": "f'(x_0)=0 \\text{ 且 } f'(x) \\text{ 在 } x_0 \\text{ 左右变号} \\Rightarrow x_0 \\text{ 是极值点}",
    "examples": [
        {"difficulty": "基础", "q": "求 $f(x)=x^3-3x$ 的极值。", "s": "$f'(x)=3(x-1)(x+1)$。$x=-1$极大值$2$，$x=1$极小值$-2$。", "a": "极大值2，极小值-2"},
        {"difficulty": "中档", "q": "求 $f(x)=x^3-3x^2+1$ 在 $[-1,3]$ 上的最值。", "s": "驻点 $x=0,2$。$f(-1)=-3,f(0)=1,f(2)=-3,f(3)=1$。最大1，最小-3。", "a": "最大值1，最小值-3"},
        {"difficulty": "进阶", "q": "求 $f(x)=x+\\frac{1}{x}(x>0)$ 的最小值。", "s": "$f'(x)=1-\\frac{1}{x^2}=0$→$x=1$。$f(1)=2$。或均值不等式。", "a": "2"}
    ],
    "traps": ["闭区间一定要算端点！", "$f'(x_0)=0$ 不一定有极值（如 $f(x)=x^3$ 在 $x=0$）", "极值点是横坐标 $x_0$，极值是函数值 $f(x_0)$"],
    "connections": "单调性 → 极值 → 最值 → 优化问题。",
    "practice_hint": "闭区间：求导→驻点→比较所有驻点+端点。开区间：判断单调性。"
},

# ═══════════════════════════════════════════════════════════════════════
# 导数切线
# ═══════════════════════════════════════════════════════════════════════
"导数切线": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📏</div><div style='font-size:20px;font-weight:800'>第 9 章</div><div style='font-size:15px;color:var(--text-secondary)'>切线的秘密 · 导数求切线</div></div>", bg="dawn"),
        _m("sage", "导数的第一个应用：求切线方程。已知曲线 y=f(x) 和切点 (x₀, f(x₀))——切线斜率就是 f'(x₀)。", expression="🧙", music="calm"),
        _m("sage", "切线方程 = 点斜式：y - f(x₀) = f'(x₀)(x - x₀)。就这么简单。", expression="😊"),
        _m("sage", "但真正的挑战是：如果切点不知道呢？比如'过曲线外一点作切线'——这就需要设切点、列方程、解方程。", expression="🤔", music="mysterious"),
        _m("sage", "三类切线题：1.已知切点→直接套 2.已知斜率→反解切点 3.过曲线外一点→设切点列方程", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：切线的本质",
    "layer1": "切线 = 在切点处与曲线有相同斜率的直线。\n\n斜率 = $f'(x_0)$。过点 $(x_0, f(x_0))$。\n\n**点斜式**：$y - f(x_0) = f'(x_0)(x - x_0)$",
    "layer2_title": "第二层：三类切线问题",
    "layer2": "1. **已知切点**：直接代入公式\n2. **已知斜率 $k$**：令 $f'(x_0)=k$，解出 $x_0$，再求切线\n3. **过曲线外一点 $(a,b)$**：设切点 $(x_0,f(x_0))$，切线 $y-f(x_0)=f'(x_0)(x-x_0)$ 过 $(a,b)$，代入解 $x_0$",
    "layer3_title": "第三层：过曲线外一点作切线",
    "layer3": "例：过点 $(0,-2)$ 作 $y=x^2$ 的切线。\n\n设切点 $(t,t^2)$。$f'(t)=2t$。切线：$y-t^2=2t(x-t)$。\n\n代入 $(0,-2)$：$-2-t^2=2t(0-t)=-2t^2$ → $t^2=2$ → $t=\\pm\\sqrt{2}$。\n\n两条切线：$y=2\\sqrt{2}x-4$ 和 $y=-2\\sqrt{2}x-4$。",
    "layer4_title": "第四层：切线的几何意义",
    "layer4": "切线是曲线在一点附近的'最佳线性近似'。\n\n在 $x_0$ 附近，$f(x) \\approx f(x_0) + f'(x_0)(x-x_0)$。\n\n这个近似是微分学的基础——也是物理学中'小量近似'的数学基础。",
    "layer5_title": "第五层：解题模板",
    "layer5": "1. 明确是哪类问题（已知切点/已知斜率/过外点）\n2. 写出点斜式\n3. 根据条件列方程解未知数",
    "formula": "y - f(x_0) = f'(x_0)(x - x_0)",
    "examples": [
        {"difficulty": "基础", "q": "求 $y=x^2$ 在 $(1,1)$ 处的切线。", "s": "$f'(1)=2$。切线：$y-1=2(x-1)$→$y=2x-1$。", "a": "$y=2x-1$"},
        {"difficulty": "中档", "q": "$y=e^x$ 的切线斜率为 1，求切点。", "s": "$f'(x_0)=e^{x_0}=1$→$x_0=0$。切点 $(0,1)$。", "a": "切点 $(0,1)$"},
        {"difficulty": "进阶", "q": "过原点作 $y=\\ln x$ 的切线。", "s": "设切点 $(t,\\ln t)$。$f'(t)=\\frac{1}{t}$。切线过原点→$\\ln t=1$→$t=e$。", "a": "$y=\\frac{x}{e}$"}
    ],
    "traps": ["先求导再代入——$f'(x_0)$ 不是 $[f(x_0)]'$（后者恒为0）", "过曲线外一点时别忘设切点"],
    "connections": "切线 → 线性近似 → 微分。导数应用的第一站。",
    "practice_hint": "三类问题：已知切点直接套，已知斜率反解切点，过外点设切点列方程。"
},

}
