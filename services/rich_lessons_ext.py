"""Extended rich lessons — all remaining chapters in deep format."""
# Import at bottom of rich_lessons.py: from services.rich_lessons_ext import EXT_LESSONS; RICH_LESSONS.update(EXT_LESSONS)

def _m(char, text="", expression=None, bg=None, music=None, html=None, choices=None, canvas=None, quiz=None):
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
        _m("player", choices=[_c("用尺子量...不对，我需要公式", 4), _c("勾股定理不行，得找个更通用的", 4)]),
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
        _m("player", choices=[_c("所以 sin75° = sin45° + sin30°？", 4), _c("需要用某个公式把 sin(α+β) 展开", 4)]),
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
        _m("player", choices=[_c("我画个图看看...", 3), _c("求导！导数>0上升，<0下降", 3)]),
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

# ═══════════════════════════════════════════════════════════════════════
"等比数列通项": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📈</div><div style='font-size:20px;font-weight:800'>第 10 章</div><div style='font-size:15px;color:var(--text-secondary)'>指数增长的魔力 · 等比数列</div></div>", bg="dawn"),
        _m("sage", "上一章你学了等差数列——加法的重复。现在看看乘法的重复——等比数列。", expression="🧙", music="calm"),
        _m("sage", "一张纸对折1次=2层，对折2次=4层，对折42次=从地球到月球！这就是等比数列的魔力：指数增长。", expression="✨"),
        _m("sage", "等比数列的通项：$a_n = a_1 \\cdot q^{n-1}$。注意指数是 n-1，不是 n。公比 q 可以是任何非零数。", expression="🤔", bg="night", music="mysterious"),
        _m("sage", "求和公式 $S_n = a_1(1-q^n)/(1-q)$ 的推导：乘以 q 然后相减——这就是错位相减法的原型。", expression="🎉", music="upbeat"),
    ],
    "layer1_title": "第一层：乘法增长的威力",
    "layer1": "等差数列每次**加**一个常量。等比数列每次**乘**一个常量。\n\n$a_1=1, d=2$ 等差：$1,3,5,7,9...$（线性增长）\n$a_1=1, q=2$ 等比：$1,2,4,8,16...$（指数增长）\n\n**乘法增长远远快于加法增长**。这就是复利的数学基础。",
    "layer2_title": "第二层：通项公式",
    "layer2": "$$a_n = a_1 \\cdot q^{n-1}$$\n\n$q>1$：递增；$0<q<1$：递减趋于0；$q<0$：正负摆动；$q=1$：常数列。\n\n等比中项：若 $a,G,b$ 成等比，则 $G^2 = ab$。",
    "layer3_title": "第三层：求和公式——错位相减的原型",
    "layer3": "$$S_n = a_1 + a_1q + a_1q^2 + ... + a_1q^{n-1}$$\n\n乘以 $q$：$qS_n = a_1q + a_1q^2 + ... + a_1q^n$\n\n相减：$(1-q)S_n = a_1(1-q^n)$\n\n$$S_n = \\frac{a_1(1-q^n)}{1-q} \\quad (q \\neq 1)$$\n\n当 $|q|<1$，$n\\to\\infty$ 时 $q^n\\to 0$，$S_\\infty = \\frac{a_1}{1-q}$（无穷递缩等比数列求和）。",
    "layer4_title": "第四层：现实世界中的等比数列",
    "layer4": "- 银行复利：本金 × $(1+r)^n$\n- 放射性衰变：$N(t) = N_0(\\frac{1}{2})^{t/T}$\n- 细菌繁殖：$N = N_0 \\cdot 2^n$\n- 音响音量：每-3dB功率减半",
    "layer5_title": "第五层：解题策略",
    "layer5": "两个未知数 $a_1$ 和 $q$，需要两个条件。\n$a_n / a_m = q^{n-m}$——可以直接求公比，跳过求首项。\n各项为正的等比数列，取对数后变成等差数列。",
    "formula": "a_n = a_1 \\cdot q^{n-1} \\\\\nS_n = \\frac{a_1(1-q^n)}{1-q} \\quad (q \\neq 1) \\\\\nS_\\infty = \\frac{a_1}{1-q} \\quad (|q|<1)",
    "examples": [
        {"difficulty": "基础", "q": "$a_1=2,q=3$,求 $a_4$。", "s": "$a_4 = 2\\times3^3 = 54$。", "a": "$54$"},
        {"difficulty": "中档", "q": "$a_2=6,a_5=48$,求 $a_n$。", "s": "$a_5/a_2 = q^3 = 8$→$q=2$。$a_2=a_1q$→$a_1=3$。$a_n=3\\cdot2^{n-1}$。", "a": "$a_n=3\\cdot2^{n-1}$"},
        {"difficulty": "进阶", "q": "$a_5a_6=9$,求 $\\log_3 a_1+...+\\log_3 a_{10}$。", "s": "$a_1a_{10}=...=a_5a_6=9$。原式$=\\log_3(9^5)=10$。", "a": "$10$"}
    ],
    "traps": ["指数是 $n-1$ 不是 $n$", "分母是 $1-q$ 不是 $q-1$", "无穷递缩要求 $|q|<1$"],
    "connections": "等比数列 × 等差数列 = 错位相减。等比数列取对数 → 等差数列。",
    "practice_hint": "$a_n/a_m = q^{n-m}$ 跳过求首项直接得公比。求和用公式，注意 $q=1$ 的特殊情况。"
},

