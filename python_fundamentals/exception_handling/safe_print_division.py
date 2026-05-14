#!/usr/bin/env python3
"""safe_print_division module."""


def safe_print_division(a, b):
    """Divide a by b, print result in finally, return result or None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
