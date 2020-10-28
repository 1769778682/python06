num = 100


def demo1():
    num = 50
    print('demo1:', num)


def demo2():
    print('demo:', num)


# def demo3():
#     print('demo:', num1)


# 调用函数
demo1()
demo2()

# 注意：
# 1.函数在执行时，先查找自己内部是否具有指定名称的局部变量，如果有，直接使用
# 2.如果内部没有局部变量，那就确认外部是否存在全局变量，如果有直接使用
# 3.如果内部外部都没有目标变量，则代码报错