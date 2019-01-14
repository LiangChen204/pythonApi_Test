#!//usr/local/bin python
# -*- coding:utf-8 -*-

# 服务端
import socket # 导入socket模块

s = socket.socket()   # 创建socket对象
# 获取本地主机名
host = ''
# 设置端口
port = 12345
# 绑定端口
s.bind((host, port))
# 等待客户端连接
s.listen(5)   # 开始TCP监听

while True:
    # 调用 socket 对象的 accept 方法。该方法等待客户端的连接，并返回 connection 对象，表示已连接到客户端。
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    # c.send('欢迎访问菜鸟教程')    # 发送TCP数据，将string中的数据发送到连接的套接字
    c.close()



