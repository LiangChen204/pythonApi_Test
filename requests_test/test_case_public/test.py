#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/5/21 16:35
@author: liangchen
@File: test
"""

#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/5/21 15:33
@author: liangchen
@File: test_get_usermessage
"""
import time
import unittest

import requests
import urllib3


class MailGardenTest(unittest.TestCase):
    @classmethod
    def SetUpClass(self):
        self.url = 'https://meal.2dfire.com'
        # 获取时间
        t = time.time()
        self.timestamp = str(round(t * 1000))
        print("timestamp的值为：")
        print(self.timestamp)

        # 不报SSL证书认证警告
        urllib3.disable_warnings()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_get_usermessage(self):
        param_data = {
            'xtoken': '4f914aeeacab92af5f8677273b97d151',
            't': '1558426548050',
            'zone_id': '00340129'
        }
        # 不报SSL证书认证警告
        urllib3.disable_warnings()
        r = requests.get('https://meal.2dfire.com' + "/enterprise/takeout/v1/get_users_status", params=param_data, verify=False)
        result = r.json()
        print(result)


if __name__ == '__main__':
    unittest.main()

