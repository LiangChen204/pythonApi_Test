#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""字典：值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组"""

# 访问字典里的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']:", dict['Name'])
print("dict['Age']:", dict['Age'])

# 修改字典:向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

# 删除字典元素
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] # 删除键是'Name'的条目
dict.clear()      # 清空词典所有条目
del dict          # 删除词典

print(dict)
#print("dict['Age']: ", dict['Age'])
# 字典键的特性
"""1.键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
    2.不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住"""
# dict = {['Name']: 'Zara', 'Age': 7}
#
# print("dict['Name']: ", dict['Name'])# TypeError: unhashable type: 'list'