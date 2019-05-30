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

from requests_test.debugtalk import get_token


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
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; vivo X9i Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 MicroMessenger/7.0.4.1420(0x27000437) Process/appbrand0 NetType/WIFI Language/zh_CN',
            'Accept': 'application/json,text/plain,*/*',
            'Accept-Language': 'zh-cn'
        }

        # 获取xtoken的值
        # cls.xtoken = ""
        cls.xtoken = "be0fb2ac50f0da7b447afd1f9acd9203"
        # cls.xtoken = get_token("https://presell.fanhaoyue.com", "15906624143", '5b0f219ac7928fb89d069482c25c9d6f')


        # 各接口提取值
        cls.get_calendar_list = []
        cls.takeout_bill_list = []
        cls.confirm_list = []
        cls.plugin_oauth_list = []

        # 不报SSL证书认证警告
        urllib3.disable_warnings()

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skip('调试')
    def test_oauth_login(self):
        params = {
            'app_id': 'wx2b17693f46728144',
            'xtoken': '',
            't': self.timestamp
        }
        data = {
                "platform_type": "internal",
                "wx_account": "mini_program_meal"
            }
        r = requests.post(self.url + '/mini-app/oauth/v1/login/' + '0711icUJ07Toj82Q70TJ0PpmUJ01icU1', data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        print(result)
        # self.xtoken = result['data']['xtoken']
        # print(self.xtoken)

    # @unittest.skip('调试')
    # 获取用户信息
    def test_a_get_usermessage(self):
        param_data = {
            'xtoken': self.xtoken,
            't': self.timestamp,
            'zone_id': '00340129'
        }
        r = requests.get(self.url + "/enterprise/takeout/v1/get_users_status", params=param_data, verify=False)
        result = r.json()
        print("第一个接口>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    # @unittest.skip('调试')
    # 嗨抢处商品
    def test_b_get_calendar(self):
        param_data = {
            'xtoken': self.xtoken,
            't': self.timestamp,
            'zone_id': '00340129'
        }
        r = requests.get(self.url + "/mini-program/zone/ordercalendar/v2/get_calendar", params=param_data, verify=False)
        result = r.json()
        self.get_calendar_list.append(result['data'][2]['hotGoodsVOS'][0]['deliveryTimes'][0]['times'][0]['time'])
        print(self.get_calendar_list[0])
        print("第二个接口>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    # @unittest.skip('调试')
    # 自定义分类处商品
    def test_c_good_list(self):
        param_data = {
            'xtoken': self.xtoken,
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
        print("第三个接口>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    # @unittest.skip('调试')
    # 快速下单接口
    def test_d_quick_order(self):
        params = {
            'company_id': '00340129',
            'entity_id': '00400503',
            'xtoken': self.xtoken,
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
        print("第四个接口>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    # @unittest.skip('调试')
    # 拉取账单接口
    def test_e_get_bill(self):
        params = {
            'seat_code': "",
            'entity_id': '00415580',
            'xtoken': self.xtoken,
            's_eid': '00415580'
        }
        data = {
                "cashierBillStatusParam": None,
                "companyId": "00340129",
                "companyTakeoutEntry": 1,
                "deliveryType": 0,
                "reserveDate": -1,
                "reserveStatus": 1,
                "orderParam": {
                    "cartTime": 0,
                    "firstLoading": 1,
                    "orderId": "",
                    "pageFrom": "welcome",
                    "recomputeFlag": False,
                    "waitingOrderId": ""
                },
                "payParam": {
                    "cardPaySelected": True,
                    "cardPays": [],
                    "giftPaySelected": False,
                    "redPacketPay": None,
                    "redPacketPaySelected": False,
                    "memberPointsSelected": True,
                    "memberPointsPay": {
                        "totalAmount": 0,
                        "exchangeRate": 0,
                        "maxExchangeAmount": 0,
                        "maxExchangeFee": 0,
                        "fee": 0
                    }
                },
                "promotionParam": {
                    "singleExchangeSelected": True,
                    "mcPromotionSelected": True,
                    "shouldReComputeKouBeiSelected": True,
                    "kouBeiSelected": False,
                    "cardId": "",
                    "marketCenterPromotions": []
                },
                "saleAddressParam": {
                    "addressId": "",
                    "companyAddressFlag": "1",
                    "latitude": "",
                    "longitude": ""
                },
                "tipParam": {
                    "customerSelectType": 0,
                    "customerSelectRate": 0,
                    "tipFee": 0
                }
            }

        r = requests.post(self.url + '/bill/v1/get_take_out_trade_bill', data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        # self.takeout_bill_list.append(result['data']['orderParam']['csrfToken'])

        print("第五个接口>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    # @unittest.skip('调试')
    # 生成账单
    def test_f_confirm_order(self):
        # print(self.get_calendar_list[0])
        params = {
            'xtoken': self.xtoken
        }
        data = {
            'entity_id': '00415580',
            'people_count': 1,
            'memo': '',
            'mobile': '15906624143',
            'invoice': 0,
            'reserve_time': '1559038200000',
            'order_fee': 999,
            'delivery_type': 0,
            'reserve_status': 1,
            'companyId': '00340129',
            'address_id': '394600204214554454',
            'companyAddressFlag': 1
        }
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        r = requests.post(self.url + '/takeout_orders/v1/confirm', params=params, data=data, headers=self.header, verify=False)
        result = r.json()
        # self.confirm_list.append(result['data']['waitingOrderId'])
        print("第六个接口>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    @unittest.skip('调试')
    # 获取插件token
    def test_g_plugin_oauth(self):
        params = {
            'app_id': 'wx6cec2d42cc7f81e0'
        }
        data = {
            "platform_type": "internal",
            "wx_account": "mini_program_meal"
        }
        r = requests.post(self.url + '/mini-program/oauth/v1/login/061bHU7k1A00vn08pP7k1cbG7k1bHU7P', data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        self.plugin_oauth_list.append(result['data']['token'])
        print("第七个接口>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)

    @unittest.skip('调试')
    # 唤起支付插件
    def test_h_bill_plugin(self):
        params = {
            'shop_kind': 0,
            'profession': 0,
            'xtoken': self.xtoken,
            'plugin_token': '9d17e4b6afd933163ab2d9643be85edb'
        }
        data = {
            {
                "billParam": {
                    "deductFee": 0,
                    "discountFee": 0,
                    "needFee": 1099,
                    "originFee": 1099,
                    "paidFee": 0,
                    "paySource": 2,
                    "serviceFee": 0,
                    "source": 1,
                    "totalFee": 1099,
                    "takeTip": False,
                    "tipType": 2,
                    "tipFee": 0,
                    "fixedRate": 0
                },
                "orderParam": {
                    "entityId": "00371258",
                    "orderId": "",
                    "seatCode": "",
                    "waitingOrderId": "003712586ae38fde016ae8e6af5f0fad"
                },
                "payTypeParam": {
                    "companyTakeoutPays": [],
                    "cardPays": [],
                    "giftPays": [],
                    "memberPointsPay": {
                        "exchangeRate": 0,
                        "fee": 0,
                        "maxExchangeAmount": 0,
                        "maxExchangeFee": 0,
                        "totalAmount": 0
                    },
                    "thirdPartyType": 3,
                    "returnUrl": ""
                },
                "promotionParam": {
                    "cardId": "",
                    "kouBeiSelected": False,
                    "marketCenterPromotions": []
                },
                "tradeParam": {
                    "csrfToken": "billCsrfToken:1SaijZT0Avd9XPeStYNm3k",
                    "openId": "",
                    "largeOpenid": "",
                    "subAppId": "wx6cec2d42cc7f81e0",
                    "fromType": 3
                },
                "saleAddressParam": {
                    "addressId": "394600204214554454"
                }
            }

        }
        r = requests.post(self.url + '/pay_bill/v1/pay_takeout_bill_by_plugin', data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        print("第八个接口>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(result)
        self.assertEqual(result['code'], 1)


if __name__ == '__main__':
    unittest.main()

