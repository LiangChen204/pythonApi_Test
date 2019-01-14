#!//usr/local/bin python
# -*- coding:utf-8 -*-

count = 0
while (count < 9):
    print("The count is:", count)
    count = count + 1

print("Good bye!")


# continue 和 break 用法

i = 1
while i < 10:
    i += 1
    if i%2 > 0: # 非双数时跳过输出
        continue
    print(i)    # 输出双数2、4、6、8、10


i = 1
while 1:            # 循环条件为1必定成立
    print(i)      # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")


"""for"""
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")


"""通过索引遍历"""
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

print("Good bye!")


"""for...else
for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，
while … else 也是一样"""
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')


"""以下实例使用了嵌套循环输出2~100之间的素数"""
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")


"""break
如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码"""
for letter in 'Python':
    if letter == 'h':
        break
    print("当前字母：", letter)

var = 10
while var > 0:
    print("当前变量:", var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")


"""continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环"""
for letter in 'Python':
    if letter == 'h':
        continue
    print("当前字母：", letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print("当前变量:", var)
print("Good bye!")

"""pass是空语句，是为了保持程序结构的完整性"""
for letter in 'Python':
    if letter == 'h':
        pass
        print("这是pass块")
    print("当前字母：", letter)
print("Good bye!")

