#选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "李飞鱼", "无愁", "紫灵"}
#选修篮球学生名单
basketball_set = {"张铁", "磨具人", "王林", "姜老刀", "曾牛", "王婵", "韩立", "天运子", "梨花园", "李飞鱼", "云麓"}
#选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎跑", "姜老刀", "天运子", "红蝶", "李飞鱼", "韩立", "曾牛"}
#选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎跑", "姜老刀", "紫灵"}

#1.找出同时选修了法语和艺术的学生
s1 = french_set.intersection(art_set)
print(s1)
#2.找出同时选修了所有四门课的学生
s2 = football_set & basketball_set & french_set & art_set
print(s2)
#3.找出选修了足球，但是没有选修篮球的学生
s3 = football_set.difference(basketball_set)
print(s3)

s3 = {s for s in football_set if s not in basketball_set}
print(s3)
#4.统计每一个学生选修的课程数量
all_student = football_set | basketball_set | french_set | art_set
print(all_student)

stu_list = [*football_set, *basketball_set, *french_set, *art_set]
for s in all_student:
    if s in stu_list:
        num = stu_list.count(s)
        print(f"{s}:{num}")




