# Step 1: Build the JSON data with translations
import json, sys, sqlite3

data = []
def add(id_val, content_en, content_vi, options_en, options_vi, answer_en, answer_vi, solution_en, solution_vi):
    data.append({
        'id': id_val,
        'content_en': content_en,
        'content_vi': content_vi,
        'options_en': options_en,
        'options_vi': options_vi,
        'answer_en': answer_en,
        'answer_vi': answer_vi,
        'solution_en': solution_en,
        'solution_vi': solution_vi
    })

# === TRANSLATIONS ===

add(133,
  "Given plane $\\alpha$ passes through $A(1,0,0),B(0,1,0),C(0,0,1)$, a normal vector of plane $\\alpha$ is ____",
  "Cho m\\u1eb7t ph\\u1eb3ng $\\alpha$ \\u0111i qua $A(1,0,0),B(0,1,0),C(0,0,1)$, m\\u1ed9t vect\\u01a1 ph\\u00e1p tuy\\u1ebfn c\\u1ee7a m\\u1eb7t ph\\u1eb3ng $\\alpha$ l\\u00e0 ____",
  None, None,
  "(1,1,1)", "(1,1,1)",
  "$\\vec{AB}=(-1,1,0)$, $\\vec{AC}=(-1,0,1)$. $\\vec{n}=\\vec{AB}\\times\\vec{AC}=(1,1,1)$",
  "$\\vec{AB}=(-1,1,0)$, $\\vec{AC}=(-1,0,1)$. $\\vec{n}=\\vec{AB}\\times\\vec{AC}=(1,1,1)$"
)

add(134,
  "Cube $ABCD-A_1B_1C_1D_1$ has edge length 1. The cosine of the angle between skew lines $AB_1$ and $BC_1$ is",
  "H\\u00ecnh l\\u1eadp ph\\u01b0\\u01a1ng $ABCD-A_1B_1C_1D_1$ c\\u00f3 c\\u1ea1nh b\\u1eb1ng 1. Cosin c\\u1ee7a g\\u00f3c gi\\u1eefa hai \\u0111\\u01b0\\u1eddng th\\u1eb3ng ch\\u00e9o nhau $AB_1$ v\\u00e0 $BC_1$ l\\u00e0",
  json.dumps(["A. \\frac{1}{2}","B. \\frac{\\sqrt{2}}{2}","C. \\frac{\\sqrt{3}}{3}","D. \\frac{1}{3}"]),
  json.dumps(["A. \\frac{1}{2}","B. \\frac{\\sqrt{2}}{2}","C. \\frac{\\sqrt{3}}{3}","D. \\frac{1}{3}"]),
  "A", "A",
  "Set D as origin: $A(1,0,0),B_1(1,1,1),B(1,1,0),C_1(0,1,1)$. $\\vec{AB_1}=(0,1,1),\\vec{BC_1}=(-1,0,1)$. $\\cos\\theta=\\frac{1}{\\sqrt{2}\\cdot\\sqrt{2}}=\\frac{1}{2}$",
  "L\\u1ea5y D l\\u00e0m g\\u1ed1c: $A(1,0,0),B_1(1,1,1),B(1,1,0),C_1(0,1,1)$. $\\vec{AB_1}=(0,1,1),\\vec{BC_1}=(-1,0,1)$. $\\cos\\theta=\\frac{1}{\\sqrt{2}\\cdot\\sqrt{2}}=\\frac{1}{2}$"
)

add(135,
  "The distance from point $P(1,2,3)$ to the $xOy$ plane is ____",
  "Kho\\u1ea3ng c\\u00e1ch t\\u1eeb \\u0111i\\u1ec3m $P(1,2,3)$ \\u0111\\u1ebfn m\\u1eb7t ph\\u1eb3ng $xOy$ l\\u00e0 ____",
  None, None,
  "3", "3",
  "Distance to the $xOy$ plane is $|z|=3$",
  "Kho\\u1ea3ng c\\u00e1ch \\u0111\\u1ebfn m\\u1eb7t ph\\u1eb3ng $xOy$ l\\u00e0 $|z|=3$"
)

add(136,
  "The normal vectors of the two half-planes of a dihedral angle $\\alpha-l-\\beta$ are $\\vec{n_1}=(1,0,1)$ and $\\vec{n_2}=(0,1,1)$. The dihedral angle is",
  "Vect\\u01a1 ph\\u00e1p tuy\\u1ebfn c\\u1ee7a hai n\\u1eeda m\\u1eb7t ph\\u1eb3ng c\\u1ee7a g\\u00f3c nh\\u1ecb di\\u1ec7n $\\alpha-l-\\beta$ l\\u1ea7n l\\u01b0\\u1ee3t l\\u00e0 $\\vec{n_1}=(1,0,1)$ v\\u00e0 $\\vec{n_2}=(0,1,1)$. G\\u00f3c nh\\u1ecb di\\u1ec7n l\\u00e0",
  json.dumps(["A. 30\\degree","B. 45\\degree","C. 60\\degree","D. 120\\degree"]),
  json.dumps(["A. 30\\degree","B. 45\\degree","C. 60\\degree","D. 120\\degree"]),
  "C", "C",
  "$\\cos\\theta=\\frac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}=\\frac{1}{\\sqrt{2}\\cdot\\sqrt{2}}=\\frac{1}{2}$, $\\theta=60\\degree$",
  "$\\cos\\theta=\\frac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}=\\frac{1}{\\sqrt{2}\\cdot\\sqrt{2}}=\\frac{1}{2}$, $\\theta=60\\degree$"
)

