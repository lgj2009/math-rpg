"""
Translate 50 Chinese math questions to English and Vietnamese (hardcoded).
Keeps ALL LaTeX intact. Only translates Chinese text.
"""
import sqlite3
import json

DB_PATH = r"D:\编程\Python\stutdy\.claude\worktrees\math-rpg-implementation\math_rpg.db"
translations = []

def t(id_val, content_en, content_vi, options_en=None, options_vi=None,
       answer_en=None, answer_vi=None, solution_en=None, solution_vi=None):
    translations.append((id_val, content_en, content_vi,
                         options_en, options_vi,
                         answer_en, answer_vi,
                         solution_en, solution_vi))

# ===== TRANSLATION DATA =====

t(1,
  "Given $\\sin\\alpha = \\frac{3}{5}$, $\\alpha \\in (0, \\frac{\\pi}{2})$, find $\\cos\\alpha$",
  "Cho $\\sin\\alpha = \\frac{3}{5}$, $\\alpha \\in (0, \\frac{\\pi}{2})$, t\\u00ednh $\\cos\\alpha$",
  None, None, None, None,
  "From $\\sin^2\\alpha + \\cos^2\\alpha = 1$, $\\alpha$ is in the first quadrant, $\\cos\\alpha = \\frac{4}{5}$",
  "T\\u1eeb $\\sin^2\\alpha + \\cos^2\\alpha = 1$, $\\alpha$ \\u1edf g\\u00f3c ph\\u1ea7n t\\u01b0 th\\u1ee9 nh\\u1ea5t, $\\cos\\alpha = \\frac{4}{5}$")

t(2,
  "Given $\\sin\\alpha = \\frac{1}{3}$, find $\\cos 2\\alpha =$ ____",
  "Cho $\\sin\\alpha = \\frac{1}{3}$, t\\u00ednh $\\cos 2\\alpha =$ ____",
  None, None, None, None,
  "$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\times \\frac{1}{9} = \\frac{7}{9}$",
  "$\\cos 2\\alpha = 1 - 2\\sin^2\\alpha = 1 - 2 \\times \\frac{1}{9} = \\frac{7}{9}$")

t(3,
  "In $\\triangle ABC$, given $a=3$, $b=4$, $\\angle C = 60\\degree$, find the length of $c$",
  "Trong $\\triangle ABC$, cho $a=3$, $b=4$, $\\angle C = 60\\degree$, t\\u00ednh \\u0111\\u1ed9 d\\u00e0i $c$",
  None, None, None, None,
  "Using the law of cosines $c^2 = a^2 + b^2 - 2ab\\cos C = 9 + 16 - 24 \\times \\frac{1}{2} = 13$, so $c = \\sqrt{13}$",
  "Theo \\u0111\\u1ecbnh l\\u00fd cosin $c^2 = a^2 + b^2 - 2ab\\cos C = 9 + 16 - 24 \\times \\frac{1}{2} = 13$, suy ra $c = \\sqrt{13}$")

t(4,
  "The value of $\\sin 75\\degree$ is",
  "Gi\\u00e1 tr\\u1ecb c\\u1ee7a $\\sin 75\\degree$ l\\u00e0",
  None, None, None, None,
  "$\\sin 75\\degree = \\sin(45\\degree+30\\degree) = \\sin 45\\degree\\cos 30\\degree + \\cos 45\\degree\\sin 30\\degree = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
  "$\\sin 75\\degree = \\sin(45\\degree+30\\degree) = \\sin 45\\degree\\cos 30\\degree + \\cos 45\\degree\\sin 30\\degree = \\frac{\\sqrt{6}+\\sqrt{2}}{4}$")

t(5,
  "In $\\triangle ABC$, given $\\angle A = 45\\degree$, $\\angle B = 60\\degree$, $a = 2$, find $b =$ ____",
  "Trong $\\triangle ABC$, cho $\\angle A = 45\\degree$, $\\angle B = 60\\degree$, $a = 2$, t\\u00ednh $b =$ ____",
  None, None, None, None,
  "By the law of sines $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$, $b = \\frac{a\\sin B}{\\sin A} = \\frac{2 \\times \\sqrt{3}/2}{\\sqrt{2}/2} = \\sqrt{6}$",
  "Theo \\u0111\\u1ecbnh l\\u00fd sin $\\frac{a}{\\sin A} = \\frac{b}{\\sin B}$, $b = \\frac{a\\sin B}{\\sin A} = \\frac{2 \\times \\sqrt{3}/2}{\\sqrt{2}/2} = \\sqrt{6}$")

t(6,
  "In $\\triangle ABC$, $a=2$, $b=3$, $c=\\sqrt{7}$, find $\\angle C$",
  "Trong $\\triangle ABC$, $a=2$, $b=3$, $c=\\sqrt{7}$, t\\u00ednh $\\angle C$",
  None, None, None, None,
  "$\\cos C = \\frac{a^2+b^2-c^2}{2ab} = \\frac{4+9-7}{2\\times2\\times3} = \\frac{1}{2}$, so $C=60\\degree$",
  "$\\cos C = \\frac{a^2+b^2-c^2}{2ab} = \\frac{4+9-7}{2\\times2\\times3} = \\frac{1}{2}$, suy ra $C=60\\degree$")

