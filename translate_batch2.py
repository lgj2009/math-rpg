#!/usr/bin/env python3
"""
Translate Chinese math questions IDs 66-95 to English and Vietnamese.
Keeps all LaTeX EXACTLY as-is. Only translates natural language.
"""
import sqlite3
import json

DB_PATH = 'd:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

def escape_latex(s):
    """Escape backslashes and quotes for Python string."""
    return s

def t(tmpl):
    """Return raw template string."""
    return tmpl

# Build translations
T = {}

T[66] = {
    "content_en": "In the regular triangular prism $ABC-A_1B_1C_1$, $AB=AA_1=1$, point $P$ satisfies $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, where $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$, then",
    "content_vi": "Trong l\u0103ng tr\u1ee5 tam gi\u00e1c \u0111\u1ec1u $ABC-A_1B_1C_1$, $AB=AA_1=1$, \u0111i\u1ec3m $P$ th\u1ecfa m\u00e3n $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, v\u1edbi $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$, khi \u0111\u00f3",
    "options_en": json.dumps(["A. When $\\lambda=1$, the perimeter of $\\triangle AB_1P$ is constant", "B. When $\\mu=1$, the volume of tetrahedron $P-A_1BC$ is constant", "C. When $\\lambda=\\frac{1}{2}$, there is exactly one point P such that $A_1P\\perp BP$", "D. When $\\mu=\\frac{1}{2}$, there is exactly one point P such that $A_1B\\perp$ plane $AB_1P$"]),
    "options_vi": json.dumps(["A. Khi $\\lambda=1$, chu vi $\\triangle AB_1P$ kh\u00f4ng \u0111\u1ed5i", "B. Khi $\\mu=1$, th\u1ec3 t\u00edch t\u1ee9 di\u1ec7n $P-A_1BC$ kh\u00f4ng \u0111\u1ed5i", "C. Khi $\\lambda=\\frac{1}{2}$, c\u00f3 \u0111\u00fang m\u1ed9t \u0111i\u1ec3m P sao cho $A_1P\\perp BP$", "D. Khi $\\mu=\\frac{1}{2}$, c\u00f3 \u0111\u00fang m\u1ed9t \u0111i\u1ec3m P sao cho $A_1B\\perp$ m\u1eb7t ph\u1eb3ng $AB_1P$"]),
    "answer_en": "B",
    "answer_vi": "B",
    "solution_en": "When $\\mu=1$, $P$ moves along $B_1C_1$. The base area and height of tetrahedron $P-A_1BC$ remain unchanged, so its volume is constant.",
    "solution_vi": "Khi $\\mu=1$, $P$ di chuy\u1ec3n tr\u00ean $B_1C_1$. Di\u1ec7n t\u00edch \u0111\u00e1y v\u00e0 chi\u1ec1u cao c\u1ee7a t\u1ee9 di\u1ec7n $P-A_1BC$ kh\u00f4ng \u0111\u1ed5i, n\u00ean th\u1ec3 t\u00edch kh\u00f4ng \u0111\u1ed5i.",
}

T[67] = {
    "content_en": "When studying folk paper-cutting, students found paper is often folded along a symmetry axis. A $20dm\\times 12dm$ rectangular paper: after 1 fold, 2 types: $10dm\\times 12dm$ and $20dm\\times 6dm$, total area $S_1=240dm^2$. After 2 folds: 3 types: $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$, total area $S_2=180dm^2$, etc. After 4 folds, number of types is ____; after $n$ folds, $\\sum_{k=1}^{n} S_k =$ ____ $dm^2$.",
    "content_vi": "Khi nghi\u00ean c\u1ee9u ngh\u1ec7 thu\u1eadt c\u1eaft gi\u1ea5y d\u00e2n gian, ng\u01b0\u1eddi ta th\u1ea5y th\u01b0\u1eddng g\u1ea5p gi\u1ea5y theo tr\u1ee5c \u0111\u1ed1i x\u1ee9ng. Gi\u1ea5y h\u00ecnh ch\u1eef nh\u1eadt $20dm\\times 12dm$: g\u1ea5p 1 l\u1ea7n \u0111\u01b0\u1ee3c 2 lo\u1ea1i: $10dm\\times 12dm$ v\u00e0 $20dm\\times 6dm$, t\u1ed5ng di\u1ec7n t\u00edch $S_1=240dm^2$. G\u1ea5p 2 l\u1ea7n \u0111\u01b0\u1ee3c 3 lo\u1ea1i: $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$, t\u1ed5ng di\u1ec7n t\u00edch $S_2=180dm^2$, v.v. Sau 4 l\u1ea7n g\u1ea5p, s\u1ed1 lo\u1ea1i l\u00e0 ____; sau $n$ l\u1ea7n g\u1ea5p, $\\sum_{k=1}^{n} S_k =$ ____ $dm^2$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "5, 720(1-1/2^n)",
    "answer_vi": "5, 720(1-1/2^n)",
    "solution_en": "After $k$ folds, there are $k+1$ types. $S_k=240\\times k\\times (\\frac{1}{2})^{k-1}$. Summing gives $720(1-\\frac{1}{2^n})$.",
    "solution_vi": "Sau $k$ l\u1ea7n g\u1ea5p c\u00f3 $k+1$ lo\u1ea1i. $S_k=240\\times k\\times (\\frac{1}{2})^{k-1}$. T\u00ednh t\u1ed5ng \u0111\u01b0\u1ee3c $720(1-\\frac{1}{2^n})$.",
}

T[68] = {
    "content_en": "Let the sides opposite interior angles $A,B,C$ of $\\triangle ABC$ be $a,b,c$ respectively. Given $b^2=ac$, point $D$ is on side $AC$, $BD\\sin\\angle ABC=a\\sin C$. (1) Prove: $BD=b$; (2) If $AD=2DC$, find $\\cos\\angle ABC$.",
    "content_vi": "G\u1ecdi c\u00e1c c\u1ea1nh \u0111\u1ed1i di\u1ec7n v\u1edbi g\u00f3c $A,B,C$ c\u1ee7a $\\triangle ABC$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 $a,b,c$. Cho $b^2=ac$, \u0111i\u1ec3m $D$ n\u1eb1m tr\u00ean c\u1ea1nh $AC$, $BD\\sin\\angle ABC=a\\sin C$. (1) Ch\u1ee9ng minh: $BD=b$; (2) N\u1ebfu $AD=2DC$, t\u00ecm $\\cos\\angle ABC$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "Proof provided, $\\cos\\angle ABC=7/12$",
    "answer_vi": "\u0110\u00e3 ch\u1ee9ng minh, $\\cos\\angle ABC=7/12$",
    "solution_en": "(1) By the law of sines $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, combined with the given condition, we prove $BD=b$. (2) By the law of cosines, $\\cos\\angle ABC=\\frac{7}{12}$.",
    "solution_vi": "(1) Theo \u0111\u1ecbnh l\u00fd sin $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, k\u1ebft h\u1ee3p \u0111i\u1ec1u ki\u1ec7n, ch\u1ee9ng minh \u0111\u01b0\u1ee3c $BD=b$. (2) Theo \u0111\u1ecbnh l\u00fd cos, $\\cos\\angle ABC=\\frac{7}{12}$.",
}

