#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_correct_last(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_correct_mid(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_correct_beg(self):
        self.assertEqual(max_integer([5, 3, 4, 2]), 5)

    def test_one_neg(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_all_neg(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
