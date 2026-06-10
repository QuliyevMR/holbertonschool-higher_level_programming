#!/usr/bin/env python3
"""
This module demonstrates the concept of Mixins in Python
using SwimMixin, FlyMixin, and a Dragon class.
"""


class SwimMixin:
    """Mixin that provides swimming functionality."""

    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying functionality."""

    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, combining swimming and flying mixins."""

    def roar(self):
        """Print the roaring behavior unique to the dragon."""
        print("The dragon roars!")