T[69] = {
    "content_en": "5 Beijing Winter Olympic volunteers are assigned to 4 events: figure skating, short track speed skating, ice hockey, curling. Each to exactly one event, each event has at least one. How many different assignment schemes?",
    "content_vi": "5 t\u00ecnh nguy\u1ec7n vi\u00ean Olympic m\u00f9a \u0111\u00f4ng B\u1eafc Kinh \u0111\u01b0\u1ee3c ph\u00e2n c\u00f4ng v\u00e0o 4 m\u00f4n: tr\u01b0\u1ee3t b\u0103ng ngh\u1ec7 thu\u1eadt, tr\u01b0\u1ee3t b\u0103ng t\u1ed1c \u0111\u1ed9 c\u1ef1 ly ng\u1eafn, kh\u00fac c\u00f4n c\u1ea7u tr\u00ean b\u0103ng, bi \u0111\u00e1 tr\u00ean b\u0103ng. M\u1ed7i ng\u01b0\u1eddi v\u00e0o \u0111\u00fang 1 m\u00f4n, m\u1ed7i m\u00f4n c\u00f3 \u00edt nh\u1ea5t 1 ng\u01b0\u1eddi. C\u00f3 bao nhi\u00eau c\u00e1ch ph\u00e2n c\u00f4ng?",
    "options_en": json.dumps(["A. 60", "B. 120", "C. 240", "D. 480"]),
    "options_vi": json.dumps(["A. 60", "B. 120", "C. 240", "D. 480"]),
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "First group then assign. 5 into 4 groups (one group has 2): choose 2 for the pair $C_5^2=10$ ways, rest alone. Permute 4 groups: $4!=24$. Total $10\\times 24=240$.",
    "solution_vi": "Nh\u00f3m tr\u01b0\u1edbc r\u1ed3i ph\u00e2n. 5 ng\u01b0\u1eddi v\u00e0o 4 nh\u00f3m (m\u1ed9t nh\u00f3m 2 ng\u01b0\u1eddi): ch\u1ecdn 2 ng\u01b0\u1eddi cho c\u1eb7p $C_5^2=10$ c\u00e1ch, c\u00f2n l\u1ea1i m\u1ed7i ng\u01b0\u1eddi m\u1ed9t nh\u00f3m. Ho\u00e1n v\u1ecb 4 nh\u00f3m: $4!=24$. T\u1ed5ng $10\\times 24=240$.",
}

T[70] = {
    "content_en": "6 students go to 3 venues A, B, C as volunteers. Each goes to exactly one venue. A has 1 student, B has 2, C has 3. How many different assignments?",
    "content_vi": "6 h\u1ecdc sinh \u0111\u1ebfn 3 \u0111\u1ecba \u0111i\u1ec3m A, B, C l\u00e0m t\u00ecnh nguy\u1ec7n vi\u00ean. M\u1ed7i h\u1ecdc sinh ch\u1ec9 \u0111\u1ebfn 1 \u0111\u1ecba \u0111i\u1ec3m. A c\u00f3 1 h\u1ecdc sinh, B c\u00f3 2, C c\u00f3 3. C\u00f3 bao nhi\u00eau c\u00e1ch ph\u00e2n c\u00f4ng?",
    "options_en": json.dumps(["A. 120", "B. 90", "C. 60", "D. 30"]),
    "options_vi": json.dumps(["A. 120", "B. 90", "C. 60", "D. 30"]),
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times 10\\times 1 = 60$.",
    "solution_vi": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times 10\\times 1 = 60$.",
}

T[71] = {
    "content_en": "Among students at a middle school, 96% like football or swimming, 60% like football, 82% like swimming. The percentage who like both is",
    "content_vi": "Trong s\u1ed1 h\u1ecdc sinh c\u1ee7a m\u1ed9t tr\u01b0\u1eddng THCS, 96% th\u00edch b\u00f3ng \u0111\u00e1 ho\u1eb7c b\u01a1i, 60% th\u00edch b\u00f3ng \u0111\u00e1, 82% th\u00edch b\u01a1i. T\u1ef7 l\u1ec7 th\u00edch c\u1ea3 hai l\u00e0",
    "options_en": json.dumps(["A. 62%", "B. 56%", "C. 46%", "D. 42%"]),
    "options_vi": json.dumps(["A. 62%", "B. 56%", "C. 46%", "D. 42%"]),
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "Inclusion-exclusion: $P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, so $P(F\\cap S)=46\\%$.",
    "solution_vi": "Nguy\u00ean l\u00fd b\u00f9 tr\u1eeb: $P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, suy ra $P(F\\cap S)=46\\%$.",
}

T[72] = {
    "content_en": "Given ellipse $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ with eccentricity $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ are the left and right foci, $A$ is the upper vertex, and $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$, then the equation of $C$ is ____",
    "content_vi": "Cho elip $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ c\u00f3 t\u00e2m sai $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 ti\u00eau \u0111i\u1ec3m tr\u00e1i v\u00e0 ph\u1ea3i, $A$ l\u00e0 \u0111\u1ec9nh tr\u00ean, v\u00e0 $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$, khi \u0111\u00f3 ph\u01b0\u01a1ng tr\u00ecnh c\u1ee7a $C$ l\u00e0 ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$x^2/4+y^2=1$",
    "answer_vi": "$x^2/4+y^2=1$",
    "solution_en": "$e=\\frac{c}{a}=\\frac{\\sqrt{3}}{2}$. Let $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_1(-\\sqrt{3}k,0),F_2(\\sqrt{3}k,0)$. Dot product $=-3k^2+k^2=-2k^2=-1$, $k=1$. So $a=2,b=1$.",
    "solution_vi": "$e=\\frac{c}{a}=\\frac{\\sqrt{3}}{2}$. \u0110\u1eb7t $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_1(-\\sqrt{3}k,0),F_2(\\sqrt{3}k,0)$. T\u00edch v\u00f4 h\u01b0\u1edbng $=-3k^2+k^2=-2k^2=-1$, $k=1$. V\u1eady $a=2,b=1$.",
}

