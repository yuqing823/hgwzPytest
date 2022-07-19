"""
-*- coding: utf-8 -*- 
@Time : 2022/7/19 15:28 
@Author : Yuqin Wang 
@File : test_calculator.py 
@Desc:
"""
import pytest

from pythoncode.calculator import Calculator


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print("CalculatorTest is starting...")

    def teardown_class(self):
        print("CalculatorTest is ending...")

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 3), (-1, -2, -3), (1000, 1000, 2000)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, -1), (-1, -2, 1), (1000, 1000, 0)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 2), (-1, -2, 2), (10, 10, 100)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 0.5), (-1, -2, 0.5), (1000, 1000, 1)
    ], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
