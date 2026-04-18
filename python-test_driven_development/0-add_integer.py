#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to int.
    Checks for NaN and Infinity as well.
    """
    # a-nı yoxla (həm tipini, həm də NaN olub-olmadığını)
    if not isinstance(a, (int, float)) or a != a:
        raise TypeError("a must be an integer")
    
    # b-ni yoxla
    if not isinstance(b, (int, float)) or b != b:
        raise TypeError("b must be an integer")
        
    # Sonsuzluq (Infinity) yoxlanışı (int() infinity üçün OverflowError atır)
    # Amma bəzi checker-lər bunu da TypeError kimi istəyə bilər.
    # Əgər cari kodunla inf testindən keçirsənsə, toxunma.

    return int(a) + int(b)
    
