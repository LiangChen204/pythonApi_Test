#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/20 20:48
@author: liangchen
Project: 登录用例的一般方式
"""

# 数据准备
import unittest

import requests

from api_demo.unittest.lib.db import *
from api_demo.unittest.lib.readExcal import *


class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserReg")    # 读取TestUserReg工作簿的所有数据

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))   # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get("name")
        # 环境检查
        if check_user(name):
            del_user(name)

        # 发送请求
        res = requests.post(url=url, json=data)

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), expect_res)

        # 数据库断言
        self.assertTrue(check_user(name))

        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(name)

    # def test_user_reg_exist(self):
    #     # 环境检查
    #     if not check_user(EXIST_USER):
    #         add_user(EXIST_USER)
    #
    #     # 发送请求
    #     data = {'name': EXIST_USER, 'password': '123456'}
    #     res = requests.post(url=self.url, json=data)
    #
    #     # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
    #     except_res = {
    #         "code": "100001",
    #         "msg": "失败，用户已存在",
    #         "data": {
    #             "name": EXIST_USER,
    #             "password": "e10adc3949ba59abbe56e057f20f883e"
    #         }
    #     }
    #
    #     # 响应断言（整体断言）
    #     self.assertDictEqual(res.json(), except_res)
    #
    #     # 数据库断言(没有注册成功，数据库没有添加新用户)
    #
    #     # 环境清理（无需清理）


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 运行所有用例

