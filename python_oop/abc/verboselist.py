#!/usr/bin/env python3
"""Module demonstrating how to extend built-in classes."""


class VerboseList(list):
    """A custom list class that prints notifications upon modification."""

    def append(self, item):
        """Appends an item to the list and prints a notification.

        Args:
            item: The element to add to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list with an iterable and prints a notification.

        Args:
            iterable: A collection of elements to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item from the list and prints a notification.

        Args:
            item: The element to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification.

        Args:
            index (int, optional): The index to pop from. Defaults to -1.

        Returns:
            The popped element.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)