t(7,
  "Given an arithmetic sequence $\\{a_n\\}$ with $a_1=2$, $d=3$, find $a_5$",
  "Cho c\\u1ea5p s\\u1ed1 c\\u1ed9ng $\\{a_n\\}$ v\\u1edbi $a_1=2$, $d=3$, t\\u00ednh $a_5$",
  None, None, None, None,
  "$a_5 = a_1 + (5-1)d = 2 + 4 \\times 3 = 14$",
  "$a_5 = a_1 + (5-1)d = 2 + 4 \\times 3 = 14$")

t(8,
  "Given a geometric sequence $\\{a_n\\}$ with $a_1=1$, $q=2$, find $S_5 =$ ____",
  "Cho c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$ v\\u1edbi $a_1=1$, $q=2$, t\\u00ednh $S_5 =$ ____",
  None, None, None, None,
  "$S_5 = a_1 \\frac{q^5-1}{q-1} = 1 \\times \\frac{2^5-1}{2-1} = 31$",
  "$S_5 = a_1 \\frac{q^5-1}{q-1} = 1 \\times \\frac{2^5-1}{2-1} = 31$")

t(9,
  "Given the sequence $\\{a_n\\}$ with $S_n = 2n^2 + n$, find $a_3$",
  "Cho d\\u00e3y s\\u1ed1 $\\{a_n\\}$ v\\u1edbi $S_n = 2n^2 + n$, t\\u00ednh $a_3$",
  None, None, None, None,
  "$a_3 = S_3 - S_2 = (2\\times9+3) - (2\\times4+2) = 21 - 10 = 11$",
  "$a_3 = S_3 - S_2 = (2\\times9+3) - (2\\times4+2) = 21 - 10 = 11$")

t(10,
  "In the geometric sequence $\\{a_n\\}$, $a_2=2$, $a_5=16$, find $S_4 =$ ____",
  "Trong c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$, $a_2=2$, $a_5=16$, t\\u00ednh $S_4 =$ ____",
  None, None, None, None,
  "$q^3 = \\frac{a_5}{a_2} = \\frac{16}{2} = 8$, $q=2$, $a_1=\\frac{a_2}{q}=1$, $S_4 = \\frac{1\\times(2^4-1)}{2-1}=15$",
  "$q^3 = \\frac{a_5}{a_2} = \\frac{16}{2} = 8$, $q=2$, $a_1=\\frac{a_2}{q}=1$, $S_4 = \\frac{1\\times(2^4-1)}{2-1}=15$")

t(11,
  "Find $\\sum\\limits_{n=1}^{100} \\frac{1}{n(n+1)}$",
  "T\\u00ednh $\\sum\\limits_{n=1}^{100} \\frac{1}{n(n+1)}$",
  None, None, None, None,
  "$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$, $\\sum_{n=1}^{100} \\frac{1}{n(n+1)} = 1 - \\frac{1}{101} = \\frac{100}{101}$",
  "$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$, $\\sum_{n=1}^{100} \\frac{1}{n(n+1)} = 1 - \\frac{1}{101} = \\frac{100}{101}$")

t(12,
  "How many ways to arrange $5$ different books in a row?",
  "C\\u00f3 bao nhi\\u00eau c\\u00e1ch x\\u1ebfp $5$ cu\\u1ed1n s\\u00e1ch kh\\u00e1c nhau th\\u00e0nh m\\u1ed9t h\\u00e0ng?",
  None, None, None, None,
  "$5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$",
  "$5! = 5 \\times 4 \\times 3 \\times 2 \\times 1 = 120$")

t(13,
  "Choose $2$ from $10$ students. ____ different ways.",
  "Ch\\u1ecdn $2$ t\\u1eeb $10$ h\\u1ecdc sinh. ____ c\\u00e1ch ch\\u1ecdn.",
  None, None, None, None,
  "$\\mathrm{C}_{10}^2 = \\frac{10\\times9}{2} = 45$",
  "$\\mathrm{C}_{10}^2 = \\frac{10\\times9}{2} = 45$")

t(14,
  "Roll two dice. Probability the sum is $7$?",
  "Gieo hai x\\u00fac x\\u1eafc. X\\u00e1c su\\u1ea5t t\\u1ed5ng b\\u1eb1ng $7$?",
  None, None, None, None,
  "Favorable outcomes: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1), 6. Total: 36. $P=\\frac{6}{36}=\\frac{1}{6}$",
  "K\\u1ebft qu\\u1ea3 thu\\u1eadn l\\u1ee3i: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1), 6. T\\u1ed5ng: 36. $P=\\frac{6}{36}=\\frac{1}{6}$")

