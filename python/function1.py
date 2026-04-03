#1.定义一个函数：根据传入的低和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）
def triangle_area(base, height):
    area = (base * height) / 2
    return area
#2.定义一个函数：计算传入的字符串中元音字母的个数（元音字母为：aeiou）
def vowel_letters_count(letters):
    count = 0
    letters = letters.lower()
    for letter in letters:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u':
            count += 1
    return count
#3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
def stu_scores(score_list):
    score_max = max(score_list)
    score_min = min(score_list)
    score_avg = round(sum(score_list) / len(score_list), 1)
    return score_max, score_min, score_avg

score_list = [432, 546, 765, 242, 241, 567]


print(triangle_area(5, 4))
print(vowel_letters_count("Ambgous"))
print(stu_scores(score_list))
