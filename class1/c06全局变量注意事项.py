gl_num = 100


def demo1():
    # 此处只是定义了一个函数内部的局部变量，只是和全局变量的变量名相同，所以不会修改全局变量的值
    num = 50
    print('demo1:', num)


def demo2():
    # 如果想要在函数内部修改全局变量的值
    global gl_num  # 告诉解释器这是个全局变量
    gl_num = 150
    print('demo:', gl_num)


def demo3():
    print('demo3:', gl_num)


# 调用函数
demo1()
demo3()
demo2()

# 注意：全局变量的定义位置一定要在所有函数定义之前，原因：代码是从上向下执行的.