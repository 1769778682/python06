# 整数(不可变类型)
num = 10
print('整数修改值之前', id(num))
num = 20
print('整数修改值之后', id(num))

# 字符串(不可变类型)
str_data = 'abc'
print('字符串修改值之前', id(str_data))
# 通过替换方法, 目标字符串已经变为一个新的字符串
new_str = str_data.replace('a', 'd')
print(str_data)
print('字符串修改值之后', id(new_str))

# 列表(可变类型)
list_data = [1, 2, 3, 4, 5]
print(list_data)
print('列表修改值之前', id(list_data))
list_data.append('6')
print(list_data)
print('列表修改值之后', id(list_data))

# 字典(可变类型)
dict_data = {'name': '刘备'}
print(dict_data)
print('字典修改值之前', id(dict_data))
dict_data['age'] = 20
print(dict_data)
print('字典修改值之后', id(dict_data))