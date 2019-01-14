#!//usr/local/bin python
# -*- coding:utf-8 -*-

# json.dumps:json.dumps 用于将 Python 对象编码成 JSON 字符串
import json
import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

jsonType = json.dumps(data)
print(jsonType)
# sort_keys是告诉编码器按照字典排序(a到z)输出
# indent参数根据数据格式缩进显示
# separators参数的作用是去掉,,:后面的空格
print(json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': ')))


# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)


# encode():Python encode() 函数用于将 Python 对象编码成 JSON 字符串
data = [{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

jsonDem = demjson.encode(data)
print(jsonDem)

# Python 可以使用 demjson.decode() 函数解码 JSON 数据
json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

textDem = demjson.decode(json)
print(textDem)