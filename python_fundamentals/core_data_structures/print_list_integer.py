#!/usr/bin/env python3
"""print_list_integer module."""


def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""
    for i in my_list:
        print("{:d}".format(i))