T[73] = {
    "content_en": "In $\\triangle ABC$, sides opposite $A,B,C$ are $a,b,c$. Given $a=3$, $c=\\sqrt{2}$, $B=45\\degree$. (1) Find $\\sin C$; (2) Point $D$ on $BC$ with $\\cos\\angle ADC = -\\frac{4}{5}$, find $\\tan\\angle DAC$.",
    "content_vi": "Trong $\\triangle ABC$, c\u1ea1nh \u0111\u1ed1i di\u1ec7n $A,B,C$ l\u00e0 $a,b,c$. Cho $a=3$, $c=\\sqrt{2}$, $B=45\\degree$. (1) T\u00ecm $\\sin C$; (2) \u0110i\u1ec3m $D$ tr\u00ean $BC$ v\u1edbi $\\cos\\angle ADC = -\\frac{4}{5}$, t\u00ecm $\\tan\\angle DAC$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$\\sin C=1/3$, $\\tan\\angle DAC=2/11$",
    "answer_vi": "$\\sin C=1/3$, $\\tan\\angle DAC=2/11$",
    "solution_en": "(1) Law of cosines: $b^2=9+2-6\\sqrt{2}\\cdot\\frac{\\sqrt{2}}{2}=5$, $b=\\sqrt{5}$. Law of sines: $\\sin C=\\frac{c\\sin B}{b}=\\frac{1}{3}$.",
    "solution_vi": "(1) \u0110\u1ecbnh l\u00fd cos: $b^2=9+2-6\\sqrt{2}\\cdot\\frac{\\sqrt{2}}{2}=5$, $b=\\sqrt{5}$. \u0110\u1ecbnh l\u00fd sin: $\\sin C=\\frac{c\\sin B}{b}=\\frac{1}{3}$.",
}

T[74] = {
    "content_en": "Let $S_n$ be sum of first $n$ terms of arithmetic sequence $\\{a_n\\}$. If $a_1\\neq 0$, $a_2=3a_1$, then $\\frac{S_{10}}{S_5}=$ ____",
    "content_vi": "G\u1ecdi $S_n$ l\u00e0 t\u1ed5ng $n$ s\u1ed1 h\u1ea1ng \u0111\u1ea7u c\u1ee7a c\u1ea5p s\u1ed1 c\u1ed9ng $\\{a_n\\}$. N\u1ebfu $a_1\\neq 0$, $a_2=3a_1$, th\u00ec $\\frac{S_{10}}{S_5}=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "4",
    "answer_vi": "4",
    "solution_en": "From $a_2=a_1+d=3a_1$, $d=2a_1$. $S_n=na_1+\\frac{n(n-1)}{2}d=n^2a_1$. $\\frac{S_{10}}{S_5}=\\frac{100}{25}=4$.",
    "solution_vi": "T\u1eeb $a_2=a_1+d=3a_1$, $d=2a_1$. $S_n=na_1+\\frac{n(n-1)}{2}d=n^2a_1$. $\\frac{S_{10}}{S_5}=\\frac{100}{25}=4$.",
}

T[75] = {
    "content_en": "Teams A and B play a best-of-7 basketball final. A's home/away arrangement: H-H-A-A-H-A-H. Home win prob 0.6, away win prob 0.5. Games independent. Probability A wins 4:1 is ____",
    "content_vi": "\u0110\u1ed9i A v\u00e0 B ch\u01a1i chung k\u1ebft b\u00f3ng r\u1ed5 th\u1ec3 th\u1ee9c th\u1eafng 4/7 tr\u1eadn. L\u1ecbch s\u00e2n nh\u00e0/s\u00e2n kh\u00e1ch c\u1ee7a A: N-N-K-K-N-K-N. X\u00e1c su\u1ea5t th\u1eafng s\u00e2n nh\u00e0 0.6, s\u00e2n kh\u00e1ch 0.5. C\u00e1c tr\u1eadn \u0111\u1ea5u \u0111\u1ed9c l\u1eadp. X\u00e1c su\u1ea5t A th\u1eafng 4:1 l\u00e0 ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "0.18",
    "answer_vi": "0.18",
    "solution_en": "A winning 4:1 means winning game 5 and winning 3 of the first 4 games. Sum probabilities over all arrangements considering home/away assignment.",
    "solution_vi": "A th\u1eafng 4:1 ngh\u0129a l\u00e0 th\u1eafng tr\u1eadn th\u1ee9 5 v\u00e0 th\u1eafng 3 trong 4 tr\u1eadn \u0111\u1ea7u. T\u00ednh t\u1ed5ng x\u00e1c su\u1ea5t cho t\u1ea5t c\u1ea3 c\u00e1c c\u00e1ch s\u1eafp x\u1ebfp x\u00e9t l\u1ecbch s\u00e2n nh\u00e0/s\u00e2n kh\u00e1ch.",
}

T[76] = {
    "content_en": "In $\\triangle ABC$, sides opposite $A,B,C$ are $a,b,c$. Let $(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C$. (1) Find $A$; (2) If $\\sqrt{2}a+b=2c$, find $\\sin C$.",
    "content_vi": "Trong $\\triangle ABC$, c\u1ea1nh \u0111\u1ed1i di\u1ec7n $A,B,C$ l\u00e0 $a,b,c$. Cho $(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C$. (1) T\u00ecm $A$; (2) N\u1ebfu $\\sqrt{2}a+b=2c$, t\u00ecm $\\sin C$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$A=60\\degree$, $\\sin C=(\\sqrt{6}+\\sqrt{2})/4$",
    "answer_vi": "$A=60\\degree$, $\\sin C=(\\sqrt{6}+\\sqrt{2})/4$",
    "solution_en": "(1) Expand and use law of sines then law of cosines gives $A=60\\degree$. (2) Use the condition $\\sqrt{2}a+b=2c$ to find $\\sin C$.",
    "solution_vi": "(1) Khai tri\u1ec3n, d\u00f9ng \u0111\u1ecbnh l\u00fd sin r\u1ed3i \u0111\u1ecbnh l\u00fd cos \u0111\u01b0\u1ee3c $A=60\\degree$. (2) D\u00f9ng \u0111i\u1ec1u ki\u1ec7n $\\sqrt{2}a+b=2c$ \u0111\u1ec3 t\u00ecm $\\sin C$.",
}

