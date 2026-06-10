#!/usr/bin/env python3
"""
This module defines a CountedIterator class that wraps an iterator
and keeps track of the number of items iterated over.
"""


class CountedIterator:
    """An iterator that counts how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize the iterator object and the counter.

        Args:
            iterable: Any iterable object (e.g., list, tuple).
        """
        self.__iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.__counter

    def __next__(self):
        """Fetch the next item and increment the counter.

        Raises:
            StopIteration: If there are no items left to iterate.
        """
        # Hər dəfə next() çağırıldıqda əvvəlcə elementi götürürük.
        # Əgər element yoxdursa, elə bu sətirdə StopIteration xətası çıxacaq.
        item = next(self.__iterator)
        
        # Əgər element uğurla götürüldüsə, sayğacı artırırıq
        self.__counter += 1
        
        return item
