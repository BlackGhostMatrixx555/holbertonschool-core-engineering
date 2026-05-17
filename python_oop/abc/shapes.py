#!/usr/bin/env python3
"""Module demonstrating interfaces and duck typing with shapes."""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """An abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """A concrete class representing a circle."""

    def __init__(self, radius):
        """Initializes the circle.

        Args:
            radius (int/float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle.

        Args:
            width (int/float): The width of the rectangle.
            height (int/float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape using duck typing.

    Args:
        shape: An object that implements area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))