T[77] = {
    "content_en": "Given $\\vec{AB}=(2,3)$, $\\vec{AC}=(3,t)$, $|\\vec{BC}|=1$, then $\\vec{AB}\\cdot\\vec{BC}=$",
    "content_vi": "Cho $\\vec{AB}=(2,3)$, $\\vec{AC}=(3,t)$, $|\\vec{BC}|=1$, khi \u0111\u00f3 $\\vec{AB}\\cdot\\vec{BC}=$",
    "options_en": json.dumps(["A. -3", "B. -2", "C. 2", "D. 3"]),
    "options_vi": json.dumps(["A. -3", "B. -2", "C. 2", "D. 3"]),
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "$\\vec{BC}=\\vec{AC}-\\vec{AB}=(1,t-3)$. $|\\vec{BC}|^2=1+(t-3)^2=1$, so $t=3$. $\\vec{BC}=(1,0)$, $\\vec{AB}\\cdot\\vec{BC}=2$.",
    "solution_vi": "$\\vec{BC}=\\vec{AC}-\\vec{AB}=(1,t-3)$. $|\\vec{BC}|^2=1+(t-3)^2=1$, suy ra $t=3$. $\\vec{BC}=(1,0)$, $\\vec{AB}\\cdot\\vec{BC}=2$.",
}

T[78] = {
    "content_en": "Let $f(x)=\\ln|2x+1|-\\ln|2x-1|$, then $f(x)$",
    "content_vi": "Cho h\u00e0m s\u1ed1 $f(x)=\\ln|2x+1|-\\ln|2x-1|$, khi \u0111\u00f3 $f(x)$",
    "options_en": json.dumps(["A. is even and increasing on $(\\frac{1}{2},+\\infty)$", "B. is odd and decreasing on $(-\\frac{1}{2},\\frac{1}{2})$", "C. is even and increasing on $(-\\infty,-\\frac{1}{2})$", "D. is odd and decreasing on $(-\\infty,-\\frac{1}{2})$"]),
    "options_vi": json.dumps(["A. l\u00e0 h\u00e0m ch\u1eb5n v\u00e0 \u0111\u1ed3ng bi\u1ebfn tr\u00ean $(\\frac{1}{2},+\\infty)$", "B. l\u00e0 h\u00e0m l\u1ebb v\u00e0 ngh\u1ecbch bi\u1ebfn tr\u00ean $(-\\frac{1}{2},\\frac{1}{2})$", "C. l\u00e0 h\u00e0m ch\u1eb5n v\u00e0 \u0111\u1ed3ng bi\u1ebfn tr\u00ean $(-\\infty,-\\frac{1}{2})$", "D. l\u00e0 h\u00e0m l\u1ebb v\u00e0 ngh\u1ecbch bi\u1ebfn tr\u00ean $(-\\infty,-\\frac{1}{2})$"]),
    "answer_en": "D",
    "answer_vi": "D",
    "solution_en": "$f(-x)=\\ln|-2x+1|-\\ln|-2x-1|=\\ln|2x-1|-\\ln|2x+1|=-f(x)$, so it is odd. For $x<-\\frac{1}{2}$, $f'(x)<0$, hence decreasing.",
    "solution_vi": "$f(-x)=\\ln|-2x+1|-\\ln|-2x-1|=\\ln|2x-1|-\\ln|2x+1|=-f(x)$, n\u00ean l\u00e0 h\u00e0m l\u1ebb. V\u1edbi $x<-\\frac{1}{2}$, $f'(x)<0$, do \u0111\u00f3 ngh\u1ecbch bi\u1ebfn.",
}

T[79] = {
    "content_en": "The constant term in the expansion of $(x+\\frac{1}{x})^6$ is ____",
    "content_vi": "S\u1ed1 h\u1ea1ng kh\u00f4ng \u0111\u1ed5i trong khai tri\u1ec3n c\u1ee7a $(x+\\frac{1}{x})^6$ l\u00e0 ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "20",
    "answer_vi": "20",
    "solution_en": "General term $T_{r+1}=C_6^r x^{6-2r}$. Set $6-2r=0$, get $r=3$. Constant term $C_6^3=20$.",
    "solution_vi": "S\u1ed1 h\u1ea1ng t\u1ed5ng qu\u00e1t $T_{r+1}=C_6^r x^{6-2r}$. Cho $6-2r=0$, \u0111\u01b0\u1ee3c $r=3$. S\u1ed1 h\u1ea1ng kh\u00f4ng \u0111\u1ed5i $C_6^3=20$.",
}

T[80] = {
    "content_en": "Given the tangent line to the curve $y=ae^x+x\\ln x$ at point $(1,ae)$ is $y=2x+b$, then",
    "content_vi": "Cho ti\u1ebfp tuy\u1ebfn c\u1ee7a \u0111\u01b0\u1eddng cong $y=ae^x+x\\ln x$ t\u1ea1i \u0111i\u1ec3m $(1,ae)$ l\u00e0 $y=2x+b$, khi \u0111\u00f3",
    "options_en": json.dumps(["A. a=e,b=-1", "B. a=e,b=1", "C. a=e^{-1},b=1", "D. a=e^{-1},b=-1"]),
    "options_vi": json.dumps(["A. a=e,b=-1", "B. a=e,b=1", "C. a=e^{-1},b=1", "D. a=e^{-1},b=-1"]),
    "answer_en": "D",
    "answer_vi": "D",
    "solution_en": "$y'=ae^x+\\ln x+1$. At $x=1$, slope $=ae+1=2$, so $a=e^{-1}$. Tangent $y=2x+b$ passes through $(1,1)$, so $b=-1$.",
    "solution_vi": "$y'=ae^x+\\ln x+1$. T\u1ea1i $x=1$, h\u1ec7 s\u1ed1 g\u00f3c $=ae+1=2$, suy ra $a=e^{-1}$. Ti\u1ebfp tuy\u1ebfn $y=2x+b$ \u0111i qua $(1,1)$, n\u00ean $b=-1$.",
}

