#!/usr/bin/python3
"""Obyektə yeni atribut əlavə etməyi yoxlayan modul."""


def add_attribute(obj, name, value):
    """Mümkündürsə obyektə yeni atribut əlavə edir, yoxsa TypeError atır.

    Args:
        obj (object): Atribut əlavə ediləcək obyekt.
        name (str): Atributun adı.
        value (any): Atributun dəyəri.

    Raises:
        TypeError: Əgər obyektə yeni atribut əlavə etmək mümkün deyilsə.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
