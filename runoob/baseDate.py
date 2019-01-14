#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 函数time.time()用于获取当前时间戳
import time

ticks = time.time()
print("当前时间戳为：", ticks)

# 获取当前时间
localtime = time.localtime(time.time())
print("当前时间为：", localtime)

# 获取格式化的时间
localtime1 = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime1)

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Wed Jan 02 19:46:51 2019"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 获取某月日历
import calendar

cal = calendar.month(2018, 12)
print("以下输出2018年1月份的日历：")
print(cal)