T[81] = {
    "content_en": "To study the residue levels of two types of ions in mice, 200 mice were randomly divided into groups A and B (100 each). Group A received ion A solution, group B received ion B solution. The mean residual percentage for group A is 5.2, for group B is 4.8. If the residual percentage of ion A follows $N(\\mu_1,\\sigma_1^2)$, find $P(|X-\\mu|<\\sigma)$.",
    "content_vi": "\u0110\u1ec3 nghi\u00ean c\u1ee9u m\u1ee9c \u0111\u1ed9 t\u1ed3n d\u01b0 c\u1ee7a hai lo\u1ea1i ion trong chu\u1ed9t, 200 con chu\u1ed9t \u0111\u01b0\u1ee3c chia ng\u1eabu nhi\u00ean th\u00e0nh nh\u00f3m A v\u00e0 B (m\u1ed7i nh\u00f3m 100 con). Nh\u00f3m A \u0111\u01b0\u1ee3c cho dung d\u1ecbch ion A, nh\u00f3m B \u0111\u01b0\u1ee3c cho dung d\u1ecbch ion B. Gi\u00e1 tr\u1ecb trung b\u00ecnh ph\u1ea7n tr\u0103m t\u1ed3n d\u01b0 c\u1ee7a nh\u00f3m A l\u00e0 5,2, nh\u00f3m B l\u00e0 4,8. N\u1ebfu ph\u1ea7n tr\u0103m t\u1ed3n d\u01b0 c\u1ee7a ion A tu\u00e2n theo $N(\\mu_1,\\sigma_1^2)$, t\u00ecm $P(|X-\\mu|<\\sigma)$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "0.68",
    "answer_vi": "0.68",
    "solution_en": "$P(|X-\\mu|<\\sigma) \\approx 0.6827$.",
    "solution_vi": "$P(|X-\\mu|<\\sigma) \\approx 0.6827$.",
}

T[82] = {
    "content_en": "Factory produces types A and B. Defective rate: A=5%, B=3%. Random pick: P(A)=0.6, P(B)=0.4. (1) Find P(defective); (2) If defective, find P(A|defective).",
    "content_vi": "Nh\u00e0 m\u00e1y s\u1ea3n xu\u1ea5t hai lo\u1ea1i A v\u00e0 B. T\u1ef7 l\u1ec7 ph\u1ebf ph\u1ea9m: A=5%, B=3%. Ch\u1ecdn ng\u1eabu nhi\u00ean: P(A)=0.6, P(B)=0.4. (1) T\u00ecm P(ph\u1ebf ph\u1ea9m); (2) N\u1ebfu l\u00e0 ph\u1ebf ph\u1ea9m, t\u00ecm P(A|ph\u1ebf ph\u1ea9m).",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1) 0.042 (2) 5/7",
    "answer_vi": "(1) 0.042 (2) 5/7",
    "solution_en": "(1) Law of total probability: $P(\\text{defective})=0.6\\times0.05+0.4\\times0.03=0.042$. (2) Bayes' theorem: $P(A|\\text{defective})=\\frac{0.6\\times0.05}{0.042}=\\frac{5}{7}$.",
    "solution_vi": "(1) C\u00f4ng th\u1ee9c x\u00e1c su\u1ea5t to\u00e0n ph\u1ea7n: $P(\\text{ph\u1ebf ph\u1ea9m})=0.6\\times0.05+0.4\\times0.03=0.042$. (2) \u0110\u1ecbnh l\u00fd Bayes: $P(A|\\text{ph\u1ebf ph\u1ea9m})=\\frac{0.6\\times0.05}{0.042}=\\frac{5}{7}$.",
}

T[83] = {
    "content_en": "A company produces a product. Daily fixed cost 2000 yuan, variable cost 30 yuan/unit. Daily output $x$ units, unit price $p=100-0.01x$ yuan. Find: (1) optimal output for maximum profit; (2) maximum profit.",
    "content_vi": "M\u1ed9t doanh nghi\u1ec7p s\u1ea3n xu\u1ea5t m\u1ed9t lo\u1ea1i s\u1ea3n ph\u1ea9m. Chi ph\u00ed c\u1ed1 \u0111\u1ecbnh h\u00e0ng ng\u00e0y 2000 \u0111\u1ed3ng, chi ph\u00ed bi\u1ebfn \u0111\u1ed5i 30 \u0111\u1ed3ng/\u0111\u01a1n v\u1ecb. S\u1ea3n l\u01b0\u1ee3ng h\u00e0ng ng\u00e0y $x$ \u0111\u01a1n v\u1ecb, \u0111\u01a1n gi\u00e1 $p=100-0.01x$ \u0111\u1ed3ng. T\u00ecm: (1) s\u1ea3n l\u01b0\u1ee3ng t\u1ed1i \u01b0u \u0111\u1ec3 l\u1ee3i nhu\u1eadn t\u1ed1i \u0111a; (2) l\u1ee3i nhu\u1eadn t\u1ed1i \u0111a.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1) 3500 units (2) 120500 yuan",
    "answer_vi": "(1) 3500 \u0111\u01a1n v\u1ecb (2) 120500 \u0111\u1ed3ng",
    "solution_en": "Revenue $R(x)=x(100-0.01x)=100x-0.01x^2$. Cost $C(x)=2000+30x$. Profit $L(x)=70x-0.01x^2-2000$. $L'(x)=70-0.02x=0$, $x=3500$. $L(3500)=70\\times3500-0.01\\times12250000-2000=120500$.",
    "solution_vi": "Doanh thu $R(x)=x(100-0.01x)=100x-0.01x^2$. Chi ph\u00ed $C(x)=2000+30x$. L\u1ee3i nhu\u1eadn $L(x)=70x-0.01x^2-2000$. $L'(x)=70-0.02x=0$, $x=3500$. $L(3500)=70\\times3500-0.01\\times12250000-2000=120500$.",
}