"裂项相消": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>💥</div><div style='font-size:20px;font-weight:800'>第 11 章</div><div style='font-size:15px;color:var(--text-secondary)'>多米诺骨牌 · 裂项相消</div></div>", bg="dawn"),
        _m("sage", "数列求和的终极技巧之一：裂项相消。把一项拆成两项的差，求和时中间全部抵消——像多米诺骨牌一样。", expression="🧙", music="calm"),
        _m("sage", "核心公式：$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$。这不是魔法——通分验证一下：右边通分 = $\\frac{n+1-n}{n(n+1)} = \\frac{1}{n(n+1)}$ = 左边。", expression="😊"),
        _m("sage", "求和时：$(1-\\frac{1}{2})+(\\frac{1}{2}-\\frac{1}{3})+...+(\\frac{1}{n}-\\frac{1}{n+1}) = 1 - \\frac{1}{n+1}$。中间全消了！", expression="✨", bg="night", music="mysterious"),
        _m("sage", "更一般：$\\frac{1}{n(n+k)} = \\frac{1}{k}(\\frac{1}{n} - \\frac{1}{n+k})$。分母差 k，前面就要乘 1/k。", expression="🎉", music="upbeat"),
    ],
    "layer1_title": "第一层：裂项的本质",
    "layer1": "裂项 = 把一个复杂分式拆成两个简单分式的差。\n\n$$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$$\n\n验证：通分右边 = $\\frac{(n+1)-n}{n(n+1)} = \\frac{1}{n(n+1)}$ ✓",
    "layer2_title": "第二层：求和——多米诺效应",
    "layer2": "$$\\sum_{n=1}^{N} \\frac{1}{n(n+1)}$$\n\n= $(1-\\frac{1}{2}) + (\\frac{1}{2}-\\frac{1}{3}) + ... + (\\frac{1}{N}-\\frac{1}{N+1})$\n\n中间项全部抵消（前一项的 $-\\frac{1}{k}$ 和后一项的 $+\\frac{1}{k}$ 互消）\n\n= $1 - \\frac{1}{N+1}$",
    "layer3_title": "第三层：通用公式",
    "layer3": "分母差 $k$：\n$$\\frac{1}{n(n+k)} = \\frac{1}{k}(\\frac{1}{n} - \\frac{1}{n+k})$$\n\n$\"差几就乘 1/几\"$——分母的差是 k，前面系数就是 1/k。",
    "layer4_title": "第四层：裂项的类型",
    "layer4": "常见裂项形式：\n1. $\\frac{1}{n(n+1)}$ → $\\frac{1}{n}-\\frac{1}{n+1}$\n2. $\\frac{1}{n(n+k)}$ → $\\frac{1}{k}(\\frac{1}{n}-\\frac{1}{n+k})$\n3. $\\frac{1}{(2n-1)(2n+1)}$ → $\\frac{1}{2}(\\frac{1}{2n-1}-\\frac{1}{2n+1})$\n4. $\\frac{1}{\\sqrt{n}+\\sqrt{n+1}}$ → $\\sqrt{n+1}-\\sqrt{n}$（有理化）",
    "layer5_title": "第五层：解题模板",
    "layer5": "1. 识别分母是否可以因式分解\n2. 确定拆分形式（通分验证）\n3. 写出前几项和末几项\n4. 消去中间项\n5. 留下首尾项",
    "formula": "\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1} \\\\\n\\frac{1}{n(n+k)} = \\frac{1}{k}(\\frac{1}{n} - \\frac{1}{n+k})",
    "examples": [
        {"difficulty": "基础", "q": "$\\sum_{n=1}^{100} \\frac{1}{n(n+1)}$。", "s": "$=1-\\frac{1}{101} = \\frac{100}{101}$。", "a": "$\\frac{100}{101}$"},
        {"difficulty": "中档", "q": "$\\sum_{n=1}^{n} \\frac{1}{n(n+2)}$。", "s": "$=\\frac{1}{2}(1+\\frac{1}{2}-\\frac{1}{n+1}-\\frac{1}{n+2})$。", "a": "$\\frac{3}{4}-\\frac{2n+3}{2(n+1)(n+2)}$"},
        {"difficulty": "进阶", "q": "$\\sum_{n=1}^{\\infty} \\frac{1}{n(n+1)}$。", "s": "=$\\lim_{N\\to\\infty}(1-\\frac{1}{N+1}) = 1$。", "a": "$1$"}
    ],
    "traps": ["分母差 $k$ 时系数是 $1/k$", "消去后留下前两项+后两项，不是只留首尾"],
    "connections": "裂项是数列求和的两大特殊技巧之一（另一是错位相减）。本质是部分分式分解。",
    "practice_hint": "分母因式分解后，用通分法验算拆分是否正确。$\\frac{1}{(an+b)(cn+d)}$ 型都可用裂项。"
},

"错位相减": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>⚔️</div><div style='font-size:20px;font-weight:800'>第 12 章</div><div style='font-size:15px;color:var(--text-secondary)'>乘法对加法 · 错位相减</div></div>", bg="dawn"),
        _m("sage", "高考数列大题的终极武器：错位相减。当等差数列乘以等比数列时，求和不能用公式——必须用这个技巧。", expression="🧙", music="calm"),
        _m("sage", "方法：写出 $S_n$，两边同乘公比 $q$，错开一位对齐，相减——大量项抵消，剩下的用等比求和公式。", expression="😊"),
        _m("sage", "例：$S_n = 1\\cdot2 + 2\\cdot4 + 3\\cdot8 + ... + n\\cdot2^n$。这是等差数列{n} × 等比数列{2^n}。", expression="🤔", bg="night", music="mysterious"),
        _m("sage", "乘2：$2S_n = 1\\cdot4 + 2\\cdot8 + ... + (n-1)2^n + n\\cdot2^{n+1}$。相减，中间全是对齐的等比数列。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：为什么需要错位相减？",
    "layer1": "等差 × 等比的数列——比如 $\\{n\\cdot 2^n\\}$——既不是等差数列也不是等比数列。\n\n它的通项是 $a_n = (An+B)q^{n-1}$ 形式。\n\n**不能用等差求和，也不能用等比求和。** 需要新工具。",
    "layer2_title": "第二层：错位相减的操作",
    "layer2": "$$S_n = a_1 + a_2 + ... + a_n$$\n$$qS_n = a_1q + a_2q + ... + a_nq$$\n\n注意到 $a_k q = (A(k)+B)q^k$ 和 $a_{k+1}$ 的系数差一个 $A$。\n\n相减后中间的 $q^k$ 项系数变成常数——变成一个等比数列！",
    "layer3_title": "第三层：模板",
    "layer3": "$$S_n = n\\cdot 2^n 的前n项和$$\n\n① $S_n = 1\\cdot2 + 2\\cdot4 + 3\\cdot8 + ... + n\\cdot2^n$\n② $2S_n = 1\\cdot4 + 2\\cdot8 + ... + (n-1)2^n + n\\cdot2^{n+1}$\n\n①-②：$-S_n = 2+4+8+...+2^n - n\\cdot2^{n+1}$\n\n前n项等比求和：$2+4+...+2^n = 2(2^n-1)$\n\n$-S_n = 2(2^n-1) - n\\cdot2^{n+1}$ → $S_n = (n-1)2^{n+1}+2$",
    "layer4_title": "第四层：通用公式",
    "layer4": "对于 $(An+B)q^{n-1}$ 型的数列，错位相减的结果是：\n\n$$S_n = (pn+r)q^n + C$$\n\n其中 $p = \\frac{A}{q-1}$，$C$ 和 $r$ 由初始条件确定。\n\n**高考常考的套路**：一步错位相减就出答案。",
    "layer5_title": "第五层：操作口诀",
    "layer5": "1. 写出 $S_n$（各项展开）\n2. 乘公比 $q$\n3. 错一位对齐\n4. 相减\n5. 中间的等比数列求和\n6. 化简得 $S_n$",
    "formula": "S_n = \\sum_{k=1}^{n} a_k \\\\\nqS_n = \\sum_{k=1}^{n} a_k q \\\\\n\\text{相减：}(1-q)S_n = a_1 + \\sum_{k=2}^{n} (a_k - a_{k-1}q) - a_n q",
    "examples": [
        {"difficulty": "基础", "q": "求 $\\sum_{k=1}^{5} k\\cdot2^k$。", "s": "套公式或直接错位。", "a": "$(5-1)2^6+2 = 258$"},
        {"difficulty": "中档", "q": "求 $S_n = \\sum_{k=1}^{n} k\\cdot2^k$。", "s": "错位相减得 $S_n = (n-1)2^{n+1}+2$。", "a": "$S_n = (n-1)2^{n+1}+2$"},
        {"difficulty": "进阶", "q": "求 $S_n = 1+3x+5x^2+...+(2n-1)x^{n-1}$。", "s": "等差{2n-1}×等比{x^{n-1}}。错位相减。", "a": "$S_n = \\frac{1+x-(2n+1)x^n+(2n-1)x^{n+1}}{(1-x)^2}$"}
    ],
    "traps": ["乘公比后要对齐——第一项对原式的第二项", "中间等比数列的项数是 n-1 不是 n", "相减别忘符号"],
    "connections": "错位相减 ← 等比数列求和公式推导（本质相同）。等差数列 × 等比数列是高考数列大题的标准模型。",
    "practice_hint": "等差×等比→错位相减。分两步：乘公比错位，中间等比求和。结果形式是 $(pn+r)q^n+C$。"
},

