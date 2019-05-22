#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/20 21:27
@author: liangchen
Project: SelfTestPro
"""
import unittest  # 导入unittest
import requests
from api_demo.unittest.lib.readExcal import *


class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    @classmethod
    def setUpClass(cls):   # 整个测试类执行一次
        cls.data_list = excel_to_list("../../data/test_user_data.xlsx", "TestUserLogin")

    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        case_data = get_test_data(self.data_list, 'test_user_login_normal')   # 从数据列表中找到该用例数据
        if not case_data:
            logging.debug("用例数据不存在")
        url = case_data.get('url')    # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')   # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, data=json.loads(data))   # 表单请求，数据转为字典格式

        logging.info("测试用例：{}".format('test_user_login_normal'))
        logging.info("url：{}".format(url))
        logging.info("请求参数：{}".format(data))
        logging.info("期望结果：{}".format(expect_res))
        logging.info("实际结果：{}".format(res.text))

        self.assertEqual(res.text, expect_res)  # 断言

    def test_user_login_password_wrong(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('登录失败', res.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别
