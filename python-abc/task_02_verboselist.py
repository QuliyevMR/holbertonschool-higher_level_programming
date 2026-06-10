#!/usr/bin/env python3
"""
This module defines a custom list class VerboseList that prints notifications
when items are added or removed.
"""


class VerboseList(list):
    """A custom list that prints messages on modifications."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification with the count of items."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Remove an item and print a notification before removing."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification before popping."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
