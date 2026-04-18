#!/usr/bin/python3
"""
This module provides a function
that adds two integers.
It handles casting and type checking.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
