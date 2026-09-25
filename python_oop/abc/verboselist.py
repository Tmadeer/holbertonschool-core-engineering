#!/usr/bin/env python3
"""
This module defines VerboseList that extends the built-in list class.
"""


class VerboseList(list):
    """Custom list class that prints notifications on modifications."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list with items from x and prints a notification."""
        items_count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list at index and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
