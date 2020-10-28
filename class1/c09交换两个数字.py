# 定义两个整数变量
num1 = 10
num2 = 20

# 交换两个变量的值
# 方法1：临时变量
num3 = num2
num2 = num1
num1 = num3
print(num1)
print(num2)

# 方法二：不使用临时变量
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1)
print(num2)

# 方法三：利用Python的元组数据

num1, num2 = (num2, num1)
print(num1, num2)
