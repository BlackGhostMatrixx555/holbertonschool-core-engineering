#!/usr/bin/env python3
"""pow module."""


def pow(a, b):
    """Return a raised to the power of b."""
    result = 1
    for i in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
