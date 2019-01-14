#!//usr/local/bin python
# -*- coding:utf-8 -*-


a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

"""format 格式化函数"""
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


"""定义一个AssignValue方法，可以向 str.format() 传入对象"""
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue({"jjj":"jjj", "hhh":"hhh"})
print('value 为: {0.value}'.format(my_value))#"0"是可选的

"""数字格式化"""
print("{:.2f}".format(3.1415926))

print ("{} 对应的位置是 {{0}}".format("runoob"))

hi = '''hi 
there'''
print(hi)

"""定义Unicode 字符串：引号前小写的"u"表示这里创建的是一个 Unicode 字符串"""
print(u'Hello World !')
print(u'Hello\u0020World !')#被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）
