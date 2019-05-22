#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/20 21:34
@author: liangchen
Project: 用例包裹方法
"""

import unittest


def setUpModule():  # 当前模块执行前只执行一次
    print('=== setUpModule ===')


def tearDownModule():  # 当前模块执行后只执行一次
    print('=== tearDownModule ===')


class TestClass1(unittest.TestCase):
    @classmethod  # 声明为类方法（必须）
    def setUpClass(cls):  # 类方法，注意后面是cls，整个类只执行一次
        print('--- setUpClass ---')

    @classmethod
    def tearDownClass(cls):
        print('--- tearDownClass ---')

    def setUp(self):  # 该类中每个测试用例执行一次
        print('... setUp ...')

    def tearDown(self):
        print('... tearDown ...')

    def test_a(self):  # 测试用例
        print("a")

    def test_B(self):  # 大写B的ascii比小写a靠前，会比test_a先执行
        print("B")


class TestClass2(unittest.TestCase):  # 该模块另一个测试类
    def test_A(self):
        print("A")


if __name__ == '__main__':
    unittest.main()

