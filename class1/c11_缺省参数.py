# 定义列表数据
list_data = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]
# 排序
list_data.sort()
print(list_data)
list_data.sort(reverse=False)  # 大多数情况下，升序排列需求更多，因此默认值为False
list_data.sort(reverse=True)
print(list_data)


# 自定义函数添加缺省参数
# 定义函数时，给参数使用赋值语句，添加默认值即可完成缺省参数的设置
# 1.具备默认值的缺省参数必须放置于参数列表末尾，否则会报错
# 2.
def info(name,title='VIP', sex=True):
    if sex:
        print(f'男宾{title}一位楼上请')
    else:
        print(f'女宾{title}一位楼上请')


# 调用
info('小明')
# info('小红', False)  # 调用存在多个缺省值参数的函数时，如果要设定缺省参数值，必须制定参数名
info('小红', sex=False)