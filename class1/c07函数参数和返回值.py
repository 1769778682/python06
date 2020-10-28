# 定义函数的形式
def demo1():
    """无参数，无返回值"""
    print('函数demo1')


def demo2():
    """无参数，有返回值"""
    result = 100
    return result


def demo3(num):
    """有参数，无返回值"""
    print(num)


def demo4(num):
    """有参数，有返回值"""
    print(num)
    result = 100
    return result

# 结论：如果需要从外部给函数内部传递数据，那么就需要定义函数添加参数
# 如果需要获取函数内部的运算结果，在外部继续使用，则需要添加返回值
demo1()
demo2()
demo3(9)
demo4(8)