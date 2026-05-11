#!/usr/bin/env python3
"""pow module."""


def pow(a, b):
    """Return a raised to the power of b."""
    result = 1
    for i in range(b):
        result *= a
    return result
