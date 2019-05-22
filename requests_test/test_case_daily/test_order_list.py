#!//usr/local/bin python
# -*- coding:utf-8 -*-
import json
import unittest
import requests
import urllib3

from requests_test.debugtalk import run_sqldaily_presell
from requests_test import CONSTANT


class OrderListTest(unittest.TestCase):
    def test_all_order(self):
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        param_data = {'order_type': '', 'limit': '10', 'cursor_mark': '', 'xtoken': CONSTANT.const.DAILY_XTOKEN}
        res = requests.get(CONSTANT.const.DAILY_WEB_URL+'/order/v1/get_order_list', params=param_data, verify=False)
        result = res.json()
        sql = 'select * from `presell_stock_order` where order_id = "99928869683679f60168374e089b005f"'
        data = run_sqldaily_presell(sql)
        self.assertEqual(result['code'], 1)
        self.assertEqual(result['data']['orderList'][0]['discount'], data[4])


if __name__ == '__main__':
    unittest.main()

