#!/usr/bin/python3
"""
Bu modul ad və soyadı çap edən funksiyanı ehtiva edir.
Funksiya daxil edilən dəyərlərin string olub-olmadığını yoxlayır.
"""


def say_my_name(first_name, last_name=""):
    """
    'My name is <first name> <last name>' formatında çap edir.

    Arqumentlər:
        first_name (str): Ad.
        last_name (str): Soyad (default olaraq boş string).

    Xətalar:
        TypeError: Əgər first_name və ya last_name string deyilsə.
    """

    # first_name string olub-olmadığını yoxlayırıq
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # last_name string olub-olmadığını yoxlayırıq
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Çap formatı
    print("My name is {} {}".format(first_name, last_name))
