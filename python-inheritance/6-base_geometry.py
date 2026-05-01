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
