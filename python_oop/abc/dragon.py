#!/usr/bin/env python3
"""Module demonstrating the use of mixins with a Dragon class."""


class SwimMixin:
    """A mixin class providing swimming functionality."""

    def swim(self):
        """Prints the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class providing flying functionality."""

    def fly(self):
        """Prints the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim and fly."""

    def roar(self):
        """Prints the roaring behavior of the dragon."""
        print("The dragon roars!")