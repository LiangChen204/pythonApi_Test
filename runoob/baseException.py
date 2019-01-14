#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 走try
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常！")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 捕获异常
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常！")
except IOError:
    print("Error1: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()


# finally
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常！")
finally:
    print("Error2: 没有找到文件或读取文件失败")


try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print("Error3: 没有找到文件或读取文件失败")


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print("参数没有包含数字\n", Argument)

# 调用函数
temp_convert('oo')

# 定义异常:使用 raise 语句抛出一个指定的异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print("My exception occurred, value:", e.value)

# raise MyError('oops!!')


# 稍复杂的抛出异常例子
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print("division unsupported!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
divide(2, 0)
divide("2", "1")