t(15,
  "In $(x+1)^4$, the coefficient of $x^2$ is ____",
  "Trong $(x+1)^4$, h\\u1ec7 s\\u1ed1 c\\u1ee7a $x^2$ l\\u00e0 ____",
  None, None, None, None,
  "$T_{r+1} = \\mathrm{C}_4^r x^{4-r} \\cdot 1^r$, set $4-r=2$ gives $r=2$, coefficient $\\mathrm{C}_4^2 = 6$",
  "$T_{r+1} = \\mathrm{C}_4^r x^{4-r} \\cdot 1^r$, \\u0111\\u1eb7t $4-r=2$ \\u0111\\u01b0\\u1ee3c $r=2$, h\\u1ec7 s\\u1ed1 $\\mathrm{C}_4^2 = 6$")

t(16,
  "Roll a die. Let $X$ be the number. Find $E(X)$.",
  "Gieo x\\u00fac x\\u1eafc. G\\u1ecdi $X$ l\\u00e0 s\\u1ed1 ch\\u1ea5m. T\\u00ednh $E(X)$.",
  None, None, None, None,
  "$E(X) = \\frac{1+2+3+4+5+6}{6} = 3.5$",
  "$E(X) = \\frac{1+2+3+4+5+6}{6} = 3.5$")

t(17,
  "Space diagonal of a cube with edge $2$ is",
  "\\u0110\\u01b0\\u1eddng ch\\u00e9o kh\\u00f4ng gian c\\u1ee7a h\\u00ecnh l\\u1eadp ph\\u01b0\\u01a1ng c\\u1ea1nh $2$ l\\u00e0",
  None, None, None, None,
  "Space diagonal $= \\sqrt{2^2+2^2+2^2} = 2\\sqrt{3}$",
  "\\u0110\\u01b0\\u1eddng ch\\u00e9o kh\\u00f4ng gian $= \\sqrt{2^2+2^2+2^2} = 2\\sqrt{3}$")

t(18,
  "Volume of a sphere with radius $3$ is ____",
  "Th\\u1ec3 t\\u00edch h\\u00ecnh c\\u1ea7u b\\u00e1n k\\u00ednh $3$ l\\u00e0 ____",
  None, None, None, None,
  "$V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi \\times 27 = 36\\pi$",
  "$V = \\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi \\times 27 = 36\\pi$")

t(19,
  "A rectangular solid has dimensions $3,4,5$. Find $\\tan$ of the angle between the base diagonal and body diagonal.",
  "H\\u00ecnh h\\u1ed9p ch\\u1eef nh\\u1eadt c\\u00f3 k\\u00edch th\\u01b0\\u1edbc $3,4,5$. T\\u00ecm $\\tan$ g\\u00f3c gi\\u1eefa \\u0111\\u01b0\\u1eddng ch\\u00e9o \\u0111\\u00e1y v\\u00e0 \\u0111\\u01b0\\u1eddng ch\\u00e9o kh\\u1ed1i.",
  None, None, None, None,
  "Base diagonal $= \\sqrt{3^2+4^2}=5$, height $=5$, $\\tan\\theta = \\frac{5}{5} = 1$",
  "\\u0110\\u01b0\\u1eddng ch\\u00e9o \\u0111\\u00e1y $= \\sqrt{3^2+4^2}=5$, chi\\u1ec1u cao $=5$, $\\tan\\theta = \\frac{5}{5} = 1$")

t(20,
  "A triangular pyramid has an equilateral base of side $2$ and height $3$. Find its volume ____",
  "H\\u00ecnh ch\\u00f3p tam gi\\u00e1c c\\u00f3 \\u0111\\u00e1y tam gi\\u00e1c \\u0111\\u1ec1u c\\u1ea1nh $2$, chi\\u1ec1u cao $3$. T\\u00ednh th\\u1ec3 t\\u00edch ____",
  None, None, None, None,
  "$V = \\frac{1}{3}Sh = \\frac{1}{3} \\times 4 \\times 3 = 4$",
  "$V = \\frac{1}{3}Sh = \\frac{1}{3} \\times 4 \\times 3 = 4$")

t(21,
  "A cone has radius $3$, height $4$. Find its lateral area.",
  "H\\u00ecnh n\\u00f3n c\\u00f3 b\\u00e1n k\\u00ednh $3$, chi\\u1ec1u cao $4$. T\\u00ednh di\\u1ec7n t\\u00edch xung quanh.",
  None, None, None, None,
  "Slant height $l = \\sqrt{3^2+4^2}=5$, lateral area $S = \\pi r l = \\pi \\times 3 \\times 5 = 15\\pi$",
  "\\u0110\\u01b0\\u1eddng sinh $l = \\sqrt{3^2+4^2}=5$, di\\u1ec7n t\\u00edch xung quanh $S = \\pi r l = \\pi \\times 3 \\times 5 = 15\\pi$")

t(22,
  "The radius of $x^2 + y^2 = 4$ is",
  "B\\u00e1n k\\u00ednh c\\u1ee7a $x^2 + y^2 = 4$ l\\u00e0",
  None, None, None, None,
  "$x^2+y^2=r^2$, $r^2=4$, $r=2$",
  "$x^2+y^2=r^2$, $r^2=4$, $r=2$")

