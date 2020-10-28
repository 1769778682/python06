def test(num):
    print(f'参数在函数内部的内存地址:{id(num)}')
    result = 10
    print(f'返回值在函数内部的内存地址:{id(result)}')
    return result


a = 5
print(f'调用函数前内存地址:{id(a)}')
result_num = test(a)
print(f'调用函数后, 实参内存地址:{id(a)}')
print(f'调用函数后, 返回值内存地址:{id(result_num)}')

# 函数的参数和返回值传递的都是数据的地址(变量对数据的引用)
