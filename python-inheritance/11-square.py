#!/usr/bin/python3
"""Rectangle-dan miras alan Square klassını təyin edən modul."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle əsasında kvadratı təmsil edən klass."""

    def __init__(self, size):
        """Square klassının init metodu.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Kvadratın string təqdimatını qaytarır."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
