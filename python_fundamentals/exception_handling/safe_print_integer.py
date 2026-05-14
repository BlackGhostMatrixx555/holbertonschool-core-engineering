#!/usr/bin/env python3
"""safe_print_integer module."""


def safe_print_integer(value):
    """Print value as integer, return True if success, False otherwise."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
