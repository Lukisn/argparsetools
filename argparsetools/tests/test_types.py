#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentTypeError
from math import isnan
from unittest import TestCase, main

from hypothesis import given
from hypothesis.strategies import integers, floats, complex_numbers, text

from argparsetools.types import integer, floating_point, complex_number,\
    fraction, decimal


def notnan(x):
    if isnan(x):
        return False
    return True


def notzero(x):
    if x == 0:
        return False
    return True


class TestInteger(TestCase):

    @given(integers())
    def test_integer_passes(self, i):
        self.assertIsInstance(integer(str(i)), int)

    @given(floats())
    def test_float_fails(self, f):
        with self.assertRaises(ArgumentTypeError):
            integer(f)

    @given(text())
    def test_text_fails(self, t):
        with self.assertRaises(ArgumentTypeError):
            integer(t)


class TestFloatingPoint(TestCase):

    @given(integers())
    def test_integer_passes(self, i):
        floating_point(str(i))

    @given(floats().filter(lambda f: not isnan(f)))
    def test_floating_point_passes(self, f):
        floating_point(str(f))


class TestComplexNumber(TestCase):

    @given(complex_numbers())
    def test_complex_passes(self, c):
        self.assertEqual(c, complex_number(str(c)))


class TestFraction(TestCase):

    @given(integers(),
           integers().filter(notzero).filter(lambda x: x > 0))
    def test_integer_passes(self, i, j):
        fraction(f"{i}/{j}")

    @given(floats().filter(notnan),
           floats().filter(notnan).filter(lambda x: x > 0))
    def test_floating_point_passes(self, f, g):
        fraction(f"{f}/{g}")


class TestDecimal(TestCase):

    @given(integers())
    def test_integer_passes(self, i):
        decimal(str(i))

    @given(floats().filter(lambda f: not isnan(f)))
    def test_floating_point_passes(self, f):
        decimal(str(f))

    @given(text())
    def test_string_fails(self, t):
        with self.assertRaises(ArgumentTypeError):
            decimal(t)


if __name__ == "__main__":
    main()
