#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle klassını təyin edən modul."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry əsasında düzbucaqlını təmsil edən klass."""

    def __init__(self, width, height):
        """Rectangle klassının init metodu.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        # Əvvəlcə integer_validator ilə dəyərləri yoxlayırıq
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Yoxlanışdan keçərsə, private olaraq mənimsədirik
        self.__width = width
        self.__height = height
