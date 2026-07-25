"""Idempotent seed data. Safe to run multiple times — uses INSERT OR IGNORE."""
import sqlite3
import json
from database import get_db

MODULES = [
    (1, "三角函数与解三角形", 15, 1, 1, "📐", "和差角公式、二倍角公式、正弦定理、余弦定理"),
    (2, "数列", 12, 1, 2, "🔢", "等差/等比数列通项与求和、裂项相消、错位相减"),
    (3, "统计与概率", 17, 1, 3, "🎲", "排列组合、二项式定理、分布列与期望"),
    (4, "立体几何", 17, 2, 4, "📦", "空间向量法：建系→法向量→角与距离"),
    (5, "解析几何", 17, 2, 5, "📈", "椭圆/双曲线/抛物线、联立+韦达定理"),
    (6, "导数及其应用", 17, 2, 6, "📉", "单调性、极值最值、切线问题"),
    (7, "集合与常用逻辑", 5, 3, 7, "🔤", "集合运算、充要条件"),
    (8, "复数与向量", 10, 3, 8, "🧮", "复数运算、向量坐标运算"),
]

CONCEPT_DEPS = [
    ("完全平方公式", None, "必修一 P32"),
    ("一元二次函数图像", "完全平方公式", "必修一 P36"),
    ("一元二次不等式", "一元二次函数图像", "必修一 P40"),
    ("穿根法", "一元二次不等式", "必修一 P42"),
    ("正弦定理", None, "必修五 P2"),
    ("余弦定理", None, "必修五 P6"),
    ("和差角公式", None, "必修四 P25"),
    ("二倍角公式", "和差角公式", "必修四 P30"),
    ("等差数列通项", None, "必修五 P35"),
    ("等比数列通项", None, "必修五 P48"),
    ("裂项相消", "等差数列通项", "必修五 P55"),
    ("错位相减", "等比数列通项", "必修五 P56"),
    ("空间向量坐标运算", None, "选修2-1 P85"),
    ("法向量求法", "空间向量坐标运算", "选修2-1 P90"),
    ("导数定义", None, "选修2-2 P2"),
    ("导数单调性", "导数定义", "选修2-2 P22"),
    ("导数极值最值", "导数单调性", "选修2-2 P28"),
    ("导数切线", "导数定义", "选修2-2 P16"),
    ("椭圆标准方程", None, "选修2-1 P38"),
    ("双曲线标准方程", None, "选修2-1 P50"),
    ("抛物线标准方程", None, "选修2-1 P60"),
]


def seed():
    db = get_db()
    cur = db.cursor()

    # Modules
    cur.executemany(
        "INSERT OR IGNORE INTO modules (id, name, weight, tier, sort_order, icon, description) VALUES (?,?,?,?,?,?,?)",
        MODULES
    )

    # Concept dependencies
    for name, parent, ref in CONCEPT_DEPS:
        cur.execute(
            "INSERT OR IGNORE INTO concept_dependencies (concept_name, parent_concept, textbook_ref) VALUES (?,?,?)",
            (name, parent, ref)
        )

    # Season
    cur.execute(
        "INSERT OR IGNORE INTO seasons (id, name, start_date, end_date, reward_tiers, active) VALUES (1, '第1赛季: 函数觉醒', '2026-07-01', '2026-08-30', '[]', 1)"
    )

    db.commit()
    db.close()
    print("Seed data loaded.")


if __name__ == "__main__":
    from database import init_db
    init_db()
    seed()
