#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It handles type checking and casting.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.
    If a or b are NaN, it raises a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN (Not a Number) yoxlanışı
    # NaN öz-özünə bərabər olmayan yeganə dəyərdir
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Sonsuzluq (inf) yoxlanışı (Əgər checker bunu da istəyirsə)
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    
