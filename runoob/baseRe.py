#!//usr/local/bin python
# -*- coding:utf-8 -*-

# re.match函数
import re
print(re.match('www', 'www.runoob.com').span()) # 在起始的位置匹配,span()返回一个元组包含匹配（开始，结束）的位置
print(re.match('com', 'www.runoob.com')) # 不在起始的位置匹配,返回none


# 匹配对应字符
line = "Cats are smarter than dogs"

# (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符
# (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
# 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

# re.search函数
print(re.search('www', 'www.runoob.com').span()) # 在起始的位置匹配,span()返回一个元组包含匹配（开始，结束）的位置
print(re.search('com', 'www.runoob.com').span()) # 不在起始的位置匹配

line = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# re.match与re.search的区别
matchObj1 = re.match(r'dogs', line, re.M | re.I)
if matchObj1:
    print("match --> matchObj.group() : ", matchObj1.group())
else:
    print("No match!!")

searchObj1 = re.search(r'dogs', line, re.M | re.I)
if searchObj1:
    print("search --> searchObj1.group() : ", searchObj1.group())
else:
    print("No search!!")

# 检索和替换
# re.sub用于替换字符串中的匹配项
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是：", num)

# 删除非数字（-）的字符串:'\D' 匹配非数字
num = re.sub(r'\D', "", num)
print("电话号码是：", num)

# 将字符串中的匹配的数字乘以 2
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# re.compile 函数
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)

"""
group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。"""
print(m.group(0))
print(m.start(0))
print(m.end(0))
print(m.span(0))

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)
print(m.group(0)) # 返回匹配成功的整个子串
print(m.span(0)) # 返回匹配成功的整个子串的索引
print(m.group(1)) # 返回第一个分组匹配成功的子串
print(m.span(1)) # 返回第一个分组匹配成功的子串的索引
print(m.group(2)) # 返回第二个分组匹配成功的子串
print(m.span(2)) # 返回第二个分组匹配成功的子串
print(m.groups()) # 等价于 (m.group(1), m.group(2), ...)
# print(m.group(3)) # 不存在第三个分组

# findall:findall 匹配所有
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

# re.finditer:在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

# re.split:split 方法按照能够匹配的子串将字符串分割后返回列表
s = re.split('\W+', 'runoob, runoob, runoob.')
print(s)
s = re.split('(\W+)', ' runoob, runoob, runoob.')
print(s)
s = re.split('\W+', ' runoob, runoob, runoob.', 1)
print(s)
s = re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(s)