add(137,
  "In a regular quadrilateral pyramid $S-ABCD$, the base edge length is 2, and the lateral edge length is $\\sqrt{6}$. The height $SO$ is ____",
  "Trong h\\u00ecnh ch\\u00f3p t\\u1ee9 gi\\u00e1c \\u0111\\u1ec1u $S-ABCD$, c\\u1ea1nh \\u0111\\u00e1y d\\u00e0i 2, c\\u1ea1nh b\\u00ean d\\u00e0i $\\sqrt{6}$. Chi\\u1ec1u cao $SO$ l\\u00e0 ____",
  None, None,
  "2", "2",
  "Half the diagonal of the base square $=\\sqrt{2}$. $SO=\\sqrt{SA^2-AO^2}=\\sqrt{6-2}=2$",
  "N\\u1eeda \\u0111\\u01b0\\u1eddng ch\\u00e9o h\\u00ecnh vu\\u00f4ng \\u0111\\u00e1y $=\\sqrt{2}$. $SO=\\sqrt{SA^2-AO^2}=\\sqrt{6-2}=2$"
)

add(138,
  "Given three points $A(1,2,3),B(2,4,1),C(3,1,5)$, the area of $\\triangle ABC$ is",
  "Cho ba \\u0111i\\u1ec3m $A(1,2,3),B(2,4,1),C(3,1,5)$, di\\u1ec7n t\\u00edch c\\u1ee7a $\\triangle ABC$ l\\u00e0",
  json.dumps(["A. \\frac{\\sqrt{230}}{2}","B. \\frac{\\sqrt{210}}{2}","C. 5\\sqrt{2}","D. \\sqrt{115}"]),
  json.dumps(["A. \\frac{\\sqrt{230}}{2}","B. \\frac{\\sqrt{210}}{2}","C. 5\\sqrt{2}","D. \\sqrt{115}"]),
  "B", "B",
  "$\\vec{AB}=(1,2,-2),\\vec{AC}=(2,-1,2)$. $|\\vec{AB}\\times\\vec{AC}|=\\sqrt{210}$. $S=\\frac{1}{2}\\times\\sqrt{210}$",
  "$\\vec{AB}=(1,2,-2),\\vec{AC}=(2,-1,2)$. $|\\vec{AB}\\times\\vec{AC}|=\\sqrt{210}$. $S=\\frac{1}{2}\\times\\sqrt{210}$"
)

add(139,
  "Given $\\vec{a}=(2,-1,3)$, $\\vec{b}=(-4,2,x)$, and $\\vec{a}\\parallel\\vec{b}$, then $x=$ ____",
  "Cho $\\vec{a}=(2,-1,3)$, $\\vec{b}=(-4,2,x)$, v\\u00e0 $\\vec{a}\\parallel\\vec{b}$, th\\u00ec $x=$ ____",
  None, None,
  "-6", "-6",
  "From $\\vec{a}\\parallel\\vec{b}$ we get $\\frac{2}{-4}=\\frac{-1}{2}=\\frac{3}{x}$, so $x=-6$",
  "T\\u1eeb $\\vec{a}\\parallel\\vec{b}$ suy ra $\\frac{2}{-4}=\\frac{-1}{2}=\\frac{3}{x}$, v\\u1eady $x=-6$"
)

add(140,
  "The focal length of the ellipse $\\frac{x^2}{16}+\\frac{y^2}{9}=1$ is",
  "Ti\\u00eau c\\u1ef1 c\\u1ee7a elip $\\frac{x^2}{16}+\\frac{y^2}{9}=1$ l\\u00e0",
  json.dumps(["A. 2\\sqrt{7}","B. \\sqrt{7}","C. 5","D. 7"]),
  json.dumps(["A. 2\\sqrt{7}","B. \\sqrt{7}","C. 5","D. 7"]),
  "A", "A",
  "$a^2=16,b^2=9$, $c^2=7$, $2c=2\\sqrt{7}$",
  "$a^2=16,b^2=9$, $c^2=7$, $2c=2\\sqrt{7}$"
)

