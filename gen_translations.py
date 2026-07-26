import json

t = {}

t[51] = {
    "content_en": "Given vectors $\\vec{a},\\vec{b}$ satisfy $|\\vec{a}-\\vec{b}|=\\sqrt{3}$, $|\\vec{a}+\\vec{b}|=|2\\vec{a}-\\vec{b}|$, find $|\\vec{b}|=$ ____",
    "content_vi": "Cho vect\u01a1 $\\vec{a},\\vec{b}$ th\u1ecfa m\u00e3n $|\\vec{a}-\\vec{b}|=\\sqrt{3}$, $|\\vec{a}+\\vec{b}|=|2\\vec{a}-\\vec{b}|$, t\u00ecm $|\\vec{b}|=$ ____",
    "options_en": None, "options_vi": None, "answer_en": None, "answer_vi": None,
    "solution_en": "Expanding $|\\vec{a}+\\vec{b}|^2=|2\\vec{a}-\\vec{b}|^2$ and combining with $|\\vec{a}-\\vec{b}|^2=3$, we get $|\\vec{b}|=\\sqrt{3}$.",
    "solution_vi": "Khai tri\u1ec3n $|\\vec{a}+\\vec{b}|^2=|2\\vec{a}-\\vec{b}|^2$ k\u1ebft h\u1ee3p v\u1edbi $|\\vec{a}-\\vec{b}|^2=3$, gi\u1ea3i \u0111\u01b0\u1ee3c $|\\vec{b}|=\\sqrt{3}$."
}
t[52] = {
    "content_en": "In $\\triangle ABC$, point $D$ is on side $AB$ with $BD=2DA$. Let $\\vec{CA}=\\vec{m}$, $\\vec{CD}=\\vec{n}$. Then $\\vec{CB}=$",
    "content_vi": "Trong $\\triangle ABC$, \u0111i\u1ec3m $D$ tr\u00ean c\u1ea1nh $AB$ v\u1edbi $BD=2DA$. \u0110\u1eb7t $\\vec{CA}=\\vec{m}$, $\\vec{CD}=\\vec{n}$. Khi \u0111\u00f3 $\\vec{CB}=$",
    "options_en": '["A. 3\\\\vec{m}-2\\\\vec{n}","B. -2\\\\vec{m}+3\\\\vec{n}","C. 3\\\\vec{m}+2\\\\vec{n}","D. 2\\\\vec{m}+3\\\\vec{n}"]',
    "options_vi": '["A. 3\\\\vec{m}-2\\\\vec{n}","B. -2\\\\vec{m}+3\\\\vec{n}","C. 3\\\\vec{m}+2\\\\vec{n}","D. 2\\\\vec{m}+3\\\\vec{n}"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$\\vec{CB}=\\vec{CA}+\\vec{AB}=\\vec{m}+3\\vec{AD}=\\vec{m}+3(\\vec{n}-\\vec{m})=-2\\vec{m}+3\\vec{n}$.",
    "solution_vi": "$\\vec{CB}=\\vec{CA}+\\vec{AB}=\\vec{m}+3\\vec{AD}=\\vec{m}+3(\\vec{n}-\\vec{m})=-2\\vec{m}+3\\vec{n}$."
}
t[53] = {
    "content_en": "Randomly select 2 different integers from 2 to 8. The probability that they are coprime is",
    "content_vi": "Ch\u1ecdn ng\u1eabu nhi\u00ean 2 s\u1ed1 nguy\u00ean kh\u00e1c nhau t\u1eeb 2 \u0111\u1ebfn 8. X\u00e1c su\u1ea5t ch\u00fang nguy\u00ean t\u1ed1 c\u00f9ng nhau l\u00e0",
    "options_en": '["A. \\\\frac{1}{6}","B. \\\\frac{1}{3}","C. \\\\frac{1}{2}","D. \\\\frac{2}{3}"]',
    "options_vi": '["A. \\\\frac{1}{6}","B. \\\\frac{1}{3}","C. \\\\frac{1}{2}","D. \\\\frac{2}{3}"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "Total: $C_7^2=21$. Coprime pairs: (2,3)(2,5)(2,7)(3,4)(3,5)(3,7)(3,8)(4,5)(4,7)(5,6)(5,7)(5,8)(6,7)(7,8)=14. Probability $\\frac{14}{21}=\\frac{2}{3}$.",
    "solution_vi": "T\u1ed5ng: $C_7^2=21$. C\u1eb7p nguy\u00ean t\u1ed1: (2,3)(2,5)(2,7)(3,4)(3,5)(3,7)(3,8)(4,5)(4,7)(5,6)(5,7)(5,8)(6,7)(7,8)=14. X\u00e1c su\u1ea5t $\\frac{14}{21}=\\frac{2}{3}$."
}
t[54] = {
    "content_en": "Given $f(x)=x^3-x+1$, the difference between the max and min of $f(x)$ on $[-2,2]$ is ____",
    "content_vi": "Cho $f(x)=x^3-x+1$, hi\u1ec7u gi\u1eefa GTLN v\u00e0 GTNN c\u1ee7a $f(x)$ tr\u00ean $[-2,2]$ l\u00e0 ____",
    "options_en": None, "options_vi": None, "answer_en": None, "answer_vi": None,
    "solution_en": "$f'(x)=3x^2-1$, critical points $x=\\pm\\frac{1}{\\sqrt{3}}$. $f(-2)=-5$, $f(2)=7$. Max=7, Min=-5, diff=12.",
    "solution_vi": "$f'(x)=3x^2-1$, \u0111i\u1ec3m t\u1edbi h\u1ea1n $x=\\pm\\frac{1}{\\sqrt{3}}$. $f(-2)=-5$, $f(2)=7$. GTLN=7, GTNN=-5, hi\u1ec7u=12."
}
t[55] = {
    "content_en": "Write the equation of a line tangent to both circles $x^2+y^2=1$ and $(x-3)^2+(y-4)^2=16$ ____",
    "content_vi": "Vi\u1ebft ph\u01b0\u01a1ng tr\u00ecnh \u0111\u01b0\u1eddng th\u1eb3ng ti\u1ebfp x\u00fac v\u1edbi c\u1ea3 hai \u0111\u01b0\u1eddng tr\u00f2n $x^2+y^2=1$ v\u00e0 $(x-3)^2+(y-4)^2=16$ ____",
    "options_en": None, "options_vi": None, "answer_en": None, "answer_vi": None,
    "solution_en": "Centers distance=5, radii=1,4. Circles externally tangent. Common tangent: $x=-1$ (tangent to first at $(-1,0)$).",
    "solution_vi": "Kho\u1ea3ng c\u00e1ch t\u00e2m=5, b\u00e1n k\u00ednh =1,4. 2 \u0111\u01b0\u1eddng tr\u00f2n ti\u1ebfp x\u00fac ngo\u00e0i. Ti\u1ebfp tuy\u1ebfn chung: $x=-1$ (tx \u0111\u01b0\u1eddng tr\u00f2n th\u1ee9 nh\u1ea5t t\u1ea1i $(-1,0)$)."
}
t[56] = {
    "content_en": "Let $U=\\{1,2,3,4,5\\}$, $M=\\{1,4\\}$, $N=\\{2,5\\}$. Then $N\\cup \\complement_U M=$",
    "content_vi": "Cho $U=\\{1,2,3,4,5\\}$, $M=\\{1,4\\}$, $N=\\{2,5\\}$. Khi \u0111\u00f3 $N\\cup \\complement_U M=$",
    "options_en": '["A. \\\\{2,3,5\\\\}","B. \\\\{1,3,4\\\\}","C. \\\\{1,2,4,5\\\\}","D. \\\\{2,3,4,5\\\\}"]',
    "options_vi": '["A. \\\\{2,3,5\\\\}","B. \\\\{1,3,4\\\\}","C. \\\\{1,2,4,5\\\\}","D. \\\\{2,3,4,5\\\\}"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$\\complement_U M=\\{2,3,5\\}$, $N\\cup \\complement_U M=\\{2,3,5\\}$.",
    "solution_vi": "$\\complement_U M=\\{2,3,5\\}$, $N\\cup \\complement_U M=\\{2,3,5\\}$."
}
t[57] = {
    "content_en": "Let $\\{a_n\\}$ be an arithmetic sequence with sum $S_n$. If $a_1=1$, $S_5=25$, then $a_5=$",
    "content_vi": "Cho c\u1ea5p s\u1ed1 c\u1ed9ng $\\{a_n\\}$ c\u00f3 t\u1ed5ng $S_n$. N\u1ebfu $a_1=1$, $S_5=25$, th\u00ec $a_5=$",
    "options_en": '["A. 7","B. 8","C. 9","D. 10"]',
    "options_vi": '["A. 7","B. 8","C. 9","D. 10"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$S_5=5a_1+10d=5+10d=25$, so $d=2$. $a_5=a_1+4d=1+8=9$.",
    "solution_vi": "$S_5=5a_1+10d=5+10d=25$, suy ra $d=2$. $a_5=a_1+4d=1+8=9$."
}
t[58] = {
    "content_en": "In rectangular prism $ABCD-A_1B_1C_1D_1$, $B_1D$ makes $30\\degree$ angles with both plane $ABCD$ and plane $AA_1B_1B$. Then",
    "content_vi": "Trong h\u00ecnh h\u1ed9p CN $ABCD-A_1B_1C_1D_1$, $B_1D$ t\u1ea1o v\u1edbi m\u1eb7t $ABCD$ v\u00e0 m\u1eb7t $AA_1B_1B$ c\u00f9ng g\u00f3c $30\\degree$. Khi \u0111\u00f3",
    "options_en": '["A. AB=2AD","B. AB=\\\\sqrt{3}AD","C. AB=AD","D. AB t\u1ea1o v\u1edbi m\u1eb7t AB_1C_1D g\u00f3c 30\\\\degree"]',
    "options_vi": '["A. AB=2AD","B. AB=\\\\sqrt{3}AD","C. AB=AD","D. AB t\u1ea1o v\u1edbi m\u1eb7t AB_1C_1D g\u00f3c 30\\\\degree"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "Let $AB=a, AD=b, AA_1=c$. Set up equations and use vector angle formula, obtaining $a=2b$.",
    "solution_vi": "\u0110\u1eb7t $AB=a, AD=b, AA_1=c$. L\u1eadp pt v\u00e0 d\u00f9ng c\u00f4ng th\u1ee9c g\u00f3c vect\u01a1, gi\u1ea3i \u0111\u01b0\u1ee3c $a=2b$."
}
t[59] = {
    "content_en": "In $\\triangle ABC$, angles $A,B,C$ have opposite sides $a,b,c$. Given $a=3$, $b=2\\sqrt{6}$, $B=2A$. (1) Find $\\cos A$; (2) Find $c$.",
    "content_vi": "Trong $\\triangle ABC$, $A,B,C$ c\u00f3 c\u1ea1nh \u0111\u1ed1i $a,b,c$. Cho $a=3$, $b=2\\sqrt{6}$, $B=2A$. (1) T\u00ecm $\\cos A$; (2) T\u00ecm $c$.",
    "options_en": None, "options_vi": None,
    "answer_en": "cosA=\u221a6/3, c=5", "answer_vi": "cosA=\u221a6/3, c=5",
    "solution_en": "(1) $\\frac{a}{\\sin A}=\\frac{b}{\\sin 2A}$, $\\frac{3}{\\sin A}=\\frac{2\\sqrt{6}}{2\\sin A\\cos A}$, $\\cos A=\\frac{\\sqrt{6}}{3}$. (2) By cos law, $c=5$.",
    "solution_vi": "(1) $\\frac{a}{\\sin A}=\\frac{b}{\\sin 2A}$, $\\frac{3}{\\sin A}=\\frac{2\\sqrt{6}}{2\\sin A\\cos A}$, $\\cos A=\\frac{\\sqrt{6}}{3}$. (2) Theo \u0111l cos, $c=5$."
}
t[60] = {
    "content_en": "Given $z=1-2i$ and $z+a\\bar{z}+b=0$, where $a,b$ are real, then",
    "content_vi": "Cho $z=1-2i$ v\u00e0 $z+a\\bar{z}+b=0$, $a,b$ l\u00e0 s\u1ed1 th\u1ef1c, th\u00ec",
    "options_en": '["A. a=1,b=-2","B. a=-1,b=2","C. a=1,b=2","D. a=-1,b=-2"]',
    "options_vi": '["A. a=1,b=-2","B. a=-1,b=2","C. a=1,b=2","D. a=-1,b=-2"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "Sub $z=1-2i$, $\\bar{z}=1+2i$. $(1-2i)+a(1+2i)+b=0$. Real: $1+a+b=0$, Imag: $-2+2a=0$. So $a=1,b=-2$.",
    "solution_vi": "Thay $z=1-2i$, $\\bar{z}=1+2i$. $(1-2i)+a(1+2i)+b=0$. Th\u1ef1c: $1+a+b=0$, \u1ea2o: $-2+2a=0$. Suy ra $a=1,b=-2$."
}
t[61] = {
    "content_en": "Let $F$ be focus of parabola $C: y^2=4x$. $A$ on $C$, $B(3,0)$. If $|AF|=|BF|$, then $|AB|=$",
    "content_vi": "G\u1ecdi $F$ l\u00e0 ti\u00eau \u0111i\u1ec3m parabol $C: y^2=4x$. $A$ tr\u00ean $C$, $B(3,0)$. N\u1ebfu $|AF|=|BF|$, th\u00ec $|AB|=$",
    "options_en": '["A. 2","B. 2\\\\sqrt{2}","C. 3","D. 3\\\\sqrt{2}"]',
    "options_vi": '["A. 2","B. 2\\\\sqrt{2}","C. 3","D. 3\\\\sqrt{2}"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$F(1,0)$, $|BF|=2$. Let $A(\\frac{y^2}{4},y)$. From $|AF|=2$: $\\frac{y^4}{16}-\\frac{y^2}{2}+1+y^2=4$, solve $A(1,2)$. $|AB|=\\sqrt{4+4}=2\\sqrt{2}$.",
    "solution_vi": "$F(1,0)$, $|BF|=2$. \u0110\u1eb7t $A(\\frac{y^2}{4},y)$. T\u1eeb $|AF|=2$: $\\frac{y^4}{16}-\\frac{y^2}{2}+1+y^2=4$, gi\u1ea3i $A(1,2)$. $|AB|=\\sqrt{4+4}=2\\sqrt{2}$."
}
t[62] = {
    "content_en": "In expansion of $(1-\\frac{y}{x})(x+y)^8$, coefficient of $x^2y^6$ is ____",
    "content_vi": "Trong khai tri\u1ec3n $(1-\\frac{y}{x})(x+y)^8$, h\u1ec7 s\u1ed1 c\u1ee7a $x^2y^6$ l\u00e0 ____",
    "options_en": None, "options_vi": None, "answer_en": None, "answer_vi": None,
    "solution_en": "In $(x+y)^8$: $x^3y^5$ coeff=$C_8^5=56$, $x^2y^6$ coeff=$C_8^6=28$. After $(1-\\frac{y}{x})$: coeff=$C_8^6-C_8^5=28-56=-28$.",
    "solution_vi": "Trong $(x+y)^8$: $x^3y^5$ h\u1ec7 s\u1ed1=$C_8^5=56$, $x^2y^6$ h\u1ec7 s\u1ed1=$C_8^6=28$. Sau $(1-\\frac{y}{x})$: h\u1ec7 s\u1ed1=$C_8^6-C_8^5=28-56=-28$."
}
t[63] = {
    "content_en": "Let $A=\\{x \\mid -2 < x < 4\\}$, $B=\\{2,3,4,5\\}$. Then $A\\cap B=$",
    "content_vi": "Cho $A=\\{x \\mid -2 < x < 4\\}$, $B=\\{2,3,4,5\\}$. Khi \u0111\u00f3 $A\\cap B=$",
    "options_en": '["A. \\\\{2\\\\}","B. \\\\{2,3\\\\}","C. \\\\{3,4\\\\}","D. \\\\{2,3,4\\\\}"]',
    "options_vi": '["A. \\\\{2\\\\}","B. \\\\{2,3\\\\}","C. \\\\{3,4\\\\}","D. \\\\{2,3,4\\\\}"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$A=(-2,4)$, $A\\cap B=\\{2,3\\}$.",
    "solution_vi": "$A=(-2,4)$, $A\\cap B=\\{2,3\\}$."
}
t[64] = {
    "content_en": "Which interval is $f(x)=7\\sin(x-\\frac{\\pi}{6})$ increasing on?",
    "content_vi": "Kho\u1ea3ng n\u00e0o $f(x)=7\\sin(x-\\frac{\\pi}{6})$ \u0111\u1ed3ng bi\u1ebfn?",
    "options_en": '["A. (0,\\\\frac{\\\\pi}{2})","B. (\\\\frac{\\\\pi}{2},\\\\pi)","C. (\\\\pi,\\\\frac{3\\\\pi}{2})","D. (\\\\frac{3\\\\pi}{2},2\\\\pi)"]',
    "options_vi": '["A. (0,\\\\frac{\\\\pi}{2})","B. (\\\\frac{\\\\pi}{2},\\\\pi)","C. (\\\\pi,\\\\frac{3\\\\pi}{2})","D. (\\\\frac{3\\\\pi}{2},2\\\\pi)"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$-\\frac{\\pi}{2}+2k\\pi \\leq x-\\frac{\\pi}{6} \\leq \\frac{\\pi}{2}+2k\\pi$. $k=0$: $x\\in[-\\frac{\\pi}{3},\\frac{2\\pi}{3}]$. $(0,\\frac{\\pi}{2})$ inside.",
    "solution_vi": "$-\\frac{\\pi}{2}+2k\\pi \\leq x-\\frac{\\pi}{6} \\leq \\frac{\\pi}{2}+2k\\pi$. $k=0$: $x\\in[-\\frac{\\pi}{3},\\frac{2\\pi}{3}]$. $(0,\\frac{\\pi}{2})$ n\u1eb1m trong."
}
t[65] = {
    "content_en": "If two tangents can be drawn from $(a,b)$ to $y=e^x$, then",
    "content_vi": "N\u1ebfu t\u1eeb $(a,b)$ k\u1ebb \u0111\u01b0\u1ee3c hai ti\u1ebfp tuy\u1ebfn \u0111\u1ebfn $y=e^x$, th\u00ec",
    "options_en": '["A. e^b < a","B. e^a < b","C. 0 < a < e^b","D. 0 < b < e^a"]',
    "options_vi": '["A. e^b < a","B. e^a < b","C. 0 < a < e^b","D. 0 < b < e^a"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "Tangent at $(x_0,e^{x_0})$: $y-e^{x_0}=e^{x_0}(x-x_0)$. Sub $(a,b)$: $b=e^{x_0}(a-x_0+1)$. Two tangents means two $x_0$ solutions. $0<b<e^a$.",
    "solution_vi": "Ti\u1ebfp tuy\u1ebfn t\u1ea1i $(x_0,e^{x_0})$: $y-e^{x_0}=e^{x_0}(x-x_0)$. Thay $(a,b)$: $b=e^{x_0}(a-x_0+1)$. Hai ti\u1ebfp tuy\u1ebfn = hai nghi\u1ec7m $x_0$. $0<b<e^a$."
}
t[66] = {
    "content_en": "In regular triangular prism $ABC-A_1B_1C_1$, $AB=AA_1=1$. $P$ satisfies $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$. Then",
    "content_vi": "Trong l\u0103ng tr\u1ee5 tam gi\u00e1c \u0111\u1ec1u $ABC-A_1B_1C_1$, $AB=AA_1=1$. $P$ th\u1ecfa $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$. Khi \u0111\u00f3",
    "options_en": '["A. Khi \\\\lambda=1, chu vi \\\\triangle AB_1P kh\u00f4ng \u0111\u1ed5i","B. Khi \\\\mu=1, th\u1ec3 t\u00edch P-A_1BC kh\u00f4ng \u0111\u1ed5i","C. Khi \\\\lambda=\\\\frac{1}{2}, duy nh\u1ea5t P: A_1P\\\\perp BP","D. Khi \\\\mu=\\\\frac{1}{2}, duy nh\u1ea5t P: A_1B\\\\perp m\u1eb7t AB_1P"]',
    "options_vi": '["A. Khi \\\\lambda=1, chu vi \\\\triangle AB_1P kh\u00f4ng \u0111\u1ed5i","B. Khi \\\\mu=1, th\u1ec3 t\u00edch P-A_1BC kh\u00f4ng \u0111\u1ed5i","C. Khi \\\\lambda=\\\\frac{1}{2}, duy nh\u1ea5t P: A_1P\\\\perp BP","D. Khi \\\\mu=\\\\frac{1}{2}, duy nh\u1ea5t P: A_1B\\\\perp m\u1eb7t AB_1P"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "When $\\mu=1$, $P$ moves on $B_1C_1$. Base area and height of pyramid $P-A_1BC$ constant, so volume constant.",
    "solution_vi": "Khi $\\mu=1$, $P$ di chuy\u1ec3n tr\u00ean $B_1C_1$. Di\u1ec7n t\u00edch \u0111\u00e1y v\u00e0 chi\u1ec1u cao $P-A_1BC$ kh\u00f4ng \u0111\u1ed5i, th\u1ec3 t\u00edch kh\u00f4ng \u0111\u1ed5i."
}
t[67] = {
    "content_en": "Students studying folk paper-cutting: paper folded along symmetry axis. $20dm\\times 12dm$ paper. After 1 fold: 2 shapes $10dm\\times 12dm$, $20dm\\times 6dm$, $S_1=240dm^2$. After 2 folds: 3 shapes $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$, $S_2=180dm^2$. How many shapes after 4 folds? ____ After $n$ folds, $\\sum_{k=1}^n S_k =$ ____ $dm^2$.",
    "content_vi": "HS nghi\u00ean c\u1ee9u c\u1eaft gi\u1ea5y d\u00e2n gian: g\u1ea5p gi\u1ea5y theo tr\u1ee5c \u0111\u1ed1i x\u1ee9ng. Gi\u1ea5y $20dm\\times 12dm$: sau 1 l\u1ea7n g\u1ea5p \u0111\u01b0\u1ee3c 2 lo\u1ea1i $10dm\\times 12dm$, $20dm\\times 6dm$, $S_1=240dm^2$; sau 2 l\u1ea7n: 3 lo\u1ea1i $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$, $S_2=180dm^2$. S\u1ed1 lo\u1ea1i sau 4 l\u1ea7n? ____ Sau $n$ l\u1ea7n, $\\sum_{k=1}^n S_k =$ ____ $dm^2$.",
    "options_en": None, "options_vi": None,
    "answer_en": "5, 720(1-1/2^n)", "answer_vi": "5, 720(1-1/2^n)",
    "solution_en": "After $k$ folds: $k+1$ types. $S_k=240\\times k\\times(\\frac12)^{k-1}$. Sum = $720(1-\\frac1{2^n})$.",
    "solution_vi": "Sau $k$ l\u1ea7n: $k+1$ lo\u1ea1i. $S_k=240\\times k\\times(\\frac12)^{k-1}$. T\u1ed5ng = $720(1-\\frac1{2^n})$."
}
t[68] = {
    "content_en": "Let angles of $\\triangle ABC$ be $A,B,C$, opposite sides $a,b,c$. $b^2=ac$, $D$ on $AC$: $BD\\sin\\angle ABC=a\\sin C$. (1) Prove $BD=b$. (2) If $AD=2DC$, find $\\cos\\angle ABC$.",
    "content_vi": "G\u00f3c $\\triangle ABC$ l\u00e0 $A,B,C$, c\u1ea1nh \u0111\u1ed1i $a,b,c$. $b^2=ac$, $D$ tr\u00ean $AC$: $BD\\sin\\angle ABC=a\\sin C$. (1) CM $BD=b$. (2) N\u1ebfu $AD=2DC$, t\u00ecm $\\cos\\angle ABC$.",
    "options_en": None, "options_vi": None,
    "answer_en": "See proof, cos\u2220ABC=7/12", "answer_vi": "Xem CM, cos\u2220ABC=7/12",
    "solution_en": "(1) $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, with condition, prove $BD=b$. (2) Cos law: $\\cos\\angle ABC=\\frac{7}{12}$.",
    "solution_vi": "(1) $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, k\u1ebft h\u1ee3p \u0111k, CM $BD=b$. (2) \u0110l cos: $\\cos\\angle ABC=\\frac{7}{12}$."
}
t[69] = {
    "content_en": "5 Beijing Winter Olympics volunteers to 4 events (fig skating, short track, hockey, curling). Each to 1 event, each event at least 1. Number of plans:",
    "content_vi": "5 TNV Olympic M\u00f9a \u0111\u00f4ng B\u1eafc Kinh v\u00e0o 4 m\u00f4n (tr\u01b0\u1ee3t b\u0103ng NT, tr\u01b0\u1ee3t t\u1ed1c \u0111\u1ed9, kh\u00fac c\u00f4n c\u1ea7u, bi \u0111\u00e1). M\u1ed7i ng\u01b0\u1eddi 1 m\u00f4n, m\u1ed7i m\u00f4n \u00edt nh\u1ea5t 1. S\u1ed1 c\u00e1ch:",
    "options_en": '["A. 60 c\u00e1ch","B. 120 c\u00e1ch","C. 240 c\u00e1ch","D. 480 c\u00e1ch"]',
    "options_vi": '["A. 60 c\u00e1ch","B. 120 c\u00e1ch","C. 240 c\u00e1ch","D. 480 c\u00e1ch"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "Group then assign. 5 into 4 groups (one group of 2). Choose 2: $C_5^2=10$. Permute 4 groups: $4!=24$. Total $10\\times24=240$.",
    "solution_vi": "Nh\u00f3m r\u1ed3i ph\u00e2n. 5 v\u00e0o 4 nh\u00f3m (1 nh\u00f3m 2). Ch\u1ecdn 2: $C_5^2=10$. X\u1ebfp 4 nh\u00f3m: $4!=24$. T\u1ed5ng $10\\times24=240$."
}
t[70] = {
    "content_en": "6 students to 3 venues A, B, C. Each to 1 venue. A gets 1, B gets 2, C gets 3. Number of arrangements:",
    "content_vi": "6 HS \u0111\u1ebfn 3 \u0111\u1ecba \u0111i\u1ec3m A, B, C. M\u1ed7i ng\u01b0\u1eddi 1 \u0111\u1ecba \u0111i\u1ec3m. A nh\u1eadn 1, B 2, C 3. S\u1ed1 c\u00e1ch:",
    "options_en": '["A. 120 c\u00e1ch","B. 90 c\u00e1ch","C. 60 c\u00e1ch","D. 30 c\u00e1ch"]',
    "options_vi": '["A. 120 c\u00e1ch","B. 90 c\u00e1ch","C. 60 c\u00e1ch","D. 30 c\u00e1ch"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times10\\times1 = 60$.",
    "solution_vi": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times10\\times1 = 60$."
}
t[71] = {
    "content_en": "96% of students like football or swimming, 60% like football, 82% like swimming. % who like both:",
    "content_vi": "96% HS th\u00edch b\u00f3ng \u0111\u00e1 ho\u1eb7c b\u01a1i, 60% th\u00edch b\u00f3ng \u0111\u00e1, 82% th\u00edch b\u01a1i. % th\u00edch c\u1ea3 hai:",
    "options_en": '["A. 62%","B. 56%","C. 46%","D. 42%"]',
    "options_vi": '["A. 62%","B. 56%","C. 46%","D. 42%"]',
    "answer_en": None, "answer_vi": None,
    "solution_en": "$P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, so $P(F\\cap S)=46\\%$.",
    "solution_vi": "$P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, suy ra $P(F\\cap S)=46\\%$."
}
t[72] = {
    "content_en": "Ellipse $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ eccentricity $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ left/right foci, $A$ top vertex, $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$. Equation of $C$: ____",
    "content_vi": "Elip $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ t\u00e2m sai $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ ti\u00eau \u0111i\u1ec3m T/P, $A$ \u0111\u1ec9nh tr\u00ean, $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$. PT $C$: ____",
    "options_en": None, "options_vi": None,
    "answer_en": "x\u00b2/4+y\u00b2=1", "answer_vi": "x\u00b2/4+y\u00b2=1",
    "solution_en": "$e=c/a=\\sqrt{3}/2$. Let $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_{1,2}=(\\pm\\sqrt{3}k,0)$. Dot=$-3k^2+k^2=-2k^2=-1$, so $k=1$. $a=2,b=1$.",
    "solution_vi": "$e=c/a=\\sqrt{3}/2$. \u0110\u1eb7t $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_{1,2}=(\\pm\\sqrt{3}k,0)$. T\u00edch vh=$-3k^2+k^2=-2k^2=-1$, $k=1$. $a=2,b=1$."
}

with open('translations_51_72.json', 'w', encoding='utf-8') as f:
    json.dump(t, f, ensure_ascii=False, indent=2)
print(f"Saved translations for {len(t)} questions (51-72)")