T[84] = {
    "content_en": "A city's population at the start of 2020 is 1 million, annual growth rate 3%. The city plans to build 50,000 sq m of housing annually. Per capita housing area at start of 2020 is 20 sq m. (1) Find population at start of 2030 (in 10,000s); (2) Find annual housing construction needed (in 10,000 sq m). (Given: $1.03^{10}\\approx1.344$)",
    "content_vi": "D\u00e2n s\u1ed1 c\u1ee7a m\u1ed9t th\u00e0nh ph\u1ed1 \u0111\u1ea7u n\u0103m 2020 l\u00e0 1 tri\u1ec7u ng\u01b0\u1eddi, t\u1ef7 l\u1ec7 t\u0103ng d\u00e2n s\u1ed1 h\u00e0ng n\u0103m 3%. Th\u00e0nh ph\u1ed1 d\u1ef1 \u0111\u1ecbnh x\u00e2y 50.000 m\u00e9t vu\u00f4ng nh\u00e0 \u1edf m\u1ed7i n\u0103m. Di\u1ec7n t\u00edch nh\u00e0 \u1edf b\u00ecnh qu\u00e2n \u0111\u1ea7u n\u0103m 2020 l\u00e0 20 m\u00e9t vu\u00f4ng/ng\u01b0\u1eddi. (1) T\u00ecm d\u00e2n s\u1ed1 \u0111\u1ea7u n\u0103m 2030 (\u0111\u01a1n v\u1ecb: v\u1ea1n); (2) T\u00ednh l\u01b0\u1ee3ng nh\u00e0 \u1edf c\u1ea7n x\u00e2y h\u00e0ng n\u0103m (\u0111\u01a1n v\u1ecb: v\u1ea1n m\u00e9t vu\u00f4ng). (Cho: $1.03^{10}\\approx1.344$)",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1) 1.34 million (2) 67,200 sq m",
    "answer_vi": "(1) 134 v\u1ea1n (2) 6.72 v\u1ea1n m\u00e9t vu\u00f4ng",
    "solution_en": "(1) $P_{10}=100\\times1.03^{10}=134.4\\approx134$ (10,000s). (2) Additional housing needed: $34\\times20=680$ (10,000 sq m). Considering per capita unchanged: annual increment needed is about 67,200 sq m.",
    "solution_vi": "(1) $P_{10}=100\\times1.03^{10}=134.4\\approx134$ v\u1ea1n. (2) Nhu c\u1ea7u nh\u00e0 \u1edf t\u0103ng th\u00eam: $34\\times20=680$ v\u1ea1n m\u00e9t vu\u00f4ng. X\u00e9t di\u1ec7n t\u00edch b\u00ecnh qu\u00e2n kh\u00f4ng \u0111\u1ed5i, nhu c\u1ea7u h\u00e0ng n\u0103m kho\u1ea3ng 6.72 v\u1ea1n m\u00e9t vu\u00f4ng.",
}

T[85] = {
    "content_en": "A farm plans to build a greenhouse with rectangular base 20m x 10m. The roof is a slanted rectangular plane. Highest point 4m above ground, lowest 2m. Find the roof area.",
    "content_vi": "M\u1ed9t trang tr\u1ea1i d\u1ef1 \u0111\u1ecbnh x\u00e2y nh\u00e0 k\u00ednh c\u00f3 \u0111\u00e1y h\u00ecnh ch\u1eef nh\u1eadt 20m x 10m. M\u00e1i nh\u00e0 l\u00e0 m\u1eb7t ph\u1eb3ng h\u00ecnh ch\u1eef nh\u1eadt nghi\u00eang. \u0110i\u1ec3m cao nh\u1ea5t c\u00e1ch m\u1eb7t \u0111\u1ea5t 4m, th\u1ea5p nh\u1ea5t 2m. T\u00ednh di\u1ec7n t\u00edch m\u00e1i nh\u00e0.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$20\\sqrt{105}\\approx 205$ m\u00b2",
    "answer_vi": "$20\\sqrt{105}\\approx 205$ m\u00b2",
    "solution_en": "Four roof vertices: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\\vec{u}=(20,0,2)$, $\\vec{v}=(0,10,2)$. $\\vec{u}\\times\\vec{v}=(-20,-40,200)$. Area $=|\\vec{u}\\times\\vec{v}|=20\\sqrt{105}\\approx205$ m\u00b2.",
    "solution_vi": "B\u1ed1n \u0111\u1ec9nh m\u00e1i: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\\vec{u}=(20,0,2)$, $\\vec{v}=(0,10,2)$. $\\vec{u}\\times\\vec{v}=(-20,-40,200)$. Di\u1ec7n t\u00edch $=|\\vec{u}\\times\\vec{v}|=20\\sqrt{105}\\approx205$ m\u00b2.",
}

T[86] = {
    "content_en": "To learn about citizens' awareness of garbage classification policy, 200 citizens were surveyed: 18-30: 60/80 know; 31-50: 50/70 know; 51+: 25/50 know. (1) 95% confidence awareness relates to age? (2) Random 3 citizens, $X$ = #who know. Find $E(X)$.",
    "content_vi": "\u0110\u1ec3 t\u00ecm hi\u1ec3u m\u1ee9c \u0111\u1ed9 nh\u1eadn bi\u1ebft c\u1ee7a ng\u01b0\u1eddi d\u00e2n v\u1ec1 ch\u00ednh s\u00e1ch ph\u00e2n lo\u1ea1i r\u00e1c, 200 ng\u01b0\u1eddi d\u00e2n \u0111\u01b0\u1ee3c kh\u1ea3o s\u00e1t: 18-30: 60/80 bi\u1ebft; 31-50: 50/70 bi\u1ebft; 51+: 25/50 bi\u1ebft. (1) C\u00f3 95% tin c\u1eady r\u1eb1ng nh\u1eadn bi\u1ebft li\u00ean quan \u0111\u1ebfn tu\u1ed5i? (2) Ch\u1ecdn ng\u1eabu nhi\u00ean 3 ng\u01b0\u1eddi d\u00e2n, $X$ = s\u1ed1 ng\u01b0\u1eddi bi\u1ebft. T\u00ecm $E(X)$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1) Yes (2) 2.025",
    "answer_vi": "(1) C\u00f3 (2) 2.025",
    "solution_en": "(1) Chi-square test: $\\chi^2\\approx7.8>3.841$, significant. (2) Overall awareness rate $p=135/200=0.675$, $E(X)=np=3\\times0.675=2.025$.",
    "solution_vi": "(1) Ki\u1ec3m \u0111\u1ecbnh Chi-square: $\\chi^2\\approx7.8>3.841$, kh\u00e1c bi\u1ec7t c\u00f3 \u00fd ngh\u0129a. (2) T\u1ef7 l\u1ec7 nh\u1eadn bi\u1ebft chung $p=135/200=0.675$, $E(X)=np=3\\times0.675=2.025$.",
}

