#!//usr/local/bin python
# -*- coding:utf-8 -*-
import ast
import unittest
import requests
import urllib3
import json
# from requests_test import CONSTANT
from requests_test.lib.readExcal import *


#定义测试类

class CartListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类执行一次
        cls.data_list = excel_to_list("../data/test_cart_data.xlsx", "TestCartList")

    def test_cart_list_normal(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        # print(CONSTANT.const.PRE_XTOKEN)

        case_data = get_test_data(self.data_list, 'test_cart_list_normal')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        path = case_data.get('path')
        # print(type(case_data.get('param_data')))
        param_data = ast.literal_eval(case_data.get('param_data'))  # 使用 ast.literal_eval 将str类型转换为dict类型
        # print(param_data)

        expect_res = int(case_data.get('expect_res')) # 获取期望值
        # print(type(expect_res))

        r = requests.get(url + path, params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))

        self.assertEqual(result['code'], expect_res)
        # self.assertEqual(result['data']['cartList'][0]['cartVoList'][0]['customerVo']['name'], 'Shine✨_陈')

    def test_cart_list_source_wrong(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'xtoken': 'e7bb1e2aac34b31bccc9073094dc940b', 'source': 'source_wrong'}
        r = requests.get("https://meal.2dfire-pre.com" + '/v2/cart/list', params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
        # print(result)

        self.assertEqual(result['code'], 1)

    def test_cart_list_source_null(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'xtoken': 'e7bb1e2aac34b31bccc9073094dc940b', 'source': ''}
        r = requests.get("https://meal.2dfire-pre.com" + '/v2/cart/list', params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
        # print(result)

        self.assertEqual(result['code'], 1)

    def test_cart_list_xtoken_wrong(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        # print(CONSTANT.const.PRE_XTOKEN)
        param_data = {'xtoken': '219df319479a501fff756a52a6dcce', 'source': 'presell'}
        r = requests.get("https://meal.2dfire-pre.com" +'/v2/cart/list', params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))

        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "请先授权")

    def test_cart_list_xtoken_null(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'xtoken': '', 'source': 'presell'}
        r = requests.get("https://meal.2dfire-pre.com" + '/v2/cart/list', params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
        # print(result)

        self.assertEqual(result['code'], "-1")
        self.assertEqual(result['message'], "请先授权")


if __name__ == '__main__':
    unittest.main()