#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/1/20 21:32
@author: liangchen
Project: 各类断言集合
"""
import unittest

case = unittest.TestCase()
case.assertEqual(1, 2.0/2)  # 通过1=2.0/2
case.assertEqual(1, True)  # 通过
case.assertIs(1.0, 2.0/2)  # 失败，不是同一对象
case.assertListEqual([1, 2], [1, 2])   # 通过（顺序要一致）
case.assertDictEqual({"a": 1, "b": 2}, {"b": 2, "a": 1})  # 通过，字典本无序
case.assertIsNone({})  # 失败
case.assertFalse({})  # 通过，空字典为False
case.assertIn("h", "hello")  # 通过
case.assertGreater(3, 2)  # 通过，3>2
case.assertIsInstance({"a": 1}, dict)  # 通过