add(141,
  "The directrix of the parabola $y^2=8x$ is ____",
  "\\u0110\\u01b0\\u1eddng chu\\u1ea9n c\\u1ee7a parabol $y^2=8x$ l\\u00e0 ____",
  None, None,
  "x=-2", "x=-2",
  "$2p=8$, $p=4$, directrix $x=-\\frac{p}{2}=-2$",
  "$2p=8$, $p=4$, \\u0111\\u01b0\\u1eddng chu\\u1ea9n $x=-\\frac{p}{2}=-2$"
)

add(142,
  "The asymptotes of the hyperbola $\\frac{x^2}{9}-\\frac{y^2}{16}=1$ are",
  "C\\u00e1c \\u0111\\u01b0\\u1eddng ti\\u1ec7m c\\u1eadn c\\u1ee7a hyperbol $\\frac{x^2}{9}-\\frac{y^2}{16}=1$ l\\u00e0",
  json.dumps(["A. y=\\pm\\frac{3}{4}x","B. y=\\pm\\frac{4}{3}x","C. y=\\pm\\frac{9}{16}x","D. y=\\pm\\frac{16}{9}x"]),
  json.dumps(["A. y=\\pm\\frac{3}{4}x","B. y=\\pm\\frac{4}{3}x","C. y=\\pm\\frac{9}{16}x","D. y=\\pm\\frac{16}{9}x"]),
  "B", "B",
  "$a=3,b=4$, asymptotes $y=\\pm\\frac{b}{a}x=\\pm\\frac{4}{3}x$",
  "$a=3,b=4$, ti\\u1ec7m c\\u1eadn $y=\\pm\\frac{b}{a}x=\\pm\\frac{4}{3}x$"
)

add(143,
  "A point P on the ellipse $\\frac{x^2}{25}+\\frac{y^2}{16}=1$ is 6 units from the left focus. Its distance to the right focus is ____",
  "M\\u1ed9t \\u0111i\\u1ec3m P tr\\u00ean elip $\\frac{x^2}{25}+\\frac{y^2}{16}=1$ c\\u00e1ch ti\\u00eau \\u0111i\\u1ec3m tr\\u00e1i 6 \\u0111\\u01a1n v\\u1ecb. Kho\\u1ea3ng c\\u00e1ch t\\u1eeb P \\u0111\\u1ebfn ti\\u00eau \\u0111i\\u1ec3m ph\\u1ea3i l\\u00e0 ____",
  None, None,
  "4", "4",
  "$|PF_1|+|PF_2|=2a=10$, $|PF_2|=4$",
  "$|PF_1|+|PF_2|=2a=10$, $|PF_2|=4$"
)

add(144,
  "An ellipse centered at origin with foci on the $x$-axis has major axis length 10 and minor axis length 6. Its equation is",
  "M\\u1ed9t elip c\\u00f3 t\\u00e2m t\\u1ea1i g\\u1ed1c t\\u1ecda \\u0111\\u1ed9, ti\\u00eau \\u0111i\\u1ec3m tr\\u00ean tr\\u1ee5c $x$, \\u0111\\u1ed9 d\\u00e0i tr\\u1ee5c l\\u1edbn 10, \\u0111\\u1ed9 d\\u00e0i tr\\u1ee5c b\\u00e9 6. Ph\\u01b0\\u01a1ng tr\\u00ecnh elip l\\u00e0",
  json.dumps(["A. \\frac{x^2}{25}+\\frac{y^2}{9}=1","B. \\frac{x^2}{9}+\\frac{y^2}{25}=1","C. \\frac{x^2}{100}+\\frac{y^2}{36}=1","D. \\frac{x^2}{5}+\\frac{y^2}{3}=1"]),
  json.dumps(["A. \\frac{x^2}{25}+\\frac{y^2}{9}=1","B. \\frac{x^2}{9}+\\frac{y^2}{25}=1","C. \\frac{x^2}{100}+\\frac{y^2}{36}=1","D. \\frac{x^2}{5}+\\frac{y^2}{3}=1"]),
  "A", "A",
  "$a=5,b=3$, equation: $\\frac{x^2}{25}+\\frac{y^2}{9}=1$",
  "$a=5,b=3$, ph\\u01b0\\u01a1ng tr\\u00ecnh: $\\frac{x^2}{25}+\\frac{y^2}{9}=1$"
)

add(145,
  "The focus of the parabola $y=ax^2$ is $(0,\\frac{1}{4})$, then $a=$ ____",
  "Ti\\u00eau \\u0111i\\u1ec3m c\\u1ee7a parabol $y=ax^2$ l\\u00e0 $(0,\\frac{1}{4})$, th\\u00ec $a=$ ____",
  None, None,
  "1", "1",
  "Standard form $x^2=\\frac{1}{a}y$, $2p=\\frac{1}{a}$, focus $(0,\\frac{p}{2})=(0,\\frac{1}{4a})=(0,\\frac{1}{4})$, so $a=1$",
  "D\\u1ea1ng chu\\u1ea9n $x^2=\\frac{1}{a}y$, $2p=\\frac{1}{a}$, ti\\u00eau \\u0111i\\u1ec3m $(0,\\frac{p}{2})=(0,\\frac{1}{4a})=(0,\\frac{1}{4})$, suy ra $a=1$"
)