t(23,
  "Distance from $(1,2)$ to $(4,6)$ is ____",
  "Kho\\u1ea3ng c\\u00e1ch t\\u1eeb $(1,2)$ \\u0111\\u1ebfn $(4,6)$ l\\u00e0 ____",
  None, None, None, None,
  "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9+16}=5$",
  "$d = \\sqrt{(4-1)^2 + (6-2)^2} = \\sqrt{9+16}=5$")

t(24,
  "Focal length of $\\frac{x^2}{9} + \\frac{y^2}{4} = 1$ is",
  "Ti\\u00eau c\\u1ef1 c\\u1ee7a $\\frac{x^2}{9} + \\frac{y^2}{4} = 1$ l\\u00e0",
  None, None, None, None,
  "$a^2=9$, $b^2=4$, $c^2 = a^2-b^2 = 5$, focal length $2c = 2\\sqrt{5}$",
  "$a^2=9$, $b^2=4$, $c^2 = a^2-b^2 = 5$, ti\\u00eau c\\u1ef1 $2c = 2\\sqrt{5}$")

t(25,
  "Focus of $y^2 = 8x$ is at (____, 0)",
  "Ti\\u00eau \\u0111i\\u1ec3m c\\u1ee7a $y^2 = 8x$ t\\u1ea1i (____, 0)",
  None, None, None, None,
  "$y^2 = 2px$, $2p=8$, $p=4$, focus $(\\frac{p}{2}, 0) = (2, 0)$",
  "$y^2 = 2px$, $2p=8$, $p=4$, ti\\u00eau \\u0111i\\u1ec3m $(\\frac{p}{2}, 0) = (2, 0)$")

t(26,
  "Asymptotes of $\\frac{x^2}{3} - \\frac{y^2}{4} = 1$",
  "Ti\\u1ec7m c\\u1eadn c\\u1ee7a $\\frac{x^2}{3} - \\frac{y^2}{4} = 1$",
  None, None, None, None,
  "$a^2=3$, $b^2=4$, asymptotes $y = \\pm\\frac{b}{a}x = \\pm\\frac{2}{\\sqrt{3}}x$",
  "$a^2=3$, $b^2=4$, ti\\u1ec7m c\\u1eadn $y = \\pm\\frac{b}{a}x = \\pm\\frac{2}{\\sqrt{3}}x$")

t(27,
  "Derivative of $f(x)=x^2$ at $x=2$ is",
  "\\u0110\\u1ea1o h\\u00e0m c\\u1ee7a $f(x)=x^2$ t\\u1ea1i $x=2$ l\\u00e0",
  None, None, None, None,
  "$f'(x)=2x$, $f'(2)=4$",
  "$f'(x)=2x$, $f'(2)=4$")

t(28,
  "Derivative of $f(x)=\\sin x$ at $x=\\frac{\\pi}{3}$ is ____",
  "\\u0110\\u1ea1o h\\u00e0m c\\u1ee7a $f(x)=\\sin x$ t\\u1ea1i $x=\\frac{\\pi}{3}$ l\\u00e0 ____",
  None, None, None, None,
  "$f'(x)=\\cos x$, $f'(\\frac{\\pi}{3})=\\cos\\frac{\\pi}{3}=\\frac{1}{2}$",
  "$f'(x)=\\cos x$, $f'(\\frac{\\pi}{3})=\\cos\\frac{\\pi}{3}=\\frac{1}{2}$")

t(29,
  "The local maximum of $f(x)=x^3-3x$ is",
  "C\\u1ef1c \\u0111\\u1ea1i c\\u1ee7a $f(x)=x^3-3x$ l\\u00e0",
  None, None, None, None,
  "$f'(x)=3x^2-3=0$, $x=\\pm1$. $f''(x)=6x$, $f''(-1)=-6<0$ so $x=-1$ is a local max, $f(-1)=-1+3=2$",
  "$f'(x)=3x^2-3=0$, $x=\\pm1$. $f''(x)=6x$, $f''(-1)=-6<0$ n\\u00ean $x=-1$ l\\u00e0 \\u0111i\\u1ec3m c\\u1ef1c \\u0111\\u1ea1i, $f(-1)=-1+3=2$")

t(30,
  "Tangent to $f(x)=\\ln x$ at $x=1$: $y =$ ____",
  "Ti\\u1ebfp tuy\\u1ebfn c\\u1ee7a $f(x)=\\ln x$ t\\u1ea1i $x=1$: $y =$ ____",
  None, None, None, None,
  "$f'(x)=\\frac{1}{x}$, $f'(1)=1$, $f(1)=0$, $y = 1\\times(x-1)+0 = x-1$",
  "$f'(x)=\\frac{1}{x}$, $f'(1)=1$, $f(1)=0$, $y = 1\\times(x-1)+0 = x-1$")

