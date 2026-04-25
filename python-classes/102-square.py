#!/usr/bin/python3
"""Square sinfi üçün modul."""


class Square:
    """Kvadratı təyin edən və sahəsinə görə müqayisə edən sinif."""

    def __init__(self, size=0):
        """Yeni Kvadrat yaradılır.
        Args:
            size (number): Kvadratın tərəfi (int və ya float).
        """
        self.size = size

    @property
    def size(self):
        """Size dəyərini oxumaq üçün property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size dəyərini təyin edən setter."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    # Müqayisə operatorlarının təyini
    def __eq__(self, other):
        """== (Bərabərdir) müqayisəsi."""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= (Bərabər deyil) müqayisəsi."""
        return self.area() != other.area()

    def __lt__(self, other):
        """< (Kiçikdir) müqayisəsi."""
        return self.area() < other.area()

    def __le__(self, other):
        """<= (Kiçikdir və ya bərabərdir) müqayisəsi."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> (Böyükdür) müqayisəsi."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= (Böyükdür və ya bərabərdir) müqayisəsi."""
        return self.area() >= other.area()
