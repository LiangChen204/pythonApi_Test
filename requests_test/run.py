#!//usr/local/bin python
# -*- coding:utf-8 -*-

import unittest
from BSTestRunner import BSTestRunner
import time
import ssl

#ssl._create_default_https_context = ssl._create_unverified_context

#指定测试用例和测试报告的路径
test_dir = './test_case'
report_dir = './reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_cart_modify.py')

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'test_report.html'

#运行用例并且生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="shop API Test Report", description="China City Shop Test Report")
    runner.run(discover)
