#!/usr/bin/env python3
"""Module defining the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: Indicates that area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a strictly positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to check.

        Raises:
            TypeError: If value is not exactly an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))