"椭圆标准方程": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🥚</div><div style='font-size:20px;font-weight:800'>第 13 章</div><div style='font-size:15px;color:var(--text-secondary)'>完美的椭圆 · 圆锥曲线</div></div>", bg="dawn"),
        _m("sage", "椭圆是到两个焦点距离之和为常数的点的轨迹。不是'压扁的圆'——它有自己独特的几何定义。", expression="🧙", music="calm"),
        _m("sage", "椭圆上任意一点 P 满足 $|PF_1| + |PF_2| = 2a$。这个定义可以推导出标准方程 $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1$。", expression="😊"),
        _m("sage", "关键参数：$a$ 长半轴，$b$ 短半轴，$c$ 半焦距。$c^2 = a^2 - b^2$。离心率 $e = c/a$，$0<e<1$。", expression="🤔", bg="night", music="mysterious"),
        _m("sage", "椭圆的焦点三角形面积公式 $S = b^2\\tan\\frac{\\theta}{2}$ 是高考高频考点。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：椭圆的定义",
    "layer1": "**定义**：平面内到两定点 $F_1,F_2$ 距离之和为常数 $2a$ 的点的轨迹。\n\n其中 $|F_1F_2| = 2c$，$2a > 2c$。\n\n$|PF_1|+|PF_2| = 2a$（椭圆上任意一点 P）",
    "layer2_title": "第二层：标准方程",
    "layer2": "从定义推导标准方程：以 $F_1(-c,0),F_2(c,0)$ 为焦点，设 $P(x,y)$。\n\n$\\sqrt{(x+c)^2+y^2} + \\sqrt{(x-c)^2+y^2} = 2a$\n\n化简得：$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$，其中 $b^2 = a^2 - c^2$。\n\n焦点在 y 轴时：$\\frac{y^2}{a^2} + \\frac{x^2}{b^2} = 1$。",
    "layer3_title": "第三层：关键参数",
    "layer3": "- $a$ 长半轴，$b$ 短半轴，$c$ 半焦距\n- $c^2 = a^2 - b^2$（注意是减号）\n- 离心率 $e = \\frac{c}{a}$，$0<e<1$\n- $e$ 越接近 1 → 越扁；$e$ 越接近 0 → 越圆",
    "layer4_title": "第四层：焦点三角形",
    "layer4": "$\\triangle PF_1F_2$ 称为焦点三角形。\n\n面积公式：$S = b^2\\tan\\frac{\\theta}{2}$（$\\theta = \\angle F_1PF_2$）\n\n周长：$2a + 2c$\n\n余弦定理 + 椭圆定义联用是高考最爱。",
    "layer5_title": "第五层：解题策略",
    "layer5": "椭圆问题的两大工具：\n1. 定义法：$|PF_1|+|PF_2|=2a$\n2. 方程法：设点代入方程\n\n焦点三角形面积公式 $S=b^2\\tan\\frac{\\theta}{2}$ 要熟练。",
    "formula": "\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\quad (a>b>0) \\\\\nc^2 = a^2 - b^2,\\quad e = \\frac{c}{a} \\\\\nS_{\\triangle PF_1F_2} = b^2\\tan\\frac{\\theta}{2}",
    "examples": [
        {"difficulty": "基础", "q": "椭圆 $\\frac{x^2}{16}+\\frac{y^2}{9}=1$ 的焦距？", "s": "$a=4,b=3$。$c^2=7$。$2c=2\\sqrt{7}$。", "a": "$2\\sqrt{7}$"},
        {"difficulty": "中档", "q": "$a=5,c=4$，焦点在x轴，求椭圆方程。", "s": "$b^2=25-16=9$。$\\frac{x^2}{25}+\\frac{y^2}{9}=1$。", "a": "$\\frac{x^2}{25}+\\frac{y^2}{9}=1$"},
        {"difficulty": "进阶", "q": "椭圆 $\\frac{x^2}{4}+\\frac{y^2}{3}=1$，$\\angle F_1PF_2=60°$，求 $S_{\\triangle}$。", "s": "$S = b^2\\tan30° = 3\\times\\frac{\\sqrt{3}}{3} = \\sqrt{3}$。", "a": "$\\sqrt{3}$"}
    ],
    "traps": ["$c^2 = a^2 - b^2$（椭圆），双曲线是 $c^2 = a^2 + b^2$", "$a$ 永远是大的数（长半轴）"],
    "connections": "椭圆 + 双曲线 + 抛物线 = 圆锥曲线（用一个平面截圆锥的三种截面）。",
    "practice_hint": "椭圆中 $a$ 最大。给了焦点三角形角度→面积公式。求轨迹→用定义。"
},