t(31,
  "Max of $f(x)=x^3-6x^2+9x+1$ on $[0,4]$",
  "Gi\\u00e1 tr\\u1ecb l\\u1edbn nh\\u1ea5t c\\u1ee7a $f(x)=x^3-6x^2+9x+1$ tr\\u00ean $[0,4]$",
  None, None, None, None,
  "$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0$, $x=1,3$. $f(0)=1$, $f(1)=5$, $f(3)=1$, $f(4)=5$. Max = $5$.",
  "$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0$, $x=1,3$. $f(0)=1$, $f(1)=5$, $f(3)=1$, $f(4)=5$. Max = $5$.")

t(32,
  "Given $A=\\{1,2,3\\}$, $B=\\{2,3,4\\}$, find $A\\cap B$",
  "Cho $A=\\{1,2,3\\}$, $B=\\{2,3,4\\}$, t\\u00ecm $A\\cap B$",
  None, None, None, None,
  "$A\\cap B = \\{2,3\\}$",
  "$A\\cap B = \\{2,3\\}$")

t(33,
  "Given $A=\\{x\\mid x>2\\}$, $B=\\{x\\mid x\\le 5\\}$, find $A\\cup B$ in $\\mathbb{R}$",
  "Cho $A=\\{x\\mid x>2\\}$, $B=\\{x\\mid x\\le 5\\}$, t\\u00ecm $A\\cup B$ trong $\\mathbb{R}$",
  None, None, None, None,
  "On the real line, $A\\cup B$ covers all real numbers, so it is $\\mathbb{R}$",
  "Tr\\u00ean tr\\u1ee5c s\\u1ed1 th\\u1ef1c, $A\\cup B$ ph\\u1ee7 to\\u00e0n b\\u1ed9 s\\u1ed1 th\\u1ef1c, k\\u1ebft qu\\u1ea3 l\\u00e0 $\\mathbb{R}$")

t(34,
  "For $x\\in\\mathbb{R}$, '$x=1$' is a _____ condition for '$x^2=1$'",
  "V\\u1edbi $x\\in\\mathbb{R}$, '$x=1$' l\\u00e0 \\u0111i\\u1ec1u ki\\u1ec7n _____ c\\u1ee7a '$x^2=1$'",
  json.dumps(["A. Necessary and sufficient condition",
               "B. Sufficient but not necessary condition",
               "C. Necessary but not sufficient condition",
               "D. Neither sufficient nor necessary condition"]),
  json.dumps(["A. \\u0110i\\u1ec1u ki\\u1ec7n c\\u1ea7n v\\u00e0 \\u0111\\u1ee7",
               "B. \\u0110i\\u1ec1u ki\\u1ec7n \\u0111\\u1ee7 nh\\u01b0ng kh\\u00f4ng c\\u1ea7n",
               "C. \\u0110i\\u1ec1u ki\\u1ec7n c\\u1ea7n nh\\u01b0ng kh\\u00f4ng \\u0111\\u1ee7",
               "D. Kh\\u00f4ng \\u0111\\u1ee7 v\\u00e0 kh\\u00f4ng c\\u1ea7n"]),
  None, None,
  "$x=1\\Rightarrow x^2=1$, but $x^2=1\\Rightarrow x=\\pm1$, so it is sufficient but not necessary",
  "$x=1\\Rightarrow x^2=1$, nh\\u01b0ng $x^2=1\\Rightarrow x=\\pm1$, n\\u00ean l\\u00e0 \\u0111i\\u1ec1u ki\\u1ec7n \\u0111\\u1ee7 nh\\u01b0ng kh\\u00f4ng c\\u1ea7n")

t(35,
  "Number of subsets of $\\{1,2,3\\}$ is ____",
  "S\\u1ed1 t\\u1eadp con c\\u1ee7a $\\{1,2,3\\}$ l\\u00e0 ____",
  None, None, None, None,
  "$2^3 = 8$: $\\emptyset,\\{1\\},\\{2\\},\\{3\\},\\{1,2\\},\\{1,3\\},\\{2,3\\},\\{1,2,3\\}$",
  "$2^3 = 8$: $\\emptyset,\\{1\\},\\{2\\},\\{3\\},\\{1,2\\},\\{1,3\\},\\{2,3\\},\\{1,2,3\\}$")

t(36,
  "For $x\\in\\mathbb{R}$, '$x>2$' is a _____ condition for '$x^2>4$'",
  "V\\u1edbi $x\\in\\mathbb{R}$, '$x>2$' l\\u00e0 \\u0111i\\u1ec1u ki\\u1ec7n _____ c\\u1ee7a '$x^2>4$'",
  json.dumps(["A. Necessary and sufficient condition",
               "B. Sufficient but not necessary condition",
               "C. Necessary but not sufficient condition",
               "D. Neither sufficient nor necessary condition"]),
  json.dumps(["A. \\u0110i\\u1ec1u ki\\u1ec7n c\\u1ea7n v\\u00e0 \\u0111\\u1ee7",
               "B. \\u0110i\\u1ec1u ki\\u1ec7n \\u0111\\u1ee7 nh\\u01b0ng kh\\u00f4ng c\\u1ea7n",
               "C. \\u0110i\\u1ec1u ki\\u1ec7n c\\u1ea7n nh\\u01b0ng kh\\u00f4ng \\u0111\\u1ee7",
               "D. Kh\\u00f4ng \\u0111\\u1ee7 v\\u00e0 kh\\u00f4ng c\\u1ea7n"]),
  None, None,
  "$x>2\\Rightarrow x^2>4$, but $x^2>4\\Rightarrow x<-2$ or $x>2$, so sufficient but not necessary",
  "$x>2\\Rightarrow x^2>4$, nh\\u01b0ng $x^2>4\\Rightarrow x<-2$ ho\\u1eb7c $x>2$, n\\u00ean \\u0111\\u1ee7 nh\\u01b0ng kh\\u00f4ng c\\u1ea7n")

