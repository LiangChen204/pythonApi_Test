#!//usr/local/bin python
# -*- coding:utf-8 -*-

import unittest
import requests
import urllib3
import json
from requests_test import CONSTANT

#定义测试类
class CartListTest(unittest.TestCase):

    def test_cart_list(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'xtoken': CONSTANT.const.DAILY_XTOKEN, 'source': 'presell'}
        r = requests.get(CONSTANT.const.DAILY_WEB_URL+'/v2/cart/list', params=param_data, verify=False)
        result = r.json()
        # print(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))

        self.assertEqual(result['code'], 1)
        # self.assertEqual(result['data']['cartList'][0]['cartVoList'][0]['customerVo']['name'], 'Shine✨_陈')


if __name__ == '__main__':
    unittest.main()