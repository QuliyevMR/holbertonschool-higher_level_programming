#!/usr/bin/python3
"""
Bu modul BaseGeometry sinfini ehtiva edir.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün əsas sinif."""

    def area(self):
        """
        Sahəni hesablayır.
        
        Raises:
            Exception: Əgər alt sinif bu metodu implement etməyibsə.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Dəyərin tam ədəd olmasını və 0-dan böyük olmasını yoxlayır.

        Args:
            name (str): Dəyərin adı.
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: Əgər dəyər int deyilsə.
            ValueError: Əgər dəyər <= 0 olarsa.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
