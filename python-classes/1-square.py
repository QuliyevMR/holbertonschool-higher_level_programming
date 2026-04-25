#!/usr/bin/python3
"""
This module defines a Square class.
It focuses on the basics of OOP and private attributes.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The width and height of the square.
        """
        self.__size = size
