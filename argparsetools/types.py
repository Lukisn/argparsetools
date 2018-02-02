#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for use with arparse's type keyword argument to
the add_argument method.
"""

from argparse import ArgumentTypeError
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from functools import partial
from math import isinf, isnan


# Numeric =====================================================================
def integer(string):
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid number"
        raise ArgumentTypeError(msg)
    if not num.is_integer():
        msg = f"'{string}' is not a valid integer number"
        raise ArgumentTypeError(msg)
    num = int(num)
    return num


def floating_point(string, allow_nan=True, allow_inf=True):
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid floating point number"
        raise ArgumentTypeError(msg)
    if not allow_nan and isnan(num):
        msg = ""
        raise ArgumentTypeError(msg)
    if not allow_inf and isinf(num):
        msg = ""
        raise ArgumentTypeError(msg)
    return num


def complex_number(string):
    try:
        num = complex(string)
    except ValueError:
        msg = f"'{string}' is not a valid complex number"
        raise ArgumentTypeError(msg)
    return num


def fraction(string):
    try:
        num = Fraction(string)
    except ValueError:
        msg = f"'{string}' is not a valid fraction number"
        raise ArgumentTypeError(msg)
    return num


def decimal(string):
    try:
        num = Decimal(string)
    except InvalidOperation:
        msg = f"'{string}' is not a valid decimal number"
        raise ArgumentTypeError(msg)
    return num


def positive(string, strict=True):
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid number"
        raise ArgumentTypeError(msg)
    if strict:  # don't allow zero
        if num <= 0:
            msg = f"'{string}' is not a strictly positive number"
            raise ArgumentTypeError(msg)
    else:  # allow zero
        if num < 0:
            msg = f"'{string}' is not a positive number"
            raise ArgumentTypeError(msg)
    return num


def strictly_positive():
    return partial(positive, strict=True)


def loosely_positive():
    return partial(positive, strict=False)


def negative(string, strict=True):
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid number"
        raise ArgumentTypeError(msg)
    if strict:  # don't allow zero
        if num >= 0:
            msg = f"'{string}' is not a strictly negative number"
            raise ArgumentTypeError(msg)
    else:  # allow zero
        if num > 0:
            msg = f"'{string}' is not a negative number"
            raise ArgumentTypeError(msg)
    return num


def strictly_negative():
    return partial(negative, strict=True)


def loosely_negative():
    return partial(negative, strict=False)


# TODO: incorporate inclusion and exclusion of minimum and maximum values
def interval(string, minimum=float("-inf"), maximum=float("inf"),
             include_minimum=True, include_maximum=True):
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid number"
        raise ArgumentTypeError(msg)
    if num < minimum:
        msg = f"Number '{string}' is less than minimum {minimum}"
        raise ArgumentTypeError(msg)
    if num > maximum:
        msg = f"Number '{string}' is greater than maximum {maximum}"
        raise ArgumentTypeError(msg)
    return num


def at_least(minimum):
    return partial(interval, minimum=minimum)


def at_most(maximum):
    return partial(interval, maximum=maximum)


def in_range(minimum, maximum):
    return partial(interval, minimum=minimum, maximum=maximum)


def odd(string):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if not num % 2:
        msg = f"'{string}' is not an odd number"
        raise ArgumentTypeError(msg)
    return num


def even(string):
    try:
        num = int(string)
    except ValueError:
        msg  = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if num % 2:
        msg = f"'{string}' is not an even number"
        raise ArgumentTypeError(msg)
    return num


def divisible_by(string, divisor):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if num % divisor:
        msg = f"'{string}' is not divisible by {divisor}"
        raise ArgumentTypeError(msg)
    return num


def divisor_of(string, quantity):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if quantity % num:
        msg = f"'{string}' is not a divisor of {quantity}"
        raise ArgumentTypeError(msg)
    return num


def power_of(string, base):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    raise NotImplementedError


def prime(string):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)


# Strings =====================================================================


# Filesystem ==================================================================

