#定义一个函数，根据传入的数字，计算该数字阶乘的结果
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))