#定义一个函数，根据传入的分数，计算对应的分数等级并返回
#   分数 >= 90 A
#       >= 75 B
#       >= 60 C
#        < 60 D


def score_level(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score < 60:
        return "D"
    return None

print(score_level(92))

#2.定义一个函数，用于判断一个字符串是否是回文，返回bool值

def string_judge(string):
    if string == string[::-1]:
        return True
    else:
        return False

#3.定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒
def time_trans(seconds):
    hours = seconds // 3600
    remaining = seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return hours, minutes, seconds
print(time_trans(3610))

#4.定义一个函数，根据传入的三角形三个边的边长，判定三角形的类型
def triangle_judge(len1, len2, len3):
    if len1 + len2 <= len3 or len1 + len3 <= len2 or len2 + len3 <= len1:
        return "It is not a triangle"
    elif len1 == len2 == len3:
        return "It is a equilateral triangle"
    elif len1 == len2 or len2 == len3 or len3 == len1:
        return "It is an isosceles triangle"
    else:
        return "It is a triangle"

print(triangle_judge(5, 5, 5))
print(triangle_judge(5, 5, 3))
print(triangle_judge(5, 1, 2))