#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Custom actions for use with argparse's action keyword argument to the
add_argument method.
"""

from argparse import Action
from sys import exit


class PrintUsage(Action):

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_usage()
        exit()