T[87] = {
    "content_en": "A park plans to build a parabolic arch bridge. Span 40m, highest point 10m above water. (1) Find parabolic equation; (2) Boat mast 8m above water, boat 6m wide (symmetric about y-axis). Can it pass safely?",
    "content_vi": "M\u1ed9t c\u00f4ng vi\u00ean d\u1ef1 \u0111\u1ecbnh x\u00e2y c\u1ea7u v\u00f2m h\u00ecnh parabol. Nh\u1ecbp c\u1ea7u 40m, \u0111i\u1ec3m cao nh\u1ea5t c\u00e1ch m\u1eb7t n\u01b0\u1edbc 10m. (1) T\u00ecm ph\u01b0\u01a1ng tr\u00ecnh parabol; (2) Thuy\u1ec1n c\u00f3 c\u1ed9t bu\u1ed3m cao 8m tr\u00ean m\u1eb7t n\u01b0\u1edbc, r\u1ed9ng 6m (\u0111\u1ed1i x\u1ee9ng qua tr\u1ee5c y). Thuy\u1ec1n c\u00f3 th\u1ec3 \u0111i qua an to\u00e0n kh\u00f4ng?",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1) $y=10-x^2/40$ (2) Yes",
    "answer_vi": "(1) $y=10-x^2/40$ (2) \u0110\u01b0\u1ee3c",
    "solution_en": "(1) Let $y=a(x-20)(x+20)$. Highest point $(0,10)$ gives $a=-\\frac{1}{40}$, so $y=10-\\frac{x^2}{40}$. (2) Boat 6m wide centered: $x=\\pm3$ gives $y=10-\\frac{9}{40}=9.775>8$, safe.",
    "solution_vi": "(1) \u0110\u1eb7t $y=a(x-20)(x+20)$. \u0110i\u1ec3m cao nh\u1ea5t $(0,10)$ suy ra $a=-\\frac{1}{40}$, v\u1eady $y=10-\\frac{x^2}{40}$. (2) Thuy\u1ec1n r\u1ed9ng 6m: $x=\\pm3$ cho $y=10-\\frac{9}{40}=9.775>8$, an to\u00e0n.",
}

T[88] = {
    "content_en": "The value of $\\cos 15\\degree$ is",
    "content_vi": "Gi\u00e1 tr\u1ecb c\u1ee7a $\\cos 15\\degree$ l\u00e0",
    "options_en": json.dumps(["A. \\frac{\\sqrt{6}+\\sqrt{2}}{4}", "B. \\frac{\\sqrt{6}-\\sqrt{2}}{4}", "C. \\frac{\\sqrt{3}+1}{2}", "D. \\frac{\\sqrt{3}-1}{2}"]),
    "options_vi": json.dumps(["A. \\frac{\\sqrt{6}+\\sqrt{2}}{4}", "B. \\frac{\\sqrt{6}-\\sqrt{2}}{4}", "C. \\frac{\\sqrt{3}+1}{2}", "D. \\frac{\\sqrt{3}-1}{2}"]),
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos 15\\degree=\\cos(45\\degree-30\\degree)=\\cos 45\\degree\\cos 30\\degree+\\sin 45\\degree\\sin 30\\degree=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
    "solution_vi": "$\\cos 15\\degree=\\cos(45\\degree-30\\degree)=\\cos 45\\degree\\cos 30\\degree+\\sin 45\\degree\\sin 30\\degree=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
}

T[89] = {
    "content_en": "Given $\\tan\\alpha=2$, $\\tan\\beta=3$, then $\\tan(\\alpha+\\beta)=$ ____",
    "content_vi": "Cho $\\tan\\alpha=2$, $\\tan\\beta=3$, khi \u0111\u00f3 $\\tan(\\alpha+\\beta)=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "-1",
    "answer_vi": "-1",
    "solution_en": "$\\tan(\\alpha+\\beta)=\\frac{\\tan\\alpha+\\tan\\beta}{1-\\tan\\alpha\\tan\\beta}=\\frac{2+3}{1-6}=-1$",
    "solution_vi": "$\\tan(\\alpha+\\beta)=\\frac{\\tan\\alpha+\\tan\\beta}{1-\\tan\\alpha\\tan\\beta}=\\frac{2+3}{1-6}=-1$",
}

T[90] = {
    "content_en": "Given acute angles $\\alpha,\\beta$, $\\cos\\alpha=\\frac{3}{5}$, $\\cos(\\alpha+\\beta)=-\\frac{5}{13}$, then $\\cos\\beta=$",
    "content_vi": "Cho g\u00f3c nh\u1ecdn $\\alpha,\\beta$, $\\cos\\alpha=\\frac{3}{5}$, $\\cos(\\alpha+\\beta)=-\\frac{5}{13}$, khi \u0111\u00f3 $\\cos\\beta=$",
    "options_en": json.dumps(["A. \\frac{56}{65}", "B. \\frac{33}{65}", "C. -\\frac{33}{65}", "D. \\frac{16}{65}"]),
    "options_vi": json.dumps(["A. \\frac{56}{65}", "B. \\frac{33}{65}", "C. -\\frac{33}{65}", "D. \\frac{16}{65}"]),
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\sin\\alpha=\\frac{4}{5}$, $\\sin(\\alpha+\\beta)=\\frac{12}{13}$. $\\cos\\beta=\\cos((\\alpha+\\beta)-\\alpha)=\\cos(\\alpha+\\beta)\\cos\\alpha+\\sin(\\alpha+\\beta)\\sin\\alpha=\\frac{56}{65}$",
    "solution_vi": "$\\sin\\alpha=\\frac{4}{5}$, $\\sin(\\alpha+\\beta)=\\frac{12}{13}$. $\\cos\\beta=\\cos((\\alpha+\\beta)-\\alpha)=\\cos(\\alpha+\\beta)\\cos\\alpha+\\sin(\\alpha+\\beta)\\sin\\alpha=\\frac{56}{65}$",
}