add(146,
  "The eccentricity of the hyperbola $x^2-\\frac{y^2}{3}=1$ is",
  "T\\u00e2m sai c\\u1ee7a hyperbol $x^2-\\frac{y^2}{3}=1$ l\\u00e0",
  json.dumps(["A. 1","B. 2","C. \\sqrt{2}","D. \\sqrt{3}"]),
  json.dumps(["A. 1","B. 2","C. \\sqrt{2}","D. \\sqrt{3}"]),
  "B", "B",
  "$a^2=1,b^2=3$, $c^2=4$, $e=\\frac{c}{a}=2$",
  "$a^2=1,b^2=3$, $c^2=4$, $e=\\frac{c}{a}=2$"
)

add(147,
  "An ellipse $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ has a focus at $(4,0)$ and $a=5$. Then $b=$ ____",
  "Elip $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1(a>b>0)$ c\\u00f3 m\\u1ed9t ti\\u00eau \\u0111i\\u1ec3m t\\u1ea1i $(4,0)$ v\\u00e0 $a=5$. Khi \\u0111\\u00f3 $b=$ ____",
  None, None,
  "3", "3",
  "$c=4$, $b^2=a^2-c^2=25-16=9$, $b=3$",
  "$c=4$, $b^2=a^2-c^2=25-16=9$, $b=3$"
)

add(148,
  "Point P is on the parabola $y^2=4x$, and its distance to the focus is 5. The x-coordinate of P is",
  "\\u0110i\\u1ec3m P n\\u1eb1m tr\\u00ean parabol $y^2=4x$, kho\\u1ea3ng c\\u00e1ch t\\u1eeb P \\u0111\\u1ebfn ti\\u00eau \\u0111i\\u1ec3m l\\u00e0 5. Ho\\u00e0nh \\u0111\\u1ed9 c\\u1ee7a P l\\u00e0",
  json.dumps(["A. 3","B. 4","C. 5","D. 6"]),
  json.dumps(["A. 3","B. 4","C. 5","D. 6"]),
  "B", "B",
  "Focus $F(1,0)$. By definition $|PF|=x_P+1=5$, $x_P=4$",
  "Ti\\u00eau \\u0111i\\u1ec3m $F(1,0)$. Theo \\u0111\\u1ecbnh ngh\\u0129a $|PF|=x_P+1=5$, $x_P=4$"
)

add(149,
  "The left and right foci of ellipse $\\frac{x^2}{4}+\\frac{y^2}{3}=1$ are $F_1,F_2$. $P$ is a point on the ellipse with $\\angle F_1PF_2=60\\degree$. The area of $\\triangle F_1PF_2$ is ____",
  "Ti\\u00eau \\u0111i\\u1ec3m tr\\u00e1i v\\u00e0 ph\\u1ea3i c\\u1ee7a elip $\\frac{x^2}{4}+\\frac{y^2}{3}=1$ l\\u00e0 $F_1,F_2$. $P$ l\\u00e0 \\u0111i\\u1ec3m tr\\u00ean elip v\\u1edbi $\\angle F_1PF_2=60\\degree$. Di\\u1ec7n t\\u00edch $\\triangle F_1PF_2$ l\\u00e0 ____",
  None, None,
  "\\u221a3", "\\u221a3",
  "$a=2,c=1$. Using the focal triangle area formula: $S=b^2\\tan\\frac{\\theta}{2}=3\\times\\tan30\\degree=\\sqrt{3}$",
  "$a=2,c=1$. D\\u00f9ng c\\u00f4ng th\\u1ee9c di\\u1ec7n t\\u00edch tam gi\\u00e1c ti\\u00eau \\u0111i\\u1ec3m: $S=b^2\\tan\\frac{\\theta}{2}=3\\times\\tan30\\degree=\\sqrt{3}$"
)

add(150,
  "The derivative of $f(x)=x^2$ at $x=1$ is",
  "\\u0110\\u1ea1o h\\u00e0m c\\u1ee7a $f(x)=x^2$ t\\u1ea1i $x=1$ l\\u00e0",
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  "B", "B",
  "$f'(x)=2x$, $f'(1)=2$",
  "$f'(x)=2x$, $f'(1)=2$"
)

add(151,
  "The tangent line to the curve $y=x^3$ at point $(1,1)$ is ____",
  "Ti\\u1ebfp tuy\\u1ebfn c\\u1ee7a \\u0111\\u01b0\\u1eddng cong $y=x^3$ t\\u1ea1i \\u0111i\\u1ec3m $(1,1)$ l\\u00e0 ____",
  None, None,
  "y=3x-2", "y=3x-2",
  "$y'=3x^2$, $k=3$. Tangent: $y-1=3(x-1)$, $y=3x-2$",
  "$y'=3x^2$, $k=3$. Ti\\u1ebfp tuy\\u1ebfn: $y-1=3(x-1)$, $y=3x-2$"
)

