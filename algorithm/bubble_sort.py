def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        counter = 0
        for j in range(n - 1 - i):
            if my_list[j] >my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            counter += 1

        if counter == 0:
            break
        print(f"第{i + 1}轮交换了{counter}次")
if __name__ == '__main__':
    my_list = [1, 3, 5, 2, 4, 6]
    bubble_sort(my_list)
    print(my_list)