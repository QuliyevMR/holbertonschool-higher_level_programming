#!/usr/bin/python3
"""
Bu modul genişləndirilmiş Student klasını təyin edir.
"""


class Student:
    """
    Tələbə məlumatlarını saxlayan və atributları filtrləyərək
    JSON formatına uyğunlaşdıran klas.
    """

    def __init__(self, first_name, last_name, age):
        """
        Student instansiyasını başlanğıc parametrlərlə yaradır.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Student instansiyasının lüğət təsvirini qaytarır.
        Əgər attrs siyahısı verilibsə, yalnız həmin atributları filtrləyir.
        """
        # attrs-ın siyahı olub-olmadığını və bütün elementlərinin string olduğunu yoxlayırıq
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}

        # Əks halda bütün atributları qaytarırıq
        return self.__dict__
