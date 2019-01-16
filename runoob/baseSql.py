#!//usr/local/bin python
# -*- coding:utf-8 -*-

import pymysql
db_name = ["sys"]

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456cl", db_name[0], charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#sql语句

#新建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""

#插入数据
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
sql = "select * from EMPLOYEE where AGE='20'"

try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
    data = cursor.fetchall()
    print(data)

except:
    #Rollback in case there is any error
    db.rollback()

# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
# print("Database version : %s" % data)

db.close()