add(152,
  "The decreasing interval of $f(x)=x^3-3x$ is",
  "Kho\\u1ea3ng ngh\\u1ecbch bi\\u1ebfn c\\u1ee7a h\\u00e0m s\\u1ed1 $f(x)=x^3-3x$ l\\u00e0",
  json.dumps(["A. (-\\infty,-1)","B. (-1,1)","C. (1,+\\infty)","D. (-\\infty,-1)\\cup(1,+\\infty)"]),
  json.dumps(["A. (-\\infty,-1)","B. (-1,1)","C. (1,+\\infty)","D. (-\\infty,-1)\\cup(1,+\\infty)"]),
  "B", "B",
  "$f'(x)=3x^2-3=3(x+1)(x-1)$. $f'(x)<0$ on $(-1,1)$",
  "$f'(x)=3x^2-3=3(x+1)(x-1)$. $f'(x)<0$ tr\\u00ean $(-1,1)$"
)

add(153,
  "The minimum value of $f(x)=x^3-3x^2+1$ on $[-1,3]$ is ____",
  "Gi\\u00e1 tr\\u1ecb nh\\u1ecf nh\\u1ea5t c\\u1ee7a $f(x)=x^3-3x^2+1$ tr\\u00ean $[-1,3]$ l\\u00e0 ____",
  None, None,
  "-3", "-3",
  "$f'(x)=3x^2-6x=3x(x-2)$. Critical points $x=0,2$. $f(-1)=-3,f(0)=1,f(2)=-3,f(3)=1$. Minimum $-3$",
  "$f'(x)=3x^2-6x=3x(x-2)$. \\u0110i\\u1ec3m t\\u1edbi h\\u1ea1n $x=0,2$. $f(-1)=-3,f(0)=1,f(2)=-3,f(3)=1$. Gi\\u00e1 tr\\u1ecb nh\\u1ecf nh\\u1ea5t $-3$"
)

add(154,
  "The tangent slope of $f(x)=\\ln x+ax$ at $x=1$ is 3. Then $a=$",
  "H\\u1ec7 s\\u1ed1 g\\u00f3c ti\\u1ebfp tuy\\u1ebfn c\\u1ee7a $f(x)=\\ln x+ax$ t\\u1ea1i $x=1$ b\\u1eb1ng 3. Khi \\u0111\\u00f3 $a=$",
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  "B", "B",
  "$f'(x)=\\frac{1}{x}+a$, $f'(1)=1+a=3$, $a=2$",
  "$f'(x)=\\frac{1}{x}+a$, $f'(1)=1+a=3$, $a=2$"
)

add(155,
  "The increasing interval of $f(x)=e^x-x$ is ____",
  "Kho\\u1ea3ng \\u0111\\u1ed3ng bi\\u1ebfn c\\u1ee7a $f(x)=e^x-x$ l\\u00e0 ____",
  None, None,
  "(0,+\\u221e)", "(0,+\\u221e)",
  "$f'(x)=e^x-1$. $f'(x)>0$ when $x>0$",
  "$f'(x)=e^x-1$. $f'(x)>0$ khi $x>0$"
)

add(156,
  "The minimum value of $f(x)=x+\\frac{1}{x}$ for $x>0$ is",
  "Gi\\u00e1 tr\\u1ecb nh\\u1ecf nh\\u1ea5t c\\u1ee7a $f(x)=x+\\frac{1}{x}$ v\\u1edbi $x>0$ l\\u00e0",
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  json.dumps(["A. 1","B. 2","C. 3","D. 4"]),
  "B", "B",
  "$f'(x)=1-\\frac{1}{x^2}=0$, $x=1$. $f(1)=2$. Or by AM-GM: $x+\\frac{1}{x}\\ge2$",
  "$f'(x)=1-\\frac{1}{x^2}=0$, $x=1$. $f(1)=2$. Ho\\u1eb7c d\\u00f9ng B\\u0110T Cauchy: $x+\\frac{1}{x}\\ge2$"
)

add(157,
  "The minimum value of $f(x)=x\\ln x$ is ____",
  "Gi\\u00e1 tr\\u1ecb nh\\u1ecf nh\\u1ea5t c\\u1ee7a $f(x)=x\\ln x$ l\\u00e0 ____",
  None, None,
  "-1/e", "-1/e",
  "$f'(x)=\\ln x+1=0$, $x=\\frac{1}{e}$. $f(\\frac{1}{e})=-\\frac{1}{e}$",
  "$f'(x)=\\ln x+1=0$, $x=\\frac{1}{e}$. $f(\\frac{1}{e})=-\\frac{1}{e}$"
)

