#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.
    If a or b are NaN, raises a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Yalnız NaN yoxlanışı qalır.
    # Sonsuzluq (inf) isə int() funksiyasına gedib təbii olaraq OverflowError verəcək.
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    
