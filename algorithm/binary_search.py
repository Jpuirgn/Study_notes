def binary_search_recuresion(my_list, target):
    n = len(my_list)
    if n == 0:
        return False
    mid = n//2
    if target == my_list[mid]:
        return True
    elif target < my_list[mid]:
        return binary_search_recuresion(my_list[:mid], target)
    else:
        return binary_search_recuresion(my_list[mid + 1:], target)

    return False


def binary_search(my_list, target):
    start = 0
    end = len(my_list) - 1
    n = len(my_list)
    while start <= end:
        if n == 0:
            return False
        mid = (start + end) // 2
        if target == my_list[mid]:
            return True
        elif target < my_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

my_list = [12, 23, 34, 51, 76, 83, 91]
print(binary_search_recuresion(my_list, 23))
print(binary_search_recuresion(my_list, 12))
print(binary_search_recuresion(my_list, 24))
print("-" * 20)
print(binary_search(my_list, 23))
print(binary_search(my_list, 12))
print(binary_search(my_list, 24))