"抛物线标准方程": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🎯</div><div style='font-size:20px;font-weight:800'>第 14 章</div><div style='font-size:15px;color:var(--text-secondary)'>平抛的轨迹 · 抛物线</div></div>", bg="dawn"),
        _m("sage", "抛物线是到焦点和到准线距离相等的点的轨迹。$|PF| = d(P, 准线)$。", expression="🧙", music="calm"),
        _m("sage", "标准方程：$y^2 = 2px$。焦点 $(p/2, 0)$，准线 $x = -p/2$。", expression="😊"),
        _m("sage", "记忆口诀：$p$ 是焦点到准线的距离。开口方向看平方项对面。$y^2=2px$ 开口朝右，$y^2=-2px$ 开口朝左，$x^2=2py$ 开口朝上。", expression="🤔", music="mysterious"),
        _m("sage", "抛物线上任意点到焦点的距离 = 该点到准线的距离 = 该点的横坐标 + p/2。这个性质在'抛物线定义'题型中反复用。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：抛物线的定义",
    "layer1": "平面内到定点（焦点）和到定直线（准线）距离相等的点的轨迹。\n\n$|PF| = d(P, 准线)$\n\n注意：椭圆是到两焦点距离之和为常数，双曲线是到两焦点距离之差为常数，抛物线是到一个焦点和一个准线的距离相等。",
    "layer2_title": "第二层：四种标准方程",
    "layer2": "| 方程 | 焦点 | 准线 | 开口 |\n|------|------|------|------|\n| $y^2=2px$ | $(\\frac{p}{2},0)$ | $x=-\\frac{p}{2}$ | 右 |\n| $y^2=-2px$ | $(-\\frac{p}{2},0)$ | $x=\\frac{p}{2}$ | 左 |\n| $x^2=2py$ | $(0,\\frac{p}{2})$ | $y=-\\frac{p}{2}$ | 上 |\n| $x^2=-2py$ | $(0,-\\frac{p}{2})$ | $y=\\frac{p}{2}$ | 下 |",
    "layer3_title": "第三层：关键性质",
    "layer3": "1. $|PF| = x_P + \\frac{p}{2}$（对于 $y^2=2px$）——焦点半径公式\n2. 过焦点的弦（焦点弦）满足 $\\frac{1}{|AF|}+\\frac{1}{|BF|} = \\frac{2}{p}$\n3. 抛物线在光学中的应用：平行于轴的光线反射后经过焦点",
    "layer4_title": "第四层：相对于椭圆和双曲线",
    "layer4": "椭圆：$e<1$ | 抛物线：$e=1$ | 双曲线：$e>1$\n\n离心率 $e=1$ 是抛物线的特征——也是圆锥曲线中抛物线的定义特征。",
    "layer5_title": "第五层：解题策略",
    "layer5": "抛物线题的核心：**用定义**。\n\n$|PF|$ = $P$ 到准线距离。这个转化把几何问题变成代数计算。",
    "formula": "y^2 = 2px \\quad \\text{焦点}(\\frac{p}{2},0),\\ \\text{准线}\\ x=-\\frac{p}{2} \\\\\n|PF| = x_P + \\frac{p}{2}",
    "examples": [
        {"difficulty": "基础", "q": "$y^2=8x$的焦点坐标？", "s": "$2p=8$→$p=4$。焦点 $(2,0)$。", "a": "$(2,0)$"},
        {"difficulty": "中档", "q": "P在$y^2=4x$上，$|PF|=5$，求P横坐标。", "s": "$|PF| = x_P+1 = 5$→$x_P=4$。", "a": "$4$"},
        {"difficulty": "进阶", "q": "过$y^2=2x$焦点作直线交于A,B，$|AB|=4$，求AB方程。", "s": "设$y=k(x-\\frac{1}{2})$，代入$y^2=2x$。用弦长公式解k。", "a": "$k = \\pm\\frac{\\sqrt{2}}{2}$"}
    ],
    "traps": ["不要记错$p$和$p/2$——焦点是$(p/2,0)$不是$(p,0)$", "$y^2=2px$开口朝右（x轴正方向）"],
    "connections": "椭圆($e<1$) + 抛物线($e=1$) + 双曲线($e>1$) = 圆锥曲线完整家族。",
    "practice_hint": "看到$|PF|$→用定义转化成坐标。抛物线比其他两种圆锥曲线更依赖定义法。"
},

"双曲线标准方程": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🌀</div><div style='font-size:20px;font-weight:800'>第 15 章</div><div style='font-size:15px;color:var(--text-secondary)'>渐近之美 · 双曲线</div></div>", bg="dawn"),
        _m("sage", "双曲线是到两焦点距离之差的绝对值为常数的点的轨迹。$||PF_1|-|PF_2|| = 2a$。", expression="🧙", music="calm"),
        _m("sage", "关键差异：$c^2 = a^2 + b^2$（注意是加号！椭圆是减号）。离心率 $e = c/a > 1$。", expression="😊"),
        _m("sage", "双曲线有渐近线：$y = \\pm\\frac{b}{a}x$——曲线无限趋近但永不相交。等轴双曲线 $a=b$ 时渐近线互相垂直。", expression="🤔", bg="night", music="mysterious"),
    ],
    "layer1_title": "第一层：双曲线的定义",
    "layer1": "$||PF_1| - |PF_2|| = 2a$（常数），其中 $|F_1F_2| = 2c > 2a$\n\n焦点在 x 轴：$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$\n焦点在 y 轴：$\\frac{y^2}{a^2} - \\frac{x^2}{b^2} = 1$",
    "layer2_title": "第二层：与椭圆的关键区别",
    "layer2": "| 性质 | 椭圆 | 双曲线 |\n|------|------|--------|\n| 定义 | $PF_1+PF_2=2a$ | $|PF_1-PF_2|=2a$ |\n| $c^2=$ | $a^2-b^2$ | $a^2+b^2$ |\n| 离心率 | $0<e<1$ | $e>1$ |\n| 渐近线 | 无 | $y=\\pm\\frac{b}{a}x$ |",
    "layer3_title": "第三层：渐近线",
    "layer3": "双曲线 $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$ 的渐近线为 $y = \\pm\\frac{b}{a}x$。\n\n令方程右边从 1 变为 0：$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 0$ → $y = \\pm\\frac{b}{a}x$。\n\n这个方法适用于任何双曲线——令 =0 即得渐近线。",
    "layer4_title": "第四层：等轴双曲线",
    "layer4": "当 $a=b$ 时，$x^2-y^2=a^2$，渐近线 $y=\\pm x$（互相垂直）。\n\n离心率 $e = \\sqrt{2}$（固定值）。\n\n反比例函数 $y=\\frac{k}{x}$ 是等轴双曲线旋转 45° 后的形式。",
    "layer5_title": "第五层：解题策略",
    "layer5": "双曲线题的关键：\n1. 先判断焦点在哪条轴\n2. $c^2=a^2+b^2$（千万别写成减号）\n3. 渐近线用 =0 法快速求",
    "formula": "\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1 \\\\\nc^2 = a^2 + b^2,\\quad e = \\frac{c}{a} > 1 \\\\\n\\text{渐近线: } y = \\pm\\frac{b}{a}x",
    "examples": [
        {"difficulty": "基础", "q": "双曲线 $\\frac{x^2}{9}-\\frac{y^2}{16}=1$ 的渐近线？", "s": "$a=3,b=4$。$y=\\pm\\frac{4}{3}x$。", "a": "$y=\\pm\\frac{4}{3}x$"},
        {"difficulty": "中档", "q": "$a=2,e=\\sqrt{3}$，求双曲线方程。", "s": "$c=2\\sqrt{3}$。$b^2=c^2-a^2=12-4=8$。$\\frac{x^2}{4}-\\frac{y^2}{8}=1$。", "a": "$\\frac{x^2}{4}-\\frac{y^2}{8}=1$"},
        {"difficulty": "进阶", "q": "渐近线 $y=\\pm2x$ 且过 $(1,3)$，求方程。", "s": "$\\frac{b}{a}=2$→$b=2a$。代入点解得 $a^2=1,b^2=4$。", "a": "$x^2-\\frac{y^2}{4}=1$"}
    ],
    "traps": ["$c^2 = a^2 + b^2$（加号！椭圆是减号）", "焦点在哪条轴看正号在哪个分母"],
    "connections": "椭圆 + 抛物线 + 双曲线 = 圆锥曲线三兄弟。统一定义：到焦点距离与到准线距离之比为 e。",
    "practice_hint": "渐近线用 =0 法：令方程 =0 → 解出 y。先判断焦点位置再列方程。"
},

