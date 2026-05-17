#!/usr/bin/env python3
"""Module defining a full Square class with string representation."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the printable string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)