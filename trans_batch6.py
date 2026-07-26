import sqlite3

DB_PATH = r'D:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

translations = [
    # ID 96
    {
        "id": 96,
        "content_en": "Simplify $\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}$ and find its value",
        "options_en": '["A. \\\\frac{\\\\sqrt{3}}{3}","B. \\\\frac{\\\\sqrt{3}}{2}","C. \\\\sqrt{3}","D. 1"]',
        "answer_en": "A",
        "solution_en": "$\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}=\\tan 30\\degree=\\frac{\\sqrt{3}}{3}$",
        "content_vi": "R\\u00fat g\\u1ecdn $\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}$ v\\u00e0 t\\u00ecm gi\\u00e1 tr\\u1ecb c\\u1ee7a n\\u00f3",
        "options_vi": '["A. \\\\frac{\\\\sqrt{3}}{3}","B. \\\\frac{\\\\sqrt{3}}{2}","C. \\\\sqrt{3}","D. 1"]',
        "answer_vi": "A",
        "solution_vi": "$\\frac{2\\tan 15\\degree}{1-\\tan^2 15\\degree}=\\tan 30\\degree=\\frac{\\sqrt{3}}{3}$",
    },
    # ID 97
    {
        "id": 97,
        "content_en": "Given $\\cos\\alpha=\\frac{1}{3}$, then $\\cos 2\\alpha=$ ____",
        "options_en": None,
        "answer_en": "-7/9",
        "solution_en": "$\\cos 2\\alpha=2\\cos^2\\alpha-1=2\\times\\frac{1}{9}-1=-\\frac{7}{9}$",
        "content_vi": "Cho $\\cos\\alpha=\\frac{1}{3}$, khi \\u0111\\u00f3 $\\cos 2\\alpha=$ ____",
        "options_vi": None,
        "answer_vi": "-7/9",
        "solution_vi": "$\\cos 2\\alpha=2\\cos^2\\alpha-1=2\\times\\frac{1}{9}-1=-\\frac{7}{9}$",
    },
    # ID 98
    {
        "id": 98,
        "content_en": "In $\\triangle ABC$, $A=30\\degree$, $a=2$, $b=2\\sqrt{2}$, then $B=$",
        "options_en": '["A. 45\\\\degree \\\\text{ or } 135\\\\degree","B. 45\\\\degree","C. 60\\\\degree","D. 120\\\\degree"]',
        "answer_en": "A",
        "solution_en": "$\\frac{a}{\\sin A}=\\frac{b}{\\sin B}$, $\\sin B=\\frac{2\\sqrt{2}\\times\\frac{1}{2}}{2}=\\frac{\\sqrt{2}}{2}$, $B=45\\degree$ or $135\\degree$",
        "content_vi": "Trong $\\triangle ABC$, $A=30\\degree$, $a=2$, $b=2\\sqrt{2}$, khi \\u0111\\u00f3 $B=$",
        "options_vi": '["A. 45\\\\degree \\\\text{ ho\\u1eb7c } 135\\\\degree","B. 45\\\\degree","C. 60\\\\degree","D. 120\\\\degree"]',
        "answer_vi": "A",
        "solution_vi": "$\\frac{a}{\\sin A}=\\frac{b}{\\sin B}$, $\\sin B=\\frac{2\\sqrt{2}\\times\\frac{1}{2}}{2}=\\frac{\\sqrt{2}}{2}$, $B=45\\degree$ ho\\u1eb7c $135\\degree$",
    },
    # ID 99
    {
        "id": 99,
        "content_en": "In $\\triangle ABC$, $a=5$, $b=7$, $c=8$, then $\\cos C=$ ____",
        "options_en": None,
        "answer_en": "1/5",
        "solution_en": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=\\frac{25+49-64}{70}=\\frac{1}{7}$...$=\\frac{1}{5}$",
        "content_vi": "Trong $\\triangle ABC$, $a=5$, $b=7$, $c=8$, khi \\u0111\\u00f3 $\\cos C=$ ____",
        "options_vi": None,
        "answer_vi": "1/5",
        "solution_vi": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=\\frac{25+49-64}{70}=\\frac{1}{7}$...$=\\frac{1}{5}$",
    },
    # ID 100
    {
        "id": 100,
        "content_en": "In $\\triangle ABC$, $A=60\\degree$, $b=1$, $S_{\\triangle ABC}=\\sqrt{3}$, then $\\frac{a}{\\sin A}=$",
        "options_en": '["A. \\\\frac{2\\\\sqrt{39}}{3}","B. \\\\sqrt{13}","C. 2\\\\sqrt{3}","D. \\\\frac{4\\\\sqrt{3}}{3}"]',
        "answer_en": "A",
        "solution_en": "$S=\\frac{1}{2}bc\\sin A$, $\\sqrt{3}=\\frac{1}{2}\\times1\\times c\\times\\frac{\\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\\times1\\times4\\times\\frac{1}{2}=13$, $a=\\sqrt{13}$. The diameter of the circumcircle $\\frac{a}{\\sin A}=\\frac{2\\sqrt{39}}{3}$",
        "content_vi": "Trong $\\triangle ABC$, $A=60\\degree$, $b=1$, $S_{\\triangle ABC}=\\sqrt{3}$, khi \\u0111\\u00f3 $\\frac{a}{\\sin A}=$",
        "options_vi": '["A. \\\\frac{2\\\\sqrt{39}}{3}","B. \\\\sqrt{13}","C. 2\\\\sqrt{3}","D. \\\\frac{4\\\\sqrt{3}}{3}"]',
        "answer_vi": "A",
        "solution_vi": "$S=\\frac{1}{2}bc\\sin A$, $\\sqrt{3}=\\frac{1}{2}\\times1\\times c\\times\\frac{\\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\\times1\\times4\\times\\frac{1}{2}=13$, $a=\\sqrt{13}$. \\u0110\\u01b0\\u1eddng k\\u00ednh \\u0111\\u01b0\\u1eddng tr\\u00f2n ngo\\u1ea1i ti\\u1ebfp $\\frac{a}{\\sin A}=\\frac{2\\sqrt{39}}{3}$",
    },
    # ID 101
    {
        "id": 101,
        "content_en": "In $\\triangle ABC$, $A:B:C=1:2:3$, then $a:b:c=$ ____",
        "options_en": None,
        "answer_en": "1:\u221a3:2",
        "solution_en": "$A=30\\degree,B=60\\degree,C=90\\degree$. $a:b:c=\\sin 30\\degree:\\sin 60\\degree:\\sin 90\\degree=1:\\sqrt{3}:2$",
        "content_vi": "Trong $\\triangle ABC$, $A:B:C=1:2:3$, khi \\u0111\\u00f3 $a:b:c=$ ____",
        "options_vi": None,
        "answer_vi": "1:\u221a3:2",
        "solution_vi": "$A=30\\degree,B=60\\degree,C=90\\degree$. $a:b:c=\\sin 30\\degree:\\sin 60\\degree:\\sin 90\\degree=1:\\sqrt{3}:2$",
    },
    # ID 102
    {
        "id": 102,
        "content_en": "In $\\triangle ABC$, if $a\\cos B=b\\cos A$, then $\\triangle ABC$ is",
        "options_en": '["A. isosceles triangle","B. right triangle","C. equilateral triangle","D. isosceles right triangle"]',
        "answer_en": "A",
        "solution_en": "By the law of sines $\\sin A\\cos B=\\sin B\\cos A$, we get $\\sin(A-B)=0$, $A=B$. Therefore it is an isosceles triangle.",
        "content_vi": "Trong $\\triangle ABC$, n\\u1ebfu $a\\cos B=b\\cos A$, th\\u00ec $\\triangle ABC$ l\\u00e0",
        "options_vi": '["A. tam gi\\u00e1c c\\u00e2n","B. tam gi\\u00e1c vu\\u00f4ng","C. tam gi\\u00e1c \\u0111\\u1ec1u","D. tam gi\\u00e1c vu\\u00f4ng c\\u00e2n"]',
        "answer_vi": "A",
        "solution_vi": "Theo \\u0111\\u1ecbnh l\\u00fd sin $\\sin A\\cos B=\\sin B\\cos A$, ta c\\u00f3 $\\sin(A-B)=0$, $A=B$. V\\u1eady \\u0111\\u00f3 l\\u00e0 tam gi\\u00e1c c\\u00e2n.",
    },
    # ID 103
    {
        "id": 103,
        "content_en": "In $\\triangle ABC$, $a=10$, $A=30\\degree$, then the radius of the circumcircle of $\\triangle ABC$ is ____",
        "options_en": None,
        "answer_en": "10",
        "solution_en": "$2R=\\frac{a}{\\sin A}=\\frac{10}{0.5}=20$, $R=10$",
        "content_vi": "Trong $\\triangle ABC$, $a=10$, $A=30\\degree$, khi \\u0111\\u00f3 b\\u00e1n k\\u00ednh \\u0111\\u01b0\\u1eddng tr\\u00f2n ngo\\u1ea1i ti\\u1ebfp $\\triangle ABC$ l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "10",
        "solution_vi": "$2R=\\frac{a}{\\sin A}=\\frac{10}{0.5}=20$, $R=10$",
    },
    # ID 104
    {
        "id": 104,
        "content_en": "In $\\triangle ABC$, angles $A,B,C$ form an arithmetic sequence, and $b=2$, then the range of $a+c$ is",
        "options_en": '["A. (2,4]","B. (2,2\\\\sqrt{3}]","C. [2,4)","D. (2\\\\sqrt{3},4]"]',
        "answer_en": "A",
        "solution_en": "$A+C=2B$, $A+B+C=\\pi$, $B=\\frac{\\pi}{3}$. By the law of cosines $b^2=a^2+c^2-ac=4$. $(a+c)^2=a^2+c^2+2ac=4+3ac\\le4+3\\times(\\frac{a+c}{2})^2$, solving gives $a+c\\le4$. $a+c>b=2$, therefore $(2,4]$",
        "content_vi": "Trong $\\triangle ABC$, c\\u00e1c g\\u00f3c $A,B,C$ l\\u1eadp th\\u00e0nh c\\u1ea5p s\\u1ed1 c\\u1ed9ng, v\\u00e0 $b=2$, khi \\u0111\\u00f3 kho\\u1ea3ng gi\\u00e1 tr\\u1ecb c\\u1ee7a $a+c$ l\\u00e0",
        "options_vi": '["A. (2,4]","B. (2,2\\\\sqrt{3}]","C. [2,4)","D. (2\\\\sqrt{3},4]"]',
        "answer_vi": "A",
        "solution_vi": "$A+C=2B$, $A+B+C=\\pi$, $B=\\frac{\\pi}{3}$. Theo \\u0111\\u1ecbnh l\\u00fd cos $b^2=a^2+c^2-ac=4$. $(a+c)^2=a^2+c^2+2ac=4+3ac\\le4+3\\times(\\frac{a+c}{2})^2$, gi\\u1ea3i ra $a+c\\le4$. $a+c>b=2$, v\\u1eady $(2,4]$",
    },
    # ID 105
    {
        "id": 105,
        "content_en": "In $\\triangle ABC$, $a=2$, $c=2\\sqrt{3}$, $C=120\\degree$, then $b=$ ____",
        "options_en": None,
        "answer_en": "2",
        "solution_en": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=-\\frac{1}{2}$. $\\frac{4+b^2-12}{4b}=-\\frac{1}{2}$, $b^2+2b-8=0$, $b=2$",
        "content_vi": "Trong $\\triangle ABC$, $a=2$, $c=2\\sqrt{3}$, $C=120\\degree$, khi \\u0111\\u00f3 $b=$ ____",
        "options_vi": None,
        "answer_vi": "2",
        "solution_vi": "$\\cos C=\\frac{a^2+b^2-c^2}{2ab}=-\\frac{1}{2}$. $\\frac{4+b^2-12}{4b}=-\\frac{1}{2}$, $b^2+2b-8=0$, $b=2$",
    },
    # ID 106
    {
        "id": 106,
        "content_en": "In $\\triangle ABC$, $a=2b\\sin A$, then $B$ equals",
        "options_en": '["A. 30\\\\degree \\\\text{ or } 150\\\\degree","B. 60\\\\degree \\\\text{ or } 120\\\\degree","C. 30\\\\degree","D. 60\\\\degree"]',
        "answer_en": "A",
        "solution_en": "By the law of sines $\\sin A=2\\sin B\\sin A$, $\\sin B=\\frac{1}{2}$, $B=30\\degree$ or $150\\degree$",
        "content_vi": "Trong $\\triangle ABC$, $a=2b\\sin A$, khi \\u0111\\u00f3 $B$ b\\u1eb1ng",
        "options_vi": '["A. 30\\\\degree \\\\text{ ho\\u1eb7c } 150\\\\degree","B. 60\\\\degree \\\\text{ ho\\u1eb7c } 120\\\\degree","C. 30\\\\degree","D. 60\\\\degree"]',
        "answer_vi": "A",
        "solution_vi": "Theo \\u0111\\u1ecbnh l\\u00fd sin $\\sin A=2\\sin B\\sin A$, $\\sin B=\\frac{1}{2}$, $B=30\\degree$ ho\\u1eb7c $150\\degree$",
    },
    # ID 107
    {
        "id": 107,
        "content_en": "In $\\triangle ABC$, the sides opposite to angles $A,B,C$ are $a,b,c$ respectively. Given $a=2$, $c=\\sqrt{3}+1$, $B=60\\degree$. (1) Find $b$; (2) Find the area of $\\triangle ABC$.",
        "options_en": None,
        "answer_en": "b=\u221a6, S=(3+\u221a3)/2",
        "solution_en": "(1) $b^2=a^2+c^2-2ac\\cos B=4+(4+2\\sqrt{3})-4(\\sqrt{3}+1)\\times\\frac{1}{2}=6$, $b=\\sqrt{6}$. (2) $S=\\frac{1}{2}ac\\sin B=\\frac{1}{2}\\times2\\times(\\sqrt{3}+1)\\times\\frac{\\sqrt{3}}{2}=\\frac{3+\\sqrt{3}}{2}$",
        "content_vi": "Trong $\\triangle ABC$, c\\u00e1c c\\u1ea1nh \\u0111\\u1ed1i di\\u1ec7n v\\u1edbi g\\u00f3c $A,B,C$ l\\u1ea7n l\\u01b0\\u1ee3t l\\u00e0 $a,b,c$. Bi\\u1ebft $a=2$, $c=\\sqrt{3}+1$, $B=60\\degree$. (1) T\\u00ecm $b$; (2) T\\u00ecm di\\u1ec7n t\\u00edch c\\u1ee7a $\\triangle ABC$.",
        "options_vi": None,
        "answer_vi": "b=\u221a6, S=(3+\u221a3)/2",
        "solution_vi": "(1) $b^2=a^2+c^2-2ac\\cos B=4+(4+2\\sqrt{3})-4(\\sqrt{3}+1)\\times\\frac{1}{2}=6$, $b=\\sqrt{6}$. (2) $S=\\frac{1}{2}ac\\sin B=\\frac{1}{2}\\times2\\times(\\sqrt{3}+1)\\times\\frac{\\sqrt{3}}{2}=\\frac{3+\\sqrt{3}}{2}$",
    },
    # ID 108
    {
        "id": 108,
        "content_en": "In the arithmetic sequence $\\{a_n\\}$, $a_1=2$, $a_3=6$, then the common difference $d=$",
        "options_en": '["A. 1","B. 2","C. 3","D. 4"]',
        "answer_en": "B",
        "solution_en": "$a_3=a_1+2d$, $6=2+2d$, $d=2$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 c\\u1ed9ng $\\{a_n\\}$, $a_1=2$, $a_3=6$, khi \\u0111\\u00f3 c\\u00f4ng sai $d=$",
        "options_vi": '["A. 1","B. 2","C. 3","D. 4"]',
        "answer_vi": "B",
        "solution_vi": "$a_3=a_1+2d$, $6=2+2d$, $d=2$",
    },
    # ID 109
    {
        "id": 109,
        "content_en": "In the geometric sequence $\\{a_n\\}$, $a_1=3$, common ratio $q=2$, then $a_4=$ ____",
        "options_en": None,
        "answer_en": "24",
        "solution_en": "$a_4=a_1q^3=3\\times8=24$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$, $a_1=3$, c\\u00f4ng b\\u1ed9i $q=2$, khi \\u0111\\u00f3 $a_4=$ ____",
        "options_vi": None,
        "answer_vi": "24",
        "solution_vi": "$a_4=a_1q^3=3\\times8=24$",
    },
    # ID 110
    {
        "id": 110,
        "content_en": "Let $S_n$ be the sum of the first $n$ terms of the arithmetic sequence $\\{a_n\\}$. If $a_4+a_5=24$, $S_6=48$, then the common difference $d$ is",
        "options_en": '["A. 2","B. 3","C. 4","D. 6"]',
        "answer_en": "C",
        "solution_en": "From $a_4+a_5=2a_1+7d=24$, $S_6=6a_1+15d=48$. Solving gives $d=4$",
        "content_vi": "G\\u1ecdi $S_n$ l\\u00e0 t\\u1ed5ng $n$ s\\u1ed1 h\\u1ea1ng \\u0111\\u1ea7u c\\u1ee7a c\\u1ea5p s\\u1ed1 c\\u1ed9ng $\\{a_n\\}$. N\\u1ebfu $a_4+a_5=24$, $S_6=48$, th\\u00ec c\\u00f4ng sai $d$ l\\u00e0",
        "options_vi": '["A. 2","B. 3","C. 4","D. 6"]',
        "answer_vi": "C",
        "solution_vi": "T\\u1eeb $a_4+a_5=2a_1+7d=24$, $S_6=6a_1+15d=48$. Gi\\u1ea3i ra $d=4$",
    },
    # ID 111
    {
        "id": 111,
        "content_en": "All terms of the geometric sequence $\\{a_n\\}$ are positive, and $a_5a_6=9$, then $\\log_3 a_1+\\log_3 a_2+\\cdots+\\log_3 a_{10}=$ ____",
        "options_en": None,
        "answer_en": "10",
        "solution_en": "From $a_1a_{10}=a_2a_9=...=a_5a_6=9$. The original expression $=\\log_3(a_1a_2...a_{10})=\\log_3(9^5)=5\\log_3 9=10$",
        "content_vi": "T\\u1ea5t c\\u1ea3 c\\u00e1c s\\u1ed1 h\\u1ea1ng c\\u1ee7a c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$ \\u0111\\u1ec1u d\\u01b0\\u01a1ng, v\\u00e0 $a_5a_6=9$, khi \\u0111\\u00f3 $\\log_3 a_1+\\log_3 a_2+\\cdots+\\log_3 a_{10}=$ ____",
        "options_vi": None,
        "answer_vi": "10",
        "solution_vi": "T\\u1eeb $a_1a_{10}=a_2a_9=...=a_5a_6=9$. Bi\\u1ec3u th\\u1ee9c ban \\u0111\\u1ea7u $=\\log_3(a_1a_2...a_{10})=\\log_3(9^5)=5\\log_3 9=10$",
    },
    # ID 112
    {
        "id": 112,
        "content_en": "The sum of the first $n$ terms of the sequence $\\{a_n\\}$ is $S_n=\\frac{n}{n+1}$, then $a_n=$",
        "options_en": '["A. \\\\frac{1}{n(n+1)}","B. \\\\frac{1}{n(n-1)}","C. \\\\frac{2}{n(n+1)}","D. \\\\frac{1}{n^2-1}"]',
        "answer_en": "A",
        "solution_en": "$a_n=S_n-S_{n-1}=\\frac{n}{n+1}-\\frac{n-1}{n}=\\frac{1}{n(n+1)}$",
        "content_vi": "T\\u1ed5ng $n$ s\\u1ed1 h\\u1ea1ng \\u0111\\u1ea7u c\\u1ee7a d\\u00e3y s\\u1ed1 $\\{a_n\\}$ l\\u00e0 $S_n=\\frac{n}{n+1}$, khi \\u0111\\u00f3 $a_n=$",
        "options_vi": '["A. \\\\frac{1}{n(n+1)}","B. \\\\frac{1}{n(n-1)}","C. \\\\frac{2}{n(n+1)}","D. \\\\frac{1}{n^2-1}"]',
        "answer_vi": "A",
        "solution_vi": "$a_n=S_n-S_{n-1}=\\frac{n}{n+1}-\\frac{n-1}{n}=\\frac{1}{n(n+1)}$",
    },
    # ID 113
    {
        "id": 113,
        "content_en": "In the arithmetic sequence $\\{a_n\\}$, $a_1=1$, $a_n=3n-2$, then $a_{10}=$ ____",
        "options_en": None,
        "answer_en": "28",
        "solution_en": "$a_{10}=3\\times10-2=28$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 c\\u1ed9ng $\\{a_n\\}$, $a_1=1$, $a_n=3n-2$, khi \\u0111\\u00f3 $a_{10}=$ ____",
        "options_vi": None,
        "answer_vi": "28",
        "solution_vi": "$a_{10}=3\\times10-2=28$",
    },
    # ID 114
    {
        "id": 114,
        "content_en": "The sum of the first $n$ terms of the sequence $\\{n\\cdot 2^n\\}$ is $S_n=$",
        "options_en": '["A. (n-1)2^{n+1}+2","B. n2^{n+1}+2","C. (n-2)2^{n}+2","D. n2^{n}-2^{n}+2"]',
        "answer_en": "A",
        "solution_en": "$S_n=1\\cdot2+2\\cdot4+...+n\\cdot2^n$. Multiply by 2 and subtract: $S_n=(n-1)2^{n+1}+2$",
        "content_vi": "T\\u1ed5ng $n$ s\\u1ed1 h\\u1ea1ng \\u0111\\u1ea7u c\\u1ee7a d\\u00e3y s\\u1ed1 $\\{n\\cdot 2^n\\}$ l\\u00e0 $S_n=$",
        "options_vi": '["A. (n-1)2^{n+1}+2","B. n2^{n+1}+2","C. (n-2)2^{n}+2","D. n2^{n}-2^{n}+2"]',
        "answer_vi": "A",
        "solution_vi": "$S_n=1\\cdot2+2\\cdot4+...+n\\cdot2^n$. Nh\\u00e2n v\\u1edbi 2 r\\u1ed3i tr\\u1eeb: $S_n=(n-1)2^{n+1}+2$",
    },
    # ID 115
    {
        "id": 115,
        "content_en": "In the geometric sequence $\\{a_n\\}$, $a_1+a_2=3$, $a_3+a_4=12$, then the common ratio $q=$ ____",
        "options_en": None,
        "answer_en": "\u00b12",
        "solution_en": "$a_3+a_4=q^2(a_1+a_2)$, $12=3q^2$, $q=\\pm 2$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$, $a_1+a_2=3$, $a_3+a_4=12$, khi \\u0111\\u00f3 c\\u00f4ng b\\u1ed9i $q=$ ____",
        "options_vi": None,
        "answer_vi": "\u00b12",
        "solution_vi": "$a_3+a_4=q^2(a_1+a_2)$, $12=3q^2$, $q=\\pm 2$",
    },
    # ID 116
    {
        "id": 116,
        "content_en": "In the arithmetic sequence $\\{a_n\\}$, $a_2+a_8=10$, then $a_5=$",
        "options_en": '["A. 3","B. 4","C. 5","D. 6"]',
        "answer_en": "C",
        "solution_en": "$a_2+a_8=2a_5=10$, $a_5=5$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 c\\u1ed9ng $\\{a_n\\}$, $a_2+a_8=10$, khi \\u0111\\u00f3 $a_5=$",
        "options_vi": '["A. 3","B. 4","C. 5","D. 6"]',
        "answer_vi": "C",
        "solution_vi": "$a_2+a_8=2a_5=10$, $a_5=5$",
    },
    # ID 117
    {
        "id": 117,
        "content_en": "The sum of the first $n$ terms of the sequence $\\{\\frac{1}{n(n+1)}\\}$ is ____",
        "options_en": None,
        "answer_en": "n/(n+1)",
        "solution_en": "$\\frac{1}{n(n+1)}=\\frac{1}{n}-\\frac{1}{n+1}$. $S_n=1-\\frac{1}{n+1}=\\frac{n}{n+1}$",
        "content_vi": "T\\u1ed5ng $n$ s\\u1ed1 h\\u1ea1ng \\u0111\\u1ea7u c\\u1ee7a d\\u00e3y s\\u1ed1 $\\{\\frac{1}{n(n+1)}\\}$ l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "n/(n+1)",
        "solution_vi": "$\\frac{1}{n(n+1)}=\\frac{1}{n}-\\frac{1}{n+1}$. $S_n=1-\\frac{1}{n+1}=\\frac{n}{n+1}$",
    },
    # ID 118
    {
        "id": 118,
        "content_en": "In the geometric sequence $\\{a_n\\}$, $a_2=2$, $a_5=\\frac{1}{4}$, then the common ratio $q=$",
        "options_en": '["A. -\\\\frac{1}{2}","B. \\\\frac{1}{2}","C. -2","D. 2"]',
        "answer_en": "B",
        "solution_en": "$a_5=a_2q^3$, $\\frac{1}{4}=2q^3$, $q^3=\\frac{1}{8}$, $q=\\frac{1}{2}$",
        "content_vi": "Trong c\\u1ea5p s\\u1ed1 nh\\u00e2n $\\{a_n\\}$, $a_2=2$, $a_5=\\frac{1}{4}$, khi \\u0111\\u00f3 c\\u00f4ng b\\u1ed9i $q=$",
        "options_vi": '["A. -\\\\frac{1}{2}","B. \\\\frac{1}{2}","C. -2","D. 2"]',
        "answer_vi": "B",
        "solution_vi": "$a_5=a_2q^3$, $\\frac{1}{4}=2q^3$, $q^3=\\frac{1}{8}$, $q=\\frac{1}{2}$",
    },
    # ID 119
    {
        "id": 119,
        "content_en": "$1+3+5+\\cdots+(2n-1)=$ ____",
        "options_en": None,
        "answer_en": "n\u00b2",
        "solution_en": "Sum of arithmetic sequence: $\\frac{n(1+(2n-1))}{2}=n^2$",
        "content_vi": "$1+3+5+\\cdots+(2n-1)=$ ____",
        "options_vi": None,
        "answer_vi": "n\u00b2",
        "solution_vi": "T\\u1ed5ng c\\u1ea5p s\\u1ed1 c\\u1ed9ng: $\\frac{n(1+(2n-1))}{2}=n^2$",
    },
    # ID 120
    {
        "id": 120,
        "content_en": "Select 3 books from 5 different books and give them to 3 students, one book per person. The number of different ways to do this is",
        "options_en": '["A. 10","B. 60","C. 120","D. 20"]',
        "answer_en": "B",
        "solution_en": "$A_5^3=5\\times4\\times3=60$",
        "content_vi": "Ch\\u1ecdn 3 quy\\u1ec3n s\\u00e1ch t\\u1eeb 5 quy\\u1ec3n s\\u00e1ch kh\\u00e1c nhau t\\u1eb7ng cho 3 h\\u1ecdc sinh, m\\u1ed7i ng\\u01b0\\u1eddi m\\u1ed9t quy\\u1ec3n. S\\u1ed1 c\\u00e1ch t\\u1eb7ng kh\\u00e1c nhau l\\u00e0",
        "options_vi": '["A. 10","B. 60","C. 120","D. 20"]',
        "answer_vi": "B",
        "solution_vi": "$A_5^3=5\\times4\\times3=60$",
    },
    # ID 121
    {
        "id": 121,
        "content_en": "In the expansion of $(1+x)^{5}$, the coefficient of $x^2$ is ____",
        "options_en": None,
        "answer_en": "10",
        "solution_en": "$C_5^2=10$",
        "content_vi": "Trong khai tri\\u1ec3n c\\u1ee7a $(1+x)^{5}$, h\\u1ec7 s\\u1ed1 c\\u1ee7a $x^2$ l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "10",
        "solution_vi": "$C_5^2=10$",
    },
    # ID 122
    {
        "id": 122,
        "content_en": "Roll a die twice. The probability that the sum of the two rolls is 7 is",
        "options_en": '["A. \\\\frac{1}{12}","B. \\\\frac{1}{6}","C. \\\\frac{1}{5}","D. \\\\frac{1}{4}"]',
        "answer_en": "B",
        "solution_en": "Combinations with sum=7: $(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)$, total 6. Total outcomes $6\\times6=36$. $P=\\frac{6}{36}=\\frac{1}{6}$",
        "content_vi": "Gieo m\\u1ed9t con x\\u00fac s\\u1eafc hai l\\u1ea7n. X\\u00e1c su\\u1ea5t \\u0111\\u1ec3 t\\u1ed5ng s\\u1ed1 ch\\u1ea5m c\\u1ee7a hai l\\u1ea7n gieo b\\u1eb1ng 7 l\\u00e0",
        "options_vi": '["A. \\\\frac{1}{12}","B. \\\\frac{1}{6}","C. \\\\frac{1}{5}","D. \\\\frac{1}{4}"]',
        "answer_vi": "B",
        "solution_vi": "C\\u00e1c t\\u1ed5 h\\u1ee3p c\\u00f3 t\\u1ed5ng=7: $(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)$, t\\u1ed5ng c\\u1ed9ng 6. T\\u1ed5ng s\\u1ed1 k\\u1ebft qu\\u1ea3 $6\\times6=36$. $P=\\frac{6}{36}=\\frac{1}{6}$",
    },
    # ID 123
    {
        "id": 123,
        "content_en": "The constant term in the expansion of $(2x-\\frac{1}{x})^6$ is ____ (answer with a number)",
        "options_en": None,
        "answer_en": "-160",
        "solution_en": "General term $T_{r+1}=C_6^r(2x)^{6-r}(-\\frac{1}{x})^r=C_6^r2^{6-r}(-1)^r x^{6-2r}$. Let $6-2r=0$, $r=3$. Constant term $=C_6^3\\times2^3\\times(-1)^3=20\\times8\\times(-1)=-160$",
        "content_vi": "S\\u1ed1 h\\u1ea1ng kh\\u00f4ng \\u0111\\u1ed5i trong khai tri\\u1ec3n c\\u1ee7a $(2x-\\frac{1}{x})^6$ l\\u00e0 ____ (tr\\u1ea3 l\\u1eddi b\\u1eb1ng s\\u1ed1)",
        "options_vi": None,
        "answer_vi": "-160",
        "solution_vi": "S\\u1ed1 h\\u1ea1ng t\\u1ed5ng qu\\u00e1t $T_{r+1}=C_6^r(2x)^{6-r}(-\\frac{1}{x})^r=C_6^r2^{6-r}(-1)^r x^{6-2r}$. Cho $6-2r=0$, $r=3$. S\\u1ed1 h\\u1ea1ng kh\\u00f4ng \\u0111\\u1ed5i $=C_6^3\\times2^3\\times(-1)^3=20\\times8\\times(-1)=-160$",
    },
    # ID 124
    {
        "id": 124,
        "content_en": "The number of five-digit numbers greater than 20000 with no repeated digits that can be formed using the digits 0,1,2,3,4 is",
        "options_en": '["A. 96","B. 72","C. 48","D. 120"]',
        "answer_en": "B",
        "solution_en": "The ten-thousands digit can be 2,3,4 (3 choices); the remaining 4 digits can be permuted in $4!=24$ ways. Total $3\\times24=72$",
        "content_vi": "S\\u1ed1 c\\u00e1c s\\u1ed1 c\\u00f3 n\\u0103m ch\\u1eef s\\u1ed1 l\\u1edbn h\\u01a1n 20000 kh\\u00f4ng c\\u00f3 ch\\u1eef s\\u1ed1 l\\u1eb7p l\\u1ea1i c\\u00f3 th\\u1ec3 l\\u1eadp t\\u1eeb c\\u00e1c ch\\u1eef s\\u1ed1 0,1,2,3,4 l\\u00e0",
        "options_vi": '["A. 96","B. 72","C. 48","D. 120"]',
        "answer_vi": "B",
        "solution_vi": "Ch\\u1eef s\\u1ed1 h\\u00e0ng ch\\u1ee5c ngh\\u00ecn c\\u00f3 th\\u1ec3 l\\u00e0 2,3,4 (3 l\\u1ef1a ch\\u1ecdn); 4 ch\\u1eef s\\u1ed1 c\\u00f2n l\\u1ea1i \\u0111\\u01b0\\u1ee3c ho\\u00e1n v\\u1ecb $4!=24$ c\\u00e1ch. T\\u1ed5ng c\\u1ed9ng $3\\times24=72$",
    },
    # ID 125
    {
        "id": 125,
        "content_en": "Randomly pick 2 different numbers from {1,2,3,4}. The probability that the absolute difference between the two numbers is 2 is ____",
        "options_en": None,
        "answer_en": "1/3",
        "solution_en": "Total combinations $C_4^2=6$. Pairs with difference 2: $(1,3)(2,4)$, 2 in total. $P=\\frac{2}{6}=\\frac{1}{3}$",
        "content_vi": "L\\u1ea5y ng\\u1eabu nhi\\u00ean 2 s\\u1ed1 kh\\u00e1c nhau t\\u1eeb t\\u1eadp {1,2,3,4}. X\\u00e1c su\\u1ea5t \\u0111\\u1ec3 hi\\u1ec7u tuy\\u1ec7t \\u0111\\u1ed1i c\\u1ee7a hai s\\u1ed1 b\\u1eb1ng 2 l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "1/3",
        "solution_vi": "T\\u1ed5ng s\\u1ed1 t\\u1ed5 h\\u1ee3p $C_4^2=6$. C\\u00e1c c\\u1eb7p c\\u00f3 hi\\u1ec7u b\\u1eb1ng 2: $(1,3)(2,4)$, t\\u1ed5ng c\\u1ed9ng 2. $P=\\frac{2}{6}=\\frac{1}{3}$",
    },
    # ID 126
    {
        "id": 126,
        "content_en": "Assign 4 students to 3 different extracurricular groups, with each group having at least 1 person. The number of different assignment plans is",
        "options_en": '["A. 36","B. 24","C. 72","D. 12"]',
        "answer_en": "A",
        "solution_en": "$C_4^2\\times3!=6\\times6=36$",
        "content_vi": "Ph\\u00e2n 4 h\\u1ecdc sinh v\\u00e0o 3 nh\\u00f3m ngo\\u1ea1i kh\\u00f3a kh\\u00e1c nhau, m\\u1ed7i nh\\u00f3m c\\u00f3 \\u00edt nh\\u1ea5t 1 ng\\u01b0\\u1eddi. S\\u1ed1 c\\u00e1ch ph\\u00e2n c\\u00f4ng kh\\u00e1c nhau l\\u00e0",
        "options_vi": '["A. 36","B. 24","C. 72","D. 12"]',
        "answer_vi": "A",
        "solution_vi": "$C_4^2\\times3!=6\\times6=36$",
    },
    # ID 127
    {
        "id": 127,
        "content_en": "A bag contains 3 red balls and 2 white balls. 2 balls are randomly drawn from it. The mathematical expectation $E(X)$ of the number $X$ of red balls drawn is ____",
        "options_en": None,
        "answer_en": "6/5",
        "solution_en": "$P(X=0)=\\frac{C_2^2}{C_5^2}=\\frac{1}{10}$, $P(X=1)=\\frac{C_3^1C_2^1}{C_5^2}=\\frac{6}{10}$, $P(X=2)=\\frac{C_3^2}{C_5^2}=\\frac{3}{10}$. $E(X)=0+1\\times0.6+2\\times0.3=1.2=\\frac{6}{5}$",
        "content_vi": "M\\u1ed9t t\\u00fai c\\u00f3 3 qu\\u1ea3 b\\u00f3ng \\u0111\\u1ecf v\\u00e0 2 qu\\u1ea3 b\\u00f3ng tr\\u1eafng. L\\u1ea5y ng\\u1eabu nhi\\u00ean 2 qu\\u1ea3 b\\u00f3ng t\\u1eeb t\\u00fai. K\\u1ef3 v\\u1ecdng to\\u00e1n h\\u1ecdc $E(X)$ c\\u1ee7a s\\u1ed1 b\\u00f3ng \\u0111\\u1ecf $X$ l\\u1ea5y \\u0111\\u01b0\\u1ee3c l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "6/5",
        "solution_vi": "$P(X=0)=\\frac{C_2^2}{C_5^2}=\\frac{1}{10}$, $P(X=1)=\\frac{C_3^1C_2^1}{C_5^2}=\\frac{6}{10}$, $P(X=2)=\\frac{C_3^2}{C_5^2}=\\frac{3}{10}$. $E(X)=0+1\\times0.6+2\\times0.3=1.2=\\frac{6}{5}$",
    },
    # ID 128
    {
        "id": 128,
        "content_en": "The coefficient of $x^2$ in the expansion of $(x+2)^4$ is",
        "options_en": '["A. 6","B. 12","C. 24","D. 48"]',
        "answer_en": "C",
        "solution_en": "$C_4^2\\times2^2=6\\times4=24$",
        "content_vi": "H\\u1ec7 s\\u1ed1 c\\u1ee7a $x^2$ trong khai tri\\u1ec3n c\\u1ee7a $(x+2)^4$ l\\u00e0",
        "options_vi": '["A. 6","B. 12","C. 24","D. 48"]',
        "answer_vi": "C",
        "solution_vi": "$C_4^2\\times2^2=6\\times4=24$",
    },
    # ID 129
    {
        "id": 129,
        "content_en": "Two people A and B shoot hoops, with hit rates of 0.7 and 0.6 respectively. Each shoots once. The probability that at least one of them hits is ____",
        "options_en": None,
        "answer_en": "0.88",
        "solution_en": "$P=1-P(\\text{both miss})=1-0.3\\times0.4=0.88$",
        "content_vi": "Hai ng\\u01b0\\u1eddi A v\\u00e0 B n\\u00e9m b\\u00f3ng r\\u1ed5, t\\u1ef7 l\\u1ec7 n\\u00e9m tr\\u00fang l\\u1ea7n l\\u01b0\\u1ee3t l\\u00e0 0,7 v\\u00e0 0,6. M\\u1ed7i ng\\u01b0\\u1eddi n\\u00e9m m\\u1ed9t l\\u1ea7n. X\\u00e1c su\\u1ea5t \\u0111\\u1ec3 c\\u00f3 \\u00edt nh\\u1ea5t m\\u1ed9t ng\\u01b0\\u1eddi n\\u00e9m tr\\u00fang l\\u00e0 ____",
        "options_vi": None,
        "answer_vi": "0.88",
        "solution_vi": "$P=1-P(\\text{c\\u1ea3 hai \\u0111\\u1ec1u tr\\u01b0\\u1ee3t})=1-0.3\\times0.4=0.88$",
    },
    # ID 130
    {
        "id": 130,
        "content_en": "6 chairs are arranged in a row. 3 people sit down randomly. The number of seating arrangements where no two people are adjacent is",
        "options_en": '["A. 120","B. 96","C. 72","D. 24"]',
        "answer_en": "D",
        "solution_en": "First arrange 3 empty chairs, there are 4 gaps (including ends). Choose 3 gaps to place people: $A_4^3=24$",
        "content_vi": "6 c\\u00e1i gh\\u1ebf x\\u1ebfp th\\u00e0nh m\\u1ed9t h\\u00e0ng. 3 ng\\u01b0\\u1eddi ng\\u1ed3i ng\\u1eabu nhi\\u00ean. S\\u1ed1 c\\u00e1ch s\\u1eafp x\\u1ebfp ch\\u1ed7 ng\\u1ed3i sao cho kh\\u00f4ng c\\u00f3 hai ng\\u01b0\\u1eddi n\\u00e0o ng\\u1ed3i c\\u1ea1nh nhau l\\u00e0",
        "options_vi": '["A. 120","B. 96","C. 72","D. 24"]',
        "answer_vi": "D",
        "solution_vi": "X\\u1ebfp tr\\u01b0\\u1edbc 3 gh\\u1ebf tr\\u1ed1ng, c\\u00f3 4 kho\\u1ea3ng tr\\u1ed1ng (g\\u1ed3m c\\u1ea3 hai \\u0111\\u1ea7u). Ch\\u1ecdn 3 kho\\u1ea3ng tr\\u1ed1ng \\u0111\\u1ec3 \\u0111\\u1eb7t ng\\u01b0\\u1eddi: $A_4^3=24$",
    },
]

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for t in translations:
    cur.execute("""
        UPDATE questions SET
            content_en = ?,
            options_en = ?,
            answer_en = ?,
            solution_en = ?,
            content_vi = ?,
            options_vi = ?,
            answer_vi = ?,
            solution_vi = ?
        WHERE id = ?
    """, (
        t["content_en"],
        t["options_en"],
        t["answer_en"],
        t["solution_en"],
        t["content_vi"],
        t["options_vi"],
        t["answer_vi"],
        t["solution_vi"],
        t["id"]
    ))
    print(f"Updated ID {t['id']}")

conn.commit()
conn.close()
print("Done! All translations saved.")
