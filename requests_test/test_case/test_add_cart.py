#!//usr/local/bin python
# -*- coding:utf-8 -*-
import datetime
import json
import time
import unittest

# 定义H5购物车测试类
import requests
import urllib3
import const

class CartTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://api.l.whereask.com/purchase/api/presell/carts/v1'
        self.xtoken = const.DAILY_XTOKEN
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
# 创建购物车
    def test_cart_create(self):
        form_data = {'entity_id': '99001331', 'seat_code': 'presell_10c34bce7bc345448013cd21f06b9197'}
        # header = {"content-type": "application/x-www-form-urlencoded;application/json;charset=UTF-8;"}
        res = requests.post(self.url+"/create?xtoken="+self.xtoken, data=form_data, verify=False)
        result = res.json()
        # print("creat:" + res.text)

        self.assertEqual(result['code'], 1)
        self.assertEqual(result['data'], "请求成功")

# 获取购物车列表
    def test_cart_list(self):
        param_data = {'entity_id': '99001331', 'seat_code': 'presell_10c34bce7bc345448013cd21f06b9197', 'xtoken': self.xtoken}
        res = requests.get(self.url+'/list', params=param_data, verify=False)
        result = res.json()
        # print("list:"+res.text)

        self.assertEqual(result['code'], 1)
        self.assertEqual(result['data']['owner'], '10c34bce7bc345448013cd21f06b9197')
        # self.assertEqual(result['data']['kindMenuDic']['9900133161d53eb70161d5408fba0000']['kindMenuName'], '一直在')

# # 检测购物车
    def test_async_modify(self):
        param_data = {'entity_id': '99001331', 'seat_code': 'presell_10c34bce7bc345448013cd21f06b9197', 'order_id': '99001331682c2f57016835db02bb0107', 'source': 'presell', 'xtoken': self.xtoken, 's_eid': '99001331'}
        data = {
	                "source": "H5OM012",
	                "menuName": "小鲫鱼",
	                "memo": "",
	                "menuId": "000013314c7d25ca014c91cd86d6006e",
	                "makeId": "",
	                "specDetailId": "",
	                "num": 2,
	                "kindType": 1,
	                "uid": "10c34bce7bc345448013cd21f06b9197",
	                "index": "65211664967497710c34bce7bc345448",
	                "multiMenuId": ""
                }
        header = {'content-type': 'application/json'}
        res = requests.post(self.url+'/async_modify', params=param_data, json=data, headers=header, verify=False)
        result = res.json()
        # print(result)

        self.assertEqual(result['code'], 1)

if __name__ == '__main__':
    unittest.main()