t(37,
  "$(1+i)^2 =$",
  "$(1+i)^2 =$",
  None, None, None, None,
  "$(1+i)^2 = 1+2i+i^2 = 1+2i-1 = 2i$",
  "$(1+i)^2 = 1+2i+i^2 = 1+2i-1 = 2i$")

t(38,
  "Solve $z^2 = -1$: $z =$ ____ (using $i$)",
  "Gi\\u1ea3i $z^2 = -1$: $z =$ ____ (d\\u00f9ng $i$)",
  None, None, None, None,
  "$i^2=-1$ and $(-i)^2=-1$, so $z=\\pm i$",
  "$i^2=-1$ v\\u00e0 $(-i)^2=-1$, v\\u1eady $z=\\pm i$")

t(39,
  "Given $\\vec{a}=(1,2)$, $\\vec{b}=(3,4)$, find $\\vec{a}\\cdot\\vec{b}$",
  "Cho $\\vec{a}=(1,2)$, $\\vec{b}=(3,4)$, t\\u00ednh $\\vec{a}\\cdot\\vec{b}$",
  None, None, None, None,
  "$\\vec{a}\\cdot\\vec{b} = 1\\times3 + 2\\times4 = 11$",
  "$\\vec{a}\\cdot\\vec{b} = 1\\times3 + 2\\times4 = 11$")

t(40,
  "Given $|\\vec{a}|=2$, $|\\vec{b}|=3$, angle $60\\degree$, find $\\vec{a}\\cdot\\vec{b} =$ ____",
  "Cho $|\\vec{a}|=2$, $|\\vec{b}|=3$, g\\u00f3c $60\\degree$, t\\u00ednh $\\vec{a}\\cdot\\vec{b} =$ ____",
  None, None, None, None,
  "$\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos 60\\degree = 2\\times3\\times\\frac{1}{2} = 3$",
  "$\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos 60\\degree = 2\\times3\\times\\frac{1}{2} = 3$")

t(41,
  "Given $\\vec{a}=(1,2)$, $\\vec{b}=(2,1)$, find $\\cos\\theta$ between them",
  "Cho $\\vec{a}=(1,2)$, $\\vec{b}=(2,1)$, t\\u00ecm $\\cos\\theta$ gi\\u1eefa ch\\u00fang",
  None, None, None, None,
  "$\\vec{a}\\cdot\\vec{b}=4$, $|\\vec{a}|=|\\vec{b}|=\\sqrt{5}$, $\\cos\\theta=\\frac{4}{5}$",
  "$\\vec{a}\\cdot\\vec{b}=4$, $|\\vec{a}|=|\\vec{b}|=\\sqrt{5}$, $\\cos\\theta=\\frac{4}{5}$")

t(42,
  "Given $M=\\{-2,-1,0,1,2\\}$, $N=\\{x\\mid x^2-x-6\\geq 0\\}$, find $M\\cap N=$",
  "Cho $M=\\{-2,-1,0,1,2\\}$, $N=\\{x\\mid x^2-x-6\\geq 0\\}$, t\\u00ecm $M\\cap N=$",
  None, None, None, None,
  "$x^2-x-6\\geq 0 \\Rightarrow x\\leq -2$ or $x\\geq 3$, so $M\\cap N=\\{-2\\}$",
  "$x^2-x-6\\geq 0 \\Rightarrow x\\leq -2$ ho\\u1eb7c $x\\geq 3$, v\\u1eady $M\\cap N=\\{-2\\}$")

t(43,
  "Given $z=\\frac{1-i}{2+2i}$, find $z-\\bar{z}=$",
  "Cho $z=\\frac{1-i}{2+2i}$, t\\u00ednh $z-\\bar{z}=$",
  None, None, None, None,
  "$z=\\frac{1-i}{2(1+i)}=\\frac{(1-i)^2}{2(1+i)(1-i)}=\\frac{-2i}{4}=-\\frac{i}{2}$, $\\bar{z}=\\frac{i}{2}$, $z-\\bar{z}=-i$",
  "$z=\\frac{1-i}{2(1+i)}=\\frac{(1-i)^2}{2(1+i)(1-i)}=\\frac{-2i}{4}=-\\frac{i}{2}$, $\\bar{z}=\\frac{i}{2}$, $z-\\bar{z}=-i$")

