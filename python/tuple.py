#语数英
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周铁", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69 ,82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

#1.计算每个学生的总分、各科平均分、然后一并输出出来
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"姓名:{s[1]}\t\t总分:{total}\t\t平均分:{avg:.1f}")

print()
#2.统计各科成绩的最低分、最高分、平均分、并输出
chinese_score = [s[2] for s in students]
math_score = [s[3] for s in students]
english_score = [s[4] for s in students]

print(f"语文最低分:{min(chinese_score)}\t语文最高分:{max(chinese_score)}\t语文平均分:{sum(chinese_score) / len(chinese_score)}")
print(f"数学最低分:{min(math_score)}\t数学最高分:{max(math_score)}\t数学平均分:{sum(math_score) / len(math_score)}")
print(f"英语最低分:{min(english_score)}\t英语最高分:{max(english_score)}\t英语平均分:{sum(english_score) / len(english_score)}")

print()
#3.查找成绩优秀(平均分大于90分)的学生，并输出

print("优秀学生: ")
for idc, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"{idc}\t{name}\t{chinese}\t{math}\t{english}")