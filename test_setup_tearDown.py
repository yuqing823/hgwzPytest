"""
-*- coding: utf-8 -*- 
@Time : 2022/7/19 11:21 
@Author : Yuqin Wang 
@File : test_setup_tearDown.py 
@Desc:
"""
import time

import pytest


class TestClass():
    global time_format
    time_format = "%Y-%m-%d %H:%M:%S"

    def setup_class(self):
        time.sleep(1)
        print(time.strftime(time_format, time.localtime()), "*************【 测试类前 】*************")

    def teardown_class(self):
        time.sleep(1)
        print(time.strftime(time_format, time.localtime()), "*************【 测试类后 】*************")

    def setup_method(self):
        print(time.strftime(time_format, time.localtime()), "--------------[ 用例开始 ]--------------")

    def teardown_method(self):
        print(time.strftime(time_format, time.localtime()), "--------------[ 用例结束 ]--------------")

    @pytest.mark.parametrize("a", [1, 11, 111])
    @pytest.mark.parametrize("b", [2, 22, 222])
    @pytest.mark.parametrize("c", [3, 33, 333])
    def test_one(self, a, b, c):
        print("test_one")

    @pytest.mark.parametrize("a", [1, 11, 111])
    @pytest.mark.parametrize("b", [2, 22, 222])
    @pytest.mark.parametrize("c", [3, 33, 333])
    def test_two(self, a, b, c):
        print("test_two")

    @pytest.mark.parametrize("a", [1, 11, 111])
    @pytest.mark.parametrize("b", [2, 22, 222])
    @pytest.mark.parametrize("c", [3, 33, 333])
    def test_three(self, a, b, c):
        print("test_three")
