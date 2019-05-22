#!//usr/local/bin python
# -*- coding:utf-8 -*-
import unittest

# 定义测试类
import requests
import urllib3
from requests_test.debugtalk import get_token
from requests_test import CONSTANT

class CartModifyTest(unittest.TestCase):

    def test_cart_modify(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'xtoken': CONSTANT.const.DAILY_XTOKEN, 'entity_id': '99001331', 'seat_code': 'presell_10c34bce7bc345448013cd21f06b9197', 'source': 'presell', 'business_scenario': 3}
        json_data = {
            "index": "65211664967497710c34bce7bc345448",
	        "kindType": 1,
	        "makeId": "",
	        "menuId": "000013314c7d25ca014c91cd86d6006e",
	        "multiMenuId": "",
	        "num": 4,
	        "specDetailId": "",
	        "uid": "10c34bce7bc345448013cd21f06b9197"
        }
        header = {'Content-Type': 'application/json'}
        r = requests.post(CONSTANT.const.DAILY_WEB_URL + '/v1/cart/modify', params=param_data, json=json_data, headers=header, verify=False)
        result = r.json()
        print(result)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['data'], True)


if __name__ == '__main__':
    unittest.main()