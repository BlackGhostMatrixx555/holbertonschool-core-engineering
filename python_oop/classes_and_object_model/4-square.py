#!/usr/bin/env python3
"""Module defining a Square class with getter and setter for size."""


class Square:
    """Represents a square with controlled access to size."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int): the size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: the current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): the new size.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
