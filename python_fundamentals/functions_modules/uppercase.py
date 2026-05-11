#!/usr/bin/env python3
"""uppercase module."""


def uppercase(str):
    """Print str in uppercase."""
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
