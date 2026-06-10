#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python
using Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Override fly method for the flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method for the flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method for the flying fish."""
        print("The flying fish lives both in water and the sky!")
