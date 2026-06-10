#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound of the animal."""
        pass


class Dog(Animal):
    """Subclass representing a dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