add(158,
  "The function $f(x)=x^3+ax^2+bx+c$ has extrema at $x=-1$ and $x=2$. Then $a+b=$",
  "H\\u00e0m s\\u1ed1 $f(x)=x^3+ax^2+bx+c$ \\u0111\\u1ea1t c\\u1ef1c tr\\u1ecb t\\u1ea1i $x=-1$ v\\u00e0 $x=2$. Khi \\u0111\\u00f3 $a+b=$",
  json.dumps(["A. -3","B. -9","C. 3","D. -15"]),
  json.dumps(["A. -3","B. -9","C. 3","D. -15"]),
  "B", "B",
  "$f'(x)=3x^2+2ax+b$. $f'(-1)=3-2a+b=0$, $f'(2)=12+4a+b=0$. Solving: $a=-\\frac{3}{2},b=-6$. $a+b=-9$",
  "$f'(x)=3x^2+2ax+b$. $f'(-1)=3-2a+b=0$, $f'(2)=12+4a+b=0$. Gi\\u1ea3i: $a=-\\frac{3}{2},b=-6$. $a+b=-9$"
)

add(159,
  "If the line $y=2x+b$ is tangent to the curve $y=e^x$, then $b=$ ____",
  "N\\u1ebfu \\u0111\\u01b0\\u1eddng th\\u1eb3ng $y=2x+b$ l\\u00e0 ti\\u1ebfp tuy\\u1ebfn c\\u1ee7a \\u0111\\u01b0\\u1eddng cong $y=e^x$, th\\u00ec $b=$ ____",
  None, None,
  "2-2ln2", "2-2ln2",
  "Let point of tangency be $(x_0,e^{x_0})$. $f'(x_0)=e^{x_0}=2$, $x_0=\\ln2$. Point $(\\ln2,2)$. Substitute: $2=2\\ln2+b$, $b=2-2\\ln2$",
  "G\\u1ecdi ti\\u1ebfp \\u0111i\\u1ec3m l\\u00e0 $(x_0,e^{x_0})$. $f'(x_0)=e^{x_0}=2$, $x_0=\\ln2$. \\u0110i\\u1ec3m $(\\ln2,2)$. Thay v\\u00e0o: $2=2\\ln2+b$, $b=2-2\\ln2$"
)

add(160,
  "Let $U=\\{1,2,3,4,5,6\\}$ and $A=\\{1,3,5\\}$. Then $\\complement_U A=$",
  "Cho $U=\\{1,2,3,4,5,6\\}$ v\\u00e0 $A=\\{1,3,5\\}$. Khi \\u0111\\u00f3 $\\complement_U A=$",
  json.dumps(["A. \\{1,2,3\\}","B. \\{2,4,6\\}","C. \\{1,3,5\\}","D. \\{4,5,6\\}"]),
  json.dumps(["A. \\{1,2,3\\}","B. \\{2,4,6\\}","C. \\{1,3,5\\}","D. \\{4,5,6\\}"]),
  "B", "B",
  "$\\complement_U A=U-A=\\{2,4,6\\}$",
  "$\\complement_U A=U-A=\\{2,4,6\\}$"
)

add(161,
  "Given $A=\\{x \\mid -1<x<3\\}$, $B=\\{x \\mid x\\ge 1\\}$, then $A\\cup B=$ ____",
  "Cho $A=\\{x \\mid -1<x<3\\}$, $B=\\{x \\mid x\\ge 1\\}$, th\\u00ec $A\\cup B=$ ____",
  None, None,
  "(-1,+\\u221e)", "(-1,+\\u221e)",
  "$A\\cup B=\\{x\\mid x>-1\\}$",
  "$A\\cup B=\\{x\\mid x>-1\\}$"
)

add(162,
  'The statement "$x>2$" is a ____ condition for "$x>3$".',
  'M\\u1ec7nh \\u0111\\u1ec1 "$x>2$" l\\u00e0 \\u0111i\\u1ec1u ki\\u1ec7n ____ c\\u1ee7a "$x>3$".',
  json.dumps(["A. Sufficient but not necessary","B. Necessary but not sufficient","C. Necessary and sufficient","D. Neither sufficient nor necessary"]),
  json.dumps(["A. \\u0110\\u1ee7 nh\\u01b0ng kh\\u00f4ng c\\u1ea7n","B. C\\u1ea7n nh\\u01b0ng kh\\u00f4ng \\u0111\\u1ee7","C. C\\u1ea7n v\\u00e0 \\u0111\\u1ee7","D. Kh\\u00f4ng \\u0111\\u1ee7 v\\u00e0 kh\\u00f4ng c\\u1ea7n"]),
  "B", "B",
  "$x>3\\Rightarrow x>2$ but $x>2\\not\\Rightarrow x>3$",
  "$x>3\\Rightarrow x>2$ nh\\u01b0ng $x>2\\not\\Rightarrow x>3$"
)

