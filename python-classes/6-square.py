#!/usr/bin/python3
"""Square sinfi üçün modul."""


class Square:
    """Kvadratı təyin edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni Kvadrat yaradılır.
        Args:
            size (int): Kvadratın tərəfi.
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
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini qaytarır.
        Sahə düsturu: $size^2$
        """
        return self.__size ** 2

    def my_print(self):
        """Kvadratı # işarəsi ilə koordinatlara uyğun çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y oxu üzrə boşluq (yeni sətirlər)
        [print("") for _ in range(self.__position[1])]

        # X oxu üzrə boşluq və kvadratın özü
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
