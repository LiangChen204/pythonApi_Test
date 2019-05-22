#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/4/19 14:03
@author: liangchen
Project: 线上饭好约主要流程
"""
import json
import time
import unittest

import requests
import urllib3

# import const
# from requests_test import CONSTANT
from requests_test import getSign
from requests_test.debugtalk import get_token
from requests_test import *
from requests_test.getSign import requset2sign


class MaillyFlowTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wxurl = 'https://meal.2dfire.com'
        self.public_discount_path = '/presell/shop/v1/entity_search_commodity'
        self.xtoken = get_token("https://presell.fanhaoyue.com", "15906624143", '5b0f219ac7928fb89d069482c25c9d6f')
        print('dddddddd:' + str(self.xtoken))
        # self.xtoken = []
        self.discount_list = []
        self.lock_stock = []
        self.cart_list = []
        self.get_bill = []
        self.s = requests.session()
        # 获取时间
        t = time.time()
        self.timestamp = str(round(t * 1000))

        # 请求头
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'lang': 'zh_CN',
            'equipmentid': '302a0bb155cac42b8eb27a351e1af4aa',
            'version': '1160000',
            'user-agent': 'Hestia/1.16.0 (iPhone; iOS 11.2.6; Scale/3.00)',
            'cache-control': "no-cache"
        }

        # 不报SSL证书认证警告
        urllib3.disable_warnings()

    @unittest.skip("暂时不用")
    def test_a_get_token(self):
        """
        获取token
        :param evn: 环境(不同环境配置不一致，根据不同环境截取到.com/presell-api/或端口号)
        :param mobile: 手机号
        :param password: 密文密码(可以抓包获得)
        :return: token
        """
        # print("开始调用登陆接口>>>>>>>>>>>>")
        url = "https://presell.fanhaoyue.com" + '/member/action/v2/login'
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'version': '1160000',
                   'equipmentId': '302a0bb155cac42b8eb27a351e1af4aa'}
        request = {'appKey': '300001', 'area_code': '+86', 'equipment_id': '9F9DEEEE707D4EF3A030062BCF6C0A82',
                   'mobile': '15906624143',
                   'password': '5b0f219ac7928fb89d069482c25c9d6f', 'timestamp': str(round(time.time() * 1000)), 'token': '', 'uid': ''}
        request['sign'] = getSign.getSign(request)
        r = requests.post(url, headers=headers, data=request, verify=False)
        print("登陆接口登陆完毕<<<<<<<<<<<<<<")
        print(r.json()['data']['token'])
        self.xtoken.append(r.json()['data']['token'])

# 拉取店铺首页所以折扣id(接口校验加返回下一个接口要用的几个字段)
#     @unittest.skip("暂时不用")
    def test_b_public_discount(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^")
        print(self.xtoken)
        # 获取该接口sign值
        request = {
                'appKey': '300001',
                'entity_id': '00033912',
                'format': 'json',
                's_eid': '00033912',
                'source': '0',
                'timestamp': self.timestamp,
                'token': self.xtoken,
                'type': '1',
                'uid': '15906624143'
        }
        sign = requset2sign(request)
        # 组装接口入参
        param_data = {
            'appKey': '300001',
            'entity_id': '00033912',
            'format': 'json',
            's_eid': '00033912',
            'sign': sign,
            'source': '0',
            'timestamp': self.timestamp,
            'token': self.xtoken,
            'type': '1',
            'uid': '15906624143'
        }
        r = requests.get("https://presell.fanhaoyue.com" + "/presell/shop/v1/entity_search_commodity", params=param_data, headers=self.header, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^第一个接口返回结果：" + str(result))
        self.discount_list.append(result['data'][0]['presellStockId'])
        self.discount_list.append(result['data'][0]['mealTime'])
        print("%%%%%%%%%%%%%%%%%%%%%%self.discount_list:")
        print(self.discount_list)

        self.assertEqual(result['code'], 1)

# 锁单接口
#     @unittest.skip("暂时不用")
    def test_c_lock_stock(self):
        print("%%%%%%%%%%%%%%%%%%%%%%self.discount_list:")
        print(self.discount_list)
        # 获取sign值
        request = {
            'appKey': '300001',
            'entity_id': '00033912',
            'format': 'json',
            'meal_time': self.discount_list[1],
            'order_type': '1',
            'presell_stock_id': self.discount_list[0],
            's_eid': "00033912",
            'source': '44',
            'timestamp': self.timestamp,
            'token': self.xtoken,
            'uid': '15906624143'
        }
        sign = requset2sign(request)

        form_data = {
            'appKey': '300001',
            'entity_id': '00033912',
            'format': 'json',
            'meal_time': self.discount_list[1],
            'order_type': '1',
            'presell_stock_id': self.discount_list[0],
            's_eid': "00033912",
            'sign': sign,
            'source': '44',
            'timestamp': self.timestamp,
            'token': self.xtoken,
            'uid': '15906624143'
        }
        r = requests.post("https://presell.fanhaoyue.com" + '/presell/v1/lock_stock', data=form_data, headers=self.header, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^第二个接口返回结果：" + str(result))
        self.lock_stock.append(result['data']['seatCode'])
        self.lock_stock.append(result['data']['orderId'])
        self.assertEqual(result['code'], 1, msg="接口有误，code不一致")

# 拉取购物车数据接口
#     @unittest.skip("暂时不用")
    def test_d_cart_list(self):
        print("%%%%%%%%%%%%%%%%%%%%%%self.lock_stock:")
        print(self.lock_stock)
        param_data = {
            'entity_id': '00033912',
            'seat_code': self.lock_stock[0],
            'xtoken': self.xtoken
        }
        r = requests.get("https://meal.2dfire.com" + "/presell/carts/v1/list", params=param_data, headers=self.header, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^第三个接口返回结果：" + str(result))
        self.cart_list.append(result['data']['cartTime'])
        self.assertEqual(result['code'], 1)

# 拉取账单接口
#     @unittest.skip("暂时不用")
    def test_e_get_bill(self):
        print("%%%%%%%%%%%%%%%%%%%%%%self.cart_list:")
        print(self.cart_list)
        url = "https://meal.2dfire.com/presell/trade/v1/for_here/get_trade_bill"
        params = {
            "entity_id": "00033912",
            "seat_code": self.lock_stock[0],
            "xtoken": self.xtoken,
            "s_eid": "00033912"
        }
        data = {
            "requestFromApp": 1,
            "cashierBillStatusParam": None,
            "orderParam": {
                "orderId": "",
                "waitingOrderId": self.lock_stock[1],
                "pageFrom": "cart",
                "cartTime": self.cart_list[0],
                "firstLoading": 1,
                "recomputeFlag": False
            },
            "tipParam": {
                "customerSelectType": 0,
                "customerSelectRate": 0,
                "tipFee": 0
            },
            "payParam": {
                "giftPaySelected": True,
                "cardPaySelected": True,
                "cardPays": [],
                "memberPointsSelected": False,
                "redPacketPay": None,
                "redPacketPaySelected": False,
                "memberPointsPay": {}
            },
            "promotionParam": {
                "singleExchangeSelected": True,
                "mcPromotionSelected": True,
                "shouldReComputeKouBeiSelected": True,
                "kouBeiSelected": False,
                "cardId": "",
                "marketCenterPromotions": []
            }
        }
        self.header['Content-Type'] = "application/json"
        r = requests.post(url, data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^第四个接口返回结果：" + str(result))
        self.get_bill.append(result['data']['orderParam']['csrfToken'])
        self.get_bill.append(result['data']['orderParam']['needFee'])
        self.get_bill.append(result['data']['orderParam']['originFee'])
        self.get_bill.append(result['data']['orderParam']['discountFee'])
        print("%%%%%%%%%%%%%%%%%%%%%%self.get_bill:")
        print(self.get_bill)
        self.assertEqual(result['code'], 1)


# 唤起支付接口
#     @unittest.skip("暂时不用")
    def test_f_pay_presell(self):
        print("%%%%%%%%%%%%%%%%%%%%%%self.get_bill:")
        print(self.get_bill)
        url = "https://meal.2dfire.com/presell/trade/v1/for_here/pay_presell_bill"
        params = {
            'shop_kind': '0',
            'profession': '0',
            'xtoken': self.xtoken,
            's_eid': '00033912'
        }
        data = {
                "billParam": {
                    "deductFee": 0,
                    "discountFee": self.get_bill[2],
                    "needFee": self.get_bill[1],
                    "originFee": self.get_bill[2],
                    "paidFee": 0,
                    "paySource": 4,
                    "serviceFee": 0,
                    "source": 1,
                    "totalFee": self.get_bill[1],
                    "takeTip": False,
                    "tipType": 2,
                    "tipFee": 0,
                    "fixedRate": 0
                },
                "orderParam": {
                    "entityId": "00033912",
                    "orderId": self.lock_stock[1],
                    "seatCode": self.lock_stock[0],
                    "waitingOrderId": self.lock_stock[1]
                },
                "payTypeParam": {
                    "companyTakeoutPays": [],
                    "cardPays": [],
                    "redPacketPay": None,
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
                    "marketCenterPromotions": [],
                    "cutPricePromotions": []
                },
                "tradeParam": {
                    "csrfToken": self.get_bill[0],
                    "openId": "",
                    "largeOpenid": "",
                    "subAppId": "wx6cec2d42cc7f81e0",
                    "fromType": 3
                }
            }
        self.header['Content-Type'] = "application/json"
        r = requests.post(url, data=json.dumps(data), headers=self.header, params=params, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^第五个接口返回结果：" + str(result))
        self.assertEqual(result['code'], 1)


# 取消订单接口
#     @unittest.skip("暂时不用")
    def test_z_cancel_order(self):
        param_data = {
            'order_id': self.lock_stock[1],
            'entity_id': '00033912',
            'reasons[]': "撤销原订单",
            'xtoken': self.xtoken
        }
        r = requests.post("https://meal.2dfire.com" + "/presell/trade/v1/cancel_order", params=param_data, headers=self.header, verify=False)
        result = r.json()
        print("^^^^^^^^^^^^^最后一个接口返回结果：" + str(result))
        self.assertEqual(result['code'], 1)
        pass

    @classmethod
    def tearDownClass(cls):
        pass



if __name__ == '__main__':
    unittest.main()




