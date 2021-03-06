a = 10
print(id(a))  # 数据10的存储地址1969516288
a = 20
print(id(a))  # 数据20的存储地址1969516608
b = a
print(id(b))  # 数据20的存储地址1969516608

# 扩展：任何语言中，
# 数据如果没有被任何变量引用，
# 那么一定会被回收掉，只是回收时间长短有区别
c = 10
print(id(c))
# 注意：虽然未被引用数据的地址没有变化，但是不代表数据不会被回收
# 在Python当中，对某个固定范围内的整数数据，是有数据缓存池机制存在的