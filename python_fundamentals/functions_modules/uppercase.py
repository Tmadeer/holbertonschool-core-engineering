#!/usr/bin/env python3
def uppercase(str):
    """Print str converted to uppercase, followed by a newline."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result = result + chr(ord(c) - 32)
        else:
            result = result + c
    print(result)
