#1.输入一个字符串，判断该字符串是否是回文
str1 = input("输入一个字符串并判断是非是回文: ")
if str1 == str1[::-1]:
    print("{str1}是回文")
else:
    print("{str1}不是回文")
#2.将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容遍历输出出来
str2 = input("输入10个字符串，将其全部转变为大写")
str3 =[]
str2_upper = str2.upper()
str3.append(str2_upper)
for item in str3:
    print(item)