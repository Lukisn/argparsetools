#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Type checking functions for file system types for use with arparse."""

from argparse import ArgumentTypeError


def valid_path(string):
    raise NotImplementedError


def existing_file(string):
    raise NotImplementedError


def non_existing_file(string):
    raise NotImplementedError


def file_under(string, root):
    raise NotImplementedError


def existing_directory(string):
    raise NotImplementedError


def non_existing_directory(string):
    raise NotImplementedError


def empty_directory(string):
    raise NotImplementedError


def directory_under(string, root):
    raise NotImplementedError
