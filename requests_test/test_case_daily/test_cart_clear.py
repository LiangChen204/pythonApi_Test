#!//usr/local/bin python
# -*- coding:utf-8 -*-
import unittest
import requests
import urllib3

from requests_test.debugtalk import get_token


class CartClearTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://api.l.whereask.com/purchase_server/mini-program/presell'
        # self.xtoken = get_token('http://consumer-api.2dfire-daily.com', '15906624143',
        #                         'ccd9d460f0b4713f78ef3cc9fb87ca26')
        # 不报SSL证书认证警告
        urllib3.disable_warnings()

    def test_cart_clear(self):
        param_data = {'xtoken': self.xtoken}
        form_data = {'source': 'presell', 'clear_all': '', 'entity_id': '99001331', 'seat_code': 'presell_10c34bce7bc345448013cd21f06b9197', 'business_scenario': 3}
        res = requests.post(self.url+'/v1/cart/clear', params=param_data, data=form_data, verify=False)
        result = res.json()

        self.assertEqual(result['code'], 1)


if __name__ == '__main__':
    unittest.main()



