#合并如下三个列表，并对合并后的列表进行元素的去重，排好序(升序)后输出
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
#solution:
new_list1 = list1 + list2 + list3
new_list2 =[]
for item in new_list1:
    if item not in new_list2:
        new_list2.append(item)

print(new_list1)
print(new_list2)

#将如下列表中能被3或5整除的元素提出来，并获取这些数字对应的平方，组成一个新列表
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#solution:
new_list3 = [i**2 for i in list4 if i % 3 == 0 or i % 5 == 0]
print(new_list3)



#将如下列表中的正数提取出来，封装为一个新列表
list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
#solution:
new_list4 = [i for i in list5 if i >0]
print(new_list4)