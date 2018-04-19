#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for numeric types for use with arparse."""

from argparse import ArgumentTypeError
from functools import partial
from math import isinf, isnan


def integer(string):
    """Check if the input string is an integer valued number.

    :param string: input string to check
    :type string: str
    :return: checked integer number
    :rtype: int
    """
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


def floating(string, allow_nan=False, allow_inf=False):
    """Check if the input string is a floating point number.

    :param string: input string to check
    :type string: str
    :param allow_nan: option for allowing Not-a-Number (NaN) values (default:
        ``False``)
    :type allow_nan: bool
    :param allow_inf: option for allowing positive and negative infinity values
        (default: ``False``)
    :type allow_inf: bool
    :return: checked floating point number
    :rtype: float
    """
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


def positive(string, strict=False):
    """Check if the input string is a positive floating point number.`

    :param string: input string to check
    :type string: str
    :param strict: option for checking positivity strictly (default: ``False`)
    :type strict: bool
    :return: checked floating point number
    :rtype: float
    """
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
    """Check if the input string is a strictly positive floating point number.

    :return: positive function with ``strict`` option set to ``True``
    :rtype: function
    """
    return partial(positive, strict=True)


def negative(string, strict=False):
    """Check if the input string is a negative floating point number.

    :param string:
    :param strict:
    :return:
    """
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
    """Check if the input string is a strictly negative floating point number.

    :return: negative function with ``strict`` option set to ``True``.
    :rtype: function
    """
    return partial(negative, strict=True)


def interval(string, min=float("-inf"), max=float("inf"),
             include_min=True, include_max=True):
    """Check that the input string is in the interval.

    The default interval is the closed interval from negative to positive
    infinity.

    :param string:
    :param min:
    :param max:
    :param include_min:
    :param include_max:
    :return:
    """
    try:
        num = float(string)
    except ValueError:
        msg = f"'{string}' is not a valid number"
        raise ArgumentTypeError(msg)
    if include_min:
        if num < min:
            msg = f"Number '{string}' is < the inclusive minimum {min}"
            raise ArgumentTypeError(msg)
    else:  # not include_minimum -> exclude minimum
        if num <= min:
            msg = f"Number '{string}' is <= to the  exclusive minimum {min}"
            raise ArgumentTypeError(msg)
    if include_max:
        if num > max:
            msg = f"Number '{string}' is > the inclusive maximum {max}"
            raise ArgumentTypeError(msg)
    else:  # not include_maximum -> exclude maximum
        if num >= max:
            msg = f"Number '{string}' is >= the exclusive maximum {max}"
            raise ArgumentTypeError(msg)
    return num


def open_interval(minimum, maximum):
    return partial(interval, min=minimum, max=maximum,
                   include_min=False, include_max=False)


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
    return num


def prime(string):
    try:
        num = int(string)
    except ValueError:
        msg = f"'{string}' is not a valid integer"
        raise ArgumentTypeError(msg)
    raise NotImplementedError
    return num
