"""
Translate 60 Chinese math questions to English and Vietnamese.
Updates math_rpg.db with content_en, content_vi, options_en, options_vi,
answer_en, answer_vi, solution_en, solution_vi fields.
"""

import sqlite3
import json

DB_PATH = "d:/编程/Python/stutdy/.claude/worktrees/math-rpg-implementation/math_rpg.db"

# ============================================================
# Translations data: keyed by question ID
# Each entry: { 'content_en': ..., 'content_vi': ..., 'options_en': ..., 'options_vi': ...,
#               'answer_en': ..., 'answer_vi': ..., 'solution_en': ..., 'solution_vi': ... }
# None means the field should be set to NULL (was None in original)
# ============================================================

translations = {
    # --- ID 73 ---
    73: {
        'content_en': 'In $\triangle ABC$, the sides opposite angles $A, B, C$ are $a, b, c$ respectively. Given $a=3$, $c=\sqrt{2}$, $B=45°$. (1) Find the value of $\sin C$; (2) Take a point $D$ on side $BC$ such that $\cos\angle ADC = -\frac{4}{5}$, find $\tan\angle DAC$.',
        'content_vi': 'Trong $\triangle ABC$, các cạnh đối diện với góc $A, B, C$ lần lượt là $a, b, c$. Biết $a=3$, $c=\sqrt{2}$, $B=45°$. (1) Tính giá trị của $\sin C$; (2) Lấy điểm $D$ trên cạnh $BC$ sao cho $\cos\angle ADC = -\frac{4}{5}$, tính $\tan\angle DAC$.',
        'options_en': None,
        'options_vi': None,
        'answer_en': 'sinC=1/3, tan∠DAC=2/11',
        'answer_vi': 'sinC=1/3, tan∠DAC=2/11',
        'solution_en': '(1) Cosine theorem $b^2=9+2-6\sqrt{2}\cdot\frac{\sqrt{2}}{2}=5$, $b=\sqrt{5}$. Sine theorem $\sin C=\frac{c\sin B}{b}=\frac{1}{3}$.',
        'solution_vi': '(1) Định lý cosin $b^2=9+2-6\sqrt{2}\cdot\frac{\sqrt{2}}{2}=5$, $b=\sqrt{5}$. Định lý sin $\sin C=\frac{c\sin B}{b}=\frac{1}{3}$.',
    },

    # --- ID 74 ---
    74: {
        'content_en': 'Let $S_n$ be the sum of the first $n$ terms of the arithmetic sequence $\{a_n\}$. If $a_1\neq 0$, $a_2=3a_1$, then $\frac{S_{10}}{S_5}=$ ____',
        'content_vi': 'Gọi $S_n$ là tổng $n$ số hạng đầu của cấp số cộng $\{a_n\}$. Nếu $a_1\neq 0$, $a_2=3a_1$, thì $\frac{S_{10}}{S_5}=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '4',
        'answer_vi': '4',
        'solution_en': 'From $a_2=a_1+d=3a_1$ we get $d=2a_1$. $S_n=na_1+\frac{n(n-1)}{2}d=na_1+n(n-1)a_1=n^2a_1$. $\frac{S_{10}}{S_5}=\frac{100}{25}=4$.',
        'solution_vi': 'Từ $a_2=a_1+d=3a_1$ suy ra $d=2a_1$. $S_n=na_1+\frac{n(n-1)}{2}d=na_1+n(n-1)a_1=n^2a_1$. $\frac{S_{10}}{S_5}=\frac{100}{25}=4$.',
    },

    # --- ID 75 ---
    75: {
        'content_en': 'Teams A and B play a basketball final series, adopting a best-of-seven format (when a team wins four games, that team wins and the series ends). Based on previous results, Team A\'s home/away schedule is "home, home, away, away, home, away, home". Suppose Team A\'s probability of winning at home is 0.6, and winning away is 0.5, and the results of each game are independent. The probability that Team A wins 4:1 is ____',
        'content_vi': 'Đội A và đội B thi đấu chung kết bóng rổ theo thể thức thắng 4 trận trước (thắng 4 trong 7 trận). Theo kết quả trước đó, lịch sân nhà/sân khách của đội A lần lượt là "nhà, nhà, khách, khách, nhà, khách, nhà". Giả sử xác suất đội A thắng trên sân nhà là 0,6 và thắng trên sân khách là 0,5, kết quả các trận độc lập với nhau. Xác suất đội A thắng 4:1 là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '0.18',
        'answer_vi': '0,18',
        'solution_en': 'Team A winning 4:1 means Team A wins the 5th game, and wins 3 of the first 4 games. Calculate the sum of probabilities of all arrangements.',
        'solution_vi': 'Đội A thắng 4:1 nghĩa là trận thứ 5 đội A thắng, 4 trận đầu đội A thắng 3 thua 1. Tính tổng xác suất của các cách sắp xếp.',
    },

    # --- ID 76 ---
    76: {
        'content_en': 'In $\triangle ABC$, the sides opposite interior angles $A,B,C$ are $a,b,c$ respectively. Given $(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C$. (1) Find $A$; (2) If $\sqrt{2}a+b=2c$, find $\sin C$.',
        'content_vi': 'Trong $\triangle ABC$, các cạnh đối diện với góc trong $A,B,C$ lần lượt là $a,b,c$. Cho $(\sin B-\sin C)^2=\sin^2 A-\sin B\sin C$. (1) Tìm $A$; (2) Nếu $\sqrt{2}a+b=2c$, tìm $\sin C$.',
        'options_en': None,
        'options_vi': None,
        'answer_en': 'A=60°, sinC=(√6+√2)/4',
        'answer_vi': 'A=60°, sinC=(√6+√2)/4',
        'solution_en': '(1) Expand to get $\sin^2 B+\sin^2 C-2\sin B\sin C = \sin^2 A-\sin B\sin C$. Convert to sides using the sine theorem, then by the cosine theorem $A=60°$.',
        'solution_vi': '(1) Khai triển được $\sin^2 B+\sin^2 C-2\sin B\sin C = \sin^2 A-\sin B\sin C$. Dùng định lý sin chuyển thành cạnh, rồi dùng định lý cosin được $A=60°$.',
    },

    # --- ID 77 ---
    77: {
        'content_en': 'Given $\vec{AB}=(2,3)$, $\vec{AC}=(3,t)$, $|\vec{BC}|=1$, then $\vec{AB}\cdot\vec{BC}=$',
        'content_vi': 'Cho $\vec{AB}=(2,3)$, $\vec{AC}=(3,t)$, $|\vec{BC}|=1$, thì $\vec{AB}\cdot\vec{BC}=$',
        'options_en': ['A. -3', 'B. -2', 'C. 2', 'D. 3'],
        'options_vi': ['A. -3', 'B. -2', 'C. 2', 'D. 3'],
        'answer_en': 'C',
        'answer_vi': 'C',
        'solution_en': '$\vec{BC}=\vec{AC}-\vec{AB}=(1,t-3)$. $|\vec{BC}|^2=1+(t-3)^2=1$, so $t=3$. $\vec{BC}=(1,0)$, $\vec{AB}\cdot\vec{BC}=2\times1+3\times0=2$.',
        'solution_vi': '$\vec{BC}=\vec{AC}-\vec{AB}=(1,t-3)$. $|\vec{BC}|^2=1+(t-3)^2=1$, suy ra $t=3$. $\vec{BC}=(1,0)$, $\vec{AB}\cdot\vec{BC}=2\times1+3\times0=2$.',
    },

    # --- ID 78 ---
    78: {
        'content_en': 'Let $f(x)=\ln|2x+1|-\ln|2x-1|$, then $f(x)$',
        'content_vi': 'Cho $f(x)=\ln|2x+1|-\ln|2x-1|$, thì $f(x)$',
        'options_en': ['A. is an even function and strictly increasing on $(\\frac{1}{2},+\\infty)$', 'B. is an odd function and strictly decreasing on $(-\\frac{1}{2},\\frac{1}{2})$', 'C. is an even function and strictly increasing on $(-\\infty,-\\frac{1}{2})$', 'D. is an odd function and strictly decreasing on $(-\\infty,-\\frac{1}{2})$'],
        'options_vi': ['A. là hàm chẵn và đồng biến trên $(\\frac{1}{2},+\\infty)$', 'B. là hàm lẻ và nghịch biến trên $(-\\frac{1}{2},\\frac{1}{2})$', 'C. là hàm chẵn và đồng biến trên $(-\\infty,-\\frac{1}{2})$', 'D. là hàm lẻ và nghịch biến trên $(-\\infty,-\\frac{1}{2})$'],
        'answer_en': 'D',
        'answer_vi': 'D',
        'solution_en': '$f(-x)=\ln|-2x+1|-\ln|-2x-1|=\ln|2x-1|-\ln|2x+1|=-f(x)$, odd function. For $x<-\frac{1}{2}$, $f\'(x)<0$, decreasing.',
        'solution_vi': '$f(-x)=\ln|-2x+1|-\ln|-2x-1|=\ln|2x-1|-\ln|2x+1|=-f(x)$, hàm lẻ. Khi $x<-\frac{1}{2}$, $f\'(x)<0$, nghịch biến.',
    },

    # --- ID 79 ---
    79: {
        'content_en': 'The constant term in the expansion of $(x+\frac{1}{x})^6$ is ____',
        'content_vi': 'Số hạng không đổi trong khai triển của $(x+\frac{1}{x})^6$ là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '20',
        'answer_vi': '20',
        'solution_en': 'General term $T_{r+1}=C_6^r x^{6-2r}$. Set $6-2r=0$, get $r=3$. Constant term $C_6^3=20$.',
        'solution_vi': 'Số hạng tổng quát $T_{r+1}=C_6^r x^{6-2r}$. Cho $6-2r=0$, được $r=3$. Số hạng không đổi $C_6^3=20$.',
    },

    # --- ID 80 ---
    80: {
        'content_en': 'The tangent line to the curve $y=ae^x+x\ln x$ at point $(1,ae)$ is $y=2x+b$. Then',
        'content_vi': 'Tiếp tuyến của đường cong $y=ae^x+x\ln x$ tại điểm $(1,ae)$ là $y=2x+b$. Khi đó',
        'options_en': ['A. a=e,b=-1', 'B. a=e,b=1', 'C. a=e^{-1},b=1', 'D. a=e^{-1},b=-1'],
        'options_vi': ['A. a=e,b=-1', 'B. a=e,b=1', 'C. a=e^{-1},b=1', 'D. a=e^{-1},b=-1'],
        'answer_en': 'D',
        'answer_vi': 'D',
        'solution_en': "$y'=ae^x+\ln x+1$. At $x=1$ the slope is $ae+1=2$, so $a=e^{-1}$. The tangent $y=2x+b$ passes through $(1,1)$, so $b=-1$.",
        'solution_vi': "$y'=ae^x+\ln x+1$. Tại $x=1$, hệ số góc là $ae+1=2$, suy ra $a=e^{-1}$. Tiếp tuyến $y=2x+b$ đi qua $(1,1)$, suy ra $b=-1$.",
    },

    # --- ID 81 ---
    81: {
        'content_en': 'To study the residual levels of two types of ions (A and B) in mice, the following experiment was conducted: 200 mice were randomly divided into two groups A and B, 100 each. Group A was given ion A solution, group B was given ion B solution. Each mouse received the same volume and molar concentration. After some time, the percentage of ions remaining in the mice was measured. The average residual percentage for ion A was 5.2, and for ion B was 4.8. Based on the experimental data, estimate: if the residual percentage of ion A follows a normal distribution $N(\mu_1,\sigma_1^2)$, find the confidence interval for its mean. (Adapted to finding probability)',
        'content_vi': 'Để nghiên cứu mức độ tồn dư của hai loại ion A và B trong chuột, tiến hành thí nghiệm sau: 200 con chuột được chia ngẫu nhiên thành hai nhóm A và B, mỗi nhóm 100 con. Nhóm A được cho uống dung dịch ion A, nhóm B được cho uống dung dịch ion B. Mỗi con chuột được cho uống cùng thể tích và cùng nồng độ mol. Sau một thời gian, đo tỷ lệ phần trăm ion còn lại trong chuột. Tỷ lệ tồn dư trung bình của ion A là 5,2, của ion B là 4,8. Dựa trên số liệu thí nghiệm, ước lượng: nếu tỷ lệ tồn dư của ion A tuân theo phân phối chuẩn $N(\mu_1,\sigma_1^2)$, tìm khoảng tin cậy cho trung bình. (Chuyển thể thành tìm xác suất)',
        'options_en': None,
        'options_vi': None,
        'answer_en': '0.68',
        'answer_vi': '0,68',
        'solution_en': '$P(|X-\mu|<\sigma) \approx 0.6827$.',
        'solution_vi': '$P(|X-\mu|<\sigma) \approx 0.6827$.',
    },

    # --- ID 82 ---
    82: {
        'content_en': 'A factory produces products of two models, A and B. The defect rate of model A is 5%, and of model B is 3%. The probability of randomly picking a product of model A is 0.6, and of model B is 0.4. (1) Find the probability that a randomly selected product is defective; (2) Given that the selected product is defective, find the probability that it is model A.',
        'content_vi': 'Một nhà máy sản xuất hai loại sản phẩm A và B. Tỷ lệ phế phẩm của loại A là 5%, của loại B là 3%. Xác suất chọn ngẫu nhiên được sản phẩm loại A là 0,6, loại B là 0,4. (1) Tính xác suất sản phẩm được chọn là phế phẩm; (2) Biết rằng sản phẩm được chọn là phế phẩm, tính xác suất nó là loại A.',
        'options_en': None,
        'options_vi': None,
        'answer_en': '(1)0.042 (2)5/7',
        'answer_vi': '(1)0,042 (2)5/7',
        'solution_en': '(1) Law of total probability: $P(\text{defective})=0.6\times0.05+0.4\times0.03=0.03+0.012=0.042$. (2) Bayes\' theorem: $P(A|\text{defective})=\frac{0.6\times0.05}{0.042}=\frac{0.03}{0.042}=\frac{5}{7}$.',
        'solution_vi': '(1) Công thức xác suất toàn phần: $P(\text{phế phẩm})=0,6\times0,05+0,4\times0,03=0,03+0,012=0,042$. (2) Định lý Bayes: $P(A|\text{phế phẩm})=\frac{0,6\times0,05}{0,042}=\frac{0,03}{0,042}=\frac{5}{7}$.',
    },

    # --- ID 83 ---
    83: {
        'content_en': 'A company produces a product. The daily fixed cost is 2000 yuan, and the variable cost per unit is 30 yuan. Suppose the daily production volume is $x$ units, and the unit price is $p=100-0.01x$ yuan. Find: (1) the production volume that maximizes daily profit; (2) the maximum daily profit.',
        'content_vi': 'Một doanh nghiệp sản xuất một loại sản phẩm. Chi phí cố định hàng ngày là 2000 nhân dân tệ, chi phí biến đổi mỗi sản phẩm là 30 nhân dân tệ. Giả sử sản xuất $x$ sản phẩm mỗi ngày, giá bán mỗi sản phẩm là $p=100-0,01x$ nhân dân tệ. Tìm: (1) sản lượng tối đa hóa lợi nhuận hàng ngày; (2) lợi nhuận tối đa.',
        'options_en': None,
        'options_vi': None,
        'answer_en': '(1)3500 units (2)120500 yuan',
        'answer_vi': '(1)3500 sản phẩm (2)120500 nhân dân tệ',
        'solution_en': 'Total revenue $R(x)=x(100-0.01x)=100x-0.01x^2$. Total cost $C(x)=2000+30x$. Profit $L(x)=70x-0.01x^2-2000$. $L\'(x)=70-0.02x=0$, $x=3500$. $L(3500)=70\times3500-0.01\times12250000-2000=245000-122500-2000=120500$.',
        'solution_vi': 'Tổng doanh thu $R(x)=x(100-0,01x)=100x-0,01x^2$. Tổng chi phí $C(x)=2000+30x$. Lợi nhuận $L(x)=70x-0,01x^2-2000$. $L\'(x)=70-0,02x=0$, $x=3500$. $L(3500)=70\times3500-0,01\times12250000-2000=245000-122500-2000=120500$.',
    },

    # --- ID 84 ---
    84: {
        'content_en': 'A city\'s population at the beginning of 2020 was 1 million, with an annual growth rate of 3%. The city plans to build 50,000 square meters of new housing each year. The per capita living area at the beginning of 2020 is 20 square meters. (1) Find the city\'s population at the beginning of 2030 (rounded to the nearest 10,000); (2) If the per capita living area remains unchanged, find how many square meters of new housing are needed each year to meet the population growth demand. (Reference data: $1.03^{10}\approx1.344$)',
        'content_vi': 'Đầu năm 2020, dân số của một thành phố là 1 triệu người, với tỷ lệ tăng dân số hàng năm là 3%. Thành phố dự kiến xây mới 5 vạn mét vuông nhà ở mỗi năm. Diện tích nhà ở bình quân đầu người đầu năm 2020 là 20 mét vuông. (1) Tính dân số thành phố đầu năm 2030 (chính xác đến vạn); (2) Nếu diện tích nhà ở bình quân đầu người không đổi, tính diện tích nhà ở mới cần xây mỗi năm để đáp ứng nhu cầu tăng dân số.',
        'options_en': None,
        'options_vi': None,
        'answer_en': '(1)1.34 million (2)67,200 m²',
        'answer_vi': '(1)134 vạn (2)6,72 vạn m²',
        'solution_en': '(1) $P_{10}=100\times1.03^{10}=134.4\approx134$ ten-thousands. (2) Additional housing needed: $34\times20=680$ ten-thousand m², annual average $68$ ten-thousand m²... Keeping per capita constant, annual increase needed: $100\times0.03\times20=60$ ten-thousand m², plus existing 5 ten-thousand m²... Actual demand about 67,200 m² per year.',
        'solution_vi': '(1) $P_{10}=100\times1,03^{10}=134,4\approx134$ vạn. (2) Cần tăng thêm nhà ở $34\times20=680$ vạn m², trung bình mỗi năm $68$ vạn m²... Giữ bình quân không đổi, mỗi năm cần $100\times0,03\times20=60$ vạn m² tăng thêm, cộng với 5 vạn m² hiện có... Nhu cầu thực tế khoảng 6,72 vạn m² mỗi năm.',
    },

    # --- ID 85 ---
    85: {
        'content_en': 'As shown in the figure, a farm plans to build a greenhouse with a rectangular base. The roof is an inclined rectangular plane. The highest point is 4 meters above the ground, the lowest point is 2 meters above the ground. The base is 20 meters long and 10 meters wide. Find the area of the greenhouse roof. (Hint: The roof plane area can be viewed as the magnitude of the cross product of the two diagonal vectors.)',
        'content_vi': 'Như hình vẽ, một trang trại dự định xây một nhà kính có đáy hình chữ nhật. Mái nhà là mặt phẳng hình chữ nhật nghiêng. Điểm cao nhất cách mặt đất 4 mét, điểm thấp nhất cách mặt đất 2 mét. Đáy nhà kính dài 20 mét, rộng 10 mét. Tính diện tích mái nhà kính.',
        'options_en': None,
        'options_vi': None,
        'answer_en': '20√105≈205 m²',
        'answer_vi': '20√105≈205 m²',
        'solution_en': 'Roof vertices: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\vec{u}=(20,0,2)$, $\vec{v}=(0,10,2)$. $\vec{u}\times\vec{v}=(-20,-40,200)$. Area $|\vec{u}\times\vec{v}|=\sqrt{400+1600+40000}=20\sqrt{105}\approx205$ m².',
        'solution_vi': 'Các đỉnh mái: $(0,0,2),(20,0,2),(20,10,4),(0,10,4)$. $\vec{u}=(20,0,2)$, $\vec{v}=(0,10,2)$. $\vec{u}\times\vec{v}=(-20,-40,200)$. Diện tích $|\vec{u}\times\vec{v}|=\sqrt{400+1600+40000}=20\sqrt{105}\approx205$ m².',
    },

    # --- ID 86 ---
    86: {
        'content_en': 'A city conducted a survey to understand public awareness of the "waste sorting" policy. 200 citizens were randomly surveyed. Results: among 80 people aged 18-30, 60 were aware; among 70 people aged 31-50, 50 were aware; among 50 people aged 51+, 25 were aware. (1) Based on the data, can we conclude at 95% confidence that awareness is related to age group? (2) If 3 citizens are randomly selected from the city, let $X$ be the number who are aware of waste sorting. Find $E(X)$.',
        'content_vi': 'Một thành phố khảo sát mức độ hiểu biết về chính sách "phân loại rác" của người dân. Khảo sát ngẫu nhiên 200 người. Kết quả: 60/80 người 18-30 tuổi biết, 50/70 người 31-50 tuổi biết, 25/50 người trên 51 tuổi biết. (1) Dựa trên số liệu, có thể kết luận ở mức tin cậy 95% rằng hiểu biết có liên quan đến nhóm tuổi không? (2) Chọn ngẫu nhiên 3 người từ thành phố, gọi $X$ là số người biết về phân loại rác. Tính $E(X)$.',
        'options_en': None,
        'options_vi': None,
        'answer_en': '(1)Related (2)2.025',
        'answer_vi': '(1)Có liên quan (2)2,025',
        'solution_en': '(1) Chi-square test of contingency table, $\chi^2\approx7.8>3.841$, significant difference exists. (2) Overall awareness rate $p=\frac{135}{200}=0.675$, $E(X)=np=3\times0.675=2.025$.',
        'solution_vi': '(1) Kiểm định Chi-square bảng liên hợp, $\chi^2\approx7,8>3,841$, có khác biệt đáng kể. (2) Tỷ lệ hiểu biết chung $p=\frac{135}{200}=0,675$, $E(X)=np=3\times0,675=2,025$.',
    },

    # --- ID 87 ---
    87: {
        'content_en': 'A park plans to build a parabolic arch bridge. The span of the arch is 40 meters, and the highest point is 10 meters above the water surface. Take the water surface as the $x$-axis, and the vertical line from the highest point downward as the $y$-axis. (1) Find the parabolic equation of the arch; (2) If a boat\'s mast is 8 meters above the water and the boat is 6 meters wide (symmetric about the $y$-axis), can the boat safely pass through the bridge?',
        'content_vi': 'Một công viên dự định xây một cầu vòm hình parabol. Nhịp vòm dài 40 mét, điểm cao nhất cách mặt nước 10 mét. Lấy mặt nước làm trục $x$, đường thẳng đứng từ điểm cao nhất xuống làm trục $y$. (1) Tìm phương trình parabol của vòm cầu; (2) Nếu cột buồm của thuyền cao 8 mét so với mặt nước, thuyền rộng 6 mét (đối xứng qua trục $y$), thuyền có thể đi qua cầu an toàn không?',
        'options_en': None,
        'options_vi': None,
        'answer_en': '(1)y=10-x²/40 (2)Yes',
        'answer_vi': '(1)y=10-x²/40 (2)Có thể',
        'solution_en': '(1) Let $y=a(x-20)(x+20)$. Substituting the highest point $(0,10)$ gives $a=-\frac{1}{40}$, $y=10-\frac{x^2}{40}$. (2) Boat width 6m centered on y-axis, $x=\pm3$ gives $y=10-\frac{9}{40}=9.775>8$, so it can pass safely.',
        'solution_vi': '(1) Đặt $y=a(x-20)(x+20)$. Thay điểm cao nhất $(0,10)$ được $a=-\frac{1}{40}$, $y=10-\frac{x^2}{40}$. (2) Thuyền rộng 6m đối xứng qua trục y, $x=\pm3$ cho $y=10-\frac{9}{40}=9,775>8$, có thể đi qua an toàn.',
    },

    # --- ID 88 ---
    88: {
        'content_en': 'The value of $\cos 15\degree$ is',
        'content_vi': 'Giá trị của $\cos 15\degree$ là',
        'options_en': ['A. \\frac{\\sqrt{6}+\\sqrt{2}}{4}', 'B. \\frac{\\sqrt{6}-\\sqrt{2}}{4}', 'C. \\frac{\\sqrt{3}+1}{2}', 'D. \\frac{\\sqrt{3}-1}{2}'],
        'options_vi': ['A. \\frac{\\sqrt{6}+\\sqrt{2}}{4}', 'B. \\frac{\\sqrt{6}-\\sqrt{2}}{4}', 'C. \\frac{\\sqrt{3}+1}{2}', 'D. \\frac{\\sqrt{3}-1}{2}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\cos 15\degree=\cos(45\degree-30\degree)=\cos 45\degree\cos 30\degree+\sin 45\degree\sin 30\degree=\frac{\sqrt{6}+\sqrt{2}}{4}$',
        'solution_vi': '$\cos 15\degree=\cos(45\degree-30\degree)=\cos 45\degree\cos 30\degree+\sin 45\degree\sin 30\degree=\frac{\sqrt{6}+\sqrt{2}}{4}$',
    },

    # --- ID 89 ---
    89: {
        'content_en': 'Given $\tan\alpha=2$, $\tan\beta=3$, then $\tan(\alpha+\beta)=$ ____',
        'content_vi': 'Cho $\tan\alpha=2$, $\tan\beta=3$, thì $\tan(\alpha+\beta)=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '-1',
        'answer_vi': '-1',
        'solution_en': '$\tan(\alpha+\beta)=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}=\frac{2+3}{1-6}=-1$',
        'solution_vi': '$\tan(\alpha+\beta)=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}=\frac{2+3}{1-6}=-1$',
    },

    # --- ID 90 ---
    90: {
        'content_en': 'Given $\alpha,\beta$ are acute angles, $\cos\alpha=\frac{3}{5}$, $\cos(\alpha+\beta)=-\frac{5}{13}$, then $\cos\beta=$',
        'content_vi': 'Cho $\alpha,\beta$ là góc nhọn, $\cos\alpha=\frac{3}{5}$, $\cos(\alpha+\beta)=-\frac{5}{13}$, thì $\cos\beta=$',
        'options_en': ['A. \\frac{56}{65}', 'B. \\frac{33}{65}', 'C. -\\frac{33}{65}', 'D. \\frac{16}{65}'],
        'options_vi': ['A. \\frac{56}{65}', 'B. \\frac{33}{65}', 'C. -\\frac{33}{65}', 'D. \\frac{16}{65}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\sin\alpha=\frac{4}{5}$, $\sin(\alpha+\beta)=\frac{12}{13}$. $\cos\beta=\cos((\alpha+\beta)-\alpha)=\cos(\alpha+\beta)\cos\alpha+\sin(\alpha+\beta)\sin\alpha=\frac{56}{65}$',
        'solution_vi': '$\sin\alpha=\frac{4}{5}$, $\sin(\alpha+\beta)=\frac{12}{13}$. $\cos\beta=\cos((\alpha+\beta)-\alpha)=\cos(\alpha+\beta)\cos\alpha+\sin(\alpha+\beta)\sin\alpha=\frac{56}{65}$',
    },

    # --- ID 91 ---
    91: {
        'content_en': 'Given $\sin\alpha+\cos\alpha=\frac{1}{5}$, $\alpha\in(0,\pi)$, then $\tan\alpha=$ ____',
        'content_vi': 'Cho $\sin\alpha+\cos\alpha=\frac{1}{5}$, $\alpha\in(0,\pi)$, thì $\tan\alpha=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '-4/3',
        'answer_vi': '-4/3',
        'solution_en': '$\sin\alpha\cos\alpha=-\frac{12}{25}$. From $(\sin\alpha-\cos\alpha)^2=\frac{49}{25}$, $\sin\alpha-\cos\alpha=\frac{7}{5}$. Solving gives $\sin\alpha=\frac{4}{5}$, $\cos\alpha=-\frac{3}{5}$, $\tan\alpha=-\frac{4}{3}$',
        'solution_vi': '$\sin\alpha\cos\alpha=-\frac{12}{25}$. Từ $(\sin\alpha-\cos\alpha)^2=\frac{49}{25}$, $\sin\alpha-\cos\alpha=\frac{7}{5}$. Giải được $\sin\alpha=\frac{4}{5}$, $\cos\alpha=-\frac{3}{5}$, $\tan\alpha=-\frac{4}{3}$',
    },

    # --- ID 92 ---
    92: {
        'content_en': 'Given $\sin\alpha=\frac{\sqrt{5}}{5}$, $\sin\beta=\frac{\sqrt{10}}{10}$, $\alpha$ and $\beta$ are acute angles, then $\alpha+\beta=$',
        'content_vi': 'Cho $\sin\alpha=\frac{\sqrt{5}}{5}$, $\sin\beta=\frac{\sqrt{10}}{10}$, $\alpha$ và $\beta$ là góc nhọn, thì $\alpha+\beta=$',
        'options_en': ['A. \\frac{\\pi}{4}', 'B. \\frac{\\pi}{3}', 'C. \\frac{\\pi}{2}', 'D. \\frac{2\\pi}{3}'],
        'options_vi': ['A. \\frac{\\pi}{4}', 'B. \\frac{\\pi}{3}', 'C. \\frac{\\pi}{2}', 'D. \\frac{2\\pi}{3}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\cos\alpha=\frac{2\sqrt{5}}{5}$, $\cos\beta=\frac{3\sqrt{10}}{10}$. $\cos(\alpha+\beta)=\frac{\sqrt{2}}{2}$, $\alpha+\beta\in(0,\pi)$, $\alpha+\beta=\frac{\pi}{4}$',
        'solution_vi': '$\cos\alpha=\frac{2\sqrt{5}}{5}$, $\cos\beta=\frac{3\sqrt{10}}{10}$. $\cos(\alpha+\beta)=\frac{\sqrt{2}}{2}$, $\alpha+\beta\in(0,\pi)$, $\alpha+\beta=\frac{\pi}{4}$',
    },

    # --- ID 93 ---
    93: {
        'content_en': 'Given $\sin\alpha=\frac{4}{5}$, then $\sin 2\alpha=$ ____',
        'content_vi': 'Cho $\sin\alpha=\frac{4}{5}$, thì $\sin 2\alpha=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '24/25(α≤90°)',
        'answer_vi': '24/25(α≤90°)',
        'solution_en': '$\cos\alpha=\frac{3}{5}$, $\sin 2\alpha=2\sin\alpha\cos\alpha=\frac{24}{25}$',
        'solution_vi': '$\cos\alpha=\frac{3}{5}$, $\sin 2\alpha=2\sin\alpha\cos\alpha=\frac{24}{25}$',
    },

    # --- ID 94 ---
    94: {
        'content_en': 'Given $\tan\alpha=2$, then $\cos 2\alpha=$',
        'content_vi': 'Cho $\tan\alpha=2$, thì $\cos 2\alpha=$',
        'options_en': ['A. -\\frac{3}{5}', 'B. -\\frac{4}{5}', 'C. \\frac{3}{5}', 'D. \\frac{4}{5}'],
        'options_vi': ['A. -\\frac{3}{5}', 'B. -\\frac{4}{5}', 'C. \\frac{3}{5}', 'D. \\frac{4}{5}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\cos 2\alpha=\frac{1-\tan^2\alpha}{1+\tan^2\alpha}=\frac{1-4}{1+4}=-\frac{3}{5}$',
        'solution_vi': '$\cos 2\alpha=\frac{1-\tan^2\alpha}{1+\tan^2\alpha}=\frac{1-4}{1+4}=-\frac{3}{5}$',
    },

    # --- ID 95 ---
    95: {
        'content_en': 'Given $\sin(\frac{\pi}{4}+\alpha)=\frac{3}{5}$, then $\sin 2\alpha=$ ____',
        'content_vi': 'Cho $\sin(\frac{\pi}{4}+\alpha)=\frac{3}{5}$, thì $\sin 2\alpha=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '7/25',
        'answer_vi': '7/25',
        'solution_en': '$\sin(\frac{\pi}{4}+\alpha)=\frac{\sqrt{2}}{2}(\sin\alpha+\cos\alpha)=\frac{3}{5}$, so $\sin\alpha+\cos\alpha=\frac{3\sqrt{2}}{5}$. Squaring gives $1+\sin 2\alpha=\frac{18}{25}$, $\sin 2\alpha=\frac{7}{25}$',
        'solution_vi': '$\sin(\frac{\pi}{4}+\alpha)=\frac{\sqrt{2}}{2}(\sin\alpha+\cos\alpha)=\frac{3}{5}$, suy ra $\sin\alpha+\cos\alpha=\frac{3\sqrt{2}}{5}$. Bình phương được $1+\sin 2\alpha=\frac{18}{25}$, $\sin 2\alpha=\frac{7}{25}$',
    },

    # --- ID 96 ---
    96: {
        'content_en': 'Simplify $\frac{2\tan 15\degree}{1-\tan^2 15\degree}$. Its value is',
        'content_vi': 'Rút gọn $\frac{2\tan 15\degree}{1-\tan^2 15\degree}$. Giá trị của nó là',
        'options_en': ['A. \\frac{\\sqrt{3}}{3}', 'B. \\frac{\\sqrt{3}}{2}', 'C. \\sqrt{3}', 'D. 1'],
        'options_vi': ['A. \\frac{\\sqrt{3}}{3}', 'B. \\frac{\\sqrt{3}}{2}', 'C. \\sqrt{3}', 'D. 1'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\frac{2\tan 15\degree}{1-\tan^2 15\degree}=\tan 30\degree=\frac{\sqrt{3}}{3}$',
        'solution_vi': '$\frac{2\tan 15\degree}{1-\tan^2 15\degree}=\tan 30\degree=\frac{\sqrt{3}}{3}$',
    },

    # --- ID 97 ---
    97: {
        'content_en': 'Given $\cos\alpha=\frac{1}{3}$, then $\cos 2\alpha=$ ____',
        'content_vi': 'Cho $\cos\alpha=\frac{1}{3}$, thì $\cos 2\alpha=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '-7/9',
        'answer_vi': '-7/9',
        'solution_en': '$\cos 2\alpha=2\cos^2\alpha-1=2\times\frac{1}{9}-1=-\frac{7}{9}$',
        'solution_vi': '$\cos 2\alpha=2\cos^2\alpha-1=2\times\frac{1}{9}-1=-\frac{7}{9}$',
    },

    # --- ID 98 ---
    98: {
        'content_en': 'In $\triangle ABC$, $A=30\degree$, $a=2$, $b=2\sqrt{2}$, then $B=$',
        'content_vi': 'Trong $\triangle ABC$, $A=30\degree$, $a=2$, $b=2\sqrt{2}$, thì $B=$',
        'options_en': ['A. 45\degree \\text{ or } 135\degree', 'B. 45\degree', 'C. 60\degree', 'D. 120\degree'],
        'options_vi': ['A. 45\degree \\text{ hoặc } 135\degree', 'B. 45\degree', 'C. 60\degree', 'D. 120\degree'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\frac{a}{\sin A}=\frac{b}{\sin B}$, $\sin B=\frac{2\sqrt{2}\times\frac{1}{2}}{2}=\frac{\sqrt{2}}{2}$, $B=45\degree$ or $135\degree$',
        'solution_vi': '$\frac{a}{\sin A}=\frac{b}{\sin B}$, $\sin B=\frac{2\sqrt{2}\times\frac{1}{2}}{2}=\frac{\sqrt{2}}{2}$, $B=45\degree$ hoặc $135\degree$',
    },

    # --- ID 99 ---
    99: {
        'content_en': 'In $\triangle ABC$, $a=5$, $b=7$, $c=8$, then $\cos C=$ ____',
        'content_vi': 'Trong $\triangle ABC$, $a=5$, $b=7$, $c=8$, thì $\cos C=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '1/5',
        'answer_vi': '1/5',
        'solution_en': '$\cos C=\frac{a^2+b^2-c^2}{2ab}=\frac{25+49-64}{70}=\frac{1}{5}$',
        'solution_vi': '$\cos C=\frac{a^2+b^2-c^2}{2ab}=\frac{25+49-64}{70}=\frac{1}{5}$',
    },

    # --- ID 100 ---
    100: {
        'content_en': 'In $\triangle ABC$, $A=60\degree$, $b=1$, $S_{\triangle ABC}=\sqrt{3}$, then $\frac{a}{\sin A}=$',
        'content_vi': 'Trong $\triangle ABC$, $A=60\degree$, $b=1$, $S_{\triangle ABC}=\sqrt{3}$, thì $\frac{a}{\sin A}=$',
        'options_en': ['A. \\frac{2\\sqrt{39}}{3}', 'B. \\sqrt{13}', 'C. 2\\sqrt{3}', 'D. \\frac{4\\sqrt{3}}{3}'],
        'options_vi': ['A. \\frac{2\\sqrt{39}}{3}', 'B. \\sqrt{13}', 'C. 2\\sqrt{3}', 'D. \\frac{4\\sqrt{3}}{3}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$S=\frac{1}{2}bc\sin A$, $\sqrt{3}=\frac{1}{2}\times1\times c\times\frac{\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\times1\times4\times\frac{1}{2}=13$, $a=\sqrt{13}$. Circumdiameter $\frac{a}{\sin A}=\frac{2\sqrt{39}}{3}$',
        'solution_vi': '$S=\frac{1}{2}bc\sin A$, $\sqrt{3}=\frac{1}{2}\times1\times c\times\frac{\sqrt{3}}{2}$, $c=4$. $a^2=1+16-2\times1\times4\times\frac{1}{2}=13$, $a=\sqrt{13}$. Đường kính đường tròn ngoại tiếp $\frac{a}{\sin A}=\frac{2\sqrt{39}}{3}$',
    },

    # --- ID 101 ---
    101: {
        'content_en': 'In $\triangle ABC$, $A:B:C=1:2:3$, then $a:b:c=$ ____',
        'content_vi': 'Trong $\triangle ABC$, $A:B:C=1:2:3$, thì $a:b:c=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '1:√3:2',
        'answer_vi': '1:√3:2',
        'solution_en': '$A=30\degree,B=60\degree,C=90\degree$. $a:b:c=\sin 30\degree:\sin 60\degree:\sin 90\degree=1:\sqrt{3}:2$',
        'solution_vi': '$A=30\degree,B=60\degree,C=90\degree$. $a:b:c=\sin 30\degree:\sin 60\degree:\sin 90\degree=1:\sqrt{3}:2$',
    },

    # --- ID 102 ---
    102: {
        'content_en': 'In $\triangle ABC$, if $a\cos B=b\cos A$, then $\triangle ABC$ is',
        'content_vi': 'Trong $\triangle ABC$, nếu $a\cos B=b\cos A$, thì $\triangle ABC$ là',
        'options_en': ['A. Isosceles triangle', 'B. Right triangle', 'C. Equilateral triangle', 'D. Isosceles right triangle'],
        'options_vi': ['A. Tam giác cân', 'B. Tam giác vuông', 'C. Tam giác đều', 'D. Tam giác vuông cân'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': 'By the sine theorem $\sin A\cos B=\sin B\cos A$, so $\sin(A-B)=0$, $A=B$. Hence it is an isosceles triangle.',
        'solution_vi': 'Theo định lý sin $\sin A\cos B=\sin B\cos A$, suy ra $\sin(A-B)=0$, $A=B$. Vậy nó là tam giác cân.',
    },

    # --- ID 103 ---
    103: {
        'content_en': 'In $\triangle ABC$, $a=10$, $A=30\degree$, then the circumradius of $\triangle ABC$ is ____',
        'content_vi': 'Trong $\triangle ABC$, $a=10$, $A=30\degree$, thì bán kính đường tròn ngoại tiếp của $\triangle ABC$ là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '10',
        'answer_vi': '10',
        'solution_en': '$2R=\frac{a}{\sin A}=\frac{10}{0.5}=20$, $R=10$',
        'solution_vi': '$2R=\frac{a}{\sin A}=\frac{10}{0,5}=20$, $R=10$',
    },

    # --- ID 104 ---
    104: {
        'content_en': 'In $\triangle ABC$, angles $A,B,C$ form an arithmetic sequence, and $b=2$, then the range of $a+c$ is',
        'content_vi': 'Trong $\triangle ABC$, các góc $A,B,C$ tạo thành cấp số cộng, và $b=2$, thì khoảng giá trị của $a+c$ là',
        'options_en': ['A. (2,4]', 'B. (2,2\\sqrt{3}]', 'C. [2,4)', 'D. (2\\sqrt{3},4]'],
        'options_vi': ['A. (2,4]', 'B. (2,2\\sqrt{3}]', 'C. [2,4)', 'D. (2\\sqrt{3},4]'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$A+C=2B$, $A+B+C=\pi$, $B=\frac{\pi}{3}$. By cosine theorem $b^2=a^2+c^2-ac=4$. $(a+c)^2=a^2+c^2+2ac=4+3ac\le4+3\times(\frac{a+c}{2})^2$, solving gives $a+c\le4$. $a+c>b=2$, hence $(2,4]$',
        'solution_vi': '$A+C=2B$, $A+B+C=\pi$, $B=\frac{\pi}{3}$. Theo định lý cosin $b^2=a^2+c^2-ac=4$. $(a+c)^2=a^2+c^2+2ac=4+3ac\le4+3\times(\frac{a+c}{2})^2$, giải được $a+c\le4$. $a+c>b=2$, vậy $(2,4]$',
    },

    # --- ID 105 ---
    105: {
        'content_en': 'In $\triangle ABC$, $a=2$, $c=2\sqrt{3}$, $C=120\degree$, then $b=$ ____',
        'content_vi': 'Trong $\triangle ABC$, $a=2$, $c=2\sqrt{3}$, $C=120\degree$, thì $b=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '2',
        'answer_vi': '2',
        'solution_en': '$\cos C=\frac{a^2+b^2-c^2}{2ab}=-\frac{1}{2}$. $\frac{4+b^2-12}{4b}=-\frac{1}{2}$, $b^2+2b-8=0$, $b=2$',
        'solution_vi': '$\cos C=\frac{a^2+b^2-c^2}{2ab}=-\frac{1}{2}$. $\frac{4+b^2-12}{4b}=-\frac{1}{2}$, $b^2+2b-8=0$, $b=2$',
    },

    # --- ID 106 ---
    106: {
        'content_en': 'In $\triangle ABC$, $a=2b\sin A$, then $B$ equals',
        'content_vi': 'Trong $\triangle ABC$, $a=2b\sin A$, thì $B$ bằng',
        'options_en': ['A. 30\degree \\text{ or } 150\degree', 'B. 60\degree \\text{ or } 120\degree', 'C. 30\degree', 'D. 60\degree'],
        'options_vi': ['A. 30\degree \\text{ hoặc } 150\degree', 'B. 60\degree \\text{ hoặc } 120\degree', 'C. 30\degree', 'D. 60\degree'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': 'By the sine theorem $\sin A=2\sin B\sin A$, $\sin B=\frac{1}{2}$, $B=30\degree$ or $150\degree$',
        'solution_vi': 'Theo định lý sin $\sin A=2\sin B\sin A$, $\sin B=\frac{1}{2}$, $B=30\degree$ hoặc $150\degree$',
    },

    # --- ID 107 ---
    107: {
        'content_en': 'In $\triangle ABC$, the sides opposite angles $A,B,C$ are $a,b,c$ respectively. Given $a=2$, $c=\sqrt{3}+1$, $B=60\degree$. (1) Find $b$; (2) Find the area of $\triangle ABC$.',
        'content_vi': 'Trong $\triangle ABC$, các cạnh đối diện với góc $A,B,C$ lần lượt là $a,b,c$. Biết $a=2$, $c=\sqrt{3}+1$, $B=60\degree$. (1) Tìm $b$; (2) Tính diện tích $\triangle ABC$.',
        'options_en': None,
        'options_vi': None,
        'answer_en': 'b=√6, S=(3+√3)/2',
        'answer_vi': 'b=√6, S=(3+√3)/2',
        'solution_en': '(1) $b^2=a^2+c^2-2ac\cos B=4+(4+2\sqrt{3})-4(\sqrt{3}+1)\times\frac{1}{2}=6$, $b=\sqrt{6}$. (2) $S=\frac{1}{2}ac\sin B=\frac{1}{2}\times2\times(\sqrt{3}+1)\times\frac{\sqrt{3}}{2}=\frac{3+\sqrt{3}}{2}$',
        'solution_vi': '(1) $b^2=a^2+c^2-2ac\cos B=4+(4+2\sqrt{3})-4(\sqrt{3}+1)\times\frac{1}{2}=6$, $b=\sqrt{6}$. (2) $S=\frac{1}{2}ac\sin B=\frac{1}{2}\times2\times(\sqrt{3}+1)\times\frac{\sqrt{3}}{2}=\frac{3+\sqrt{3}}{2}$',
    },

    # --- ID 108 ---
    108: {
        'content_en': 'In the arithmetic sequence $\{a_n\}$, $a_1=2$, $a_3=6$, then the common difference $d=$',
        'content_vi': 'Trong cấp số cộng $\{a_n\}$, $a_1=2$, $a_3=6$, thì công sai $d=$',
        'options_en': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
        'options_vi': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
        'answer_en': 'B',
        'answer_vi': 'B',
        'solution_en': '$a_3=a_1+2d$, $6=2+2d$, $d=2$',
        'solution_vi': '$a_3=a_1+2d$, $6=2+2d$, $d=2$',
    },

    # --- ID 109 ---
    109: {
        'content_en': 'In the geometric sequence $\{a_n\}$, $a_1=3$, common ratio $q=2$, then $a_4=$ ____',
        'content_vi': 'Trong cấp số nhân $\{a_n\}$, $a_1=3$, công bội $q=2$, thì $a_4=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '24',
        'answer_vi': '24',
        'solution_en': '$a_4=a_1q^3=3\times8=24$',
        'solution_vi': '$a_4=a_1q^3=3\times8=24$',
    },

    # --- ID 110 ---
    110: {
        'content_en': 'Let $S_n$ be the sum of the first $n$ terms of the arithmetic sequence $\{a_n\}$. If $a_4+a_5=24$, $S_6=48$, then the common difference $d$ is',
        'content_vi': 'Gọi $S_n$ là tổng $n$ số hạng đầu của cấp số cộng $\{a_n\}$. Nếu $a_4+a_5=24$, $S_6=48$, thì công sai $d$ là',
        'options_en': ['A. 2', 'B. 3', 'C. 4', 'D. 6'],
        'options_vi': ['A. 2', 'B. 3', 'C. 4', 'D. 6'],
        'answer_en': 'C',
        'answer_vi': 'C',
        'solution_en': 'From $a_4+a_5=2a_1+7d=24$, $S_6=6a_1+15d=48$. Solving gives $d=4$',
        'solution_vi': 'Từ $a_4+a_5=2a_1+7d=24$, $S_6=6a_1+15d=48$. Giải được $d=4$',
    },

    # --- ID 111 ---
    111: {
        'content_en': 'All terms of the geometric sequence $\{a_n\}$ are positive, and $a_5a_6=9$, then $\log_3 a_1+\log_3 a_2+\cdots+\log_3 a_{10}=$ ____',
        'content_vi': 'Tất cả các số hạng của cấp số nhân $\{a_n\}$ đều dương, và $a_5a_6=9$, thì $\log_3 a_1+\log_3 a_2+\cdots+\log_3 a_{10}=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '10',
        'answer_vi': '10',
        'solution_en': 'Since $a_1a_{10}=a_2a_9=...=a_5a_6=9$. Original expression $=\log_3(a_1a_2...a_{10})=\log_3(9^5)=5\log_3 9=10$',
        'solution_vi': 'Vì $a_1a_{10}=a_2a_9=...=a_5a_6=9$. Biểu thức $=\log_3(a_1a_2...a_{10})=\log_3(9^5)=5\log_3 9=10$',
    },

    # --- ID 112 ---
    112: {
        'content_en': 'The sum of the first $n$ terms of sequence $\{a_n\}$ is $S_n=\frac{n}{n+1}$, then $a_n=$',
        'content_vi': 'Tổng $n$ số hạng đầu của dãy số $\{a_n\}$ là $S_n=\frac{n}{n+1}$, thì $a_n=$',
        'options_en': ['A. \\frac{1}{n(n+1)}', 'B. \\frac{1}{n(n-1)}', 'C. \\frac{2}{n(n+1)}', 'D. \\frac{1}{n^2-1}'],
        'options_vi': ['A. \\frac{1}{n(n+1)}', 'B. \\frac{1}{n(n-1)}', 'C. \\frac{2}{n(n+1)}', 'D. \\frac{1}{n^2-1}'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$a_n=S_n-S_{n-1}=\frac{n}{n+1}-\frac{n-1}{n}=\frac{1}{n(n+1)}$',
        'solution_vi': '$a_n=S_n-S_{n-1}=\frac{n}{n+1}-\frac{n-1}{n}=\frac{1}{n(n+1)}$',
    },

    # --- ID 113 ---
    113: {
        'content_en': 'In the arithmetic sequence $\{a_n\}$, $a_1=1$, $a_n=3n-2$, then $a_{10}=$ ____',
        'content_vi': 'Trong cấp số cộng $\{a_n\}$, $a_1=1$, $a_n=3n-2$, thì $a_{10}=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '28',
        'answer_vi': '28',
        'solution_en': '$a_{10}=3\times10-2=28$',
        'solution_vi': '$a_{10}=3\times10-2=28$',
    },

    # --- ID 114 ---
    114: {
        'content_en': 'The sum of the first $n$ terms of the sequence $\{n\cdot 2^n\}$ is $S_n=$',
        'content_vi': 'Tổng $n$ số hạng đầu của dãy $\{n\cdot 2^n\}$ là $S_n=$',
        'options_en': ['A. (n-1)2^{n+1}+2', 'B. n2^{n+1}+2', 'C. (n-2)2^{n}+2', 'D. n2^{n}-2^{n}+2'],
        'options_vi': ['A. (n-1)2^{n+1}+2', 'B. n2^{n+1}+2', 'C. (n-2)2^{n}+2', 'D. n2^{n}-2^{n}+2'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$S_n=1\cdot2+2\cdot4+...+n\cdot2^n$. Multiply by 2 and subtract: $S_n=(n-1)2^{n+1}+2$',
        'solution_vi': '$S_n=1\cdot2+2\cdot4+...+n\cdot2^n$. Nhân với 2 rồi trừ: $S_n=(n-1)2^{n+1}+2$',
    },

    # --- ID 115 ---
    115: {
        'content_en': 'In the geometric sequence $\{a_n\}$, $a_1+a_2=3$, $a_3+a_4=12$, then the common ratio $q=$ ____',
        'content_vi': 'Trong cấp số nhân $\{a_n\}$, $a_1+a_2=3$, $a_3+a_4=12$, thì công bội $q=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '±2',
        'answer_vi': '±2',
        'solution_en': '$a_3+a_4=q^2(a_1+a_2)$, $12=3q^2$, $q=\pm 2$',
        'solution_vi': '$a_3+a_4=q^2(a_1+a_2)$, $12=3q^2$, $q=\pm 2$',
    },

    # --- ID 116 ---
    116: {
        'content_en': 'In the arithmetic sequence $\{a_n\}$, $a_2+a_8=10$, then $a_5=$',
        'content_vi': 'Trong cấp số cộng $\{a_n\}$, $a_2+a_8=10$, thì $a_5=$',
        'options_en': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
        'options_vi': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
        'answer_en': 'C',
        'answer_vi': 'C',
        'solution_en': '$a_2+a_8=2a_5=10$, $a_5=5$',
        'solution_vi': '$a_2+a_8=2a_5=10$, $a_5=5$',
    },

    # --- ID 117 ---
    117: {
        'content_en': 'The sum of the first $n$ terms of the sequence $\{\frac{1}{n(n+1)}\}$ is ____',
        'content_vi': 'Tổng $n$ số hạng đầu của dãy $\{\frac{1}{n(n+1)}\}$ là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': 'n/(n+1)',
        'answer_vi': 'n/(n+1)',
        'solution_en': '$\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$. $S_n=1-\frac{1}{n+1}=\frac{n}{n+1}$',
        'solution_vi': '$\frac{1}{n(n+1)}=\frac{1}{n}-\frac{1}{n+1}$. $S_n=1-\frac{1}{n+1}=\frac{n}{n+1}$',
    },

    # --- ID 118 ---
    118: {
        'content_en': 'In the geometric sequence $\{a_n\}$, $a_2=2$, $a_5=\frac{1}{4}$, then the common ratio $q=$',
        'content_vi': 'Trong cấp số nhân $\{a_n\}$, $a_2=2$, $a_5=\frac{1}{4}$, thì công bội $q=$',
        'options_en': ['A. -\\frac{1}{2}', 'B. \\frac{1}{2}', 'C. -2', 'D. 2'],
        'options_vi': ['A. -\\frac{1}{2}', 'B. \\frac{1}{2}', 'C. -2', 'D. 2'],
        'answer_en': 'B',
        'answer_vi': 'B',
        'solution_en': '$a_5=a_2q^3$, $\frac{1}{4}=2q^3$, $q^3=\frac{1}{8}$, $q=\frac{1}{2}$',
        'solution_vi': '$a_5=a_2q^3$, $\frac{1}{4}=2q^3$, $q^3=\frac{1}{8}$, $q=\frac{1}{2}$',
    },

    # --- ID 119 ---
    119: {
        'content_en': '$1+3+5+\cdots+(2n-1)=$ ____',
        'content_vi': '$1+3+5+\cdots+(2n-1)=$ ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': 'n²',
        'answer_vi': 'n²',
        'solution_en': 'Arithmetic series sum: $\frac{n(1+(2n-1))}{2}=n^2$',
        'solution_vi': 'Tổng cấp số cộng: $\frac{n(1+(2n-1))}{2}=n^2$',
    },

    # --- ID 120 ---
    120: {
        'content_en': 'Choose 3 books from 5 different books to give to 3 students, one book each. The number of different ways to give the books is',
        'content_vi': 'Chọn 3 cuốn sách từ 5 cuốn sách khác nhau để tặng cho 3 học sinh, mỗi người một cuốn. Số cách tặng khác nhau là',
        'options_en': ['A. 10 ways', 'B. 60 ways', 'C. 120 ways', 'D. 20 ways'],
        'options_vi': ['A. 10 cách', 'B. 60 cách', 'C. 120 cách', 'D. 20 cách'],
        'answer_en': 'B',
        'answer_vi': 'B',
        'solution_en': '$A_5^3=5\times4\times3=60$',
        'solution_vi': '$A_5^3=5\times4\times3=60$',
    },

    # --- ID 121 ---
    121: {
        'content_en': 'In the expansion of $(1+x)^{5}$, the coefficient of $x^2$ is ____',
        'content_vi': 'Trong khai triển của $(1+x)^{5}$, hệ số của $x^2$ là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '10',
        'answer_vi': '10',
        'solution_en': '$C_5^2=10$',
        'solution_vi': '$C_5^2=10$',
    },

    # --- ID 122 ---
    122: {
        'content_en': 'When rolling a fair die twice, the probability that the sum of the two outcomes is 7 is',
        'content_vi': 'Khi gieo một con xúc xắc cân đối hai lần, xác suất tổng hai mặt xuất hiện bằng 7 là',
        'options_en': ['A. \\frac{1}{12}', 'B. \\frac{1}{6}', 'C. \\frac{1}{5}', 'D. \\frac{1}{4}'],
        'options_vi': ['A. \\frac{1}{12}', 'B. \\frac{1}{6}', 'C. \\frac{1}{5}', 'D. \\frac{1}{4}'],
        'answer_en': 'B',
        'answer_vi': 'B',
        'solution_en': 'Combinations with sum=7: $(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)$ total 6. Total outcomes $6\times6=36$. $P=\frac{6}{36}=\frac{1}{6}$',
        'solution_vi': 'Các tổng bằng 7: $(1,6)(2,5)(3,4)(4,3)(5,2)(6,1)$ có 6. Tổng kết quả $6\times6=36$. $P=\frac{6}{36}=\frac{1}{6}$',
    },

    # --- ID 123 ---
    123: {
        'content_en': 'The constant term in the expansion of $(2x-\frac{1}{x})^6$ is ____ (answer with a number)',
        'content_vi': 'Số hạng không đổi trong khai triển của $(2x-\frac{1}{x})^6$ là ____ (trả lời bằng số)',
        'options_en': None,
        'options_vi': None,
        'answer_en': '-160',
        'answer_vi': '-160',
        'solution_en': 'General term $T_{r+1}=C_6^r(2x)^{6-r}(-\frac{1}{x})^r=C_6^r2^{6-r}(-1)^r x^{6-2r}$. Set $6-2r=0$, $r=3$. Constant term $=C_6^3\times2^3\times(-1)^3=20\times8\times(-1)=-160$',
        'solution_vi': 'Số hạng tổng quát $T_{r+1}=C_6^r(2x)^{6-r}(-\frac{1}{x})^r=C_6^r2^{6-r}(-1)^r x^{6-2r}$. Cho $6-2r=0$, $r=3$. Số hạng không đổi $=C_6^3\times2^3\times(-1)^3=20\times8\times(-1)=-160$',
    },

    # --- ID 124 ---
    124: {
        'content_en': 'Using the digits 0,1,2,3,4, the number of 5-digit numbers greater than 20000 without repeating digits is',
        'content_vi': 'Dùng các chữ số 0,1,2,3,4, số lượng số có 5 chữ số lớn hơn 20000 không lặp chữ số là',
        'options_en': ['A. 96', 'B. 72', 'C. 48', 'D. 120'],
        'options_vi': ['A. 96', 'B. 72', 'C. 48', 'D. 120'],
        'answer_en': 'B',
        'answer_vi': 'B',
        'solution_en': 'The ten-thousands digit can be 2,3,4 (3 choices); the remaining 4 digits are permuted: $4!=24$. Total $3\times24=72$',
        'solution_vi': 'Chữ số hàng vạn có thể là 2,3,4 (3 cách); 4 chữ số còn lại hoán vị: $4!=24$. Tổng $3\times24=72$',
    },

    # --- ID 125 ---
    125: {
        'content_en': 'Choose 2 different numbers from {1,2,3,4}. The probability that the absolute difference of the two chosen numbers is 2 is ____',
        'content_vi': 'Chọn 2 số khác nhau từ {1,2,3,4}. Xác suất hiệu tuyệt đối của hai số được chọn bằng 2 là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '1/3',
        'answer_vi': '1/3',
        'solution_en': 'Total $C_4^2=6$. Pairs with difference 2: $(1,3)(2,4)$ total 2. $P=\frac{2}{6}=\frac{1}{3}$',
        'solution_vi': 'Tổng $C_4^2=6$. Các cặp có hiệu bằng 2: $(1,3)(2,4)$ có 2. $P=\frac{2}{6}=\frac{1}{3}$',
    },

    # --- ID 126 ---
    126: {
        'content_en': 'Assign 4 students to 3 different extracurricular groups, with each group getting at least 1 student. The number of different assignment plans is',
        'content_vi': 'Phân công 4 học sinh vào 3 nhóm ngoại khóa khác nhau, mỗi nhóm có ít nhất 1 học sinh. Số cách phân công khác nhau là',
        'options_en': ['A. 36 ways', 'B. 24 ways', 'C. 72 ways', 'D. 12 ways'],
        'options_vi': ['A. 36 cách', 'B. 24 cách', 'C. 72 cách', 'D. 12 cách'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$C_4^2\times3!=6\times6=36$',
        'solution_vi': '$C_4^2\times3!=6\times6=36$',
    },

    # --- ID 127 ---
    127: {
        'content_en': 'A bag contains 3 red balls and 2 white balls. Two balls are randomly drawn. The expected value $E(X)$ of the number of red balls $X$ drawn is ____',
        'content_vi': 'Một túi có 3 bi đỏ và 2 bi trắng. Lấy ngẫu nhiên 2 bi. Kỳ vọng $E(X)$ của số bi đỏ $X$ lấy được là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '6/5',
        'answer_vi': '6/5',
        'solution_en': '$P(X=0)=\frac{C_2^2}{C_5^2}=\frac{1}{10}$, $P(X=1)=\frac{C_3^1C_2^1}{C_5^2}=\frac{6}{10}$, $P(X=2)=\frac{C_3^2}{C_5^2}=\frac{3}{10}$. $E(X)=0+1\times0.6+2\times0.3=1.2=\frac{6}{5}$',
        'solution_vi': '$P(X=0)=\frac{C_2^2}{C_5^2}=\frac{1}{10}$, $P(X=1)=\frac{C_3^1C_2^1}{C_5^2}=\frac{6}{10}$, $P(X=2)=\frac{C_3^2}{C_5^2}=\frac{3}{10}$. $E(X)=0+1\times0,6+2\times0,3=1,2=\frac{6}{5}$',
    },

    # --- ID 128 ---
    128: {
        'content_en': 'In the expansion of $(x+2)^4$, the coefficient of $x^2$ is',
        'content_vi': 'Trong khai triển của $(x+2)^4$, hệ số của $x^2$ là',
        'options_en': ['A. 6', 'B. 12', 'C. 24', 'D. 48'],
        'options_vi': ['A. 6', 'B. 12', 'C. 24', 'D. 48'],
        'answer_en': 'C',
        'answer_vi': 'C',
        'solution_en': '$C_4^2\times2^2=6\times4=24$',
        'solution_vi': '$C_4^2\times2^2=6\times4=24$',
    },

    # --- ID 129 ---
    129: {
        'content_en': 'Two people A and B shoot baskets. Their hit rates are 0.7 and 0.6 respectively. Each takes one shot. The probability that at least one of them hits is ____',
        'content_vi': 'Hai người A và B ném bóng rổ. Tỷ lệ ném trúng lần lượt là 0,7 và 0,6. Mỗi người ném một lần. Xác suất có ít nhất một người ném trúng là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '0.88',
        'answer_vi': '0,88',
        'solution_en': '$P=1-P(\text{both miss})=1-0.3\times0.4=0.88$',
        'solution_vi': '$P=1-P(\text{cả hai đều trượt})=1-0,3\times0,4=0,88$',
    },

    # --- ID 130 ---
    130: {
        'content_en': '6 chairs are arranged in a row. 3 people randomly sit down. The number of seating arrangements where no two people are adjacent is',
        'content_vi': '6 chiếc ghế xếp thành một hàng. 3 người ngồi ngẫu nhiên. Số cách sắp xếp chỗ ngồi sao cho không có hai người nào ngồi cạnh nhau là',
        'options_en': ['A. 120', 'B. 96', 'C. 72', 'D. 24'],
        'options_vi': ['A. 120', 'B. 96', 'C. 72', 'D. 24'],
        'answer_en': 'D',
        'answer_vi': 'D',
        'solution_en': 'Place 3 empty chairs first, creating 4 gaps (including ends). Choose 3 gaps to seat the people: $A_4^3=24$',
        'solution_vi': 'Xếp trước 3 ghế trống, tạo ra 4 khoảng trống (kể cả hai đầu). Chọn 3 khoảng trống để xếp người: $A_4^3=24$',
    },

    # --- ID 131 ---
    131: {
        'content_en': 'Toss two fair coins simultaneously. The probability of getting exactly one head is ____',
        'content_vi': 'Tung đồng thời hai đồng xu cân đối. Xác suất có đúng một mặt ngửa là ____',
        'options_en': None,
        'options_vi': None,
        'answer_en': '1/2',
        'answer_vi': '1/2',
        'solution_en': 'Sample space: {HH, HT, TH, TT}. Exactly one head: {HT, TH}. $P=\frac{2}{4}=\frac{1}{2}$',
        'solution_vi': 'Không gian mẫu: {HH, HT, TH, TT}. Đúng một mặt ngửa: {HT, TH}. $P=\frac{2}{4}=\frac{1}{2}$',
    },

    # --- ID 132 ---
    132: {
        'content_en': 'Given vectors $\vec{a}=(1,0,-1)$, $\vec{b}=(-1,1,0)$, then $\vec{a}\cdot\vec{b}=$',
        'content_vi': 'Cho vectơ $\vec{a}=(1,0,-1)$, $\vec{b}=(-1,1,0)$, thì $\vec{a}\cdot\vec{b}=$',
        'options_en': ['A. -1', 'B. 0', 'C. 1', 'D. 2'],
        'options_vi': ['A. -1', 'B. 0', 'C. 1', 'D. 2'],
        'answer_en': 'A',
        'answer_vi': 'A',
        'solution_en': '$\vec{a}\cdot\vec{b}=1\times(-1)+0\times1+(-1)\times0=-1$',
        'solution_vi': '$\vec{a}\cdot\vec{b}=1\times(-1)+0\times1+(-1)\times0=-1$',
    },
}


def update_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch all questions we're going to translate to verify they exist
    ids = list(translations.keys())
    placeholders = ','.join('?' for _ in ids)
    cursor.execute(f'SELECT id FROM questions WHERE id IN ({placeholders})', ids)
    existing_ids = {row[0] for row in cursor.fetchall()}

    for qid in ids:
        if qid not in existing_ids:
            print(f'WARNING: Question ID {qid} not found in database, skipping.')
            continue

        t = translations[qid]

        # Helper: serialize options list to JSON string, or None
        def to_json(val):
            if val is None:
                return None
            return json.dumps(val, ensure_ascii=False)

        cursor.execute('''
            UPDATE questions SET
                content_en = ?,
                content_vi = ?,
                options_en = ?,
                options_vi = ?,
                answer_en = ?,
                answer_vi = ?,
                solution_en = ?,
                solution_vi = ?
            WHERE id = ?
        ''', (
            t['content_en'],
            t['content_vi'],
            to_json(t['options_en']),
            to_json(t['options_vi']),
            t['answer_en'],
            t['answer_vi'],
            t['solution_en'],
            t['solution_vi'],
            qid
        ))
        print(f'Updated question ID {qid}')

    conn.commit()
    conn.close()
    print(f'\nAll {len(existing_ids & set(ids))} questions updated successfully.')


if __name__ == '__main__':
    update_database()
