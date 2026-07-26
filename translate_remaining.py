# -*- coding: utf-8 -*-
"""Translate remaining Chinese math questions to English and Vietnamese."""

import sqlite3
import json

DB_PATH = 'd:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

# Each entry: (id, content_en, options_en, answer_en, solution_en,
#                    content_vi, options_vi, answer_vi, solution_vi)
# For None options, use None for both options_en and options_vi.
# For options stored as JSON arrays, pass a Python list; json.dumps handles escaping.

translations = [
    # --- ID=131 ---
    (131,
     r"Two fair coins are tossed simultaneously. The probability that exactly one lands heads up is ____",
     None,
     r"1/2",
     r"Sample space: {HH, HT, TH, TT}. Exactly one head: {HT, TH}. $P=\frac{2}{4}=\frac{1}{2}$",
     r"Tung đồng thời hai đồng xu cân đối. Xác suất để có đúng một mặt ngửa là ____",
     None,
     r"1/2",
     r"Không gian mẫu: {NN, NS, SN, SS}. Đúng một mặt ngửa: {NS, SN}. $P=\frac{2}{4}=\frac{1}{2}$"),

    # --- ID=132 ---
    (132,
     r"Given spatial vectors $\vec{a}=(1,0,-1)$, $\vec{b}=(-1,1,0)$, then $\vec{a}\cdot\vec{b}=$",
     ["A. -1", "B. 0", "C. 1", "D. 2"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1\times(-1)+0\times1+(-1)\times0=-1$",
     r"Cho vectơ không gian $\vec{a}=(1,0,-1)$, $\vec{b}=(-1,1,0)$, thì $\vec{a}\cdot\vec{b}=$",
     ["A. -1", "B. 0", "C. 1", "D. 2"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1\times(-1)+0\times1+(-1)\times0=-1$"),

    # --- ID=133 ---
    (133,
     r"Given plane $\alpha$ passes through points $A(1,0,0), B(0,1,0), C(0,0,1)$, then a normal vector of plane $\alpha$ is ____",
     None,
     r"(1,1,1)",
     r"$\vec{AB}=(-1,1,0)$, $\vec{AC}=(-1,0,1)$. $\vec{n}=\vec{AB}\times\vec{AC}=(1,1,1)$",
     r"Cho mặt phẳng $\alpha$ đi qua các điểm $A(1,0,0), B(0,1,0), C(0,0,1)$, thì một vectơ pháp tuyến của mặt phẳng $\alpha$ là ____",
     None,
     r"(1,1,1)",
     r"$\vec{AB}=(-1,1,0)$, $\vec{AC}=(-1,0,1)$. $\vec{n}=\vec{AB}\times\vec{AC}=(1,1,1)$"),

    # --- ID=134 ---
    (134,
     r"In a unit cube $ABCD-A_1B_1C_1D_1$, the cosine of the angle between skew lines $AB_1$ and $BC_1$ is",
     ["A. \\frac{1}{2}", "B. \\frac{\\sqrt{2}}{2}", "C. \\frac{\\sqrt{3}}{3}", "D. \\frac{1}{3}"],
     r"A",
     r"Set up coordinates with D as origin: $A(1,0,0), B_1(1,1,1), B(1,1,0), C_1(0,1,1)$. $\vec{AB_1}=(0,1,1), \vec{BC_1}=(-1,0,1)$. $\cos\theta=\frac{1}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$",
     r"Cho hình lập phương $ABCD-A_1B_1C_1D_1$ có cạnh bằng 1, cosin góc giữa hai đường thẳng chéo nhau $AB_1$ và $BC_1$ là",
     ["A. \\frac{1}{2}", "B. \\frac{\\sqrt{2}}{2}", "C. \\frac{\\sqrt{3}}{3}", "D. \\frac{1}{3}"],
     r"A",
     r"Lấy D làm gốc tọa độ: $A(1,0,0), B_1(1,1,1), B(1,1,0), C_1(0,1,1)$. $\vec{AB_1}=(0,1,1), \vec{BC_1}=(-1,0,1)$. $\cos\theta=\frac{1}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$"),

    # --- ID=135 ---
    (135,
     r"The distance from point $P(1,2,3)$ to the $xOy$ plane is ____",
     None,
     r"3",
     r"The distance to the $xOy$ plane is $|z|=3$",
     r"Khoảng cách từ điểm $P(1,2,3)$ đến mặt phẳng $xOy$ là ____",
     None,
     r"3",
     r"Khoảng cách đến mặt phẳng $xOy$ là $|z|=3$"),

    # --- ID=136 ---
    (136,
     r"Given the two half-plane normal vectors of a dihedral angle $\alpha-l-\beta$ are $\vec{n_1}=(1,0,1)$ and $\vec{n_2}=(0,1,1)$, then the dihedral angle is",
     ["A. 30\\degree", "B. 45\\degree", "C. 60\\degree", "D. 120\\degree"],
     r"C",
     r"$\cos\theta=\frac{|\vec{n_1}\cdot\vec{n_2}|}{|\vec{n_1}||\vec{n_2}|}=\frac{1}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$, $\theta=60\degree$",
     r"Cho các vectơ pháp tuyến của hai nửa mặt phẳng của góc nhị diện $\alpha-l-\beta$ lần lượt là $\vec{n_1}=(1,0,1)$, $\vec{n_2}=(0,1,1)$, thì góc nhị diện đó bằng",
     ["A. 30\\degree", "B. 45\\degree", "C. 60\\degree", "D. 120\\degree"],
     r"C",
     r"$\cos\theta=\frac{|\vec{n_1}\cdot\vec{n_2}|}{|\vec{n_1}||\vec{n_2}|}=\frac{1}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$, $\theta=60\degree$"),

    # --- ID=137 ---
    (137,
     r"In a regular quadrangular pyramid $S-ABCD$, the base side length is 2, the lateral edge length is $\sqrt{6}$, then the height $SO$ is ____",
     None,
     r"2",
     r"Half the diagonal of the base square $=\sqrt{2}$. $SO=\sqrt{SA^2-AO^2}=\sqrt{6-2}=2$",
     r"Cho hình chóp tứ giác đều $S-ABCD$, cạnh đáy bằng 2, cạnh bên bằng $\sqrt{6}$, thì chiều cao $SO$ bằng ____",
     None,
     r"2",
     r"Nửa đường chéo đáy hình vuông $=\sqrt{2}$. $SO=\sqrt{SA^2-AO^2}=\sqrt{6-2}=2$"),

    # --- ID=138 ---
    (138,
     r"Given three points in space $A(1,2,3), B(2,4,1), C(3,1,5)$, the area of $\triangle ABC$ is",
     ["A. \\frac{\\sqrt{230}}{2}", "B. \\frac{\\sqrt{210}}{2}", "C. 5\\sqrt{2}", "D. \\sqrt{115}"],
     r"B",
     r"$\vec{AB}=(1,2,-2), \vec{AC}=(2,-1,2)$. $|\vec{AB}\times\vec{AC}|=\sqrt{210}$. $S=\frac{1}{2}\times\sqrt{210}$",
     r"Cho ba điểm trong không gian $A(1,2,3), B(2,4,1), C(3,1,5)$, diện tích $\triangle ABC$ là",
     ["A. \\frac{\\sqrt{230}}{2}", "B. \\frac{\\sqrt{210}}{2}", "C. 5\\sqrt{2}", "D. \\sqrt{115}"],
     r"B",
     r"$\vec{AB}=(1,2,-2), \vec{AC}=(2,-1,2)$. $|\vec{AB}\times\vec{AC}|=\sqrt{210}$. $S=\frac{1}{2}\times\sqrt{210}$"),

    # --- ID=139 ---
    (139,
     r"Given $\vec{a}=(2,-1,3)$, $\vec{b}=(-4,2,x)$, and $\vec{a}\parallel\vec{b}$, then $x=$ ____",
     None,
     r"-6",
     r"From $\vec{a}\parallel\vec{b}$ we get $\frac{2}{-4}=\frac{-1}{2}=\frac{3}{x}$, $x=-6$",
     r"Cho $\vec{a}=(2,-1,3)$, $\vec{b}=(-4,2,x)$ và $\vec{a}\parallel\vec{b}$, thì $x=$ ____",
     None,
     r"-6",
     r"Từ $\vec{a}\parallel\vec{b}$ suy ra $\frac{2}{-4}=\frac{-1}{2}=\frac{3}{x}$, $x=-6$"),

    # --- ID=140 ---
    (140,
     r"The focal length of ellipse $\frac{x^2}{16}+\frac{y^2}{9}=1$ is",
     ["A. 2\\sqrt{7}", "B. \\sqrt{7}", "C. 5", "D. 7"],
     r"A",
     r"$a^2=16, b^2=9$, $c^2=7$, $2c=2\sqrt{7}$",
     r"Tiêu cự của elip $\frac{x^2}{16}+\frac{y^2}{9}=1$ là",
     ["A. 2\\sqrt{7}", "B. \\sqrt{7}", "C. 5", "D. 7"],
     r"A",
     r"$a^2=16, b^2=9$, $c^2=7$, $2c=2\sqrt{7}$"),

    # --- ID=141 ---
    (141,
     r"The directrix of the parabola $y^2=8x$ is ____",
     None,
     r"x=-2",
     r"$2p=8$, $p=4$, directrix $x=-\frac{p}{2}=-2$",
     r"Đường chuẩn của parabol $y^2=8x$ là ____",
     None,
     r"x=-2",
     r"$2p=8$, $p=4$, đường chuẩn $x=-\frac{p}{2}=-2$"),

    # --- ID=142 ---
    (142,
     r"The asymptotes of the hyperbola $\frac{x^2}{9}-\frac{y^2}{16}=1$ are",
     ["A. y=\\pm\\frac{3}{4}x", "B. y=\\pm\\frac{4}{3}x", "C. y=\\pm\\frac{9}{16}x", "D. y=\\pm\\frac{16}{9}x"],
     r"B",
     r"$a=3, b=4$, asymptotes $y=\pm\frac{b}{a}x=\pm\frac{4}{3}x$",
     r"Tiệm cận của hypebol $\frac{x^2}{9}-\frac{y^2}{16}=1$ là",
     ["A. y=\\pm\\frac{3}{4}x", "B. y=\\pm\\frac{4}{3}x", "C. y=\\pm\\frac{9}{16}x", "D. y=\\pm\\frac{16}{9}x"],
     r"B",
     r"$a=3, b=4$, tiệm cận $y=\pm\frac{b}{a}x=\pm\frac{4}{3}x$"),

    # --- ID=143 ---
    (143,
     r"A point P on the ellipse $\frac{x^2}{25}+\frac{y^2}{16}=1$ is 6 units from the left focus. The distance from P to the right focus is ____",
     None,
     r"4",
     r"$|PF_1|+|PF_2|=2a=10$, $|PF_2|=4$",
     r"Điểm P trên elip $\frac{x^2}{25}+\frac{y^2}{16}=1$ cách tiêu điểm trái một khoảng bằng 6. Khoảng cách từ P đến tiêu điểm phải là ____",
     None,
     r"4",
     r"$|PF_1|+|PF_2|=2a=10$, $|PF_2|=4$"),

    # --- ID=144 ---
    (144,
     r"Given an ellipse centered at the origin with foci on the $x$-axis, major axis length 10, minor axis length 6, its equation is",
     ["A. \\frac{x^2}{25}+\\frac{y^2}{9}=1", "B. \\frac{x^2}{9}+\\frac{y^2}{25}=1", "C. \\frac{x^2}{100}+\\frac{y^2}{36}=1", "D. \\frac{x^2}{5}+\\frac{y^2}{3}=1"],
     r"A",
     r"$a=5, b=3$, equation is $\frac{x^2}{25}+\frac{y^2}{9}=1$",
     r"Cho elip có tâm tại gốc tọa độ, tiêu điểm trên trục $x$, độ dài trục lớn 10, độ dài trục bé 6, phương trình elip là",
     ["A. \\frac{x^2}{25}+\\frac{y^2}{9}=1", "B. \\frac{x^2}{9}+\\frac{y^2}{25}=1", "C. \\frac{x^2}{100}+\\frac{y^2}{36}=1", "D. \\frac{x^2}{5}+\\frac{y^2}{3}=1"],
     r"A",
     r"$a=5, b=3$, phương trình là $\frac{x^2}{25}+\frac{y^2}{9}=1$"),

    # --- ID=145 ---
    (145,
     r"The focus of the parabola $y=ax^2$ is at $(0,\frac{1}{4})$, then $a=$ ____",
     None,
     r"1",
     r"Standard form $x^2=\frac{1}{a}y$, $2p=\frac{1}{a}$, focus $(0,\frac{p}{2})=(0,\frac{1}{4a})=(0,\frac{1}{4})$, $a=1$",
     r"Tiêu điểm của parabol $y=ax^2$ là $(0,\frac{1}{4})$, thì $a=$ ____",
     None,
     r"1",
     r"Dạng chuẩn $x^2=\frac{1}{a}y$, $2p=\frac{1}{a}$, tiêu điểm $(0,\frac{p}{2})=(0,\frac{1}{4a})=(0,\frac{1}{4})$, $a=1$"),

    # --- ID=146 ---
    (146,
     r"The eccentricity of the hyperbola $x^2-\frac{y^2}{3}=1$ is",
     ["A. 1", "B. 2", "C. \\sqrt{2}", "D. \\sqrt{3}"],
     r"B",
     r"$a^2=1, b^2=3$, $c^2=4$, $e=\frac{c}{a}=2$",
     r"Tâm sai của hypebol $x^2-\frac{y^2}{3}=1$ là",
     ["A. 1", "B. 2", "C. \\sqrt{2}", "D. \\sqrt{3}"],
     r"B",
     r"$a^2=1, b^2=3$, $c^2=4$, $e=\frac{c}{a}=2$"),

    # --- ID=147 ---
    (147,
     r"Given ellipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1(a>b>0)$ has a focus at $(4,0)$ and $a=5$, then $b=$ ____",
     None,
     r"3",
     r"$c=4$, $b^2=a^2-c^2=25-16=9$, $b=3$",
     r"Cho elip $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1(a>b>0)$ có một tiêu điểm là $(4,0)$ và $a=5$, thì $b=$ ____",
     None,
     r"3",
     r"$c=4$, $b^2=a^2-c^2=25-16=9$, $b=3$"),

    # --- ID=148 ---
    (148,
     r"Point P is on the parabola $y^2=4x$. The distance from P to the focus is 5. The x-coordinate of P is",
     ["A. 3", "B. 4", "C. 5", "D. 6"],
     r"B",
     r"Focus $F(1,0)$. By definition $|PF|=x_P+1=5$, $x_P=4$",
     r"Điểm P nằm trên parabol $y^2=4x$. Khoảng cách từ P đến tiêu điểm là 5. Hoành độ của P là",
     ["A. 3", "B. 4", "C. 5", "D. 6"],
     r"B",
     r"Tiêu điểm $F(1,0)$. Theo định nghĩa $|PF|=x_P+1=5$, $x_P=4$"),

    # --- ID=149 ---
    (149,
     r"Given ellipse $\frac{x^2}{4}+\frac{y^2}{3}=1$ with left and right foci $F_1, F_2$. Let $P$ be a point on the ellipse such that $\angle F_1PF_2=60\degree$. The area of $\triangle F_1PF_2$ is ____",
     None,
     r"√3",
     r"$a=2, c=1$. Using the focal triangle area formula $S=b^2\tan\frac{\theta}{2}=3\times\tan30\degree=\sqrt{3}$",
     r"Cho elip $\frac{x^2}{4}+\frac{y^2}{3}=1$ có các tiêu điểm $F_1,F_2$. $P$ là điểm trên elip sao cho $\angle F_1PF_2=60\degree$. Diện tích $\triangle F_1PF_2$ là ____",
     None,
     r"√3",
     r"$a=2, c=1$. Dùng công thức diện tích tam giác tiêu điểm $S=b^2\tan\frac{\theta}{2}=3\times\tan30\degree=\sqrt{3}$"),

    # --- ID=150 ---
    (150,
     r"The derivative of $f(x)=x^2$ at $x=1$ is",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=2x$, $f'(1)=2$",
     r"Đạo hàm của hàm số $f(x)=x^2$ tại $x=1$ là",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=2x$, $f'(1)=2$"),

    # --- ID=151 ---
    (151,
     r"The tangent line to the curve $y=x^3$ at point $(1,1)$ is ____",
     None,
     r"y=3x-2",
     r"$y'=3x^2$, $k=3$. Tangent: $y-1=3(x-1)$, $y=3x-2$",
     r"Tiếp tuyến của đường cong $y=x^3$ tại điểm $(1,1)$ là ____",
     None,
     r"y=3x-2",
     r"$y'=3x^2$, $k=3$. Tiếp tuyến: $y-1=3(x-1)$, $y=3x-2$"),

    # --- ID=152 ---
    (152,
     r"The interval where $f(x)=x^3-3x$ is decreasing is",
     ["A. (-\\infty,-1)", "B. (-1,1)", "C. (1,+\\infty)", "D. (-\\infty,-1)\\cup(1,+\\infty)"],
     r"B",
     r"$f'(x)=3x^2-3=3(x+1)(x-1)$. $f'(x)<0$ on $(-1,1)$",
     r"Khoảng nghịch biến của hàm số $f(x)=x^3-3x$ là",
     ["A. (-\\infty,-1)", "B. (-1,1)", "C. (1,+\\infty)", "D. (-\\infty,-1)\\cup(1,+\\infty)"],
     r"B",
     r"$f'(x)=3x^2-3=3(x+1)(x-1)$. $f'(x)<0$ trên $(-1,1)$"),

    # --- ID=153 ---
    (153,
     r"The minimum value of $f(x)=x^3-3x^2+1$ on $[-1,3]$ is ____",
     None,
     r"-3",
     r"$f'(x)=3x^2-6x=3x(x-2)$. Critical points $x=0,2$. $f(-1)=-3, f(0)=1, f(2)=-3, f(3)=1$. Minimum $-3$",
     r"Giá trị nhỏ nhất của hàm số $f(x)=x^3-3x^2+1$ trên $[-1,3]$ là ____",
     None,
     r"-3",
     r"$f'(x)=3x^2-6x=3x(x-2)$. Điểm tới hạn $x=0,2$. $f(-1)=-3, f(0)=1, f(2)=-3, f(3)=1$. Giá trị nhỏ nhất $-3$"),

    # --- ID=154 ---
    (154,
     r"Given the slope of the tangent line to $f(x)=\ln x+ax$ at $x=1$ is 3, then $a=$",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=\frac{1}{x}+a$, $f'(1)=1+a=3$, $a=2$",
     r"Cho hệ số góc của tiếp tuyến với $f(x)=\ln x+ax$ tại $x=1$ bằng 3, thì $a=$",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=\frac{1}{x}+a$, $f'(1)=1+a=3$, $a=2$"),

    # --- ID=155 ---
    (155,
     r"The interval where $f(x)=e^x-x$ is increasing is ____",
     None,
     r"(0,+∞)",
     r"$f'(x)=e^x-1$. $f'(x)>0$ when $x>0$",
     r"Khoảng đồng biến của hàm số $f(x)=e^x-x$ là ____",
     None,
     r"(0,+∞)",
     r"$f'(x)=e^x-1$. $f'(x)>0$ khi $x>0$"),

    # --- ID=156 ---
    (156,
     r"The minimum value of $f(x)=x+\frac{1}{x}(x>0)$ is",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=1-\frac{1}{x^2}=0$, $x=1$. $f(1)=2$. Or by AM-GM inequality $x+\frac{1}{x}\ge2$",
     r"Giá trị nhỏ nhất của hàm số $f(x)=x+\frac{1}{x}(x>0)$ là",
     ["A. 1", "B. 2", "C. 3", "D. 4"],
     r"B",
     r"$f'(x)=1-\frac{1}{x^2}=0$, $x=1$. $f(1)=2$. Hoặc theo bất đẳng thức AM-GM $x+\frac{1}{x}\ge2$"),

    # --- ID=157 ---
    (157,
     r"The minimum value of $f(x)=x\ln x$ is ____",
     None,
     r"-1/e",
     r"$f'(x)=\ln x+1=0$, $x=\frac{1}{e}$. $f(\frac{1}{e})=-\frac{1}{e}$",
     r"Giá trị nhỏ nhất của hàm số $f(x)=x\ln x$ là ____",
     None,
     r"-1/e",
     r"$f'(x)=\ln x+1=0$, $x=\frac{1}{e}$. $f(\frac{1}{e})=-\frac{1}{e}$"),

    # --- ID=158 ---
    (158,
     r"Given $f(x)=x^3+ax^2+bx+c$ has an extremum at $x=-1$ and also at $x=2$, then $a+b=$",
     ["A. -3", "B. -9", "C. 3", "D. -15"],
     r"B",
     r"$f'(x)=3x^2+2ax+b$. $f'(-1)=3-2a+b=0$, $f'(2)=12+4a+b=0$. Solving: $a=-\frac{3}{2}, b=-6$. $a+b=-9$",
     r"Cho $f(x)=x^3+ax^2+bx+c$ đạt cực trị tại $x=-1$ và tại $x=2$, thì $a+b=$",
     ["A. -3", "B. -9", "C. 3", "D. -15"],
     r"B",
     r"$f'(x)=3x^2+2ax+b$. $f'(-1)=3-2a+b=0$, $f'(2)=12+4a+b=0$. Giải: $a=-\frac{3}{2}, b=-6$. $a+b=-9$"),

    # --- ID=159 ---
    (159,
     r"If the line $y=2x+b$ is a tangent to the curve $y=e^x$, then $b=$ ____",
     None,
     r"2-2ln2",
     r"Let the tangent point be $(x_0, e^{x_0})$. $f'(x_0)=e^{x_0}=2$, $x_0=\ln2$. Tangent point $(\ln2,2)$. Substituting: $2=2\ln2+b$, $b=2-2\ln2$",
     r"Nếu đường thẳng $y=2x+b$ là tiếp tuyến của đường cong $y=e^x$, thì $b=$ ____",
     None,
     r"2-2ln2",
     r"Gọi tiếp điểm là $(x_0, e^{x_0})$. $f'(x_0)=e^{x_0}=2$, $x_0=\ln2$. Tiếp điểm $(\ln2,2)$. Thay vào: $2=2\ln2+b$, $b=2-2\ln2$"),

    # --- ID=160 ---
    (160,
     r"Let the universal set $U=\{1,2,3,4,5,6\}$ and set $A=\{1,3,5\}$. Then $\complement_U A=$",
     ["A. \\{1,2,3\\}", "B. \\{2,4,6\\}", "C. \\{1,3,5\\}", "D. \\{4,5,6\\}"],
     r"B",
     r"$\complement_U A = U - A = \{2,4,6\}$",
     r"Cho tập hợp vũ trụ $U=\{1,2,3,4,5,6\}$ và tập hợp $A=\{1,3,5\}$. Thì $\complement_U A=$",
     ["A. \\{1,2,3\\}", "B. \\{2,4,6\\}", "C. \\{1,3,5\\}", "D. \\{4,5,6\\}"],
     r"B",
     r"$\complement_U A = U - A = \{2,4,6\}$"),

    # --- ID=161 ---
    (161,
     r"Given sets $A=\{x \mid -1<x<3\}$, $B=\{x \mid x\ge 1\}$, then $A\cup B=$ ____",
     None,
     r"(-1,+∞)",
     r"$A\cup B=\{x\mid x>-1\}$",
     r"Cho tập hợp $A=\{x \mid -1<x<3\}$, $B=\{x \mid x\ge 1\}$, thì $A\cup B=$ ____",
     None,
     r"(-1,+∞)",
     r"$A\cup B=\{x\mid x>-1\}$"),

    # --- ID=162 ---
    (162,
     r'"$x>2$" is a _____ condition for "$x>3$"',
     ["A. Sufficient but not necessary", "B. Necessary but not sufficient", "C. Necessary and sufficient", "D. Neither necessary nor sufficient"],
     r"B",
     r"$x>3\Rightarrow x>2$ but $x>2\not\Rightarrow x>3$",
     r'"$x>2$" là điều kiện _____ cho "$x>3$"',
     ["A. Đủ nhưng không cần", "B. Cần nhưng không đủ", "C. Cần và đủ", "D. Không cần và không đủ"],
     r"B",
     r"$x>3\Rightarrow x>2$ nhưng $x>2\not\Rightarrow x>3$"),

    # --- ID=163 ---
    (163,
     r"Given sets $A=\{x \mid x^2-2x-3\le 0\}$, $B=\{x \mid \log_2 x\le 1\}$, then $A\cap B=$",
     ["A. (0,2]", "B. [-1,2]", "C. (0,3]", "D. [-1,3]"],
     r"A",
     r"$A=[-1,3]$, $B=(0,2]$. $A\cap B=(0,2]$",
     r"Cho tập hợp $A=\{x \mid x^2-2x-3\le 0\}$, $B=\{x \mid \log_2 x\le 1\}$, thì $A\cap B=$",
     ["A. (0,2]", "B. [-1,2]", "C. (0,3]", "D. [-1,3]"],
     r"A",
     r"$A=[-1,3]$, $B=(0,2]$. $A\cap B=(0,2]$"),

    # --- ID=164 ---
    (164,
     r"Given sets $A=\{1,2,3,4\}$, $B=\{x \mid x=n^2, n\in A\}$, then $A\cap B=$ ____",
     None,
     r"{1,4}",
     r"$B=\{1,4,9,16\}$. $A\cap B=\{1,4\}$",
     r"Cho tập hợp $A=\{1,2,3,4\}$, $B=\{x \mid x=n^2, n\in A\}$, thì $A\cap B=$ ____",
     None,
     r"{1,4}",
     r"$B=\{1,4,9,16\}$. $A\cap B=\{1,4\}$"),

    # --- ID=165 ---
    (165,
     r"The complex conjugate of $z=2+i$ is",
     ["A. 2+i", "B. 2-i", "C. -2+i", "D. -2-i"],
     r"B",
     r"$\bar{z}=2-i$",
     r"Số phức liên hợp của $z=2+i$ là",
     ["A. 2+i", "B. 2-i", "C. -2+i", "D. -2-i"],
     r"B",
     r"$\bar{z}=2-i$"),

    # --- ID=166 ---
    (166,
     r"If $z=\frac{1}{1+i}$, then $|z|=$ ____",
     None,
     r"√2/2",
     r"$z=\frac{1-i}{2}=\frac{1}{2}-\frac{i}{2}$. $|z|=\sqrt{(\frac{1}{2})^2+(-\frac{1}{2})^2}=\frac{\sqrt{2}}{2}$",
     r"Nếu $z=\frac{1}{1+i}$, thì $|z|=$ ____",
     None,
     r"√2/2",
     r"$z=\frac{1-i}{2}=\frac{1}{2}-\frac{i}{2}$. $|z|=\sqrt{(\frac{1}{2})^2+(-\frac{1}{2})^2}=\frac{\sqrt{2}}{2}$"),

    # --- ID=167 ---
    (167,
     r"Given $\vec{a}=(2,1)$, $\vec{b}=(1,-1)$, the projection vector of $\vec{a}$ onto $\vec{b}$ is",
     ["A. (\\frac{1}{2},-\\frac{1}{2})", "B. (-\\frac{1}{2},\\frac{1}{2})", "C. (1,-1)", "D. (-1,1)"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1$, $|\vec{b}|^2=2$. Projection $=\frac{1}{2}\vec{b}=(\frac{1}{2},-\frac{1}{2})$",
     r"Cho $\vec{a}=(2,1)$, $\vec{b}=(1,-1)$, vectơ hình chiếu của $\vec{a}$ lên $\vec{b}$ là",
     ["A. (\\frac{1}{2},-\\frac{1}{2})", "B. (-\\frac{1}{2},\\frac{1}{2})", "C. (1,-1)", "D. (-1,1)"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1$, $|\vec{b}|^2=2$. Hình chiếu $=\frac{1}{2}\vec{b}=(\frac{1}{2},-\frac{1}{2})$"),

    # --- ID=168 ---
    (168,
     r"$(1+i)^2=$ ____",
     None,
     r"2i",
     r"$(1+i)^2=1+2i+i^2=2i$",
     r"$(1+i)^2=$ ____",
     None,
     r"2i",
     r"$(1+i)^2=1+2i+i^2=2i$"),

    # --- ID=169 ---
    (169,
     r"Given $\vec{a}=(1,2)$, $\vec{b}=(3,1)$, the angle $\theta$ between $\vec{a}$ and $\vec{b}$ satisfies",
     ["A. \\cos\\theta=\\frac{5}{\\sqrt{50}}", "B. \\cos\\theta=\\frac{5}{\\sqrt{65}}", "C. \\cos\\theta=\\frac{7}{\\sqrt{50}}", "D. \\cos\\theta=\\frac{7}{\\sqrt{65}}"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1\times3+2\times1=5$, $|\vec{a}|=\sqrt{5}$, $|\vec{b}|=\sqrt{10}$. $\cos\theta=\frac{5}{\sqrt{50}}$",
     r"Cho $\vec{a}=(1,2)$, $\vec{b}=(3,1)$, góc $\theta$ giữa $\vec{a}$ và $\vec{b}$ thỏa mãn",
     ["A. \\cos\\theta=\\frac{5}{\\sqrt{50}}", "B. \\cos\\theta=\\frac{5}{\\sqrt{65}}", "C. \\cos\\theta=\\frac{7}{\\sqrt{50}}", "D. \\cos\\theta=\\frac{7}{\\sqrt{65}}"],
     r"A",
     r"$\vec{a}\cdot\vec{b}=1\times3+2\times1=5$, $|\vec{a}|=\sqrt{5}$, $|\vec{b}|=\sqrt{10}$. $\cos\theta=\frac{5}{\sqrt{50}}$"),

    # --- ID=170 ---
    (170,
     r"Given that complex number $z$ satisfies $z(1+i)=2i$, the imaginary part of $z$ is ____",
     None,
     r"1",
     r"$z=\frac{2i}{1+i}=\frac{2i(1-i)}{2}=i(1-i)=1+i$, the imaginary part is 1",
     r"Cho số phức $z$ thỏa mãn $z(1+i)=2i$, phần ảo của $z$ là ____",
     None,
     r"1",
     r"$z=\frac{2i}{1+i}=\frac{2i(1-i)}{2}=i(1-i)=1+i$, phần ảo là 1"),

    # --- ID=171 ---
    (171,
     r"Given $\vec{a}=(x,3)$, $\vec{b}=(2,-1)$, and $\vec{a}\perp\vec{b}$, then $x=$",
     ["A. -\\frac{3}{2}", "B. \\frac{3}{2}", "C. 6", "D. -6"],
     r"B",
     r"$\vec{a}\cdot\vec{b}=2x-3=0$, $x=\frac{3}{2}$",
     r"Cho $\vec{a}=(x,3)$, $\vec{b}=(2,-1)$ và $\vec{a}\perp\vec{b}$, thì $x=$",
     ["A. -\\frac{3}{2}", "B. \\frac{3}{2}", "C. 6", "D. -6"],
     r"B",
     r"$\vec{a}\cdot\vec{b}=2x-3=0$, $x=\frac{3}{2}$"),

    # --- ID=172 ---
    (172,
     r"Let complex number $z$ satisfy $|z-i|=1$, then the maximum value of $|z|$ is ____",
     None,
     r"2",
     r"$z$ is on the complex plane as a circle with center $(0,1)$ and radius 1. The maximum of $|z|$ is $1+1=2$",
     r"Cho số phức $z$ thỏa mãn $|z-i|=1$, thì giá trị lớn nhất của $|z|$ là ____",
     None,
     r"2",
     r"$z$ nằm trên mặt phẳng phức là đường tròn tâm $(0,1)$ bán kính 1. Giá trị lớn nhất của $|z|$ là $1+1=2$"),
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

success = 0
for t in translations:
    qid = t[0]
    content_en = t[1]
    options_en_raw = t[2]
    answer_en = t[3]
    solution_en = t[4]
    content_vi = t[5]
    options_vi_raw = t[6]
    answer_vi = t[7]
    solution_vi = t[8]

    # Serialize options lists to JSON
    options_en = json.dumps(options_en_raw, ensure_ascii=False) if options_en_raw is not None else None
    options_vi = json.dumps(options_vi_raw, ensure_ascii=False) if options_vi_raw is not None else None

    cursor.execute("""
        UPDATE questions
        SET content_en=?, options_en=?, answer_en=?, solution_en=?,
            content_vi=?, options_vi=?, answer_vi=?, solution_vi=?
        WHERE id=?
    """, (content_en, options_en, answer_en, solution_en,
          content_vi, options_vi, answer_vi, solution_vi, qid))

    conn.commit()
    success += 1
    print(f"Committed ID={qid}")

conn.close()
print(f"\nDone. {success} questions translated and committed.")
