def select_sort(my_list):
    n = len(my_list)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

if __name__ == '__main__':
    my_list = [1, 3, 5, 2, 4]
    select_sort(my_list)
    print(my_list)