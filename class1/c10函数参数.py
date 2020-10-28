# 问题 1：在函数内部，针对参数使用 赋值语句，会不会影响调用函数时传递的 实参变量？
# def demo(num, num_list):
#     print("*" * 30)
#
#     num = 100
#     num_list = [1, 2, 3]
#     print(num)
#     print(num_list)
#     print("*" * 30)
#
#
# num1 = 10
# num_list1 = [4, 5, 6]
# # 函数调用
# demo(num1, num_list1)
# print(num1)
# print(num_list1)
# 结论：无论传递的参数类型是可变还是不可变的，在函数内部使用赋值语句。
# 只会在函数内部修改局部变量的引用，不会影响到外部变量

# 问题 2：如果传递的参数是 可变类型，
# 在函数内部，使用 方法 修改了数据的内容，
# 同样会影响到外部的数据


def demo1(num_list):
    num_list.extend([1, 2, 3])
    print('内部', num_list)


num_list2 = [4, 5, 6]
demo1(num_list2)
print('外部', num_list2)
