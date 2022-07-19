"""
-*- coding: utf-8 -*- 
@Time : 2022/7/19 9:59 
@Author : Yuqin Wang 
@File : test_demo.py 
@Desc:霍格沃兹pytest学习
"""
import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3), (-1, -2, -3), (10000, 10000, 20000)
], ids=["int", "minus", "bigint"])
def test_add(a, b, expected):
    print("a=", a, "b=", b, "expected=", expected)
    assert add_function(a, b) == expected
