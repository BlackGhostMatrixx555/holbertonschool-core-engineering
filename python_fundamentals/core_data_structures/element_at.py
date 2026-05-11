#!/usr/bin/env python3
"""element_at module."""


def element_at(my_list, idx):
    """Return element at idx, or None if out of range or negative."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
