#!/usr/bin/env python3
"""Module that reads a UTF8 text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
