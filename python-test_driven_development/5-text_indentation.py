#!/usr/bin/python3
"""
Bu modul say_my_name funksiyasını ehtiva edir.
Funksiya ad və soyadı ekrana çıxarmaq üçün nəzərdə tutulub.
"""


def say_my_name(first_name, last_name=""):
    """
    'My name is <first name> <last name>' formatında çap edir.

    Arqumentlər:
        first_name (str): İstifadəçinin adı.
        last_name (str): İstifadəçinin soyadı (default olaraq boş string).

    Xətalar:
        TypeError: Əgər daxil edilən arqumentlər string deyilsə.
    """

    # first_name-in string olub-olmadığını yoxlayırıq
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # last_name-in string olub-olmadığını yoxlayırıq
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Çap zamanı format istifadə etmək sondakı boşluqların
    # düzgün tənzimlənməsini təmin edir.
    print("My name is {} {}".format(first_name, last_name))
