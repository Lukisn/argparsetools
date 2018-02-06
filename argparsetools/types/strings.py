#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for string types for use with arparse."""

from argparse import ArgumentTypeError


def length_range(string, minimum=0, maximum=float("inf")):
    raise NotImplementedError


def length_at_least(string, minimum):
    raise NotImplementedError


def length_at_most(string, maximum):
    raise NotImplementedError


def contains_only(string, alphabet):
    raise NotImplementedError


def letters(string):
    raise NotImplementedError


def alphanumeric(string):
    raise NotImplementedError


def regex_matches(string, pattern):
    raise NotImplementedError


def regex_in(string, pattern):
    raise NotImplementedError

