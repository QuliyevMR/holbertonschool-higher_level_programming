#!/usr/bin/python3
"""
This module defines a Square class.
It uses property getters and setters for the size attribute.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The width and height of the square.
        """
        self.size = size  # Bu birbaşa setter-i çağırır

    @property
    def size(self):
        """
        Getter: Retrieves the size of the square.

        Returns:
            int: The private size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: Sets the size of the square with validation.

        Args:
            value (int): The value to set the size to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