t(44,
  "If $f(x)=2^{x(x-a)}$ is decreasing on $(0,1)$, find $a$ range.",
  "N\\u1ebfu $f(x)=2^{x(x-a)}$ ngh\\u1ecbch bi\\u1ebfn tr\\u00ean $(0,1)$, t\\u00ecm kho\\u1ea3ng $a$.",
  None, None, None, None,
  "$g(x)=x(x-a)=x^2-ax$. $f(x)=2^{g(x)}$ decreasing iff $g(x)$ decreasing. $g'(x)=2x-a$. For $g'(x)\\leq 0$ on $(0,1)$: $a\\geq 2x$ $\\forall x$, so $a\\geq 2$.",
  "$g(x)=x(x-a)=x^2-ax$. $f(x)=2^{g(x)}$ ngh\\u1ecbch bi\\u1ebfn khi $g(x)$ ngh\\u1ecbch bi\\u1ebfn. $g'(x)=2x-a$. \\u0110\\u1ec3 $g'(x)\\leq 0$ tr\\u00ean $(0,1)$: $a\\geq 2x$ $\\forall x$, suy ra $a\\geq 2$.")

t(45,
  "Two tangents from $(0,-2)$ to $x^2+y^2-4x-1=0$, angle $\\alpha$. Find $\\sin\\alpha=$",
  "Hai ti\\u1ebfp tuy\\u1ebfn t\\u1eeb $(0,-2)$ \\u0111\\u1ebfn $x^2+y^2-4x-1=0$, g\\u00f3c $\\alpha$. T\\u00ecm $\\sin\\alpha=$",
  None, None, None, None,
  "Circle $(x-2)^2+y^2=5$, center $(2,0)$, radius $\\sqrt{5}$, tangent length $\\sqrt{3}$. $\\sin\\frac{\\alpha}{2}=\\frac{\\sqrt{5}}{\\sqrt{8}}$, so $\\sin\\alpha=\\frac{\\sqrt{15}}{4}$.",
  "\\u0110\\u01b0\\u1eddng tr\\u00f2n $(x-2)^2+y^2=5$, t\\u00e2m $(2,0)$, b\\u00e1n k\\u00ednh $\\sqrt{5}$, \\u0111\\u1ed9 d\\u00e0i ti\\u1ebfp tuy\\u1ebfn $\\sqrt{3}$. $\\sin\\frac{\\alpha}{2}=\\frac{\\sqrt{5}}{\\sqrt{8}}$, suy ra $\\sin\\alpha=\\frac{\\sqrt{15}}{4}$.")

t(46,
  "Given $\\sin(\\alpha-\\beta)=\\frac{1}{3}$, $\\cos\\alpha\\sin\\beta=\\frac{1}{6}$, find $\\cos(2\\alpha+2\\beta)=$",
  "Cho $\\sin(\\alpha-\\beta)=\\frac{1}{3}$, $\\cos\\alpha\\sin\\beta=\\frac{1}{6}$, t\\u00ecm $\\cos(2\\alpha+2\\beta)=$",
  None, None, None, None,
  "From $\\sin(\\alpha-\\beta)=\\frac{1}{3}$ and $\\cos\\alpha\\sin\\beta=\\frac{1}{6}$: $\\sin\\alpha\\cos\\beta=\\frac{1}{2}$, $\\sin(\\alpha+\\beta)=\\frac{2}{3}$, $\\cos(2\\alpha+2\\beta)=1-2\\sin^2(\\alpha+\\beta)=\\frac{1}{9}$.",
  "T\\u1eeb $\\sin(\\alpha-\\beta)=\\frac{1}{3}$ v\\u00e0 $\\cos\\alpha\\sin\\beta=\\frac{1}{6}$: $\\sin\\alpha\\cos\\beta=\\frac{1}{2}$, $\\sin(\\alpha+\\beta)=\\frac{2}{3}$, $\\cos(2\\alpha+2\\beta)=1-2\\sin^2(\\alpha+\\beta)=\\frac{1}{9}$.")

t(47,
  "Complex $z$ with $|z|=1$, find max $|z-1-i|$ ____",
  "Ph\\u1ee9c $z$ v\\u1edbi $|z|=1$, t\\u00ecm max $|z-1-i|$ ____",
  None, None, None, None,
  "Geometric: distance from unit circle to $(1,1)$. Max = center-to-point distance + radius $= \\sqrt{2}+1$.",
  "H\\u00ecnh h\\u1ecdc: kho\\u1ea3ng c\\u00e1ch t\\u1eeb \\u0111\\u01b0\\u1eddng tr\\u00f2n \\u0111\\u01a1n v\\u1ecb \\u0111\\u1ebfn $(1,1)$. Max = kho\\u1ea3ng c\\u00e1ch t\\u00e2m \\u0111\\u1ebfn \\u0111i\\u1ec3m + b\\u00e1n k\\u00ednh $= \\sqrt{2}+1$.")

