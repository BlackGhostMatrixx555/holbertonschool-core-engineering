#!/usr/bin/env python3
"""Module defining a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a Square with a given size.

        Args:
            size: the size of the square.
        """
        self.__size = size
