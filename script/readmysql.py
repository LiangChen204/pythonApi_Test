#!//usr/local/bin python
# -*- coding:utf-8 -*-

#导入开发包
import pymysql.cursors

#获取链接
connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456cl',
                                     db='wikiurl',
                                     charset='utf8mb4')

try:
    #获取会话指针
    with connection.cursor() as cursor:
        #查询语句
        sql = "select `urlname`, `urlhref` from `urls` where `id` is not null"
        conut = cursor.execute(sql)
        print(conut)

        #查询数据
        result = cursor.fetchmany(size=3)
        #result = cursor.fechall()
        print(result)

finally:
    connection.close()