t(48,
  "A school samples 60 students from junior (400) and senior (200) via stratified sampling. Number of methods?",
  "M\\u1ed9t tr\\u01b0\\u1eddng l\\u1ea5y m\\u1eabu 60 h\\u1ecdc sinh t\\u1eeb THCS (400) v\\u00e0 THPT (200) b\\u1eb1ng ph\\u00e2n t\\u1ea7ng. S\\u1ed1 c\\u00e1ch?",
  json.dumps(["A. $C_{400}^{45}\\cdot C_{200}^{15}$",
               "B. $C_{400}^{20}\\cdot C_{200}^{40}$",
               "C. $C_{400}^{30}\\cdot C_{200}^{30}$",
               "D. $C_{400}^{40}\\cdot C_{200}^{20}$"]),
  json.dumps(["A. $C_{400}^{45}\\cdot C_{200}^{15}$",
               "B. $C_{400}^{20}\\cdot C_{200}^{40}$",
               "C. $C_{400}^{30}\\cdot C_{200}^{30}$",
               "D. $C_{400}^{40}\\cdot C_{200}^{20}$"]),
  None, None,
  "Stratified: $60\\times\\frac{400}{600}=40$ junior, $60\\times\\frac{200}{600}=20$ senior. Ways: $C_{400}^{40}\\cdot C_{200}^{20}$.",
  "Ph\\u00e2n t\\u1ea7ng: $60\\times\\frac{400}{600}=40$ THCS, $60\\times\\frac{200}{600}=20$ THPT. S\\u1ed1 c\\u00e1ch: $C_{400}^{40}\\cdot C_{200}^{20}$.")

t(49,
  "Ellipse $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$, foci $F_1,F_2$. $y=x$ meets at $A,B$, area $[F_1AB]=2[F_2AB]$. Find eccentricity.",
  "Elip $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$, ti\\u00eau $F_1,F_2$. $y=x$ c\\u1eaft t\\u1ea1i $A,B$, di\\u1ec7n t\\u00edch $[F_1AB]=2[F_2AB]$. T\\u00ecm t\\u00e2m sai.",
  None, None, None, None,
  "By symmetry, distance ratio from $F_1,F_2$ to $y=x$ is $2:1$. $F_1(-c,0),F_2(c,0)$: distance formula gives $1:1$. From area ratio: $e=\\frac{c}{a}=\\frac{1}{3}$.",
  "\\u0110\\u1ed1i x\\u1ee9ng, t\\u1ec9 s\\u1ed1 kho\\u1ea3ng c\\u00e1ch t\\u1eeb $F_1,F_2$ \\u0111\\u1ebfn $y=x$ l\\u00e0 $2:1$. $F_1(-c,0),F_2(c,0)$: c\\u00f4ng th\\u1ee9c kho\\u1ea3ng c\\u00e1ch cho $1:1$. T\\u1eeb t\\u1ec9 s\\u1ed1 di\\u1ec7n t\\u00edch: $e=\\frac{c}{a}=\\frac{1}{3}$.")

t(50,
  "Let $S_n$ be sum of $n$ terms of geometric $\\{a_n\\}$. $S_4=-5$, $S_6=21S_2$. Find $S_8=$",
  "G\\u1ecdi $S_n$ l\\u00e0 t\\u1ed5ng $n$ s\\u1ed1 h\\u1ea1ng c\\u1ee7a c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$. $S_4=-5$, $S_6=21S_2$. T\\u00ecm $S_8=$",
  None, None, None, None,
  "From $S_6=21S_2$ and geometric sum formula: $q=-2$, $a_1=-1$, $S_8=\\frac{a_1(1-q^8)}{1-q}=-85$.",
  "T\\u1eeb $S_6=21S_2$ v\\u00e0 c\\u00f4ng th\\u1ee9c t\\u1ed5ng: $q=-2$, $a_1=-1$, $S_8=\\frac{a_1(1-q^8)}{1-q}=-85$.")

# ===== DATABASE UPDATE =====
print(f"Loaded {len(translations)} translations.")

def update_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for trans in translations:
        (id_val, content_en, content_vi, options_en, options_vi,
         answer_en, answer_vi, solution_en, solution_vi) = trans

        # Get original values for fallback
        cur.execute("SELECT options, answer FROM questions WHERE id = ?", (id_val,))
        r = cur.fetchone()
        if not r:
            print(f"  WARNING: Q{id_val} not found")
            continue
        orig_opts, orig_ans = r

        if options_en is None:
            options_en = orig_opts
        if options_vi is None:
            options_vi = orig_opts
        if answer_en is None:
            answer_en = orig_ans
        if answer_vi is None:
            answer_vi = orig_ans

        cur.execute("""
            UPDATE questions SET
                content_en = ?, content_vi = ?,
                options_en = ?, options_vi = ?,
                answer_en = ?, answer_vi = ?,
                solution_en = ?, solution_vi = ?
            WHERE id = ?
        """, (content_en, content_vi,
              options_en, options_vi,
              answer_en, answer_vi,
              solution_en, solution_vi,
              id_val))
        print(f"  Updated Q{id_val}")

    conn.commit()
    conn.close()
    print(f"\nDone! {len(translations)} questions updated successfully.")

if __name__ == "__main__":
    update_db()