add(163,
  "Given $A=\\{x \\mid x^2-2x-3\\le 0\\}$, $B=\\{x \\mid \\log_2 x\\le 1\\}$, then $A\\cap B=$",
  "Cho $A=\\{x \\mid x^2-2x-3\\le 0\\}$, $B=\\{x \\mid \\log_2 x\\le 1\\}$, th\\u00ec $A\\cap B=$",
  json.dumps(["A. (0,2]","B. [-1,2]","C. (0,3]","D. [-1,3]"]),
  json.dumps(["A. (0,2]","B. [-1,2]","C. (0,3]","D. [-1,3]"]),
  "A", "A",
  "$A=[-1,3]$, $B=(0,2]$. $A\\cap B=(0,2]$",
  "$A=[-1,3]$, $B=(0,2]$. $A\\cap B=(0,2]$"
)

add(164,
  "Given $A=\\{1,2,3,4\\}$, $B=\\{x \\mid x=n^2, n\\in A\\}$, then $A\\cap B=$ ____",
  "Cho $A=\\{1,2,3,4\\}$, $B=\\{x \\mid x=n^2, n\\in A\\}$, th\\u00ec $A\\cap B=$ ____",
  None, None,
  "{1,4}", "{1,4}",
  "$B=\\{1,4,9,16\\}$. $A\\cap B=\\{1,4\\}$",
  "$B=\\{1,4,9,16\\}$. $A\\cap B=\\{1,4\\}$"
)

add(165,
  "The complex conjugate of $z=2+i$ is",
  "S\\u1ed1 ph\\u1ee9c li\\u00ean h\\u1ee3p c\\u1ee7a $z=2+i$ l\\u00e0",
  json.dumps(["A. 2+i","B. 2-i","C. -2+i","D. -2-i"]),
  json.dumps(["A. 2+i","B. 2-i","C. -2+i","D. -2-i"]),
  "B", "B",
  "$\\bar{z}=2-i$",
  "$\\bar{z}=2-i$"
)

add(166,
  "If $z=\\frac{1}{1+i}$, then $|z|=$ ____",
  "N\\u1ebfu $z=\\frac{1}{1+i}$, th\\u00ec $|z|=$ ____",
  None, None,
  "\\u221a2/2", "\\u221a2/2",
  "$z=\\frac{1-i}{2}=\\frac{1}{2}-\\frac{i}{2}$. $|z|=\\sqrt{(\\frac{1}{2})^2+(-\\frac{1}{2})^2}=\\frac{\\sqrt{2}}{2}$",
  "$z=\\frac{1-i}{2}=\\frac{1}{2}-\\frac{i}{2}$. $|z|=\\sqrt{(\\frac{1}{2})^2+(-\\frac{1}{2})^2}=\\frac{\\sqrt{2}}{2}$"
)

add(167,
  "Given $\\vec{a}=(2,1)$, $\\vec{b}=(1,-1)$, the projection vector of $\\vec{a}$ onto $\\vec{b}$ is",
  "Cho $\\vec{a}=(2,1)$, $\\vec{b}=(1,-1)$, vect\\u01a1 h\\u00ecnh chi\\u1ebfu c\\u1ee7a $\\vec{a}$ l\\u00ean $\\vec{b}$ l\\u00e0",
  json.dumps(["A. (\\frac{1}{2},-\\frac{1}{2})","B. (-\\frac{1}{2},\\frac{1}{2})","C. (1,-1)","D. (-1,1)"]),
  json.dumps(["A. (\\frac{1}{2},-\\frac{1}{2})","B. (-\\frac{1}{2},\\frac{1}{2})","C. (1,-1)","D. (-1,1)"]),
  "A", "A",
  "$\\vec{a}\\cdot\\vec{b}=1$, $|\\vec{b}|^2=2$. Projection $=\\frac{1}{2}\\vec{b}=(\\frac{1}{2},-\\frac{1}{2})$",
  "$\\vec{a}\\cdot\\vec{b}=1$, $|\\vec{b}|^2=2$. H\\u00ecnh chi\\u1ebfu $=\\frac{1}{2}\\vec{b}=(\\frac{1}{2},-\\frac{1}{2})$"
)

add(168,
  "$(1+i)^2=$ ____",
  "$(1+i)^2=$ ____",
  None, None,
  "2i", "2i",
  "$(1+i)^2=1+2i+i^2=2i$",
  "$(1+i)^2=1+2i+i^2=2i$"
)

