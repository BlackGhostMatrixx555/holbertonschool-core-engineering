#!/usr/bin/env python3
"""Module defining a Square class with print method."""


class Square:
    """Represents a square that can print itself."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int): the size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

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
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters, or an empty line if size=0."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
