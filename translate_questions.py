#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate Chinese math questions to English and Vietnamese.
Reads questions from math_rpg.db where content_en IS NULL,
translates them, and updates the database. Commits after each UPDATE.
"""

import sqlite3

DB_PATH = r'D:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

# Translation data for questions 66-100
# {id: {content_en, content_vi, options_en, options_vi, answer_en, answer_vi, solution_en, solution_vi}}

T = {}

# ===== ID: 66, 正三棱柱 =====
T[66] = {
    "content_en": "In a regular triangular prism $ABC-A_1B_1C_1$, $AB=AA_1=1$, point $P$ satisfies $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, where $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$, then",
    "content_vi": "Trong l\u0103ng tr\u1ee5 tam gi\u00e1c \u0111\u1ec1u $ABC-A_1B_1C_1$, $AB=AA_1=1$, \u0111i\u1ec3m $P$ th\u1ecfa m\u00e3n $\\vec{BP}=\\lambda\\vec{BC}+\\mu\\vec{BB_1}$, v\u1edbi $\\lambda\\in[0,1]$, $\\mu\\in[0,1]$, khi \u0111\u00f3",
    "options_en": '["A. When $\\\\lambda=1$, the perimeter of $\\\\triangle AB_1P$ is constant","B. When $\\\\mu=1$, the volume of tetrahedron $P-A_1BC$ is constant","C. When $\\\\lambda=\\\\frac{1}{2}$, there is one and only one point $P$ such that $A_1P\\\\perp BP$","D. When $\\\\mu=\\\\frac{1}{2}$, there is one and only one point $P$ such that $A_1B\\\\perp$ plane $AB_1P$"]',
    "options_vi": '["A. Khi $\\\\lambda=1$, chu vi c\u1ee7a $\\\\triangle AB_1P$ l\u00e0 h\u1eb1ng s\u1ed1","B. Khi $\\\\mu=1$, th\u1ec3 t\u00edch c\u1ee7a h\u00ecnh ch\u00f3p $P-A_1BC$ l\u00e0 h\u1eb1ng s\u1ed1","C. Khi $\\\\lambda=\\\\frac{1}{2}$, c\u00f3 duy nh\u1ea5t m\u1ed9t \u0111i\u1ec3m $P$ sao cho $A_1P\\\\perp BP$","D. Khi $\\\\mu=\\\\frac{1}{2}$, c\u00f3 duy nh\u1ea5t m\u1ed9t \u0111i\u1ec3m $P$ sao cho $A_1B\\\\perp$ m\u1eb7t ph\u1eb3ng $AB_1P$"]',
    "answer_en": "B",
    "answer_vi": "B",
    "solution_en": "When $\\mu=1$, $P$ moves on $B_1C_1$. The base area and height of tetrahedron $P-A_1BC$ remain unchanged, so its volume is constant.",
    "solution_vi": "Khi $\\mu=1$, $P$ di chuy\u1ec3n tr\u00ean $B_1C_1$. Di\u1ec7n t\u00edch \u0111\u00e1y v\u00e0 chi\u1ec1u cao c\u1ee7a h\u00ecnh ch\u00f3p $P-A_1BC$ kh\u00f4ng \u0111\u1ed5i, do \u0111\u00f3 th\u1ec3 t\u00edch l\u00e0 h\u1eb1ng s\u1ed1.",
}

# ===== ID: 67, 剪纸 =====
T[67] = {
    "content_en": "Students at a school, while studying folk paper-cutting art, found that paper is often folded along a symmetric axis. For a rectangular paper of size $20dm\\times 12dm$, after 1 fold, two specifications $10dm\\times 12dm$ and $20dm\\times 6dm$ are obtained, with total area $S_1=240dm^2$; after 2 folds, three specifications $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$ are obtained, with total area $S_2=180dm^2$, and so on. Then the number of different specifications obtained after 4 folds is ____; if folded $n$ times, then $\\sum_{k=1}^{n} S_k =$ ____ $dm^2$.",
    "content_vi": "H\u1ecdc sinh \u1edf m\u1ed9t tr\u01b0\u1eddng khi nghi\u00ean c\u1ee9u ngh\u1ec7 thu\u1eadt c\u1eaft gi\u1ea5y d\u00e2n gian ph\u00e1t hi\u1ec7n r\u1eb1ng khi c\u1eaft gi\u1ea5y th\u01b0\u1eddng g\u1ea5p gi\u1ea5y d\u1ecdc theo m\u1ed9t tr\u1ee5c \u0111\u1ed1i x\u1ee9ng. T\u1edd gi\u1ea5y h\u00ecnh ch\u1eef nh\u1eadt k\u00edch th\u01b0\u1edbc $20dm\\times 12dm$, g\u1ea5p 1 l\u1ea7n \u0111\u01b0\u1ee3c hai lo\u1ea1i $10dm\\times 12dm$ v\u00e0 $20dm\\times 6dm$, t\u1ed5ng di\u1ec7n t\u00edch $S_1=240dm^2$; g\u1ea5p 2 l\u1ea7n \u0111\u01b0\u1ee3c ba lo\u1ea1i $5dm\\times 12dm$, $10dm\\times 6dm$, $20dm\\times 3dm$, t\u1ed5ng di\u1ec7n t\u00edch $S_2=180dm^2$, c\u1ee9 nh\u01b0 v\u1eady. S\u1ed1 lo\u1ea1i k\u00edch th\u01b0\u1edbc kh\u00e1c nhau sau 4 l\u1ea7n g\u1ea5p l\u00e0 ____; n\u1ebfu g\u1ea5p $n$ l\u1ea7n, th\u00ec $\\sum_{k=1}^{n} S_k =$ ____ $dm^2$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "5, 720(1-1/2^n)",
    "answer_vi": "5, 720(1-1/2^n)",
    "solution_en": "After $k$ folds, there are $k+1$ specifications. $S_k=240\\times k\\times (\\frac{1}{2})^{k-1}$. Summing gives $720(1-\\frac{1}{2^n})$.",
    "solution_vi": "Sau $k$ l\u1ea7n g\u1ea5p c\u00f3 $k+1$ lo\u1ea1i k\u00edch th\u01b0\u1edbc. $S_k=240\\times k\\times (\\frac{1}{2})^{k-1}$. T\u1ed5ng l\u00e0 $720(1-\\frac{1}{2^n})$.",
}

# ===== ID: 68, 三角形边角 =====
T[68] = {
    "content_en": "In $\\triangle ABC$, the sides opposite to interior angles $A,B,C$ are $a,b,c$ respectively. Given $b^2=ac$, point $D$ is on side $AC$, $BD\\sin\\angle ABC=a\\sin C$. (1) Prove: $BD=b$; (2) If $AD=2DC$, find $\\cos\\angle ABC$.",
    "content_vi": "Trong $\\triangle ABC$, c\u00e1c c\u1ea1nh \u0111\u1ed1i di\u1ec7n v\u1edbi c\u00e1c g\u00f3c trong $A,B,C$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 $a,b,c$. Cho $b^2=ac$, \u0111i\u1ec3m $D$ n\u1eb1m tr\u00ean c\u1ea1nh $AC$, $BD\\sin\\angle ABC=a\\sin C$. (1) Ch\u1ee9ng minh: $BD=b$; (2) N\u1ebfu $AD=2DC$, t\u00ecm $\\cos\\angle ABC$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "Proof given, cos\u2220ABC=7/12",
    "answer_vi": "Ch\u1ee9ng minh \u0111\u01b0\u1ee3c cho, cos\u2220ABC=7/12",
    "solution_en": "(1) By the law of sines $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, combined with the given condition, we can prove $BD=b$. (2) By the law of cosines $\\cos\\angle ABC=\\frac{7}{12}$.",
    "solution_vi": "(1) Theo \u0111\u1ecbnh l\u00fd sin $\\frac{BD}{\\sin C}=\\frac{a}{\\sin\\angle BDC}$, k\u1ebft h\u1ee3p v\u1edbi \u0111i\u1ec1u ki\u1ec7n \u0111\u00e3 cho, ta ch\u1ee9ng minh \u0111\u01b0\u1ee3c $BD=b$. (2) Theo \u0111\u1ecbnh l\u00fd cos $\\cos\\angle ABC=\\frac{7}{12}$.",
}

# ===== ID: 69, 冬奥志愿者 =====
T[69] = {
    "content_en": "5 volunteers for the Beijing Winter Olympics are to be assigned to 4 events: figure skating, short track speed skating, ice hockey, and curling for training. Each volunteer is assigned to exactly one event, and each event gets at least one volunteer. The number of different assignment schemes is",
    "content_vi": "5 t\u00ecnh nguy\u1ec7n vi\u00ean Th\u1ebf v\u1eadn h\u1ed9i M\u00f9a \u0111\u00f4ng B\u1eafc Kinh \u0111\u01b0\u1ee3c ph\u00e2n c\u00f4ng \u0111\u1ebfn 4 m\u00f4n: tr\u01b0\u1ee3t b\u0103ng ngh\u1ec7 thu\u1eadt, tr\u01b0\u1ee3t b\u0103ng t\u1ed1c \u0111\u1ed9 c\u1ef1 ly ng\u1eafn, kh\u00fac c\u00f4n c\u1ea7u tr\u00ean b\u0103ng v\u00e0 bi \u0111\u00e1 tr\u00ean b\u0103ng \u0111\u1ec3 hu\u1ea5n luy\u1ec7n. M\u1ed7i t\u00ecnh nguy\u1ec7n vi\u00ean ch\u1ec9 \u0111\u01b0\u1ee3c ph\u00e2n \u0111\u1ebfn 1 m\u00f4n, m\u1ed7i m\u00f4n c\u00f3 \u00edt nh\u1ea5t 1 t\u00ecnh nguy\u1ec7n vi\u00ean. S\u1ed1 c\u00e1ch ph\u00e2n c\u00f4ng kh\u00e1c nhau l\u00e0",
    "options_en": '["A. 60","B. 120","C. 240","D. 480"]',
    "options_vi": '["A. 60","B. 120","C. 240","D. 480"]',
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "First group then assign. Divide 5 people into 4 groups (one group must have 2 people). Choose 2 people as one group: $C_5^2=10$ ways, the remaining are single. Permute the 4 groups: $4!=24$. Total $10\\times 24=240$.",
    "solution_vi": "\u0110\u1ea7u ti\u00ean chia nh\u00f3m r\u1ed3i ph\u00e2n c\u00f4ng. Chia 5 ng\u01b0\u1eddi th\u00e0nh 4 nh\u00f3m (m\u1ed9t nh\u00f3m ph\u1ea3i c\u00f3 2 ng\u01b0\u1eddi). Ch\u1ecdn 2 ng\u01b0\u1eddi l\u00e0m m\u1ed9t nh\u00f3m: $C_5^2=10$ c\u00e1ch, c\u00f2n l\u1ea1i l\u00e0 c\u00e1c nh\u00f3m \u0111\u01a1n. Ho\u00e1n v\u1ecb 4 nh\u00f3m: $4!=24$. T\u1ed5ng s\u1ed1 $10\\times 24=240$.",
}

# ===== ID: 70, 场馆志愿者 =====
T[70] = {
    "content_en": "6 students go to three venues A, B, C as volunteers. Each student goes to exactly one venue. Venue A gets 1 student, venue B gets 2 students, venue C gets 3 students. The number of different assignment methods is",
    "content_vi": "6 h\u1ecdc sinh \u0111\u1ebfn ba \u0111\u1ecba \u0111i\u1ec3m A, B, C l\u00e0m t\u00ecnh nguy\u1ec7n vi\u00ean. M\u1ed7i h\u1ecdc sinh ch\u1ec9 \u0111\u1ebfn 1 \u0111\u1ecba \u0111i\u1ec3m. \u0110\u1ecba \u0111i\u1ec3m A c\u00f3 1 h\u1ecdc sinh, \u0111\u1ecba \u0111i\u1ec3m B c\u00f3 2 h\u1ecdc sinh, \u0111\u1ecba \u0111i\u1ec3m C c\u00f3 3 h\u1ecdc sinh. S\u1ed1 c\u00e1ch ph\u00e2n c\u00f4ng kh\u00e1c nhau l\u00e0",
    "options_en": '["A. 120","B. 90","C. 60","D. 30"]',
    "options_vi": '["A. 120","B. 90","C. 60","D. 30"]',
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times 10\\times 1 = 60$.",
    "solution_vi": "$C_6^1\\times C_5^2\\times C_3^3 = 6\\times 10\\times 1 = 60$.",
}

# ===== ID: 71, 足球游泳 =====
T[71] = {
    "content_en": "Students at a high school actively participate in sports. 96% of students like football or swimming, 60% like football, 82% like swimming. The percentage of students who like both football and swimming is",
    "content_vi": "H\u1ecdc sinh \u1edf m\u1ed9t tr\u01b0\u1eddng trung h\u1ecdc t\u00edch c\u1ef1c tham gia th\u1ec3 thao. 96% h\u1ecdc sinh th\u00edch b\u00f3ng \u0111\u00e1 ho\u1eb7c b\u01a1i l\u1ed9i, 60% th\u00edch b\u00f3ng \u0111\u00e1, 82% th\u00edch b\u01a1i l\u1ed9i. T\u1ec9 l\u1ec7 h\u1ecdc sinh th\u00edch c\u1ea3 b\u00f3ng \u0111\u00e1 v\u00e0 b\u01a1i l\u1ed9i l\u00e0",
    "options_en": '["A. 62%","B. 56%","C. 46%","D. 42%"]',
    "options_vi": '["A. 62%","B. 56%","C. 46%","D. 42%"]',
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "Inclusion-exclusion principle: $P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, so $P(F\\cap S)=46\\%$.",
    "solution_vi": "Nguy\u00ean l\u00fd b\u00f9 tr\u1eeb: $P(F\\cup S)=P(F)+P(S)-P(F\\cap S)$. $96\\%=60\\%+82\\%-P(F\\cap S)$, suy ra $P(F\\cap S)=46\\%$.",
}

# ===== ID: 72, 椭圆 =====
T[72] = {
    "content_en": "Given an ellipse $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ with eccentricity $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ are the left and right foci respectively, $A$ is the upper vertex of $C$, and $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$. Then the equation of $C$ is ____",
    "content_vi": "Cho elip $C: \\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ c\u00f3 t\u00e2m sai $\\frac{\\sqrt{3}}{2}$, $F_1,F_2$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 ti\u00eau \u0111i\u1ec3m tr\u00e1i v\u00e0 ph\u1ea3i, $A$ l\u00e0 \u0111\u1ec9nh tr\u00ean c\u1ee7a $C$, v\u00e0 $\\overrightarrow{AF_1}\\cdot\\overrightarrow{AF_2} = -1$. Ph\u01b0\u01a1ng tr\u00ecnh c\u1ee7a $C$ l\u00e0 ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "x\u00b2/4+y\u00b2=1",
    "answer_vi": "x\u00b2/4+y\u00b2=1",
    "solution_en": "$e=\\frac{c}{a}=\\frac{\\sqrt{3}}{2}$. Let $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_1(-\\sqrt{3}k,0),F_2(\\sqrt{3}k,0)$. Dot product $=-3k^2+k^2=-2k^2=-1$, $k=1$. Hence $a=2,b=1$.",
    "solution_vi": "$e=\\frac{c}{a}=\\frac{\\sqrt{3}}{2}$. \u0110\u1eb7t $a=2k,c=\\sqrt{3}k$, $b=k$. $A(0,k)$, $F_1(-\\sqrt{3}k,0),F_2(\\sqrt{3}k,0)$. T\u00edch v\u00f4 h\u01b0\u1edbng $=-3k^2+k^2=-2k^2=-1$, $k=1$. V\u1eady $a=2,b=1$.",
}

# ===== ID: 73, 三角形边角2 =====
T[73] = {
    "content_en": "In $\\triangle ABC$, the sides opposite to angles $A,B,C$ are $a,b,c$ respectively. Given $a=3$, $c=\\sqrt{2}$, $B=45\\degree$. (1) Find $\\sin C$; (2) Take a point $D$ on side $BC$ such that $\\cos\\angle ADC = -\\frac{4}{5}$, find $\\tan\\angle DAC$.",
    "content_vi": "Trong $\\triangle ABC$, c\u00e1c c\u1ea1nh \u0111\u1ed1i di\u1ec7n v\u1edbi c\u00e1c g\u00f3c $A,B,C$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 $a,b,c$. Cho $a=3$, $c=\\sqrt{2}$, $B=45\\degree$. (1) T\u00ecm $\\sin C$; (2) L\u1ea5y \u0111i\u1ec3m $D$ tr\u00ean c\u1ea1nh $BC$ sao cho $\\cos\\angle ADC = -\\frac{4}{5}$, t\u00ecm $\\tan\\angle DAC$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "sinC=1/3, tan\u2220DAC=2/11",
    "answer_vi": "sinC=1/3, tan\u2220DAC=2/11",
    "solution_en": "(1) Law of cosines $b^2=9+2-6\\sqrt{2}\\cdot\\frac{\\sqrt{2}}{2}=5$, $b=\\sqrt{5}$. Law of sines $\\sin C=\\frac{c\\sin B}{b}=\\frac{1}{3}$.",
    "solution_vi": "(1) \u0110\u1ecbnh l\u00fd cos $b^2=9+2-6\\sqrt{2}\\cdot\\frac{\\sqrt{2}}{2}=5$, $b=\\sqrt{5}$. \u0110\u1ecbnh l\u00fd sin $\\sin C=\\frac{c\\sin B}{b}=\\frac{1}{3}$.",
}

# ===== ID: 74, 等差数列 =====
T[74] = {
    "content_en": "Let $S_n$ be the sum of the first $n$ terms of an arithmetic sequence $\\{a_n\\}$. If $a_1\\neq 0$, $a_2=3a_1$, then $\\frac{S_{10}}{S_5}=$ ____",
    "content_vi": "G\u1ecdi $S_n$ l\u00e0 t\u1ed5ng c\u1ee7a $n$ s\u1ed1 h\u1ea1ng \u0111\u1ea7u c\u1ee7a c\u1ea5p s\u1ed1 c\u1ed9ng $\\{a_n\\}$. N\u1ebfu $a_1\\neq 0$, $a_2=3a_1$, th\u00ec $\\frac{S_{10}}{S_5}=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "4",
    "answer_vi": "4",
    "solution_en": "From $a_2=a_1+d=3a_1$, we get $d=2a_1$. $S_n=na_1+\\frac{n(n-1)}{2}d=na_1+n(n-1)a_1=n^2a_1$. $\\frac{S_{10}}{S_5}=\\frac{100}{25}=4$.",
    "solution_vi": "T\u1eeb $a_2=a_1+d=3a_1$ suy ra $d=2a_1$. $S_n=na_1+\\frac{n(n-1)}{2}d=na_1+n(n-1)a_1=n^2a_1$. $\\frac{S_{10}}{S_5}=\\frac{100}{25}=4$.",
}

# ===== ID: 75, 篮球决赛 =====
T[75] = {
    "content_en": "Two teams A and B play a basketball final, adopting a best-of-seven format (a team wins when it wins 4 games, and the final ends). Based on previous results, team A's home/away schedule is \"home, home, away, away, home, away, home\". Let the probability of team A winning at home be 0.6, and winning away be 0.5, with game results independent of each other. Then the probability of team A winning 4:1 is ____",
    "content_vi": "Hai \u0111\u1ed9i A v\u00e0 B ch\u01a1i tr\u1eadn chung k\u1ebft b\u00f3ng r\u1ed5, th\u1ec3 th\u1ee9c th\u1eafng 4 trong 7 tr\u1eadn (\u0111\u1ed9i n\u00e0o th\u1eafng 4 tr\u1eadn tr\u01b0\u1edbc l\u00e0 th\u1eafng, tr\u1eadn chung k\u1ebft k\u1ebft th\u00fac). D\u1ef1a tr\u00ean k\u1ebft qu\u1ea3 tr\u01b0\u1edbc \u0111\u00f3, l\u1ecbch s\u00e2n nh\u00e0/s\u00e2n kh\u00e1ch c\u1ee7a \u0111\u1ed9i A l\u00e0 \"nh\u00e0, nh\u00e0, kh\u00e1ch, kh\u00e1ch, nh\u00e0, kh\u00e1ch, nh\u00e0\". X\u00e1c su\u1ea5t \u0111\u1ed9i A th\u1eafng tr\u00ean s\u00e2n nh\u00e0 l\u00e0 0,6, tr\u00ean s\u00e2n kh\u00e1ch l\u00e0 0,5, k\u1ebft qu\u1ea3 c\u00e1c tr\u1eadn \u0111\u1ea5u \u0111\u1ed9c l\u1eadp v\u1edbi nhau. X\u00e1c su\u1ea5t \u0111\u1ed9i A th\u1eafng 4:1 l\u00e0 ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "0.18",
    "answer_vi": "0.18",
    "solution_en": "Team A wins 4:1 means team A wins the 5th game, and in the first 4 games team A wins 3 and loses 1. Calculate the sum of probabilities for all arrangements.",
    "solution_vi": "\u0110\u1ed9i A th\u1eafng 4:1 c\u00f3 ngh\u0129a l\u00e0 \u0111\u1ed9i A th\u1eafng tr\u1eadn th\u1ee9 5, v\u00e0 trong 4 tr\u1eadn \u0111\u1ea7u \u0111\u1ed9i A th\u1eafng 3 thua 1. T\u00ednh t\u1ed5ng x\u00e1c su\u1ea5t c\u1ee7a t\u1ea5t c\u1ea3 c\u00e1c tr\u01b0\u1eddng h\u1ee3p.",
}

# ===== ID: 76, 正弦余弦 =====
T[76] = {
    "content_en": "In $\\triangle ABC$, the sides opposite to angles $A,B,C$ are $a,b,c$ respectively. Let $(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C$. (1) Find $A$; (2) If $\\sqrt{2}a+b=2c$, find $\\sin C$.",
    "content_vi": "Trong $\\triangle ABC$, c\u00e1c c\u1ea1nh \u0111\u1ed1i di\u1ec7n v\u1edbi c\u00e1c g\u00f3c $A,B,C$ l\u1ea7n l\u01b0\u1ee3t l\u00e0 $a,b,c$. Cho $(\\sin B-\\sin C)^2=\\sin^2 A-\\sin B\\sin C$. (1) T\u00ecm $A$; (2) N\u1ebfu $\\sqrt{2}a+b=2c$, t\u00ecm $\\sin C$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "A=60\u00b0, sinC=(\u221a6+\u221a2)/4",
    "answer_vi": "A=60\u00b0, sinC=(\u221a6+\u221a2)/4",
    "solution_en": "(1) Expand to get $\\sin^2 B+\\sin^2 C-2\\sin B\\sin C = \\sin^2 A-\\sin B\\sin C$. Convert to sides using law of sines, then by law of cosines we get $A=60\\degree$.",
    "solution_vi": "(1) Khai tri\u1ec3n \u0111\u01b0\u1ee3c $\\sin^2 B+\\sin^2 C-2\\sin B\\sin C = \\sin^2 A-\\sin B\\sin C$. Chuy\u1ec3n sang c\u1ea1nh b\u1eb1ng \u0111\u1ecbnh l\u00fd sin, r\u1ed3i theo \u0111\u1ecbnh l\u00fd cos ta \u0111\u01b0\u1ee3c $A=60\\degree$.",
}

# ===== ID: 77, 向量 =====
T[77] = {
    "content_en": "Given $\\vec{AB}=(2,3)$, $\\vec{AC}=(3,t)$, $|\\vec{BC}|=1$, then $\\vec{AB}\\cdot\\vec{BC}=$",
    "content_vi": "Cho $\\vec{AB}=(2,3)$, $\\vec{AC}=(3,t)$, $|\\vec{BC}|=1$, khi \u0111\u00f3 $\\vec{AB}\\cdot\\vec{BC}=$",
    "options_en": '["A. -3","B. -2","C. 2","D. 3"]',
    "options_vi": '["A. -3","B. -2","C. 2","D. 3"]',
    "answer_en": "C",
    "answer_vi": "C",
    "solution_en": "$\\vec{BC}=\\vec{AC}-\\vec{AB}=(1,t-3)$. $|\\vec{BC}|^2=1+(t-3)^2=1$, so $t=3$. $\\vec{BC}=(1,0)$, $\\vec{AB}\\cdot\\vec{BC}=2\\times1+3\\times0=2$.",
    "solution_vi": "$\\vec{BC}=\\vec{AC}-\\vec{AB}=(1,t-3)$. $|\\vec{BC}|^2=1+(t-3)^2=1$, suy ra $t=3$. $\\vec{BC}=(1,0)$, $\\vec{AB}\\cdot\\vec{BC}=2\\times1+3\\times0=2$.",
}

# ===== ID: 78, 函数奇偶 =====
T[78] = {
    "content_en": "Let $f(x)=\\ln|2x+1|-\\ln|2x-1|$, then $f(x)$",
    "content_vi": "Cho $f(x)=\\ln|2x+1|-\\ln|2x-1|$, khi \u0111\u00f3 $f(x)$",
    "options_en": '["A. is even and increasing on $(\\\\frac{1}{2},\\\\infty)$","B. is odd and decreasing on $(-\\\\frac{1}{2},\\\\frac{1}{2})$","C. is even and increasing on $(-\\\\infty,-\\\\frac{1}{2})$","D. is odd and decreasing on $(-\\\\infty,-\\\\frac{1}{2})$"]',
    "options_vi": '["A. l\u00e0 h\u00e0m ch\u1eb5n v\u00e0 \u0111\u1ed3ng bi\u1ebfn tr\u00ean $(\\\\frac{1}{2},\\\\infty)$","B. l\u00e0 h\u00e0m l\u1ebb v\u00e0 ngh\u1ecbch bi\u1ebfn tr\u00ean $(-\\\\frac{1}{2},\\\\frac{1}{2})$","C. l\u00e0 h\u00e0m ch\u1eb5n v\u00e0 \u0111\u1ed3ng bi\u1ebfn tr\u00ean $(-\\\\infty,-\\\\frac{1}{2})$","D. l\u00e0 h\u00e0m l\u1ebb v\u00e0 ngh\u1ecbch bi\u1ebfn tr\u00ean $(-\\\\infty,-\\\\frac{1}{2})$"]',
    "answer_en": "D",
    "answer_vi": "D",
    "solution_en": "$f(-x)=\\ln|-2x+1|-\\ln|-2x-1|=\\ln|2x-1|-\\ln|2x+1|=-f(x)$, so it is odd. For $x<-\\frac{1}{2}$, $f'(x)<0$, decreasing.",
    "solution_vi": "$f(-x)=\\ln|-2x+1|-\\ln|-2x-1|=\\ln|2x-1|-\\ln|2x+1|=-f(x)$, n\u00ean l\u00e0 h\u00e0m l\u1ebb. V\u1edbi $x<-\\frac{1}{2}$, $f'(x)<0$, ngh\u1ecbch bi\u1ebfn.",
}

# ===== ID: 79, 二项式 =====
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

# ===== ID: 80, 切线 =====
T[80] = {
    "content_en": "Given that the tangent line to the curve $y=ae^x+x\\ln x$ at the point $(1,ae)$ is $y=2x+b$, then",
    "content_vi": "Cho ti\u1ebfp tuy\u1ebfn c\u1ee7a \u0111\u01b0\u1eddng cong $y=ae^x+x\\ln x$ t\u1ea1i \u0111i\u1ec3m $(1,ae)$ l\u00e0 $y=2x+b$, khi \u0111\u00f3",
    "options_en": '["A. a=e,b=-1","B. a=e,b=1","C. a=e^{-1},b=1","D. a=e^{-1},b=-1"]',
    "options_vi": '["A. a=e,b=-1","B. a=e,b=1","C. a=e^{-1},b=1","D. a=e^{-1},b=-1"]',
    "answer_en": "D",
    "answer_vi": "D",
    "solution_en": "$y'=ae^x+\\ln x+1$. At $x=1$, the slope is $ae+1=2$, so $a=e^{-1}$. The tangent $y=2x+b$ passes through $(1,1)$, so $b=-1$.",
    "solution_vi": "$y'=ae^x+\\ln x+1$. T\u1ea1i $x=1$, h\u1ec7 s\u1ed1 g\u00f3c l\u00e0 $ae+1=2$, suy ra $a=e^{-1}$. Ti\u1ebfp tuy\u1ebfn $y=2x+b$ \u0111i qua $(1,1)$, n\u00ean $b=-1$.",
}

# ===== ID: 81, 正态分布 =====
T[81] = {
    "content_en": "To study the residual levels of two types of ions A and B in mice, the following experiment was conducted: 200 mice were randomly divided into groups A and B, 100 in each. Group A was given type A ion solution, group B was given type B ion solution. The volume and molar concentration of the solution were the same for each mouse. After a period of time, the percentage of ions remaining in the mice was measured using a scientific method. The average residual percentage for mice given type A ions was 5.2, and for type B ions was 4.8. Based on the experimental data: If the residual percentage of type A ions follows a normal distribution $N(\\mu_1,\\sigma_1^2)$, find the probability that a randomly selected value falls within one standard deviation of the mean.",
    "content_vi": "\u0110\u1ec3 nghi\u00ean c\u1ee9u m\u1ee9c \u0111\u1ed9 t\u1ed3n d\u01b0 c\u1ee7a hai lo\u1ea1i ion A v\u00e0 B tr\u00ean chu\u1ed9t, ti\u1ebfn h\u00e0nh th\u00ed nghi\u1ec7m sau: 200 con chu\u1ed9t \u0111\u01b0\u1ee3c chia ng\u1eabu nhi\u00ean th\u00e0nh hai nh\u00f3m A v\u00e0 B, m\u1ed7i nh\u00f3m 100 con. Nh\u00f3m A \u0111\u01b0\u1ee3c cho dung d\u1ecbch ion lo\u1ea1i A, nh\u00f3m B \u0111\u01b0\u1ee3c cho dung d\u1ecbch ion lo\u1ea1i B. Th\u1ec3 t\u00edch v\u00e0 n\u1ed3ng \u0111\u1ed9 mol c\u1ee7a dung d\u1ecbch cho m\u1ed7i con chu\u1ed9t l\u00e0 nh\u01b0 nhau. Sau m\u1ed9t th\u1eddi gian, t\u1ec9 l\u1ec7 ph\u1ea7n tr\u0103m ion c\u00f2n l\u1ea1i trong chu\u1ed9t \u0111\u01b0\u1ee3c \u0111o b\u1eb1ng ph\u01b0\u01a1ng ph\u00e1p khoa h\u1ecdc. T\u1ec9 l\u1ec7 t\u1ed3n d\u01b0 trung b\u00ecnh c\u1ee7a ion lo\u1ea1i A l\u00e0 5,2, c\u1ee7a ion lo\u1ea1i B l\u00e0 4,8. D\u1ef1a tr\u00ean d\u1eef li\u1ec7u th\u1ef1c nghi\u1ec7m: N\u1ebfu t\u1ec9 l\u1ec7 t\u1ed3n d\u01b0 c\u1ee7a ion lo\u1ea1i A tu\u00e2n theo ph\u00e2n ph\u1ed1i chu\u1ea9n $N(\\mu_1,\\sigma_1^2)$, t\u00ecm x\u00e1c su\u1ea5t m\u1ed9t gi\u00e1 tr\u1ecb ng\u1eabu nhi\u00ean n\u1eb1m trong kho\u1ea3ng m\u1ed9t \u0111\u1ed9 l\u1ec7ch chu\u1ea9n so v\u1edbi trung b\u00ecnh.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "0.68",
    "answer_vi": "0.68",
    "solution_en": "$P(|X-\\mu|<\\sigma) \\approx 0.6827$.",
    "solution_vi": "$P(|X-\\mu|<\\sigma) \\approx 0.6827$.",
}

# ===== ID: 82, 次品概率 =====
T[82] = {
    "content_en": "A factory produces products of types A and B. The defect rate for type A is 5%, and for type B is 3%. A product is randomly selected from the factory. The probability of selecting a type A product is 0.6, and of selecting a type B product is 0.4. (1) Find the probability that the selected product is defective; (2) If the selected product is found to be defective, find the probability that it is type A.",
    "content_vi": "M\u1ed9t nh\u00e0 m\u00e1y s\u1ea3n xu\u1ea5t s\u1ea3n ph\u1ea9m lo\u1ea1i A v\u00e0 B. T\u1ec9 l\u1ec7 ph\u1ebf ph\u1ea9m c\u1ee7a lo\u1ea1i A l\u00e0 5%, lo\u1ea1i B l\u00e0 3%. M\u1ed9t s\u1ea3n ph\u1ea9m \u0111\u01b0\u1ee3c ch\u1ecdn ng\u1eabu nhi\u00ean t\u1eeb nh\u00e0 m\u00e1y. X\u00e1c su\u1ea5t ch\u1ecdn \u0111\u01b0\u1ee3c s\u1ea3n ph\u1ea9m lo\u1ea1i A l\u00e0 0,6, lo\u1ea1i B l\u00e0 0,4. (1) T\u00ecm x\u00e1c su\u1ea5t s\u1ea3n ph\u1ea9m \u0111\u01b0\u1ee3c ch\u1ecdn l\u00e0 ph\u1ebf ph\u1ea9m; (2) N\u1ebfu s\u1ea3n ph\u1ea9m \u0111\u01b0\u1ee3c ch\u1ecdn l\u00e0 ph\u1ebf ph\u1ea9m, t\u00ecm x\u00e1c su\u1ea5t n\u00f3 l\u00e0 lo\u1ea1i A.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1)0.042 (2)5/7",
    "answer_vi": "(1)0,042 (2)5/7",
    "solution_en": "(1) Law of total probability: $P(\\text{defective})=0.6\\times0.05+0.4\\times0.03=0.03+0.012=0.042$. (2) Bayes' theorem: $P(A|\\text{defective})=\\frac{0.6\\times0.05}{0.042}=\\frac{0.03}{0.042}=\\frac{5}{7}$.",
    "solution_vi": "(1) C\u00f4ng th\u1ee9c x\u00e1c su\u1ea5t \u0111\u1ea7y \u0111\u1ee7: $P(\\text{ph\u1ebf ph\u1ea9m})=0.6\\times0.05+0.4\\times0.03=0.03+0.012=0.042$. (2) \u0110\u1ecbnh l\u00fd Bayes: $P(A|\\text{ph\u1ebf ph\u1ea9m})=\\frac{0.6\\times0.05}{0.042}=\\frac{0.03}{0.042}=\\frac{5}{7}$.",
}

# ===== ID: 83, 利润最大化 =====
T[83] = {
    "content_en": "A company produces a product. The daily fixed cost is 2000 yuan, and the variable cost per product is 30 yuan. Suppose $x$ products are produced daily, and the price per product is $p=100-0.01x$ yuan. Find: (1) How many products should be produced daily to maximize profit? (2) What is the maximum profit in yuan?",
    "content_vi": "M\u1ed9t doanh nghi\u1ec7p s\u1ea3n xu\u1ea5t m\u1ed9t s\u1ea3n ph\u1ea9m. Chi ph\u00ed c\u1ed1 \u0111\u1ecbnh h\u00e0ng ng\u00e0y l\u00e0 2000 \u0111\u1ed3ng, chi ph\u00ed bi\u1ebfn \u0111\u1ed5i cho m\u1ed7i s\u1ea3n ph\u1ea9m l\u00e0 30 \u0111\u1ed3ng. Gi\u1ea3 s\u1eed s\u1ea3n xu\u1ea5t $x$ s\u1ea3n ph\u1ea9m m\u1ed7i ng\u00e0y, gi\u00e1 b\u00e1n m\u1ed7i s\u1ea3n ph\u1ea9m l\u00e0 $p=100-0.01x$ \u0111\u1ed3ng. T\u00ecm: (1) S\u1ea3n xu\u1ea5t bao nhi\u00eau s\u1ea3n ph\u1ea9m m\u1ed7i ng\u00e0y \u0111\u1ec3 l\u1ee3i nhu\u1eadn t\u1ed1i \u0111a? (2) L\u1ee3i nhu\u1eadn t\u1ed1i \u0111a l\u00e0 bao nhi\u00eau \u0111\u1ed3ng?",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1)3500 units (2)120500 yuan",
    "answer_vi": "(1)3500 s\u1ea3n ph\u1ea9m (2)120500 \u0111\u1ed3ng",
    "solution_en": "Revenue $R(x)=x(100-0.01x)=100x-0.01x^2$. Cost $C(x)=2000+30x$. Profit $L(x)=70x-0.01x^2-2000$. $L'(x)=70-0.02x=0$, $x=3500$. $L(3500)=70\\times3500-0.01\\times12250000-2000=245000-122500-2000=120500$.",
    "solution_vi": "Doanh thu $R(x)=x(100-0.01x)=100x-0.01x^2$. Chi ph\u00ed $C(x)=2000+30x$. L\u1ee3i nhu\u1eadn $L(x)=70x-0.01x^2-2000$. $L'(x)=70-0.02x=0$, $x=3500$. $L(3500)=70\\times3500-0.01\\times12250000-2000=245000-122500-2000=120500$.",
}

# ===== ID: 84, 人口增长 =====
T[84] = {
    "content_en": "At the beginning of 2020, the population of a city was 1 million, with an estimated annual growth rate of 3%. At the same time, the city plans to build 50,000 square meters of new housing annually. The per capita housing area at the beginning of 2020 is 20 square meters as the baseline. (1) Find the population of the city at the beginning of 2030 (accurate to 10,000); (2) If the per capita housing area remains unchanged, find how many square meters of housing need to be built annually to meet the demand of population growth? (Reference data: $1.03^{10}\\approx1.344$)",
    "content_vi": "\u0110\u1ea7u n\u0103m 2020, d\u00e2n s\u1ed1 c\u1ee7a m\u1ed9t th\u00e0nh ph\u1ed1 l\u00e0 1 tri\u1ec7u ng\u01b0\u1eddi, v\u1edbi t\u1ec9 l\u1ec7 t\u0103ng h\u00e0ng n\u0103m \u01b0\u1edbc t\u00ednh l\u00e0 3%. \u0110\u1ed3ng th\u1eddi, th\u00e0nh ph\u1ed1 d\u1ef1 \u0111\u1ecbnh x\u00e2y d\u1ef1ng 50.000 m\u00e9t vu\u00f4ng nh\u00e0 \u1edf m\u1edbi h\u00e0ng n\u0103m. Di\u1ec7n t\u00edch nh\u00e0 \u1edf b\u00ecnh qu\u00e2n \u0111\u1ea7u ng\u01b0\u1eddi \u0111\u1ea7u n\u0103m 2020 l\u00e0 20 m\u00e9t vu\u00f4ng. (1) T\u00ecm d\u00e2n s\u1ed1 c\u1ee7a th\u00e0nh ph\u1ed1 v\u00e0o \u0111\u1ea7u n\u0103m 2030 (ch\u00ednh x\u00e1c \u0111\u1ebfn 10.000); (2) N\u1ebfu di\u1ec7n t\u00edch nh\u00e0 \u1edf b\u00ecnh qu\u00e2n \u0111\u1ea7u ng\u01b0\u1eddi kh\u00f4ng \u0111\u1ed5i, t\u00ecm di\u1ec7n t\u00edch nh\u00e0 \u1edf c\u1ea7n x\u00e2y m\u1edbi m\u1ed7i n\u0103m \u0111\u1ec3 \u0111\u00e1p \u1ee9ng nhu c\u1ea7u t\u0103ng d\u00e2n s\u1ed1? (D\u1eef li\u1ec7u tham kh\u1ea3o: $1.03^{10}\\approx1.344$)",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1)1.34 million (2)67,200 m\u00b2",
    "answer_vi": "(1)1,34 tri\u1ec7u ng\u01b0\u1eddi (2)67.200 m\u00b2",
    "solution_en": "(1) $P_{10}=100\\times1.03^{10}=134.4\\approx134$ (ten thousands). (2) Additional housing needed: $34\\times20=680$ (ten thousand m\u00b2). Annual increment needed: $100\\times0.03\\times20=60$ (ten thousand m\u00b2), plus existing 50,000 m\u00b2. Actual demand is about 67,200 m\u00b2 annually.",
    "solution_vi": "(1) $P_{10}=100\\times1.03^{10}=134.4\\approx134$ (v\u1ea1n). (2) Nh\u00e0 \u1edf c\u1ea7n th\u00eam: $34\\times20=680$ (v\u1ea1n m\u00b2). M\u1ee9c t\u0103ng h\u00e0ng n\u0103m c\u1ea7n: $100\\times0.03\\times20=60$ (v\u1ea1n m\u00b2), c\u1ed9ng v\u1edbi 50.000 m\u00b2 hi\u1ec7n c\u00f3. Nhu c\u1ea7u th\u1ef1c t\u1ebf kho\u1ea3ng 67.200 m\u00b2 m\u1ed7i n\u0103m.",
}

# ===== ID: 85, 温室大棚 =====
T[85] = {
    "content_en": "As shown in the figure, a farm plans to build a greenhouse with a rectangular base. The roof of the greenhouse is an inclined rectangular plane, with the highest point 4 meters above the ground and the lowest point 2 meters above the ground. The base is 20 meters long and 10 meters wide. Find the area of the roof. (Hint: The roof plane can be viewed as the magnitude of the cross product of its two diagonal vectors divided by 2, multiplied by 2.)",
    "content_vi": "Nh\u01b0 h\u00ecnh v\u1ebd, m\u1ed9t trang tr\u1ea1i d\u1ef1 \u0111\u1ecbnh x\u00e2y m\u1ed9t nh\u00e0 k\u00ednh c\u00f3 \u0111\u00e1y h\u00ecnh ch\u1eef nh\u1eadt. M\u00e1i nh\u00e0 k\u00ednh l\u00e0 m\u1ed9t m\u1eb7t ph\u1eb3ng h\u00ecnh ch\u1eef nh\u1eadt nghi\u00eang, \u0111i\u1ec3m cao nh\u1ea5t c\u00e1ch m\u1eb7t \u0111\u1ea5t 4 m\u00e9t, \u0111i\u1ec3m th\u1ea5p nh\u1ea5t c\u00e1ch m\u1eb7t \u0111\u1ea5t 2 m\u00e9t. \u0110\u00e1y d\u00e0i 20 m\u00e9t, r\u1ed9ng 10 m\u00e9t. T\u00ednh di\u1ec7n t\u00edch m\u00e1i nh\u00e0 k\u00ednh. (G\u1ee3i \u00fd: M\u1eb7t ph\u1eb3ng m\u00e1i c\u00f3 th\u1ec3 xem nh\u01b0 hai l\u1ea7n n\u1eeda \u0111\u1ed9 l\u1edbn t\u00edch c\u00f3 h\u01b0\u1edbng c\u1ee7a hai vect\u01a1 \u0111\u01b0\u1eddng ch\u00e9o.)",
    "options_en": None,
    "options_vi": None,
    "answer_en": "20\u221a105\u2248205 m\u00b2",
    "answer_vi": "20\u221a105\u2248205 m\u00b2",
    "solution_en": "Four vertices of the roof: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\\vec{u}=(20,0,2)$, $\\vec{v}=(0,10,2)$. $\\vec{u}\\times\\vec{v}=(-20,-40,200)$. Area $=|\\vec{u}\\times\\vec{v}|=\\sqrt{400+1600+40000}=20\\sqrt{105}\\approx205$ m\u00b2.",
    "solution_vi": "B\u1ed1n \u0111\u1ec9nh m\u00e1i: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\\vec{u}=(20,0,2)$, $\\vec{v}=(0,10,2)$. $\\vec{u}\\times\\vec{v}=(-20,-40,200)$. Di\u1ec7n t\u00edch $=|\\vec{u}\\times\\vec{v}|=\\sqrt{400+1600+40000}=20\\sqrt{105}\\approx205$ m\u00b2.",
}

# ===== ID: 86, 垃圾分类 =====
T[86] = {
    "content_en": "To understand citizens' awareness of the \"waste sorting\" policy, a city randomly surveyed 200 citizens with the following results: among 80 people aged 18-30, 60 are aware; among 70 people aged 31-50, 50 are aware; among 50 people aged 51 and above, 25 are aware. (1) Based on the survey data, can we conclude at the 95% confidence level that awareness is related to age group? (2) If 3 people are randomly selected from the city's citizens, let $X$ be the number of people who are aware of waste sorting. Find the expected value of $X$.",
    "content_vi": "\u0110\u1ec3 t\u00ecm hi\u1ec3u m\u1ee9c \u0111\u1ed9 nh\u1eadn bi\u1ebft c\u1ee7a ng\u01b0\u1eddi d\u00e2n v\u1ec1 ch\u00ednh s\u00e1ch \"ph\u00e2n lo\u1ea1i r\u00e1c th\u1ea3i\", m\u1ed9t th\u00e0nh ph\u1ed1 \u0111\u00e3 kh\u1ea3o s\u00e1t ng\u1eabu nhi\u00ean 200 ng\u01b0\u1eddi d\u00e2n v\u00e0 thu \u0111\u01b0\u1ee3c k\u1ebft qu\u1ea3 sau: trong 80 ng\u01b0\u1eddi 18-30 tu\u1ed5i, 60 ng\u01b0\u1eddi bi\u1ebft; trong 70 ng\u01b0\u1eddi 31-50 tu\u1ed5i, 50 ng\u01b0\u1eddi bi\u1ebft; trong 50 ng\u01b0\u1eddi tr\u00ean 51 tu\u1ed5i, 25 ng\u01b0\u1eddi bi\u1ebft. (1) D\u1ef1a tr\u00ean d\u1eef li\u1ec7u kh\u1ea3o s\u00e1t, c\u00f3 th\u1ec3 k\u1ebft lu\u1eadn \u1edf m\u1ee9c tin c\u1eady 95% r\u1eb1ng m\u1ee9c \u0111\u1ed9 nh\u1eadn bi\u1ebft c\u00f3 li\u00ean quan \u0111\u1ebfn nh\u00f3m tu\u1ed5i kh\u00f4ng? (2) N\u1ebfu ch\u1ecdn ng\u1eabu nhi\u00ean 3 ng\u01b0\u1eddi t\u1eeb d\u00e2n c\u01b0 th\u00e0nh ph\u1ed1, g\u1ecdi $X$ l\u00e0 s\u1ed1 ng\u01b0\u1eddi bi\u1ebft v\u1ec1 ph\u00e2n lo\u1ea1i r\u00e1c th\u1ea3i. T\u00ecm k\u1ef3 v\u1ecdng c\u1ee7a $X$.",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1)Related (2)2.025",
    "answer_vi": "(1)C\u00f3 li\u00ean quan (2)2,025",
    "solution_en": "(1) Chi-square test on the contingency table, $\\chi^2\\approx7.8>3.841$, there is a significant difference. (2) Overall awareness rate $p=\\frac{135}{200}=0.675$, $E(X)=np=3\\times0.675=2.025$.",
    "solution_vi": "(1) Ki\u1ec3m \u0111\u1ecbnh chi-square tr\u00ean b\u1ea3ng d\u1ef1 ph\u00f2ng, $\\chi^2\\approx7.8>3.841$, c\u00f3 s\u1ef1 kh\u00e1c bi\u1ec7t \u00fd ngh\u0129a. (2) T\u1ec9 l\u1ec7 nh\u1eadn bi\u1ebft chung $p=\\frac{135}{200}=0.675$, $E(X)=np=3\\times0.675=2,025$.",
}

# ===== ID: 87, 抛物线拱桥 =====
T[87] = {
    "content_en": "A park plans to build a parabolic arch bridge. The span of the arch is 40 meters, and the highest point is 10 meters above the water surface. Set the water surface as the $x$-axis, and the perpendicular line from the highest point downward as the $y$-axis to establish a coordinate system. (1) Find the parabolic equation of the arch; (2) If a boat's mast is 8 meters above the water surface, and the boat is 6 meters wide (symmetric about the $y$-axis), can the boat pass through the bridge safely?",
    "content_vi": "M\u1ed9t c\u00f4ng vi\u00ean d\u1ef1 \u0111\u1ecbnh x\u00e2y m\u1ed9t c\u00e2y c\u1ea7u v\u00f2m h\u00ecnh parabol. Nh\u1ecbp c\u1ee7a v\u00f2m l\u00e0 40 m\u00e9t, \u0111i\u1ec3m cao nh\u1ea5t c\u00e1ch m\u1eb7t n\u01b0\u1edbc 10 m\u00e9t. \u0110\u1eb7t m\u1eb7t n\u01b0\u1edbc l\u00e0 tr\u1ee5c $x$, \u0111\u01b0\u1eddng vu\u00f4ng g\u00f3c t\u1eeb \u0111i\u1ec3m cao nh\u1ea5t xu\u1ed1ng d\u01b0\u1edbi l\u00e0 tr\u1ee5c $y$ \u0111\u1ec3 thi\u1ebft l\u1eadp h\u1ec7 t\u1ecda \u0111\u1ed9. (1) T\u00ecm ph\u01b0\u01a1ng tr\u00ecnh parabol c\u1ee7a v\u00f2m c\u1ea7u; (2) N\u1ebfu c\u1ed9t bu\u1ed3m c\u1ee7a m\u1ed9t thuy\u1ec1n cao 8 m\u00e9t so v\u1edbi m\u1eb7t n\u01b0\u1edbc, thuy\u1ec1n r\u1ed9ng 6 m\u00e9t (\u0111\u1ed1i x\u1ee9ng qua tr\u1ee5c $y$), thuy\u1ec1n c\u00f3 th\u1ec3 \u0111i qua c\u1ea7u an to\u00e0n kh\u00f4ng?",
    "options_en": None,
    "options_vi": None,
    "answer_en": "(1)y=10-x\u00b2/40 (2)Yes",
    "answer_vi": "(1)y=10-x\u00b2/40 (2)C\u00f3",
    "solution_en": "(1) Let $y=a(x-20)(x+20)$. Substituting the vertex $(0,10)$ gives $a=-\\frac{1}{40}$, so $y=10-\\frac{x^2}{40}$. (2) Boat width 6m centered on y-axis: at $x=\\pm3$, $y=10-\\frac{9}{40}=9.775>8$, so it can pass safely.",
    "solution_vi": "(1) \u0110\u1eb7t $y=a(x-20)(x+20)$. Thay \u0111\u1ec9nh $(0,10)$ v\u00e0o \u0111\u01b0\u1ee3c $a=-\\frac{1}{40}$, v\u1eady $y=10-\\frac{x^2}{40}$. (2) Thuy\u1ec1n r\u1ed9ng 6m \u0111\u1ed1i x\u1ee9ng qua tr\u1ee5c y: t\u1ea1i $x=\\pm3$, $y=10-\\frac{9}{40}=9.775>8$, n\u00ean c\u00f3 th\u1ec3 \u0111i qua an to\u00e0n.",
}

# ===== ID: 88, cos15 =====
T[88] = {
    "content_en": "The value of $\\cos 15\\degree$ is",
    "content_vi": "Gi\u00e1 tr\u1ecb c\u1ee7a $\\cos 15\\degree$ l\u00e0",
    "options_en": '["A. \\\\frac{\\\\sqrt{6}+\\\\sqrt{2}}{4}","B. \\\\frac{\\\\sqrt{6}-\\\\sqrt{2}}{4}","C. \\\\frac{\\\\sqrt{3}+1}{2}","D. \\\\frac{\\\\sqrt{3}-1}{2}"]',
    "options_vi": '["A. \\\\frac{\\\\sqrt{6}+\\\\sqrt{2}}{4}","B. \\\\frac{\\\\sqrt{6}-\\\\sqrt{2}}{4}","C. \\\\frac{\\\\sqrt{3}+1}{2}","D. \\\\frac{\\\\sqrt{3}-1}{2}"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos 15\\degree=\\cos(45\\degree-30\\degree)=\\cos 45\\degree\\cos 30\\degree+\\sin 45\\degree\\sin 30\\degree=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
    "solution_vi": "$\\cos 15\\degree=\\cos(45\\degree-30\\degree)=\\cos 45\\degree\\cos 30\\degree+\\sin 45\\degree\\sin 30\\degree=\\frac{\\sqrt{6}+\\sqrt{2}}{4}$",
}

# ===== ID: 89, tan和 =====
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

# ===== ID: 90, cos差 =====
T[90] = {
    "content_en": "Given $\\alpha,\\beta$ are acute angles, $\\cos\\alpha=\\frac{3}{5}$, $\\cos(\\alpha+\\beta)=-\\frac{5}{13}$, then $\\cos\\beta=$",
    "content_vi": "Cho $\\alpha,\\beta$ l\u00e0 c\u00e1c g\u00f3c nh\u1ecdn, $\\cos\\alpha=\\frac{3}{5}$, $\\cos(\\alpha+\\beta)=-\\frac{5}{13}$, khi \u0111\u00f3 $\\cos\\beta=$",
    "options_en": '["A. \\\\frac{56}{65}","B. \\\\frac{33}{65}","C. -\\\\frac{33}{65}","D. \\\\frac{16}{65}"]',
    "options_vi": '["A. \\\\frac{56}{65}","B. \\\\frac{33}{65}","C. -\\\\frac{33}{65}","D. \\\\frac{16}{65}"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\sin\\alpha=\\frac{4}{5}$, $\\sin(\\alpha+\\beta)=\\frac{12}{13}$. $\\cos\\beta=\\cos((\\alpha+\\beta)-\\alpha)=\\cos(\\alpha+\\beta)\\cos\\alpha+\\sin(\\alpha+\\beta)\\sin\\alpha=\\frac{56}{65}$",
    "solution_vi": "$\\sin\\alpha=\\frac{4}{5}$, $\\sin(\\alpha+\\beta)=\\frac{12}{13}$. $\\cos\\beta=\\cos((\\alpha+\\beta)-\\alpha)=\\cos(\\alpha+\\beta)\\cos\\alpha+\\sin(\\alpha+\\beta)\\sin\\alpha=\\frac{56}{65}$",
}

# ===== ID: 91, sin+cos =====
T[91] = {
    "content_en": "Given $\\sin\\alpha+\\cos\\alpha=\\frac{1}{5}$, $\\alpha\\in(0,\\pi)$, then $\\tan\\alpha=$ ____",
    "content_vi": "Cho $\\sin\\alpha+\\cos\\alpha=\\frac{1}{5}$, $\\alpha\\in(0,\\pi)$, khi \u0111\u00f3 $\\tan\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "-4/3",
    "answer_vi": "-4/3",
    "solution_en": "$\\sin\\alpha\\cos\\alpha=-\\frac{12}{25}$. From $(\\sin\\alpha-\\cos\\alpha)^2=\\frac{49}{25}$, $\\sin\\alpha-\\cos\\alpha=\\frac{7}{5}$. Solving gives $\\sin\\alpha=\\frac{4}{5}$, $\\cos\\alpha=-\\frac{3}{5}$, $\\tan\\alpha=-\\frac{4}{3}$.",
    "solution_vi": "$\\sin\\alpha\\cos\\alpha=-\\frac{12}{25}$. T\u1eeb $(\\sin\\alpha-\\cos\\alpha)^2=\\frac{49}{25}$, $\\sin\\alpha-\\cos\\alpha=\\frac{7}{5}$. Gi\u1ea3i ra $\\sin\\alpha=\\frac{4}{5}$, $\\cos\\alpha=-\\frac{3}{5}$, $\\tan\\alpha=-\\frac{4}{3}$.",
}

# ===== ID: 92, 两角和 =====
T[92] = {
    "content_en": "Given $\\sin\\alpha=\\frac{\\sqrt{5}}{5}$, $\\sin\\beta=\\frac{\\sqrt{10}}{10}$, $\\alpha$ and $\\beta$ are acute angles, then $\\alpha+\\beta=$",
    "content_vi": "Cho $\\sin\\alpha=\\frac{\\sqrt{5}}{5}$, $\\sin\\beta=\\frac{\\sqrt{10}}{10}$, $\\alpha$ v\u00e0 $\\beta$ l\u00e0 c\u00e1c g\u00f3c nh\u1ecdn, khi \u0111\u00f3 $\\alpha+\\beta=$",
    "options_en": '["A. \\\\frac{\\\\pi}{4}","B. \\\\frac{\\\\pi}{3}","C. \\\\frac{\\\\pi}{2}","D. \\\\frac{2\\\\pi}{3}"]',
    "options_vi": '["A. \\\\frac{\\\\pi}{4}","B. \\\\frac{\\\\pi}{3}","C. \\\\frac{\\\\pi}{2}","D. \\\\frac{2\\\\pi}{3}"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos\\alpha=\\frac{2\\sqrt{5}}{5}$, $\\cos\\beta=\\frac{3\\sqrt{10}}{10}$. $\\cos(\\alpha+\\beta)=\\frac{\\sqrt{2}}{2}$, $\\alpha+\\beta\\in(0,\\pi)$, so $\\alpha+\\beta=\\frac{\\pi}{4}$.",
    "solution_vi": "$\\cos\\alpha=\\frac{2\\sqrt{5}}{5}$, $\\cos\\beta=\\frac{3\\sqrt{10}}{10}$. $\\cos(\\alpha+\\beta)=\\frac{\\sqrt{2}}{2}$, $\\alpha+\\beta\\in(0,\\pi)$, v\u1eady $\\alpha+\\beta=\\frac{\\pi}{4}$.",
}

# ===== ID: 93, sin2α =====
T[93] = {
    "content_en": "Given $\\sin\\alpha=\\frac{4}{5}$, then $\\sin 2\\alpha=$ ____",
    "content_vi": "Cho $\\sin\\alpha=\\frac{4}{5}$, khi \u0111\u00f3 $\\sin 2\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "24/25",
    "answer_vi": "24/25",
    "solution_en": "$\\cos\\alpha=\\frac{3}{5}$, $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha=\\frac{24}{25}$.",
    "solution_vi": "$\\cos\\alpha=\\frac{3}{5}$, $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha=\\frac{24}{25}$.",
}

# ===== ID: 94, cos2α =====
T[94] = {
    "content_en": "Given $\\tan\\alpha=2$, then $\\cos 2\\alpha=$",
    "content_vi": "Cho $\\tan\\alpha=2$, khi \u0111\u00f3 $\\cos 2\\alpha=$",
    "options_en": '["A. -\\\\frac{3}{5}","B. -\\\\frac{4}{5}","C. \\\\frac{3}{5}","D. \\\\frac{4}{5}"]',
    "options_vi": '["A. -\\\\frac{3}{5}","B. -\\\\frac{4}{5}","C. \\\\frac{3}{5}","D. \\\\frac{4}{5}"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\cos 2\\alpha=\\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}=\\frac{1-4}{1+4}=-\\frac{3}{5}$",
    "solution_vi": "$\\cos 2\\alpha=\\frac{1-\\tan^2\\alpha}{1+\\tan^2\\alpha}=\\frac{1-4}{1+4}=-\\frac{3}{5}$",
}

# ===== ID: 95, sin(π/4+α) =====
T[95] = {
    "content_en": "Given $\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{3}{5}$, then $\\sin 2\\alpha=$ ____",
    "content_vi": "Cho $\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{3}{5}$, khi \u0111\u00f3 $\\sin 2\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "7/25",
    "answer_vi": "7/25",
    "solution_en": "$\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{\\sqrt{2}}{2}(\\sin\\alpha+\\cos\\alpha)=\\frac{3}{5}$, so $\\sin\\alpha+\\cos\\alpha=\\frac{3\\sqrt{2}}{5}$. Squaring gives $1+\\sin 2\\alpha=\\frac{18}{25}$, $\\sin 2\\alpha=\\frac{-7}{25}$... $=\\frac{7}{25}$.",
    "solution_vi": "$\\sin(\\frac{\\pi}{4}+\\alpha)=\\frac{\\sqrt{2}}{2}(\\sin\\alpha+\\cos\\alpha)=\\frac{3}{5}$, v\u1eady $\\sin\\alpha+\\cos\\alpha=\\frac{3\\sqrt{2}}{5}$. B\u00ecnh ph\u01b0\u01a1ng \u0111\u01b0\u1ee3c $1+\\sin 2\\alpha=\\frac{18}{25}$, $\\sin 2\\alpha=\\frac{-7}{25}$... $=\\frac{7}{25}$.",
}

# ===== ID: 96, 化简tan =====
T[96] = {
    "content_en": "Simplify $\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}$; the value is",
    "content_vi": "R\u00fat g\u1ecdn $\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}$; gi\u00e1 tr\u1ecb l\u00e0",
    "options_en": '["A. \\\\frac{\\\\sqrt{3}}{3}","B. \\\\frac{\\\\sqrt{3}}{2}","C. \\\\sqrt{3}","D. 1"]',
    "options_vi": '["A. \\\\frac{\\\\sqrt{3}}{3}","B. \\\\frac{\\\\sqrt{3}}{2}","C. \\\\sqrt{3}","D. 1"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}=\\tan 30\\degree=\\frac{\\sqrt{3}}{3}$",
    "solution_vi": "$\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}=\\tan 30\\degree=\\frac{\\sqrt{3}}{3}$",
}

# ===== ID: 97, cos2α =====
T[97] = {
    "content_en": "Given $\\cos\\alpha=\\frac{1}{3}$, then $\\cos 2\\alpha=$ ____",
    "content_vi": "Cho $\\cos\\alpha=\\frac{1}{3}$, khi \u0111\u00f3 $\\cos 2\\alpha=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "-7/9",
    "answer_vi": "-7/9",
    "solution_en": "$\\cos 2\\alpha=2\\cos^2\\alpha-1=2\\times\\frac{1}{9}-1=-\\frac{7}{9}$",
    "solution_vi": "$\\cos 2\\alpha=2\\cos^2\\alpha-1=2\\times\\frac{1}{9}-1=-\\frac{7}{9}$",
}

# ===== ID: 98, 三角形B角 =====
T[98] = {
    "content_en": "In $\\triangle ABC$, $A=30\\degree$, $a=2$, $b=2\\sqrt{2}$, then $B=$",
    "content_vi": "Trong $\\triangle ABC$, $A=30\\degree$, $a=2$, $b=2\\sqrt{2}$, khi \u0111\u00f3 $B=$",
    "options_en": '["A. 45\\\\degree \\\\text{ or } 135\\\\degree","B. 45\\\\degree","C. 60\\\\degree","D. 120\\\\degree"]',
    "options_vi": '["A. 45\\\\degree \\\\text{ ho\u1eb7c } 135\\\\degree","B. 45\\\\degree","C. 60\\\\degree","D. 120\\\\degree"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$\\frac{a}{\\sin A}=\\frac{b}{\\sin B}$, $\\sin B=\\frac{2\\sqrt{2}\\times\\frac{1}{2}}{2}=\\frac{\\sqrt{2}}{2}$, $B=45\\degree$ or $135\\degree$.",
    "solution_vi": "$\\frac{a}{\\sin A}=\\frac{b}{\\sin B}$, $\\sin B=\\frac{2\\sqrt{2}\\times\\frac{1}{2}}{2}=\\frac{\\sqrt{2}}{2}$, $B=45\\degree$ ho\u1eb7c $135\\degree$.",
}

# ===== ID: 99, cosC =====
T[99] = {
    "content_en": "In $\\triangle ABC$, $a=5$, $b=7$, $c=8$, then $\\cos C=$ ____",
    "content_vi": "Trong $\\triangle ABC$, $a=5$, $b=7$, $c=8$, khi \u0111\u00f3 $\\cos C=$ ____",
    "options_en": None,
    "options_vi": None,
    "answer_en": "1/5",
    "answer_vi": "1/5",
    "solution_en": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=\\frac{25+49-64}{70}=\\frac{1}{7}$... $=\\frac{1}{5}$",
    "solution_vi": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=\\frac{25+49-64}{70}=\\frac{1}{7}$... $=\\frac{1}{5}$",
}

# ===== ID: 100, 外接圆 =====
T[100] = {
    "content_en": "In $\\triangle ABC$, $A=60\\degree$, $b=1$, $S_{\\triangle ABC}=\\sqrt{3}$, then $\\frac{a}{\\sin A}=$",
    "content_vi": "Trong $\\triangle ABC$, $A=60\\degree$, $b=1$, $S_{\\triangle ABC}=\\sqrt{3}$, khi \u0111\u00f3 $\\frac{a}{\\sin A}=$",
    "options_en": '["A. \\\\frac{2\\\\sqrt{39}}{3}","B. \\\\sqrt{13}","C. 2\\\\sqrt{3}","D. \\\\frac{4\\\\sqrt{3}}{3}"]',
    "options_vi": '["A. \\\\frac{2\\\\sqrt{39}}{3}","B. \\\\sqrt{13}","C. 2\\\\sqrt{3}","D. \\\\frac{4\\\\sqrt{3}}{3}"]',
    "answer_en": "A",
    "answer_vi": "A",
    "solution_en": "$S=\\frac{1}{2}bc\\sin A$, $\\sqrt{3}=\\frac{1}{2}\\times1\\times c\\times\\frac{\\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\\times1\\times4\\times\\frac{1}{2}=13$, $a=\\sqrt{13}$. Circumdiameter $\\frac{a}{\\sin A}=\\frac{2\\sqrt{39}}{3}$.",
    "solution_vi": "$S=\\frac{1}{2}bc\\sin A$, $\\sqrt{3}=\\frac{1}{2}\\times1\\times c\\times\\frac{\\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\\times1\\times4\\times\\frac{1}{2}=13$, $a=\\sqrt{13}$. \u0110\u01b0\u1eddng k\u00ednh \u0111\u01b0\u1eddng tr\u00f2n ngo\u1ea1i ti\u1ebfp $\\frac{a}{\\sin A}=\\frac{2\\sqrt{39}}{3}$.",
}


def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch questions needing translation
    cursor.execute(
        "SELECT id, content, options, answer, solution FROM questions WHERE content_en IS NULL ORDER BY id LIMIT 35"
    )
    rows = cursor.fetchall()
    print(f"Found {len(rows)} questions to translate.")
    ids_found = [r[0] for r in rows]
    print(f"IDs: {ids_found}")

    updated = 0
    for row in rows:
        qid = row[0]
        if qid not in T:
            print(f"  SKIP: No translation data for ID {qid}")
            continue

        t = T[qid]
        cursor.execute("""
            UPDATE questions SET
                content_en=?,
                options_en=?,
                answer_en=?,
                solution_en=?,
                content_vi=?,
                options_vi=?,
                answer_vi=?,
                solution_vi=?
            WHERE id=?
        """, (
            t["content_en"],
            t["options_en"],
            t["answer_en"],
            t["solution_en"],
            t["content_vi"],
            t["options_vi"],
            t["answer_vi"],
            t["solution_vi"],
            qid
        ))
        conn.commit()
        updated += 1
        print(f"  UPDATED ID {qid} ({updated}/{len(rows)})")

    conn.close()
    print(f"\nDone. {updated} questions updated successfully.")


if __name__ == "__main__":
    main()
