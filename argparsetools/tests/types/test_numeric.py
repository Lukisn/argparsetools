#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit test cases for numeric types."""

from argparse import ArgumentTypeError
from unittest import TestCase, main

from argparsetools.types.numeric import integer, floating, positive, \
    strictly_positive, negative, strictly_negative


# TODO: gather commonly used validation values in common base class
class NumericTestCase(TestCase):

    def setUp(self):
        pass


class TestInteger(TestCase):

    def setUp(self):
        self.valid_ints = [
            "-123", "-1", "-001", "-0", "0", "001", "1", "123",
            "-1.23e300", "-1.0", "-0.0", "0.0", "1.0", "123.0", "1.23e300"]
        self.floats = [
            "-1.23e-300", "-1.1", "1.1", "1.23e-300",
            "nan", "NaN" "-inf", "inf", "+inf"]
        self.texts = ["", " ", "abc123", "None", "False", "True", "123.4.5"]

    def test_integers_pass(self):
        for i in self.valid_ints:
            self.assertIsInstance(integer(i), int)

    def test_floats_fail(self):
        for f in self.floats:
            with self.assertRaises(ArgumentTypeError):
                integer(f)

    def test_texts_fail(self):
        for t in self.texts:
            with self.assertRaises(ArgumentTypeError):
                integer(t)


class TestFloating(TestCase):

    def setUp(self):
        self.valid_ints = [
            "-123", "-1", "-001", "-0", "0", "001", "1", "123",
            "-1.23e300", "-1.0", "-0.0", "0.0", "1.0", "123.0", "1.23e300"]
        self.normal_floats = ["-1.23e-300", "-1.1", "1.1", "1.23e-300"]
        self.special_floats = ["nan", "-inf", "inf", "+inf"]
        self.texts = ["", " ", "abc123", "None", "False", "True", "123.4.5"]

    def test_integers_pass(self):
        for i in self.valid_ints:
            self.assertIsInstance(
                floating(i, allow_nan=True, allow_inf=True), float)

    def test_floating_points_pass(self):
        for f in self.normal_floats:
            self.assertIsInstance(
                floating(f, allow_nan=True, allow_inf=True), float)

    def test_special_floats_pass(self):
        for f in self.special_floats:
            self.assertIsInstance(
                floating(f, allow_nan=True, allow_inf=True), float)

    def test_special_floats_fail(self):
        for f in self.normal_floats:
            self.assertIsInstance(
                floating(f, allow_nan=False, allow_inf=False), float)

    def test_texts_fail(self):
        for t in self.texts:
            with self.assertRaises(ArgumentTypeError):
                floating(t, allow_nan=True, allow_inf=True)


class TestPositive(TestCase):

    def setUp(self):
        self.positive = [
            "1", "1.2",
        ]
        self.zeros = [
            "0", "-0", "0.0", "-0.0",
        ]
        self.negative = [
            "-1", "-1.2",
        ]

    def test_positive_values_pass(self):
        for val in self.positive:
            self.assertIsInstance(positive(val), float)

    def test_zeros_pass(self):
        for val in self.zeros:
            self.assertIsInstance(positive(val), float)

    def test_negative_values_fail(self):
        for val in self.negative:
            with self.assertRaises(ArgumentTypeError):
                positive(val)


class TestStrictlyPositive(TestCase):

    def setUp(self):
        self.zeros = [
            "0", "-0", "0.0", "-0.0",
        ]
        self.func = strictly_positive()

    def test_zeros_fail(self):
        for val in self.zeros:
            with self.assertRaises(ArgumentTypeError):
                self.func(val)


class TestNegative(TestCase):

    def setUp(self):
        self.positive = [
            "1", "1.2",
        ]
        self.zeros = [
            "0", "-0", "0.0", "-0.0",
        ]
        self.negative = [
            "-1", "-1.2",
        ]

    def test_negative_values_pass(self):
        for val in self.negative:
            self.assertIsInstance(negative(val), float)

    def test_zeros_pass(self):
        for val in self.zeros:
            self.assertIsInstance(negative(val), float)

    def test_positive_values_fail(self):
        for val in self.positive:
            with self.assertRaises(ArgumentTypeError):
                negative(val)


class TestStrictlyNegative(TestCase):

    def setUp(self):
        self.zeros = [
            "0", "-0", "0.0", "-0.0",
        ]
        self.func = strictly_negative()

    def test_zeros_fail(self):
        for val in self.zeros:
            with self.assertRaises(ArgumentTypeError):
                self.func(val)


if __name__ == "__main__":
    main()
