#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/25 16:54
@author: liangchen
Project: caselog
"""

from api_demo.unittest.config.config import *
import json

def log_case_info(case_name, url, data, expect_res, res_text):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)    # 如果data是字典格式，转化为字符串

        logging.info("测试用例：{}".format(case_name))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(data))
        logging.info("期望结果：{}".format(expect_res))
        logging.info("实际结果：{}".format(res_text))