add(169,
  "Given $\\vec{a}=(1,2)$, $\\vec{b}=(3,1)$, the angle $\\theta$ between $\\vec{a}$ and $\\vec{b}$ satisfies",
  "Cho $\\vec{a}=(1,2)$, $\\vec{b}=(3,1)$, g\\u00f3c $\\theta$ gi\\u1eefa $\\vec{a}$ v\\u00e0 $\\vec{b}$ th\\u1ecfa m\\u00e3n",
  json.dumps(["A. \\cos\\theta=\\frac{5}{\\sqrt{50}}","B. \\cos\\theta=\\frac{5}{\\sqrt{65}}","C. \\cos\\theta=\\frac{7}{\\sqrt{50}}","D. \\cos\\theta=\\frac{7}{\\sqrt{65}}"]),
  json.dumps(["A. \\cos\\theta=\\frac{5}{\\sqrt{50}}","B. \\cos\\theta=\\frac{5}{\\sqrt{65}}","C. \\cos\\theta=\\frac{7}{\\sqrt{50}}","D. \\cos\\theta=\\frac{7}{\\sqrt{65}}"]),
  "A", "A",
  "$\\vec{a}\\cdot\\vec{b}=1\\times3+2\\times1=5$, $|\\vec{a}|=\\sqrt{5}$, $|\\vec{b}|=\\sqrt{10}$. $\\cos\\theta=\\frac{5}{\\sqrt{50}}$",
  "$\\vec{a}\\cdot\\vec{b}=1\\times3+2\\times1=5$, $|\\vec{a}|=\\sqrt{5}$, $|\\vec{b}|=\\sqrt{10}$. $\\cos\\theta=\\frac{5}{\\sqrt{50}}$"
)

add(170,
  "If $z$ satisfies $z(1+i)=2i$, then the imaginary part of $z$ is ____",
  "N\\u1ebfu $z$ th\\u1ecfa m\\u00e3n $z(1+i)=2i$, th\\u00ec ph\\u1ea7n \\u1ea3o c\\u1ee7a $z$ l\\u00e0 ____",
  None, None,
  "1", "1",
  "$z=\\frac{2i}{1+i}=\\frac{2i(1-i)}{2}=i(1-i)=1+i$, imaginary part is 1",
  "$z=\\frac{2i}{1+i}=\\frac{2i(1-i)}{2}=i(1-i)=1+i$, ph\\u1ea7n \\u1ea3o l\\u00e0 1"
)

add(171,
  "Given $\\vec{a}=(x,3)$, $\\vec{b}=(2,-1)$, and $\\vec{a}\\perp\\vec{b}$, then $x=$",
  "Cho $\\vec{a}=(x,3)$, $\\vec{b}=(2,-1)$, v\\u00e0 $\\vec{a}\\perp\\vec{b}$, th\\u00ec $x=$",
  json.dumps(["A. -\\frac{3}{2}","B. \\frac{3}{2}","C. 6","D. -6"]),
  json.dumps(["A. -\\frac{3}{2}","B. \\frac{3}{2}","C. 6","D. -6"]),
  "B", "B",
  "$\\vec{a}\\cdot\\vec{b}=2x-3=0$, $x=\\frac{3}{2}$",
  "$\\vec{a}\\cdot\\vec{b}=2x-3=0$, $x=\\frac{3}{2}$"
)

add(172,
  "If $z$ satisfies $|z-i|=1$, then the maximum value of $|z|$ is ____",
  "N\\u1ebfu $z$ th\\u1ecfa m\\u00e3n $|z-i|=1$, th\\u00ec gi\\u00e1 tr\\u1ecb l\\u1edbn nh\\u1ea5t c\\u1ee7a $|z|$ l\\u00e0 ____",
  None, None,
  "2", "2",
  "$z$ lies on a circle centered at $(0,1)$ with radius 1 in the complex plane. The maximum of $|z|$ is $1+1=2$",
  "$z$ n\\u1eb1m tr\\u00ean \\u0111\\u01b0\\u1eddng tr\\u00f2n t\\u00e2m $(0,1)$ b\\u00e1n k\\u00ednh 1 trong m\\u1eb7t ph\\u1eb3ng ph\\u1ee9c. Gi\\u00e1 tr\\u1ecb l\\u1edbn nh\\u1ea5t c\\u1ee7a $|z|$ l\\u00e0 $1+1=2$"
)

# === END TRANSLATIONS ===
print(f"Prepared {len(data)} translations for DB update")

# Step 2: Update the database
DB = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

updated = 0
errors = 0
for item in data:
    try:
        cur.execute("""
            UPDATE questions SET
                content_en = ?, content_vi = ?,
                options_en = ?, options_vi = ?,
                answer_en = ?, answer_vi = ?,
                solution_en = ?, solution_vi = ?
            WHERE id = ?
        """, (item["content_en"], item["content_vi"],
              item["options_en"], item["options_vi"],
              item["answer_en"], item["answer_vi"],
              item["solution_en"], item["solution_vi"],
              item["id"]))
        if cur.rowcount > 0:
            updated += 1
            print(f"  Updated ID {item['id']}")
        else:
            print(f"  WARNING: ID {item['id']} not found")
    except Exception as e:
        print(f"  ERROR ID {item['id']}: {e}")
        errors += 1

conn.commit()
conn.close()
print(f"\nDone! Updated: {updated}, Errors: {errors}")
print(f"All {len(data)} questions processed.")
