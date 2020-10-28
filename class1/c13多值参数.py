def demo(a, *b):  # 在参数前增加一个*，可以接收元组类型的数据
    # def demo(a, *args):
    print(a)
    print(b)


# 调用函数
demo(1, 2, 3, 4, 5, 6)


def demo(x, **y):  # 在参数前添加一个 ** ，可以接收字典数据
    print(x)  # 1
    print(y)  # {'name': '刘备', 'age': 45}


demo(1, name='刘备', age=45)
