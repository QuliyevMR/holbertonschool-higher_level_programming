#!/usr/bin/python3
"""BaseGeometry klassını təyin edən modul."""


class BaseGeometry:
    """Həndəsi fiqurlar üçün əsas klass."""

    def area(self):
        """Hələ ki realizə olunmayıb, Exception qaytarır."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Daxil edilən dəyərin integer olub-olmadığını yoxlayır.

        Args:
            name (str): Dəyişənin adı.
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçik və ya bərabərdirsə.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
