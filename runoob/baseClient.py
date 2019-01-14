#!//usr/local/bin python
# -*- coding:utf-8 -*-
import socket

#创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.connect(('www.sina.com.cn', 80))

s = socket.socket()         # 创建 socket 对象
host = ''   # 获取本地主机名
port = 12345               # 设置端口号

s.connect((host, port))
print(s.recv(1024))   #  接收TCP数据，数据以字符串形式返回
s.close()