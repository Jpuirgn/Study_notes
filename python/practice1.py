'''
基于现有知识
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
'''

students_dict = {}
#1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中
def add_student():
    name = input("输入学生姓名: ")
    chinese_score = float(input("输入语文成绩: "))
    math_score = float(input("输入数学成绩: "))
    english_score = float(input("输入英语成绩: "))
    if name in students_dict:
        print("该学生已存在!")
        print("=" * 32)
    else:
        students_dict[name] = {"语文: " : chinese_score, "数学: " : math_score, "英语: " : english_score}
    print(f"{name}的信息已录入完成!")
    print("=" * 32)
#2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息
def change_student():
    change_name = input("输入要修改的学生的姓名: ")
    if change_name not in students_dict:
        print(f"{change_name}不在系统名单中!")
        print("=" * 32)
    else:
        change_chinese = float(input("输入新的语文成绩: "))
        change_math = float(input("输入新的数学成绩: "))
        change_english = float(input("输入新的英语成绩: "))
        students_dict[change_name] = {"语文: " : change_chinese, "数学: " : change_math, "英语: " : change_english}
        print(f"{change_name}的成绩已修改完成!")
        print("=" * 32)
#3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息
def delete_student():
    del_name = input("输入要删除的学生姓名: ")
    if del_name not in students_dict:
        print(f"{del_name}不在系统名单中!")
        print("=" * 32)
    else:
        students_dict.pop(del_name)
        print(f"{del_name}的信息已删除！")
        print("=" * 32)
#4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出
def query_student():
    query_name = input("输入要查询的学生姓名: ")
    if query_name not in students_dict:
        print(f"{query_name}不在系统中!")
        print("=" * 32)
    else:
        print(f"{students_dict[query_name]}")
        print("=" * 32)
#5.列出所有学生：遍历所有学生信息并输出
def each_student():
    if not students_dict:
        print("暂无学生信息!")
        print("=" * 32)
    for name, score in students_dict.items():
        print(f"姓名:{name}\t语文:{score['语文: ']}\t数学:{score['数学: ']}\t英语:{score['英语: ']}")
        print("=" * 32)
#6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学生姓名
def statistics():
    all_chinese_score = []
    all_math_score = []
    all_english_score = []

    for name, score in students_dict.items():
        all_chinese_score.append(score["语文: "])
        all_math_score.append(score["数学: "])
        all_english_score.append(score["英语: "])
    if all_chinese_score == [] or all_math_score == [] or all_english_score == []:
        print("语文，数学，英语成绩未补充完整!")
    else:
        print(f"班级语文最高分: {max(all_chinese_score)}, 班级数学最高分: {max(all_math_score)}, 班级英语最高分: {max(all_english_score)}")
        print(f"班级语文最低分: {min(all_chinese_score)}, 班级数学最低分: {min(all_math_score)}, 班级英语最低分: {min(all_english_score)}")
        print(f"语文平均分: {sum(all_chinese_score) / len(all_chinese_score):.1f}, 数学平均分: {sum(all_math_score) / len(all_math_score):.1f}, 英语平均分: {sum(all_english_score) / len(all_english_score):.1f}")


    for name, score in students_dict.items():
        if score["语文: "] == max(all_chinese_score):
            print(f"姓名: {name}, 语文成绩(班级最高): {score['语文: ']:.1f}")
        if score["数学: "] == max(all_math_score):
            print(f"姓名: {name}, 数学成绩(班级最高): {score['数学: ']:.1f}")
        if score["英语: "] == max(all_english_score):
            print(f"姓名: {name}, 英语成绩(班级最高): {score['英语: ']:.1f}")
        if score["语文: "] == min(all_chinese_score):
            print(f"姓名: {name}, 语文成绩(班级最低): {score['语文: ']:.1f}")
        if score["数学: "] == min(all_math_score):
            print(f"姓名: {name}, 数学成绩(班级最低): {score['数学: ']:.1f}")
        if score["英语: "] == min(all_english_score):
            print(f"姓名: {name}, 英语成绩(班级最低): {score['英语: ']:.1f}")


#7.退出系统
def quit_system():
    exit()

running = True
while running:
    print("=" * 32)
    print("     **教务管理系统**")
    print("     1.添加学生信息")
    print("     2.修改学生信息")
    print("     3.删除学生信息")
    print("     4.查询学生信息")
    print("     5.所有学生信息")
    print("     6.班级成绩统计")
    print("     7.退出系统")
    print("=" * 32)
    option = int(input("选择一项功能(1-7): "))
    if option == 1:
        add_student()
    elif option == 2:
        change_student()
    elif option == 3:
        delete_student()
    elif option == 4:
        query_student()
    elif option == 5:
        each_student()
    elif option == 6:
        statistics()
    elif option == 7:
        quit_system()
    else:
        print("输入预期外的值，请重新输入!")
        print("=" * 32)

'''
反思：
1.在用户输入成绩等数字类型时要将其转换为int或float类型
2.&在Python里是位运算，判断条件必须用 and
3.我在第5第6部分中访问各科成绩时，使用了score[index]索引访问的方式，字典不支持索引访问，value需要通过key访问
4.我在statistic函数部分写了 all_chinese_score = all_chinese_score.append(score["语文: "]) 这样的代码，不能写 = append, append是直接修改列表，不需要赋值回去

'''

