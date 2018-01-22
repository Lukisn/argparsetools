#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for use with arparse's type keyword argument to
the add_argument method.
"""

from argparse import ArgumentTypeError
from functools import partial


# Numeric =====================================================================
def positive_number(string, strict=True):
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


def negative_number(string, strict=True):
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


def ranged_number(string, minimum=float("-inf"), maximum=float("inf")):
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
    return partial(ranged_number, minimum=minimum)


def at_most(maximum):
    return partial(ranged_number, maximum=maximum)


def in_range(minimum, maximum):
    return partial(ranged_number, minimum=minimum, maximum=maximum)


def odd_number(string):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if not num % 2:
        msg = f"'{string}' is not an odd number"
        raise ArgumentTypeError(msg)
    return num


def even_number(string):
    try:
        num = int(string)
    except ValueError:
        msg  = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    if num % 2:
        msg = f"'{string}' is not an even number"


def divisible_by(string, divisor):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError
    raise NotImplementedError


def multiple_of(string, multiplier):
    raise NotImplementedError


# Strings =====================================================================


# Filesystem ==================================================================

