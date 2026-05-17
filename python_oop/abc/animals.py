#!/usr/bin/env python3
"""Module defining an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the animal's sound.
        
        Returns:
            str: The sound the animal makes.
        """
        pass


class Dog(Animal):
    """A concrete class representing a Dog."""

    def sound(self):
        """Returns the sound of a dog.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """A concrete class representing a Cat."""

    def sound(self):
        """Returns the sound of a cat.

        Returns:
            str: "Meow"
        """
        return "Meow"