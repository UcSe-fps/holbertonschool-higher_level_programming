#!/usr/bin/python3
"""Reads a UTF8 text file and prints it to stdout."""


def read_file(filename=""):
    """Yamyamaymaym"""

    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