"排列组合": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🎰</div><div style='font-size:20px;font-weight:800'>第 16 章</div><div style='font-size:15px;color:var(--text-secondary)'>有序还是无序·排列组合</div></div>", bg="dawn"),
        _m("sage", "从5本书选3本送给3位同学，每人1本——有几种送法？换一个问法：从5本书选3本捐给图书馆——有几种选法？", expression="🧙", music="calm"),
        _m("sage", "第一问：选后还要分配给人——有序→排列 $A_5^3=60$。第二问：只选不分配——无序→组合 $C_5^3=10$。", expression="😊"),
        _m("sage", "排列和组合的区别只有一件事：交换两个元素的位置，是否产生新的结果？是→排列，否→组合。", expression="🤔", bg="night", music="mysterious"),
        _m("sage", "组合数的对称性：$C_n^m = C_n^{n-m}$。选3个等于排除7个。这个性质在解题时非常好用。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：排列 vs 组合",
    "layer1": "**排列**：$A_n^m$ — 从 n 个中选 m 个并排序。顺序重要。\n**组合**：$C_n^m$ — 从 n 个中选 m 个。顺序不重要。\n\n判据：交换两个元素，结果变了吗？变→排列，不变→组合。",
    "layer2_title": "第二层：公式",
    "layer2": "$$A_n^m = n(n-1)...(n-m+1) = \\frac{n!}{(n-m)!}$$\n$$C_n^m = \\frac{A_n^m}{m!} = \\frac{n!}{m!(n-m)!}$$\n\n$C_n^m = C_n^{n-m}$（选 m 个 = 排除 n-m 个）\n$C_n^0 = C_n^n = 1$",
    "layer3_title": "第三层：常见模型",
    "layer3": "1. **排列**：排队、密码、比赛名次\n2. **组合**：选人、抽奖、组队\n3. **分组分配**：先分组（组合），再分配（排列）→ $C_n^m \\times A_m^m$\n4. **不相邻问题**：插空法\n5. **相邻问题**：捆绑法",
    "layer4_title": "第四层：计数原理",
    "layer4": "排列组合建立在两个基本计数原理上：\n- **分类加法**：做一件事有 k 类方法→ $N = n_1+n_2+...+n_k$\n- **分步乘法**：做一件事有 k 个步骤→ $N = n_1\\times n_2\\times...\\times n_k$",
    "layer5_title": "第五层：解题策略",
    "layer5": "1. 先判断有序/无序 → 选排列还是组合\n2. 特殊位置/特殊元素优先处理\n3. 相邻用捆绑，不相邻用插空\n4. 分组分配分两步：先组合分组，再排列分配",
    "formula": "A_n^m = \\frac{n!}{(n-m)!} \\\\\nC_n^m = \\frac{n!}{m!(n-m)!} \\\\\nC_n^m = C_n^{n-m}",
    "examples": [
        {"difficulty": "基础", "q": "5人排队，有几种排法？", "s": "$A_5^5 = 5! = 120$。", "a": "$120$"},
        {"difficulty": "中档", "q": "5本不同的书选3本送给3人。", "s": "$A_5^3 = 5\\times4\\times3 = 60$。", "a": "$60$"},
        {"difficulty": "进阶", "q": "6把椅子，3人就座，任何两人不相邻。", "s": "先排3空椅→4空位，选3个放人：$A_4^3=24$。", "a": "$24$"}
    ],
    "traps": ["$C_n^0 = 1$ 不是 0", "$C_n^m = C_n^{n-m}$——有时算 '排除' 更快", "分组后如果组之间无区别，要除以组数的阶乘"],
    "connections": "排列组合 → 二项式定理（$C_n^k$ 就是二项式系数）→ 概率（古典概型分母）。",
    "practice_hint": "判断顺序是否重要→决定用 A 还是 C。分组分配两步走：先组合再排列。"
},

"二项式定理": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📐</div><div style='font-size:20px;font-weight:800'>第 17 章</div><div style='font-size:15px;color:var(--text-secondary)'>展开的规律 · 二项式定理</div></div>", bg="dawn"),
        _m("sage", "$(a+b)^n$ 的展开式中，每一项的系数恰好是组合数 $C_n^k$。这不是巧合——展开就是'从 n 个括号里选 k 个 b'。", expression="🧙", music="calm"),
        _m("sage", "$(a+b)^n = C_n^0 a^n + C_n^1 a^{n-1}b + ... + C_n^n b^n$。通项 $T_{k+1} = C_n^k a^{n-k} b^k$。", expression="😊"),
        _m("sage", "二项式系数之和 = $2^n$（令 a=b=1）。奇数项系数和 = 偶数项系数和 = $2^{n-1}$。", expression="🤔", bg="night", music="mysterious"),
    ],
    "layer1_title": "第一层：为什么系数是组合数？",
    "layer1": "$(a+b)^n = (a+b)(a+b)...(a+b)$（n 个括号）\n\n展开式中 $a^{n-k}b^k$ 的系数 = 从 n 个括号中选出 k 个取 b 的方案数 = $C_n^k$。\n\n**这就是二项式定理的直觉。**",
    "layer2_title": "第二层：通项公式",
    "layer2": "第 $k+1$ 项：$$T_{k+1} = C_n^k \\cdot a^{n-k} \\cdot b^k$$\n\n指数规律：a 的指数从 n 递减到 0，b 的指数从 0 递增到 n。两位指数之和始终等于 n。",
    "layer3_title": "第三层：重要性质",
    "layer3": "- 系数和：$C_n^0+C_n^1+...+C_n^n = 2^n$\n- 奇数项和 = 偶数项和 = $2^{n-1}$\n- $C_n^0+C_n^2+C_n^4+... = C_n^1+C_n^3+C_n^5+... = 2^{n-1}$\n- 最大项：中间项（当 n 为偶数时第 $\\frac{n}{2}+1$ 项最大）",
    "layer4_title": "第四层：常见问题类型",
    "layer4": "1. **求指定项**：令指数 = 目标次数，解出 k\n2. **求系数和**：令 a=b=1 代入\n3. **求最大项**：解 $T_k \\leq T_{k+1}$ 不等式\n4. **证明恒等式**：取特殊值代入",
    "layer5_title": "第五层：解题模板",
    "layer5": "1. 写出通项 $T_{k+1} = C_n^k a^{n-k} b^k$\n2. 令 b 的指数 = 目标次数 → 解 k\n3. 代回求系数\n\n注意区分\"二项式系数\"($C_n^k$)和\"项的系数\"（含正负号和数字因子）。",
    "formula": "(a+b)^n = \\sum_{k=0}^{n} C_n^k a^{n-k} b^k \\\\\nT_{k+1} = C_n^k a^{n-k} b^k",
    "examples": [
        {"difficulty": "基础", "q": "$(x+2)^4$ 中 $x^2$ 的系数。", "s": "$C_4^2\\times2^2=6\\times4=24$。", "a": "$24$"},
        {"difficulty": "中档", "q": "$(2x-\\frac{1}{x})^6$ 的常数项。", "s": "$T_{k+1}=C_6^k(2x)^{6-k}(-\\frac{1}{x})^k$。$6-2k=0$→$k=3$。常数$=-160$。", "a": "$-160$"},
        {"difficulty": "进阶", "q": "$(1+x)^n$ 展开式中第5,6,7项系数成等差数列，求 n。", "s": "$2C_n^5 = C_n^4 + C_n^6$，解出 $n=7$ 或 $n=14$。", "a": "$n=7$ 或 $14$"}
    ],
    "traps": ["\"项的系数\"含符号和数字，\"二项式系数\"仅指 $C_n^k$", "常数项→令指数=0解k", "中间项：n为偶数时有1个中间项，n为奇数时有2个"],
    "connections": "二项式系数 = 组合数。杨辉三角 = 二项式系数的几何排列。牛顿二项式定理可推广到实数指数。",
    "practice_hint": "通项→令指数=目标→解k→求系数。求系数和令a=b=1。最大项：解不等式比较相邻项。"
},

