#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from functools import partial
from argparsetools.types import positive, odd


def parse_arguments(argv=None):
    parser = ArgumentParser()
    # mandatory:
    # parser.add_argument("positional")
    # optional:
    parser.add_argument("--default-positive", type=positive)  # default: strict=True
    parser.add_argument("--strict-positive", type=partial(positive, strict=True))
    parser.add_argument("--lenient-positive", type=partial(positive, strict=False))
    args = parser.parse_args(args=argv)
    # check parsed namespace here if needed
    return args


def main(argv=None):
    args = parse_arguments(argv=argv)
    print(args)


if __name__ == "__main__":
    main()
