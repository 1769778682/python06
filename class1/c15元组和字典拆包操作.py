def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 调用函数
tuple1 = 1, 2, 3, 4, 5
dict1 = {'name': '刘备', 'age': 45}
# demo(tuple1, dict1)
demo(*tuple1, **dict1)  # 利用拆包传值


# 拆包
# 给形参增加 * 或 ** , 是定义多值参数
# 给实参增加 * 或 ** , 这是拆包操作
# 在自动化阶段可能会遇到以下使用方式, 将元组数据拆分成具体的数据值
num = (100, 200)
print(*num)  # *num : 拆包的应用