"概率": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🎲</div><div style='font-size:20px;font-weight:800'>第 18 章</div><div style='font-size:15px;color:var(--text-secondary)'>不确定中的确定 · 概率</div></div>", bg="dawn"),
        _m("sage", "掷一枚骰子，得到6的概率是1/6。这不意味着掷6次一定有一次6——而是掷很多次后，频率趋近于概率。", expression="🧙", music="calm"),
        _m("sage", "概率三公式：加法 $P(A\\cup B)=P(A)+P(B)-P(AB)$，乘法 $P(AB)=P(A)P(B|A)$，全概率 $P(B)=\\sum P(A_i)P(B|A_i)$。", expression="😊"),
        _m("sage", "贝叶斯公式是概率中最美的：它告诉你'已知结果，反推原因'的概率。$P(A|B) = P(A)P(B|A)/P(B)$。", expression="🤔", bg="night", music="mysterious"),
    ],
    "layer1_title": "第一层：概率是什么",
    "layer1": "古典概型：$P(A) = \\frac{\\text{有利情况数}}{\\text{总情况数}}$（每个基本事件等可能）。\n\n统计定义：大量重复试验中事件发生的频率稳定值。",
    "layer2_title": "第二层：三个核心公式",
    "layer2": "1. **加法公式**：$P(A\\cup B) = P(A) + P(B) - P(AB)$\n2. **条件概率**：$P(B|A) = \\frac{P(AB)}{P(A)}$\n3. **全概率公式**：$P(B) = \\sum_i P(A_i)P(B|A_i)$\n4. **贝叶斯**：$P(A|B) = \\frac{P(A)P(B|A)}{P(B)}$",
    "layer3_title": "第三层：独立 vs 互斥",
    "layer3": "**互斥**：$A$ 和 $B$ 不能同时发生 → $P(AB)=0$\n**独立**：$A$ 的发生不影响 $B$ → $P(AB)=P(A)P(B)$\n\n不要混淆！互斥的事件不是独立的——如果A发生了，B就绝不可能发生（高度相关）。",
    "layer4_title": "第四层：概率的思维方式",
    "layer4": "概率论教给我们一种独特的思维方式：\n- 不确定性是可以量化的\n- 条件概率是'更新信念'的数学工具\n- 贝叶斯公式是'从证据推原因'的形式化",
    "layer5_title": "第五层：解题策略",
    "layer5": "1. 先判断是否古典概型（等可能）\n2. 复杂事件用加法公式拆解\n3. 已知条件用条件概率\n4. 多步问题用全概率公式\n5. 反推原因用贝叶斯",
    "formula": "P(A) = \\frac{n(A)}{n(\\Omega)} \\\\\nP(A\\cup B) = P(A) + P(B) - P(AB) \\\\\nP(B|A) = \\frac{P(AB)}{P(A)} \\\\\nP(A|B) = \\frac{P(A)P(B|A)}{P(B)}",
    "examples": [
        {"difficulty": "基础", "q": "掷两枚骰子，和为7的概率。", "s": "有利(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)共6种。$P=6/36=1/6$。", "a": "$1/6$"},
        {"difficulty": "中档", "q": "甲命中率0.7乙0.6，各投一次至少一人命中。", "s": "$P=1-0.3\\times0.4=0.88$。", "a": "$0.88$"},
        {"difficulty": "进阶", "q": "次品率A=5% B=3%，抽到A概率0.6。已知抽到次品，求它是A的概率。", "s": "$P(次品)=0.042$。$P(A|次品)=0.6\\times0.05/0.042=5/7$。", "a": "$5/7$"}
    ],
    "traps": ["古典概型要求等可能", "独立≠互斥", "条件概率分母不能为0"],
    "connections": "概率→分布列→期望（下一章）。概率是统计推断的数学基础。",
    "practice_hint": "先判断古典/条件/独立。复杂事件拆解。贝叶斯题画出概率树。"
},

"分布列与数学期望": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📊</div><div style='font-size:20px;font-weight:800'>第 19 章</div><div style='font-size:15px;color:var(--text-secondary)'>随机变量的画像·分布列与期望</div></div>", bg="dawn"),
        _m("sage", "概率告诉你某个事件的可能性。但如果一个随机现象有多种可能结果，每种结果有不同的概率——你需要分布列来完整描述它。", expression="🧙", music="calm"),
        _m("sage", "分布列 = 一张表，列出随机变量 X 的每个可能取值和对应的概率。期望 $E(X)$ = 每个取值乘以概率的总和——是'平均而言'的结果。", expression="😊"),
        _m("sage", "方差 $D(X) = E(X^2) - [E(X)]^2$ 衡量的是'波动有多大'。期望告诉你平均水平，方差告诉你稳定程度。", expression="🤔", bg="night", music="mysterious"),
    ],
    "layer1_title": "第一层：分布列是什么",
    "layer1": "分布列 = 随机变量 X 的取值概率表：\n\n| X | $x_1$ | $x_2$ | ... | $x_n$ |\n|---|-------|-------|-----|-------|\n| P | $p_1$ | $p_2$ | ... | $p_n$ |\n\n$\\sum p_i = 1$（所有概率加起来等于1）。",
    "layer2_title": "第二层：数学期望",
    "layer2": "$$E(X) = \\sum_{i=1}^{n} x_i \\cdot p_i$$\n\n期望 = 每个可能值 × 它的概率，然后求和。\n\n**直觉**：大量重复试验后，X 的平均值趋近于 $E(X)$。\n\n性质：$E(aX+b) = aE(X)+b$（线性）。",
    "layer3_title": "第三层：方差",
    "layer3": "$$D(X) = E[(X-E(X))^2] = E(X^2) - [E(X)]^2$$\n\n方差衡量 X 的波动程度。\n\n**计算技巧**：用第二个公式 $E(X^2)-[E(X)]^2$ 通常比定义式快。",
    "layer4_title": "第四层：常见分布",
    "layer4": "1. **二项分布** $X\\sim B(n,p)$：$E(X)=np$，$D(X)=np(1-p)$\n2. **超几何分布**：从 N 件（M 件次品）抽 n 件，次品数的分布\n3. **两点分布**（伯努利）：$X\\in\\{0,1\\}$，$E(X)=p$，$D(X)=p(1-p)$",
    "layer5_title": "第五层：解题策略",
    "layer5": "1. 确定 X 的所有可能取值\n2. 计算每个取值的概率\n3. 列表（分布列）\n4. 验证概率和为 1\n5. 用公式求 $E(X)$ 和 $D(X)$",
    "formula": "E(X) = \\sum x_i p_i \\\\\nD(X) = E(X^2) - [E(X)]^2 = \\sum x_i^2 p_i - (\\sum x_i p_i)^2 \\\\\nE(aX+b) = aE(X) + b,\\quad D(aX+b) = a^2 D(X)",
    "examples": [
        {"difficulty": "基础", "q": "掷骰子点数X的期望。", "s": "$E(X)=(1+2+3+4+5+6)/6=3.5$。", "a": "$3.5$"},
        {"difficulty": "中档", "q": "3红2白取2个，红球数X的分布列和期望。", "s": "$P(X=0)=1/10,P(X=1)=6/10,P(X=2)=3/10$。$E(X)=0+0.6+0.6=1.2$。", "a": "$E(X)=1.2$"},
        {"difficulty": "进阶", "q": "$X\\sim B(10, 0.3)$，求 $E(X), D(X)$。", "s": "$E(X)=10\\times0.3=3$。$D(X)=10\\times0.3\\times0.7=2.1$。", "a": "$E=3, D=2.1$"}
    ],
    "traps": ["概率和必须为1——不满足则分布列有误", "$D(X)=E(X^2)-[E(X)]^2$ 中 $E(X^2)\\neq[E(X)]^2$", "期望的单位和随机变量一致"],
    "connections": "分布列 → 期望 → 方差 → 正态分布。概率统计的完整链条。",
    "practice_hint": "先确定X的所有可能值→算每个概率→验证和为1→套公式求期望方差。二项分布直接代公式最快。"
},

