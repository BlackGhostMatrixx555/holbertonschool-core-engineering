#!/usr/bin/env python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file, overwriting existing content.

    Args:
        filename (str): the path to the file to write.
        text (str): the string to write to the file.

    Returns:
        int: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
