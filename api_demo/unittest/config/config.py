#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/25 15:53
@author: liangchen
Project: 日志输出
"""

import logging

# 项目路径

# 数据库配
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = '123456cl'
db = 'sys'

# 邮件配置



# log配置
logging.basicConfig(level=logging.DEBUG,   # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',   # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',   # 日期格式
                    filename='log.txt',   # 日志输出文件
                    filemode='a')   # 追加模式


if __name__ == '__main__':
    logging.info("hello")