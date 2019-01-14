#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

# 命名空间和作用域
Money = 2000

def AddMoney():
    global Money
    Money = Money + 1

print(Money)
AddMoney()
print(Money)

# dir()函数:dir() 函数返回一个排好序的字符串列表，内容是一个模块里定义过的名字
import math
content = dir(math)

print(content)

# Python中的包:简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空



