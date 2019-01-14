#!//usr/local/bin python
# -*- coding:utf-8 -*-

import unittest
import requests
import ssl
# from urllib import parse
# from time import sleep

#ssl._create_default_https_context = ssl._create_unverified_context

#定义测试类
class ShopTest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://meal.2dfire.com/mini-program/presell/v2/home_info_reform'

    def test_shop_hangzhou(self):
        data = {'xtoken': 'f3a5923919296f414ee60aa977d907e4', 'city_id': '76', 'latitude': '30.34698486328125',
                'longitude': '120.00152126736111'}
        r = requests.get(self.url, params=data)
        result = r.json()

        self.assertEqual(result['code'], 1)
        # self.assertEqual(result['data']['barrageMessageTwoVOS'][0]['shopName'], '绿茶(杭州三墩金地店)')

    def test_shop_param_error(self):
        data = {'xtoken': 'f3a5923919296f414ee60aa977d907e4', 'city_id': '76', 'latitude': '30.34698486328125',
                'longitude': '120.00152126736111'}
        r = requests.get(self.url, params=data)
        result = r.json()

        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['message'], '请先授权')

    # unittest.skip():装饰器，当运行用例时，有些用例可能不想执行等，可用装饰器暂时屏蔽该条测试用例
    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg='Your input is not 30')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作
    def tearDown(self):
        print('Test over')





if __name__ == '__main__':
    unittest.main()