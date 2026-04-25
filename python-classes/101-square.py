#!/usr/bin/python3
"""Square sinfi üçün modul."""


class Square:
    """Kvadratı təyin edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni Kvadrat yaradılır.

        Args:
            size (int): Kvadratın ölçüsü.
            position (int, int): Kvadratın koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size dəyərini oxumaq üçün property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size dəyərini təyin edən setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position dəyərini oxumaq üçün property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position dəyərini təyin edən setter."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            # Tapşırıqdakı xüsusi tələb: "integer" (tək halda)
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı terminalda çap edir."""
        print(self.__str__())

    def __str__(self):
        """Kvadratın string təmsilini qaytarır."""
        if self.__size == 0:
            return ""

        res = []
        # Y oxu (yeni sətirlər)
        for _ in range(self.__position[1]):
            res.append("")

        # Kvadratın sətirləri
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
