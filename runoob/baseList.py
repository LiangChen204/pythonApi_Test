#!//usr/local/bin python
# -*- coding:utf-8 -*-


"""更新列表"""
list = []
list.append('Google') ## 使用 append() 添加元素
list.append('Runoob')
print(list)

"""用del语句删除列表的元素"""
list1 = ['physics', 'chemistry', 1997, 2000]

print(list1)
del list1[2]

print("After deleting value at index 2 :", list1)