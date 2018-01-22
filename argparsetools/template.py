#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from argparsetools.types import positive_number, odd_number


def parse_arguments(argv=None):
    parser = ArgumentParser()
    parser.add_argument("positional", type=positive_number)
    parser.add_argument("-o", "--optional", type=odd_number)
    args = parser.parse_args(args=argv)
    # check parsed namespace here if needed
    return args


def main(argv=None):
    args = parse_arguments(argv=argv)
    print(args)


if __name__ == "__main__":
    main()
