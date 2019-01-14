#!//usr/local/bin python
# -*- coding:utf-8 -*-


a = b = c = 1
d, e, f = 1, 2, "john"

#字符串
s = 'abcdef'
s1= s[1:5]
s2 = s*2
s3 = s + "ADC"
print(a, b, c, d, e, f, s1, s2, s3)

#List(列表)
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list, list[0], list[1:3], list[2:], tinylist * 2, list + tinylist)

#元组：元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print(tuple, tuple[0], tuple[1:3], tuple[2:], tinytuple * 2, tuple + tinytuple)

#元组是不允许更新的。而列表是允许更新的
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print(tuple[2], list[2])

#字典(dictionary)是无序的对象集合，字典当中的元素是通过键来存取的，用"{ }"标识。由索引(key)和它对应的值value组成
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6732, 'dept': 'sales'}

print (dict['one'])         # 输出键为'one' 的值
print (dict[2])             # 输出键为 2 的值
print (tinydict)            # 输出完整的字典
print (tinydict.keys())     # 输出所有键
print (tinydict.values())   # 输出所有值