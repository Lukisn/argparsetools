#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for use with arparse's type keyword argument to
the add_argument method.
"""

from argparse import ArgumentTypeError
from functools import partial


# Numeric =====================================================================
def number(string, minimum=float("-inf"), maximum=float("inf")):
    try:
        num = float(string)
    except ValueError:
        raise ArgumentTypeError(f"'{string}' is not a valid number")
    if num < minimum:
        msg = f"Number '{string}' is less than minimum {minimum}"
        raise ArgumentTypeError(msg)
    if num > maximum:
        msg = f"Number '{string}' is greater than maximum {maximum}"
        raise ArgumentTypeError(msg)
    return num


def at_least(minimum):
    return partial(number, minimum=minimum)


def at_most(maximum):
    return partial(number, maximum=maximum)


def in_range(minimum, maximum):
    return partial(number, minimum=minimum, maximum=maximum)


# Strings =====================================================================


# Filesystem ==================================================================

