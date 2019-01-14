#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""元组与列表类似，不同之处在于元组的元素不能修改"""
#元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)

#访问元组中的值

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print("tup1[0]:", tup1[0])
print("tup2[1:5]:", tup2[1:5])

"""元组中的元素值是不允许修改的，但我们可以对元组进行连接组合"""
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

"""元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组"""
tup = ('physics', 'chemistry', 1997, 2000)

print
tup
del tup
# print("After deleting tup : ")
# print(tup)

"""元组索引，截取"""
L = ('spam', 'Spam', 'SPAM!')
print(L[2])
print(L[-2])
print(L[1:])

"""无关闭分隔符"""
print('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x, y)



