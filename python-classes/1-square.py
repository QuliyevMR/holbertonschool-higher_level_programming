#!/usr/bin/python3
"""
Bu modul Kvadrat klassını təyin edir.
"""
class Square:
    """
    Kvadratı təmsil edən klass.
    """
    def __init__(self, size):
        """
        Kvadrat yaradılan zaman işə düşən funksiya (constructor).
        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