T[91] = {
    "content_en": "Given $\\sin\\alpha+\\cos\\alpha=\\frac{1}{5}$, $\\alpha\\in(0,\\pi)$, then $\\tan\\alpha=$ ____",
    "content_vi": "Cho $\\sin\\alpha+\\cos\\alpha=\\frac{1}{5}$, $\\alpha\\in(0,\\pi)$, khi \u0111\u00f3 $\\tan\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "-4/3",
    "answer_vi": "-4/3",
    "solution_en": "$\\sin\\alpha\\cos\\alpha=-\\frac{12}{25}$. From $(\\sin\\alpha-\\cos\\alpha)^2=\\frac{49}{25}$, $\\sin\\alpha-\\cos\\alpha=\\frac{7}{5}$. Solve: $\\sin\\alpha=\\frac{4}{5}$, $\\cos\\alpha=-\\frac{3}{5}$, $\\tan\\alpha=-\\frac{4}{3}$",
    "solution_vi": "$\\sin\\alpha\\cos\\alpha=-\\frac{12}{25}$. T\u1eeb $(\\sin\\alpha-\\cos\\alpha)^2=\\frac{49}{25}$, $\\sin\\alpha-\\cos\\alpha=\\frac{7}{5}$. Gi\u1ea3i: $\\sin\\alpha=\\frac{4}{5}$, $\\cos\\alpha=-\\frac{3}{5}$, $\\tan\\alpha=-\\frac{4}{3}$",
}

T[92] = {
    "content_en": "Given $\\sin\\alpha=\\frac{\\sqrt{5}}{5}$, $\\sin\\beta=\\frac{\\sqrt{10}}{10}$, $\\alpha,\\beta$ acute, then $\\alpha+\\beta=$",
    "content_vi": "Cho $\\sin\\alpha=\\frac{\\sqrt{5}}{5}$, $\\sin\\beta=\\frac{\\sqrt{10}}{10}$, $\\alpha,\\beta$ nh\u1ecdn, khi \u0111\u00f3 $\\alpha+\\beta=$",
    "options_en": json.dumps(["A. \\frac{\\pi}{4}", "B. \\frac{\\pi}{3}", "C. \\frac{\\pi}{2}", "D. \\frac{2\\pi}{3}"]),
    "options_vi": json.dumps(["A. \\frac{\\pi}{4}", "B. \\frac{\\pi}{3}", "C. \\frac{\\pi}{2}", "D. \\frac{2\\pi}{3}"]),
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos\\alpha=\\frac{2\\sqrt{5}}{5}$, $\\cos\\beta=\\frac{3\\sqrt{10}}{10}$. $\\cos(\\alpha+\\beta)=\\frac{\\sqrt{2}}{2}$, $\\alpha+\\beta\\in(0,\\pi)$, $\\alpha+\\beta=\\frac{\\pi}{4}$",
    "solution_vi": "$\\cos\\alpha=\\frac{2\\sqrt{5}}{5}$, $\\cos\\beta=\\frac{3\\sqrt{10}}{10}$. $\\cos(\\alpha+\\beta)=\\frac{\\sqrt{2}}{2}$, $\\alpha+\\beta\\in(0,\\pi)$, $\\alpha+\\beta=\\frac{\\pi}{4}$",
}

T[93] = {
    "content_en": "Given $\\sin\\alpha=\\frac{4}{5}$, then $\\sin 2\\alpha=$ ____",
    "content_vi": "Cho $\\sin\\alpha=\\frac{4}{5}$, khi \u0111\u00f3 $\\sin 2\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$24/25$ ($\\alpha\\leq 90\\degree$)",
    "answer_vi": "$24/25$ ($\\alpha\\leq 90\\degree$)",
    "solution_en": "$\\cos\\alpha=\\frac{3}{5}$, $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha=\\frac{24}{25}$",
    "solution_vi": "$\\cos\\alpha=\\frac{3}{5}$, $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha=\\frac{24}{25}$",
}

T[94] = {
    "content_en": "Given $\\tan\\alpha=2$, then $\\cos 2\\alpha=$",
    "content_vi": "Cho $\\tan\\alpha=2$, khi \u0111\u00f3 $\\cos 2\\alpha=$",
    "options_en": json.dumps(["A. -\\frac{3}{5}", "B. -\\frac{4}{5}", "C. \\frac{3}{5}", "D. \\frac{4}{5}"]),
    "options_vi": json.dumps(["A. -\\frac{3}{5}", "B. -\\frac{4}{5}", "C. \\frac{3}{5}", "D. \\frac{4}{5}"]),
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos 2\\alpha=\\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}=\\frac{1-4}{1+4}=-\\frac{3}{5}$",
    "solution_vi": "$\\cos 2\\alpha=\\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}=\\frac{1-4}{1+4}=-\\frac{3}{5}$",
}

T[95] = {
    "content_en": "Given $\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{3}{5}$, then $\\sin 2\\alpha=$ ____",
    "content_vi": "Cho $\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{3}{5}$, khi \u0111\u00f3 $\\sin 2\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "$7/25$",
    "answer_vi": "$7/25$",
    "solution_en": "$\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{\\sqrt{2}}{2}(\\sin\\alpha+\\cos\\alpha)=\\frac{3}{5}$, so $\\sin\\alpha+\\cos\\alpha=\\frac{3\\sqrt{2}}{5}$. Square: $1+\\sin 2\\alpha=\\frac{18}{25}$, $\\sin 2\\alpha=\\frac{7}{25}$.",
    "solution_vi": "$\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{\\sqrt{2}}{2}(\\sin\\alpha+\\cos\\alpha)=\\frac{3}{5}$, suy ra $\\sin\\alpha+\\cos\\alpha=\\frac{3\\sqrt{2}}{5}$. B\u00ecnh ph\u01b0\u01a1ng: $1+\\sin 2\\alpha=\\frac{18}{25}$, $\\sin 2\\alpha=\\frac{7}{25}$.",
}


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    sql = '''UPDATE questions SET
        content_en=?, options_en=?, answer_en=?, solution_en=?,
        content_vi=?, options_vi=?, answer_vi=?, solution_vi=?
        WHERE id=?'''

    updated = 0
    for qid in sorted(T.keys()):
        t = T[qid]
        c.execute(sql, (t["content_en"], t["options_en"], t["answer_en"], t["solution_en"],
                         t["content_vi"], t["options_vi"], t["answer_vi"], t["solution_vi"], qid))
        conn.commit()
        updated += 1
        print(f"Updated ID {qid}")

    # Verify
    c.execute("SELECT COUNT(*) FROM questions WHERE content_en IS NULL")
    rem = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM questions WHERE content_en IS NOT NULL")
    done = c.fetchone()[0]
    print(f"\nDone! {updated} questions updated.")
    print(f"Total translated: {done}, remaining untranslated: {rem}")
    conn.close()


if __name__ == "__main__":
    main()
