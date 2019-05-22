#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/5/21 15:33
@author: liangchen
@File: test_get_usermessage
"""
import json
import time
import unittest

import requests
import urllib3


class MailGardenTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = 'https://meal.2dfire.com'
        # 获取时间
        t = time.time()
        cls.timestamp = str(round(t * 1000))

        # 请求头
        cls.header = {
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo X9i Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 MicroMessenger/7.0.4.1420(0x27000437) Process/appbrand0 NetType/WIFI Language/zh_CN'
        }

        # 不报SSL证书认证警告
        urllib3.disable_warnings()

    @classmethod
    def tearDownClass(cls):
        pass

    # @unittest.skip('调试')
    def test_a_get_usermessage(self):
        param_data = {
            'xtoken': '4f914aeeacab92af5f8677273b97d151',
            't': self.timestamp,
            'zone_id': '00340129'
        }
        r = requests.get(self.url + "/enterprise/takeout/v1/get_users_status", params=param_data, verify=False)
        result = r.json()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    def test_b_get_calendar(self):
        param_data = {
            'xtoken': '4f914aeeacab92af5f8677273b97d151',
            't': self.timestamp,
            'zone_id': '00340129'
        }
        r = requests.get(self.url + "/mini-program/zone/ordercalendar/v2/get_calendar", params=param_data, verify=False)
        result = r.json()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    def test_c_good_list(self):
        param_data = {
            'xtoken': '4f914aeeacab92af5f8677273b97d151',
            't': self.timestamp,
            'startTime': '',
            'endTime': '',
            'enterpriseId': '00340129',
            'addressId': '394600204214554454',
            'entrance': '1',
            'categoryType': '2'
        }
        r = requests.get(self.url + "/mini-program/zone/ordercalendar/v2/goods_list", params=param_data, verify=False)
        result = r.json()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    def test_d_quick_order(self):
        params = {
            'company_id': '00340129',
            'entity_id': '00400503',
            'xtoken': '4f914aeeacab92af5f8677273b97d151',
            't': self.timestamp
        }
        data = {
                "multiMenuId": "00400503698fb7210169b94a7e2e3108",
                "menuId": "004005036a929b7d016aaecff1fe6866",
                "num": 1,
                "kindType": 1,
                "specDetailId": "",
                "makeId": "",
                "childCartVos": []
            }
        r = requests.post(self.url + '/enterprise/takeout/ordercalendar/v1/quick_order', data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)



if __name__ == '__main__':
    unittest.main()

