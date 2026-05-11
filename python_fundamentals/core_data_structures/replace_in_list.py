#!/usr/bin/env python3
"""replace_in_list module."""


def replace_in_list(my_list, idx, element):
    """Replace element at idx, or return list unchanged if out of range."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
