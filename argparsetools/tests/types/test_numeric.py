#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit test cases for numeric types."""

from argparse import ArgumentTypeError
from unittest import TestCase, main

from argparsetools.types.numeric import integer, floating_point


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


class TestFloatingPoint(TestCase):

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
                floating_point(i, allow_nan=True, allow_inf=True), float)

    def test_floating_points_pass(self):
        for f in self.normal_floats:
            self.assertIsInstance(
                floating_point(f, allow_nan=True, allow_inf=True), float)

    def test_special_floats_pass(self):
        for f in self.special_floats:
            self.assertIsInstance(
                floating_point(f, allow_nan=True, allow_inf=True), float)

    def test_special_floats_fail(self):
        for f in self.normal_floats:
            self.assertIsInstance(
                floating_point(f, allow_nan=False, allow_inf=False), float)

    def test_texts_fail(self):
        for t in self.texts:
            with self.assertRaises(ArgumentTypeError):
                floating_point(t, allow_nan=True, allow_inf=True)


if __name__ == "__main__":
    main()
