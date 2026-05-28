#!/usr/bin/env python3
"""Module for appending a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file, creating it if needed.

    Args:
        filename (str): the path to the file to append to.
        text (str): the string to append to the file.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
