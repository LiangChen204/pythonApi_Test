#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 定义函数
def printme(str):
    "打印传入的字符串到标准显示设备上"
    print(str)
    return

# 正常调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

# 必备参数 例如调用printme()函数，你必须传入一个参数，不然会出现语法错误
# printme()

# 关键字参数
printme(str="My string")


# python 传不可变对象实例
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)


# 传可变对象实例
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值：", mylist)

# 使用关键字参数允许函数调用时参数的顺序与声明时不一致
def printinfo(name, age):
    "打印任何传入的字符串"
    print("Name:", name)
    print("Age:", age)
    return

# 调用printinfo函数
printinfo(age=50, name="miki")

# 默认参数：调用函数时，默认参数的值如果没有传入，则被认为是默认值
def printinfo1(name, age=35):
    print("Name", name)
    print("Age", age)
    return

# 调用printinfo1函数
printinfo1(age=50, name="miki")
printinfo1(name="miki")

# 不定长参数：一个函数能处理比当初声明时更多的参数
def printinfo2(arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# 调用printinfo2函数
printinfo2(10)
printinfo2(70, 60, 50)

# 匿名函数：使用 lambda 来创建匿名函数；lambda函数的语法只包含一个语句

sum = lambda arg1, arg2: arg1 + arg2

#调用sum函数
print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))

# return 语句
def sum(arg1, arg2):
    # 返回两个参数的和
    total = arg1 + arg2
    print("函数内：", total)
    return total

# 调用sum函数
total = sum(10, 20)


# 全局变量和局部变量
total = 0  # 这是一个全局变量

def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)