#!/usr/bin/env python3
"""Module exploring multiple inheritance with a FlyingFish class."""


class Fish:
    """A class representing a standard fish."""

    def swim(self):
        """Prints the swimming behavior of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a standard bird."""

    def fly(self):
        """Prints the flying behavior of the bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides the flying behavior for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swimming behavior for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat for a flying fish."""
        print("The flying fish lives both in water and the sky!")