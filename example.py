import json

# a = [{'姓名': 'Kaina', '年龄': 22}]
# print(type(a))
# b = json.dumps(a)
# print(type(b))


# with open("aim.json", "a", encoding='utf-8') as f:
#     a = [{'姓名': 'Kaina', '年龄': 22, '职业':'销售员', '工资': 5000}]
#     print(type(a))
#     '''
#           1.消除乱码ensure_ascii=False
#           2.把数据类型转换成字符串并存储在文件中
#     '''
#     b = json.dump(a, f, ensure_ascii=False)
#     print(type(b))
#     print('数据写入完毕')


# #1.从json文件中读取数据，并保存在json_data变量中
# json_data = open('/Users/liangchen/Desktop/test.json', encoding='utf-8').read()
# print(type(json_data))
# #2。json调用loads()方法将字符串转换成列表
# data=json.loads(json_data)
# print(type(data))
# print(data)
# for item in data:
#     print(item)


# #获取字典某一键对应的值
# f = open('/Users/liangchen/Desktop/test.json', encoding='utf-8')
# #1.将数据导入程序
# data=json.load(f)
# #2.遍历data,打印列表中的每一个字典
# for dict_data in data:
#     print(dict_data)
#     print(dict_data['姓名'], '工资='+str(dict_data['工资']))


#将一个JSON文件中的内容写到另一个JSON文件中(复制)

#1.从josn文件中读取数据，并保存在josn_data变量中
json_data=open('/Users/liangchen/Desktop/test.json',encoding='utf-8').read()
aim_f = open('aim.json', 'w', encoding='utf-8')
#2.把test.json文件中的数据Copy到aim.json中
#3.目标文件对象调用write()方法把字符串写入
aim_f.write(json_data)


#获取字典的最大值
f = open('/Users/liangchen/Desktop/test.json', encoding='utf-8')
#1.将数据导入程序
data = json.load(f)
names = []
salary = []
#根据索引从列表中找到工资最高人的姓名
index = 0
#2。遍历data,打印列表中的每一个字典
for dict_data in data:
    names.append(dict_data['姓名'])
    salary.append(dict_data['工资'])
print(names)
print(salary)
for i, value in enumerate(salary):
    if value==10000:
        index = i
print(names[index] + '工资最高:' + str(max(salary)))