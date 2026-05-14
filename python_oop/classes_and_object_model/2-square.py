#!/usr/bin/env python3
"""Module defining a Square class with size validation."""


class Square:
    """Represents a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int): the size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