"空间向量坐标运算": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>📦</div><div style='font-size:20px;font-weight:800'>第 20 章</div><div style='font-size:15px;color:var(--text-secondary)'>三维世界·空间向量</div></div>", bg="dawn"),
        _m("sage", "立体几何题难在'空间想象力'。但空间向量让立体几何变成了纯计算——建系、写坐标、套公式，不需要想象。", expression="🧙", music="calm"),
        _m("sage", "$\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2$。$\\vec{a}\\times\\vec{b}$ 得法向量。$\\cos\\theta = \\frac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}$。", expression="😊"),
        _m("sage", "三步：建系（选原点）→ 写坐标（终点-起点）→ 套公式（点积求角，叉积求法向量）。立体几何变成了代数。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：空间直角坐标系",
    "layer1": "右手系：右手拇指=x，食指=y，中指=z。\n\n点坐标 $P(x,y,z)$。两点间距离 $|AB| = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$。",
    "layer2_title": "第二层：向量的数量积（点积）",
    "layer2": "$\\vec{a}\\cdot\\vec{b} = x_1x_2 + y_1y_2 + z_1z_2$\n\n$\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta$\n\n$\\vec{a}\\cdot\\vec{b} = 0$ ↔ $\\vec{a} \\perp \\vec{b}$（垂直的充要条件）",
    "layer3_title": "第三层：向量的向量积（叉积）",
    "layer3": "$\\vec{a}\\times\\vec{b} = (y_1z_2-z_1y_2, z_1x_2-x_1z_2, x_1y_2-y_1x_2)$\n\n几何意义：$\\vec{a}\\times\\vec{b}$ 垂直于 $\\vec{a}$ 和 $\\vec{b}$（法向量），大小等于 $\\vec{a},\\vec{b}$ 张成平行四边形的面积。",
    "layer4_title": "第四层：空间向量解立体几何",
    "layer4": "1. 建系（选好原点，三条互相垂直的棱作坐标轴）\n2. 写坐标（所有关键点的坐标）\n3. 写向量（终点-起点）\n4. 套公式求角/距离",
    "layer5_title": "第五层：常见计算",
    "layer5": "- 线线角：$\\cos\\theta = \\frac{|\\vec{a}\\cdot\\vec{b}|}{|\\vec{a}||\\vec{b}|}$\n- 线面角：$\\sin\\theta = \\frac{|\\vec{n}\\cdot\\vec{a}|}{|\\vec{n}||\\vec{a}|}$（法向量和线的夹角余角）\n- 二面角：$\\cos\\theta = \\frac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}$",
    "formula": "\\vec{a}\\cdot\\vec{b} = x_1x_2 + y_1y_2 + z_1z_2 \\\\\n|\\vec{a}| = \\sqrt{x^2+y^2+z^2} \\\\\n\\cos\\theta = \\frac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}",
    "examples": [
        {"difficulty": "基础", "q": "$\\vec{a}=(1,0,-1),\\vec{b}=(-1,1,0)$，求点积。", "s": "$=1\\times(-1)+0\\times1+(-1)\\times0=-1$。", "a": "$-1$"},
        {"difficulty": "中档", "q": "$\\vec{a}=(1,2,-1),\\vec{b}=(2,-1,1)$，求夹角余弦。", "s": "点积$=2-2-1=-1$。$|\\vec{a}|=\\sqrt{6}$，$|\\vec{b}|=\\sqrt{6}$。$\\cos\\theta=-1/6$。", "a": "$-1/6$"},
        {"difficulty": "进阶", "q": "正方体棱长1，求 $AB_1$ 与 $BC_1$ 所成角。", "s": "建系→$\\vec{AB_1}=(0,1,1),\\vec{BC_1}=(-1,0,1)$。$\\cos\\theta=1/2$→$\\theta=60°$。", "a": "$60°$"}
    ],
    "traps": ["$\\vec{a}\\cdot\\vec{b}=0$ 是垂直的充要条件", "$\\vec{a}\\parallel\\vec{b}$ 等价于对应坐标成比例", "点积和叉积不要混淆——点积得数，叉积得向量"],
    "connections": "平面向量 → 空间向量（推广一维）→ 法向量 → 立体几何代数化。",
    "practice_hint": "建系→写坐标→写向量→套公式。找三条两两垂直的棱作坐标轴。"
},

