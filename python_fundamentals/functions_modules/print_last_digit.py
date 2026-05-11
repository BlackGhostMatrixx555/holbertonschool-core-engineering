#!/usr/bin/env python3
"""print_last_digit module."""


def print_last_digit(number):
    """Print and return the last digit of number (always positive)."""
    last = abs(number) % 10
    print("{}".format(last), end='')
    return last
