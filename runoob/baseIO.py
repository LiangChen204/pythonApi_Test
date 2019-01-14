#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 读取键盘输入(注意：python3中只有input（）函数)
# 1.raw_input函数
from pip._vendor.distlib.compat import raw_input
#
# str = raw_input("请输入：")
# print("你输入的内容是：", str)
#
# # 2.input函数:input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回
# str = input("请输入：")
# print("你输入的内容是：", str)

# 打开和关闭文件
fo = open("foo.txt", "w")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

# 关闭打开的文件
fo.close()
# print("末尾是否强制加空格 : ", fo.softspace) # python3已经去除

# write()方法:write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字
fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")
fo.close()

# read方法：read（）方法从一个打开的文件中读取一个字符串
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
# 查找当前位置:tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后
position = fo.tell()
print("当前文件位置：", position)
# 把指针再次重新定位到文件开头:
position = fo.seek(0, 1)
str = fo.read(10)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()

# 重命名和删除文件
# rename()方法：rename()方法需要两个参数，当前的文件名和新文件名
import os
# 创建文件test1。txt
open("test1.txt", "w+")
# 重命名文件test1.txt到test2.txt。
os.rename("test1.txt", "test1.txt")
# 删除存在的文件
os.remove("test1.txt")
# # 创建目录test
os.mkdir("test")
# 显示当前的目录
print(os.getcwd())
# 将当前目录改为"/home/newdir"
os.chdir("/Users/liangchen/PycharmProjects/SelfTestPro/runoob/test")
print(os.getcwd())
# 删除”/test”目录
os.rmdir("/Users/liangchen/PycharmProjects/SelfTestPro/runoob/test")