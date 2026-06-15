#!/usr/bin/python3
"""
Bu modul Student klasını təyin edir.
"""


class Student:
    """
    Tələbə məlumatlarını saxlayan və JSON formatına
    uyğunlaşdıran klas.
    """

    def __init__(self, first_name, last_name, age):
        """
        Student instansiyasını başlanğıc parametrlərlə yaradır.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Student instansiyasının lüğət (dict) təsvirini qaytarır.
        """
        return self.__dict__
