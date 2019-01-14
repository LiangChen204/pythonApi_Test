#!//usr/local/bin python
# -*- coding:utf-8 -*-

#基础语法
from pip._vendor.distlib.compat import raw_input

word = 'word'
sentence = "这是一个句子！"
paragraph = """这是一个段落。
包含了多个语句"""
print(word, sentence, paragraph)

#等待用户输入
#raw_input("按下enter键退出， 其他任意键显示对于内容：\n")

#同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')