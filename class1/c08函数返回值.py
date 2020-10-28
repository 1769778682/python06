# 定义一个计算函数
def calc(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d  # 元组数据使用时小括号可以省略


# 调用函数
result1 = calc(10, 10)
print(result1)
num_a, num_b, num_c, num_d = calc(10, 10)
print(num_a)
print(num_a, num_b, num_c, num_d)
