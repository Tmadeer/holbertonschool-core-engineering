#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for c in "{}".format(str):
        if ord('a') <= ord(c) <= ord('z'):
            result = "{}{}".format(result, chr(ord(c) - 32))
        else:
            result = "{}{}".format(result, c)
    print("{}".format(result))