"法向量求法": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🧭</div><div style='font-size:20px;font-weight:800'>第 21 章</div><div style='font-size:15px;color:var(--text-secondary)'>平面的方向·法向量</div></div>", bg="dawn"),
        _m("sage", "法向量是垂直于平面的向量——用平面内两个不共线的向量做叉积就得到它。", expression="🧙", music="calm"),
        _m("sage", "有了法向量，一切变得简单：线面角、二面角、点到面的距离——全都可以用法向量来算。", expression="😊"),
        _m("sage", "$\\vec{n} = \\vec{AB} \\times \\vec{AC}$。可以约简（同乘除一个数仍是法向量）。", expression="✨", music="upbeat"),
    ],
    "layer1_title": "第一层：什么是法向量",
    "layer1": "垂直于平面的向量。一个平面有无穷多个法向量（所有平行的非零向量）。\n\n求法：在平面上找两个不共线向量 $\\vec{u}, \\vec{v}$，法向量 $\\vec{n} = \\vec{u} \\times \\vec{v}$。",
    "layer2_title": "第二层：叉积求法",
    "layer2": "$\\vec{a}=(x_1,y_1,z_1), \\vec{b}=(x_2,y_2,z_2)$：\n\n$\\vec{a}\\times\\vec{b} = \\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ x_1 & y_1 & z_1 \\\\ x_2 & y_2 & z_2 \\end{vmatrix}$\n\n$= (y_1z_2-z_1y_2, z_1x_2-x_1z_2, x_1y_2-y_1x_2)$",
    "layer3_title": "第三层：法向量的应用",
    "layer3": "1. **线面角**：$\\sin\\theta = \\frac{|\\vec{n}\\cdot\\vec{a}|}{|\\vec{n}||\\vec{a}|}$\n2. **二面角**：$\\cos\\theta = \\pm\\frac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}$（注意正负判断）\n3. **点到面距离**：$d = \\frac{|\\vec{n}\\cdot\\vec{AP}|}{|\\vec{n}|}$",
    "layer4_title": "第四层：为什么法向量这么重要？",
    "layer4": "平面的方向信息完全包含在法向量中。两个法向量的夹角 = 两个平面的夹角。\n\n有了法向量，立体几何变成平面几何+向量计算——这是高中数学最重要的'降维'思想。",
    "layer5_title": "第五层：计算技巧",
    "layer5": "1. 求法向量三步：找平面内两向量→叉积→可约简\n2. 二面角的符号：看法向量是同向还是反向\n3. 点到面距离公式本质是投影长度",
    "formula": "\\vec{n} = \\vec{AB} \\times \\vec{AC} \\\\\nd(P,\\alpha) = \\frac{|\\vec{n}\\cdot\\vec{AP}|}{|\\vec{n}|}",
    "examples": [
        {"difficulty": "基础", "q": "平面过A(1,0,0)B(0,1,0)C(0,0,1)，求法向量。", "s": "$\\vec{AB}=(-1,1,0),\\vec{AC}=(-1,0,1)$。$\\vec{n}=(1,1,1)$。", "a": "$(1,1,1)$"},
        {"difficulty": "中档", "q": "二面角的两个法向量 $(1,0,1)$ 和 $(0,1,1)$，求二面角。", "s": "$\\cos\\theta = 1/(\\sqrt{2}\\cdot\\sqrt{2}) = 1/2$→$\\theta=60°$。", "a": "$60°$"},
        {"difficulty": "进阶", "q": "点P(1,2,3)到平面x+y+z=1的距离。", "s": "法向量$(1,1,1)$。取平面上点$(1,0,0)$。$d=|1+2+3-1|/\\sqrt{3}=5/\\sqrt{3}$。", "a": "$5/\\sqrt{3}$"}
    ],
    "traps": ["法向量方向可相反——$\\vec{n}$ 和 $-\\vec{n}$ 都是法向量", "二面角要判断锐角还是钝角", "一个平面有无穷多法向量——都是平行的"],
    "connections": "空间向量→叉积→法向量→线面角/二面角/距离。立体几何全部代数化。",
    "practice_hint": "建系后，先找平面上两个不共线的向量→叉积得法向量。二面角注意符号。"
},

"复数运算": {
    "deep": True,
    "vn_script": [
        _m("system", html="<div style='text-align:center;padding:50px 0'><div style='font-size:48px'>🔮</div><div style='font-size:20px;font-weight:800'>第 22 章</div><div style='font-size:15px;color:var(--text-secondary)'>虚数的世界·复数</div></div>", bg="dawn"),
        _m("sage", "$i^2 = -1$。这个定义看起来简单，但它开启了一个全新的数学世界——复数。", expression="🧙", music="calm"),
        _m("sage", "复数 $z=a+bi$ 可以看作复平面上的点 $(a,b)$。模 $|z|=\\sqrt{a^2+b^2}$，共轭 $\\bar{z}=a-bi$。", expression="😊"),
        _m("sage", "除法技巧：$\\frac{z_1}{z_2} = \\frac{z_1\\bar{z_2}}{|z_2|^2}$。分子分母同乘分母的共轭，分母变成实数。", expression="🤔", bg="night", music="mysterious"),
    ],
    "layer1_title": "第一层：为什么需要复数？",
    "layer1": "方程 $x^2 = -1$ 在实数范围内无解——但数学需要它。引入 $i$（$i^2=-1$）后，任何多项式方程都有解（代数基本定理）。\n\n复数不仅是数学需要——物理学（量子力学、电路分析）也离不开。",
    "layer2_title": "第二层：复数的运算",
    "layer2": "加法：$(a+bi)+(c+di) = (a+c)+(b+d)i$\n乘法：$(a+bi)(c+di) = (ac-bd)+(ad+bc)i$\n除法：$\\frac{a+bi}{c+di} = \\frac{(a+bi)(c-di)}{c^2+d^2}$",
    "layer3_title": "第三层：复数的几何意义",
    "layer3": "复平面：实轴（x轴）+ 虚轴（y轴）。\n$z=a+bi$ = 点 $(a,b)$。$|z|$ = 到原点的距离。\n$\\bar{z}$ = 关于实轴的镜像。\n\n$i$ 的幂循环：$i^1=i, i^2=-1, i^3=-i, i^4=1$（周期为4）。",
    "layer4_title": "第四层：复数的模和共轭",
    "layer4": "$|z| = \\sqrt{a^2+b^2}$（几何：复平面上到原点的距离）\n$z\\cdot\\bar{z} = |z|^2 = a^2+b^2$（复数乘以共轭 = 模的平方，是实数）\n$|z_1z_2| = |z_1||z_2|$（乘积的模 = 模的乘积）",
    "layer5_title": "第五层：解题策略",
    "layer5": "1. 分母有 $i$ → 分子分母同乘分母的共轭\n2. $i^n$ → 周期为4，$i^n = i^{n \\bmod 4}$\n3. $|z-a-bi|$ = 复平面上 $z$ 到点 $(a,b)$ 的距离",
    "formula": "i^2 = -1,\\quad |z| = \\sqrt{a^2+b^2} \\\\\n\\bar{z} = a-bi,\\quad z\\bar{z} = |z|^2 \\\\\n\\frac{z_1}{z_2} = \\frac{z_1\\bar{z_2}}{|z_2|^2}",
    "examples": [
        {"difficulty": "基础", "q": "计算 $(1+i)^2$。", "s": "$=1+2i+i^2 = 1+2i-1 = 2i$。", "a": "$2i$"},
        {"difficulty": "中档", "q": "计算 $\\frac{1+i}{1-i}$。", "s": "=$\\frac{(1+i)^2}{1-i^2} = \\frac{2i}{2} = i$。", "a": "$i$"},
        {"difficulty": "进阶", "q": "$|z-i|=1$，求 $|z|$ 的最大值。", "s": "z在以$(0,1)$为圆心半径1的圆上。$|z|_{max}=1+1=2$。", "a": "$2$"}
    ],
    "traps": ["$i^2=-1$，$(-i)^2=-1$，两者不同", "共轭复数的乘积是实数：$(a+bi)(a-bi)=a^2+b^2$", "$|z|$ 是实数，$\\bar{z}$ 是复数"],
    "connections": "复数 → 复平面 → 复数的三角表示 → 棣莫弗定理 → 欧拉公式 $e^{i\\theta}=\\cos\\theta+i\\sin\\theta$。",
    "practice_hint": "分母有$i$→同乘共轭。$i^n$周期为4。$|z-z_0|$ 表示距离。"
},

}
