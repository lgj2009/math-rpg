import sqlite3
import json

DB_PATH = r'D:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db'

# ============================================================
# Translations for questions ID 6 through 35
# ALL strings with LaTeX use raw strings (r"...") to preserve backslashes
# ============================================================

translations = [
    # ---- ID 6 ----
    (6,
     r"In $\triangle ABC$, $a=2$, $b=3$, $c=\sqrt{7}$, find the measure of angle $C$",
     json.dumps([r"A. $30^\circ$", r"B. $45^\circ$", r"C. $60^\circ$", r"D. $90^\circ$"]),
     "C",
     r"By the law of cosines $\cos C = \frac{a^2+b^2-c^2}{2ab} = \frac{4+9-7}{2\times2\times3} = \frac{1}{2}$, so $C=60^\circ$",

     r"Trong $\triangle ABC$, $a=2$, $b=3$, $c=\sqrt{7}$, tinh so do goc $C$",
     json.dumps([r"A. $30^\circ$", r"B. $45^\circ$", r"C. $60^\circ$", r"D. $90^\circ$"]),
     "C",
     r"Theo dinh ly cosin $\cos C = \frac{a^2+b^2-c^2}{2ab} = \frac{4+9-7}{2\times2\times3} = \frac{1}{2}$, suy ra $C=60^\circ$"),

    # ---- ID 7 ----
    (7,
     r"Given an arithmetic sequence $\{a_n\}$ with first term $a_1=2$ and common difference $d=3$, find $a_5$",
     json.dumps(["A. 11", "B. 12", "C. 13", "D. 14"]),
     "D",
     r"$a_5 = a_1 + (5-1)d = 2 + 4 \times 3 = 14$",

     r"Cho cap so cong $\{a_n\}$ co so hang dau $a_1=2$ va cong sai $d=3$, tinh $a_5$",
     json.dumps(["A. 11", "B. 12", "C. 13", "D. 14"]),
     "D",
     r"$a_5 = a_1 + (5-1)d = 2 + 4 \times 3 = 14$"),

    # ---- ID 8 ----
    (8,
     r"Given a geometric sequence $\{a_n\}$ with first term $a_1=1$ and common ratio $q=2$, find the sum of the first $5$ terms $S_5 =$ ____",
     None,
     "31",
     r"$S_5 = a_1 \frac{q^5-1}{q-1} = 1 \times \frac{2^5-1}{2-1} = 31$",

     r"Cho cap so nhan $\{a_n\}$ co so hang dau $a_1=1$ va cong boi $q=2$, tinh tong $5$ so hang dau $S_5 =$ ____",
     None,
     "31",
     r"$S_5 = a_1 \frac{q^5-1}{q-1} = 1 \times \frac{2^5-1}{2-1} = 31$"),

    # ---- ID 9 ----
    (9,
     r"Given a sequence $\{a_n\}$ whose sum of the first $n$ terms is $S_n = 2n^2 + n$, find $a_3$",
     json.dumps(["A. 9", "B. 10", "C. 11", "D. 12"]),
     "C",
     r"$a_3 = S_3 - S_2 = (2\times9+3) - (2\times4+2) = 21 - 10 = 11$",

     r"Cho day so $\{a_n\}$ co tong $n$ so hang dau $S_n = 2n^2 + n$, tinh $a_3$",
     json.dumps(["A. 9", "B. 10", "C. 11", "D. 12"]),
     "C",
     r"$a_3 = S_3 - S_2 = (2\times9+3) - (2\times4+2) = 21 - 10 = 11$"),

    # ---- ID 10 ----
    (10,
     r"In a geometric sequence $\{a_n\}$, $a_2=2$, $a_5=16$, find the sum of the first $4$ terms $S_4 =$ ____",
     None,
     "15",
     r"$q^3 = \frac{a_5}{a_2} = \frac{16}{2} = 8$, so $q=2$, $a_1=\frac{a_2}{q}=1$, $S_4 = \frac{1\times(2^4-1)}{2-1}=15$",

     r"Trong cap so nhan $\{a_n\}$, $a_2=2$, $a_5=16$, tinh tong $4$ so hang dau $S_4 =$ ____",
     None,
     "15",
     r"$q^3 = \frac{a_5}{a_2} = \frac{16}{2} = 8$, suy ra $q=2$, $a_1=\frac{a_2}{q}=1$, $S_4 = \frac{1\times(2^4-1)}{2-1}=15$"),

    # ---- ID 11 ----
    (11,
     r"Find the value of $\sum\limits_{n=1}^{100} \frac{1}{n(n+1)}$",
     None,
     "100/101",
     r"$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$, so $\sum_{n=1}^{100} \frac{1}{n(n+1)} = 1 - \frac{1}{101} = \frac{100}{101}$",

     r"Tinh gia tri cua $\sum\limits_{n=1}^{100} \frac{1}{n(n+1)}$",
     None,
     "100/101",
     r"$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$, suy ra $\sum_{n=1}^{100} \frac{1}{n(n+1)} = 1 - \frac{1}{101} = \frac{100}{101}$"),

    # ---- ID 12 ----
    (12,
     "How many different ways can $5$ different books be arranged in a row?",
     json.dumps(["A. 60", "B. 100", "C. 120", "D. 240"]),
     "C",
     r"$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$",

     "Co bao nhieu cach xep $5$ cuon sach khac nhau thanh mot hang?",
     json.dumps(["A. 60", "B. 100", "C. 120", "D. 240"]),
     "C",
     r"$5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$"),

    # ---- ID 13 ----
    (13,
     "From $10$ students, choose $2$ to participate in a competition. There are ____ different ways to choose.",
     None,
     "45",
     r"$\mathrm{C}_{10}^2 = \frac{10\times9}{2} = 45$",

     "Tu $10$ hoc sinh, chon $2$ nguoi tham gia cuoc thi. Co ____ cach chon khac nhau.",
     None,
     "45",
     r"$\mathrm{C}_{10}^2 = \frac{10\times9}{2} = 45$"),

    # ---- ID 14 ----
    (14,
     "When rolling two fair dice, what is the probability that the sum of the numbers is $7$?",
     json.dumps([r"A. $\frac{1}{6}$", r"B. $\frac{1}{4}$", r"C. $\frac{1}{3}$", r"D. $\frac{5}{36}$"]),
     "A",
     r"The elementary events with sum 7 are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): 6 cases. Total cases: 36. $P=\frac{6}{36}=\frac{1}{6}$",

     "Gieo hai con xuc xac can doi, tinh xac suat de tong so cham bang $7$",
     json.dumps([r"A. $\frac{1}{6}$", r"B. $\frac{1}{4}$", r"C. $\frac{1}{3}$", r"D. $\frac{5}{36}$"]),
     "A",
     r"Cac bien co so cap co tong 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1): 6 truong hop. Tong so: 36. $P=\frac{6}{36}=\frac{1}{6}$"),

    # ---- ID 15 ----
    (15,
     r"In the expansion of $(x+1)^4$, the coefficient of the $x^2$ term is ____",
     None,
     "6",
     r"$T_{r+1} = \mathrm{C}_4^r x^{4-r} \cdot 1^r$. Setting $4-r=2$ gives $r=2$, coefficient is $\mathrm{C}_4^2 = 6$",

     r"Trong khai trien cua $(x+1)^4$, he so cua so hang $x^2$ la ____",
     None,
     "6",
     r"$T_{r+1} = \mathrm{C}_4^r x^{4-r} \cdot 1^r$. Cho $4-r=2$ ta duoc $r=2$, he so la $\mathrm{C}_4^2 = 6$"),

    # ---- ID 16 ----
    (16,
     "Roll a fair die. Let $X$ be the number shown. Find $E(X)$",
     None,
     "3.5",
     r"$E(X) = \frac{1+2+3+4+5+6}{6} = 3.5$",

     "Gieo mot con xuc xac can doi. Goi $X$ la so cham xuat hien. Tinh $E(X)$",
     None,
     "3.5",
     r"$E(X) = \frac{1+2+3+4+5+6}{6} = 3.5$"),

    # ---- ID 17 ----
    (17,
     "The length of the space diagonal of a cube with edge length $2$ is",
     json.dumps(["A. 2", r"B. $2\sqrt{3}$", r"C. $2\sqrt{2}$", "D. 4"]),
     "B",
     r"Space diagonal $= \sqrt{2^2+2^2+2^2} = 2\sqrt{3}$",

     "Do dai duong cheo khong gian cua hinh lap phuong co canh $2$ la",
     json.dumps(["A. 2", r"B. $2\sqrt{3}$", r"C. $2\sqrt{2}$", "D. 4"]),
     "B",
     r"Duong cheo khong gian $= \sqrt{2^2+2^2+2^2} = 2\sqrt{3}$"),

    # ---- ID 18 ----
    (18,
     "The volume of a sphere with radius $3$ is ____",
     None,
     r"$36\pi$",
     r"$V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi \times 27 = 36\pi$",

     "The tich cua hinh cau co ban kinh $3$ la ____",
     None,
     r"$36\pi$",
     r"$V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi \times 27 = 36\pi$"),

    # ---- ID 19 ----
    (19,
     "A rectangular prism has length, width, and height $3$, $4$, $5$ respectively. Find the tangent of the angle between the space diagonal and the base.",
     json.dumps([r"A. $\frac{\sqrt{2}}{2}$", "B. 1", r"C. $\sqrt{2}$", r"D. $\frac{5}{4}$"]),
     "B",
     r"Base diagonal $= \sqrt{3^2+4^2}=5$, height $=5$, $\tan\theta = \frac{5}{5} = 1$",

     "Hinh hop chu nhat co chieu dai, chieu rong, chieu cao lan luot la $3$, $4$, $5$. Tinh tang cua goc giua duong cheo khong gian va mat day.",
     json.dumps([r"A. $\frac{\sqrt{2}}{2}$", "B. 1", r"C. $\sqrt{2}$", r"D. $\frac{5}{4}$"]),
     "B",
     r"Duong cheo day $= \sqrt{3^2+4^2}=5$, chieu cao $=5$, $\tan\theta = \frac{5}{5} = 1$"),

    # ---- ID 20 ----
    (20,
     "A pyramid has a square base of side length $2$ and height $3$. Its volume is ____",
     None,
     "4",
     r"$V = \frac{1}{3}Sh = \frac{1}{3} \times 4 \times 3 = 4$",

     "Hinh chop co day la hinh vuong canh $2$ va chieu cao $3$. The tich cua no la ____",
     None,
     "4",
     r"$V = \frac{1}{3}Sh = \frac{1}{3} \times 4 \times 3 = 4$"),

    # ---- ID 21 ----
    (21,
     "A cone has base radius $3$ and height $4$. Find its lateral surface area.",
     None,
     r"$15\pi$",
     r"Slant height $l = \sqrt{3^2+4^2}=5$, lateral area $S = \pi r l = \pi \times 3 \times 5 = 15\pi$",

     "Hinh non co ban kinh day $3$ va chieu cao $4$. Tinh dien tich xung quanh.",
     None,
     r"$15\pi$",
     r"Duong sinh $l = \sqrt{3^2+4^2}=5$, dien tich xung quanh $S = \pi r l = \pi \times 3 \times 5 = 15\pi$"),

    # ---- ID 22 ----
    (22,
     "The radius of the circle $x^2 + y^2 = 4$ is",
     json.dumps(["A. 1", "B. 2", "C. 4", "D. 16"]),
     "B",
     r"Standard equation of a circle $x^2+y^2=r^2$, so $r^2=4$, $r=2$",

     r"Ban kinh cua duong tron $x^2 + y^2 = 4$ la",
     json.dumps(["A. 1", "B. 2", "C. 4", "D. 16"]),
     "B",
     r"Phuong trinh chuan cua duong tron $x^2+y^2=r^2$, suy ra $r^2=4$, $r=2$"),

    # ---- ID 23 ----
    (23,
     "The distance from point $(1,2)$ to point $(4,6)$ is ____",
     None,
     "5",
     r"$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9+16}=5$",

     "Khoang cach tu diem $(1,2)$ den diem $(4,6)$ la ____",
     None,
     "5",
     r"$d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9+16}=5$"),

    # ---- ID 24 ----
    (24,
     r"The focal length of the ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ is",
     json.dumps([r"A. $2\sqrt{5}$", r"B. $\sqrt{5}$", "C. 2", "D. 5"]),
     "A",
     r"$a^2=9$, $b^2=4$, $c^2 = a^2-b^2 = 5$, so focal length $2c = 2\sqrt{5}$",

     r"Tieu cu cua elip $\frac{x^2}{9} + \frac{y^2}{4} = 1$ la",
     json.dumps([r"A. $2\sqrt{5}$", r"B. $\sqrt{5}$", "C. 2", "D. 5"]),
     "A",
     r"$a^2=9$, $b^2=4$, $c^2 = a^2-b^2 = 5$, suy ra tieu cu $2c = 2\sqrt{5}$"),

    # ---- ID 25 ----
    (25,
     r"The focus of the parabola $y^2 = 8x$ has coordinates (____, 0)",
     None,
     "2",
     r"$y^2 = 2px$, so $2p=8$, $p=4$, focus $\left(\frac{p}{2}, 0\right) = (2, 0)$",

     r"Tieu diem cua parabol $y^2 = 8x$ co toa do (____, 0)",
     None,
     "2",
     r"$y^2 = 2px$, suy ra $2p=8$, $p=4$, tieu diem $\left(\frac{p}{2}, 0\right) = (2, 0)$"),

    # ---- ID 26 ----
    (26,
     r"Find the equations of the asymptotes of the hyperbola $\frac{x^2}{3} - \frac{y^2}{4} = 1$",
     None,
     r"$y=\pm\frac{2}{\sqrt{3}}x$",
     r"$a^2=3$, $b^2=4$, asymptotes: $y = \pm\frac{b}{a}x = \pm\frac{2}{\sqrt{3}}x$",

     r"Tim phuong trinh cac duong tiem can cua hypebol $\frac{x^2}{3} - \frac{y^2}{4} = 1$",
     None,
     r"$y=\pm\frac{2}{\sqrt{3}}x$",
     r"$a^2=3$, $b^2=4$, tiem can: $y = \pm\frac{b}{a}x = \pm\frac{2}{\sqrt{3}}x$"),

    # ---- ID 27 ----
    (27,
     r"The derivative of the function $f(x)=x^2$ at $x=2$ is",
     json.dumps(["A. 2", "B. 3", "C. 4", "D. 5"]),
     "C",
     r"$f'(x)=2x$, so $f'(2)=4$",

     "Dao ham cua ham so $f(x)=x^2$ tai $x=2$ la",
     json.dumps(["A. 2", "B. 3", "C. 4", "D. 5"]),
     "C",
     r"$f'(x)=2x$, suy ra $f'(2)=4$"),

    # ---- ID 28 ----
    (28,
     r"The derivative of the function $f(x)=\sin x$ at $x=\frac{\pi}{3}$ is ____",
     None,
     "1/2",
     r"$f'(x)=\cos x$, so $f'(\frac{\pi}{3})=\cos\frac{\pi}{3}=\frac{1}{2}$",

     r"Dao ham cua ham so $f(x)=\sin x$ tai $x=\frac{\pi}{3}$ la ____",
     None,
     "1/2",
     r"$f'(x)=\cos x$, suy ra $f'(\frac{\pi}{3})=\cos\frac{\pi}{3}=\frac{1}{2}$"),

    # ---- ID 29 ----
    (29,
     "The local maximum value of the function $f(x)=x^3-3x$ is",
     json.dumps(["A. -2", "B. 0", "C. 2", "D. 4"]),
     "C",
     r"$f'(x)=3x^2-3=0$, $x=\pm1$. $f''(x)=6x$, $f''(-1)=-6<0$ so $x=-1$ is a local maximum point, $f(-1)=-1+3=2$",

     "Gia tri cuc dai cua ham so $f(x)=x^3-3x$ la",
     json.dumps(["A. -2", "B. 0", "C. 2", "D. 4"]),
     "C",
     r"$f'(x)=3x^2-3=0$, $x=\pm1$. $f''(x)=6x$, $f''(-1)=-6<0$ nen $x=-1$ la diem cuc dai, $f(-1)=-1+3=2$"),

    # ---- ID 30 ----
    (30,
     r"The tangent line to the curve $f(x)=\ln x$ at $x=1$ has equation $y =$ ____",
     None,
     r"$x-1$",
     r"$f'(x)=\frac{1}{x}$, $f'(1)=1$, $f(1)=0$, so $y = 1\times(x-1)+0 = x-1$",

     r"Phuong trinh tiep tuyen cua duong cong $f(x)=\ln x$ tai $x=1$ la $y =$ ____",
     None,
     r"$x-1$",
     r"$f'(x)=\frac{1}{x}$, $f'(1)=1$, $f(1)=0$, suy ra $y = 1\times(x-1)+0 = x-1$"),

    # ---- ID 31 ----
    (31,
     "Find the maximum value of the function $f(x)=x^3-6x^2+9x+1$ on the interval $[0,4]$",
     None,
     "5",
     r"$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0$, $x=1,3$. $f(0)=1$, $f(1)=5$, $f(3)=1$, $f(4)=5$. Maximum value is $5$",

     "Tim gia tri lon nhat cua ham so $f(x)=x^3-6x^2+9x+1$ tren doan $[0,4]$",
     None,
     "5",
     r"$f'(x)=3x^2-12x+9=3(x-1)(x-3)=0$, $x=1,3$. $f(0)=1$, $f(1)=5$, $f(3)=1$, $f(4)=5$. Gia tri lon nhat la $5$"),

    # ---- ID 32 ----
    (32,
     r"Given sets $A=\{1,2,3\}$, $B=\{2,3,4\}$, then $A\cap B$ is",
     json.dumps([r"A. $\{1,2,3,4\}$", r"B. $\{2,3\}$", r"C. $\{1,4\}$", r"D. $\{1,2,3\}$"]),
     "B",
     r"$A\cap B = \{2,3\}$",

     r"Cho cac tap hop $A=\{1,2,3\}$, $B=\{2,3,4\}$, khi do $A\cap B$ bang",
     json.dumps([r"A. $\{1,2,3,4\}$", r"B. $\{2,3\}$", r"C. $\{1,4\}$", r"D. $\{1,2,3\}$"]),
     "B",
     r"$A\cap B = \{2,3\}$"),

    # ---- ID 33 ----
    (33,
     r"Given sets $A=\{x\mid x>2\}$, $B=\{x\mid x\le 5\}$, then $A\cup B =$ ____ (answer R for all real numbers)",
     None,
     "R",
     r"On the number line, $A\cup B$ covers all real numbers, so it is $\mathbb{R}$",

     r"Cho cac tap hop $A=\{x\mid x>2\}$, $B=\{x\mid x\le 5\}$, khi do $A\cup B =$ ____ (dap an R la tap so thuc)",
     None,
     "R",
     r"Tren truc so, $A\cup B$ bao gom tat ca cac so thuc, do do la $\mathbb{R}$"),

    # ---- ID 34 ----
    (34,
     r'Let $x\in\mathbb{R}$. Then "$x=1$" is a _____ condition for "$x^2=1$"',
     json.dumps(["A. necessary and sufficient condition", "B. sufficient but not necessary condition", "C. necessary but not sufficient condition", "D. neither necessary nor sufficient condition"]),
     "B",
     r"$x=1\Rightarrow x^2=1$, but $x^2=1\Rightarrow x=\pm1$, so it is sufficient but not necessary",

     r'Cho $x\in\mathbb{R}$. Khi do "$x=1$" la dieu kien _____ cua "$x^2=1$"',
     json.dumps(["A. dieu kien can va du", "B. dieu kien du nhung khong can", "C. dieu kien can nhung khong du", "D. khong la dieu kien can cung khong la dieu kien du"]),
     "B",
     r"$x=1\Rightarrow x^2=1$, nhung $x^2=1\Rightarrow x=\pm1$, do do la dieu kien du nhung khong can"),

    # ---- ID 35 ----
    (35,
     r"The number of subsets of the set $\{1,2,3\}$ is ____",
     None,
     "8",
     r"$2^3 = 8$. They are $\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}$",

     r"So tap con cua tap hop $\{1,2,3\}$ la ____",
     None,
     "8",
     r"$2^3 = 8$. Do la $\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}$"),
]

# Now update the database
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

success = 0
for t in translations:
    (qid, content_en, options_en, answer_en, solution_en,
     content_vi, options_vi, answer_vi, solution_vi) = t

    c.execute("""
        UPDATE questions
        SET content_en=?, options_en=?, answer_en=?, solution_en=?,
            content_vi=?, options_vi=?, answer_vi=?, solution_vi=?
        WHERE id=?
    """, (content_en, options_en, answer_en, solution_en,
          content_vi, options_vi, answer_vi, solution_vi, qid))
    if c.rowcount > 0:
        success += 1

conn.commit()
conn.close()

print(f"Done! {success} questions updated successfully.")
