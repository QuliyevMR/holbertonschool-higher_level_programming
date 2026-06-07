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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Düzbucaqlının sahəsini hesablayır və qaytarır."""
        return self.__width * self.__height

    def __str__(self):
        """Düzbucaqlının string təqdimatını qaytarır."""
        return f"[Rectangle] {self.__width}/{self.__height}"
