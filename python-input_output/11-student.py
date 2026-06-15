#!/usr/bin/python3
"""
Bu modul təkmilləşdirilmiş Student klasını təyin edir.
"""


class Student:
    """
    Tələbə məlumatlarını saxlayan, JSON formatına salan
    və JSON-dan yenidən yükləyən klas.
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
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}

        return self.__dict__

    def reload_from_json(self, json):
        """
        Gələn lüğətə (json) əsasən obyektin bütün atributlarını yeniləyir.
        """
        for key, value in json.items():
            self.__dict__[key] = value
