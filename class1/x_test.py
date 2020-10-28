def demo(num, num_list):
    print("*" * 30)

    num += num
    num_list += num_list
    # 当列表数据使用 += 时，等价于 列表.extend() 方法
    print(num)
    print(num_list)
    print("*" * 30)


num1 = 10
num_list1 = [4, 5, 6]
# 函数调用
demo(num1, num_list1)
print(num1)
print(num_list1)