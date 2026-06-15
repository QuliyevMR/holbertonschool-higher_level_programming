#!/usr/bin/env python3
"""
Bu modul xüsusi Python obyektlərini pickle modulu
vasitəsilə serialize və deserialize etmək üçündür.
"""
import pickle


class CustomObject:
    """
    Ad, yaş və tələbə statusu məlumatlarını saxlayan,
    həmçinin pickle ilə yaddaşda saxlanıla bilən klas.
    """

    def __init__(self, name, age, is_student):
        """
        Obyektin ilkin məlumatlarını təyin edir.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Obyektin məlumatlarını tələb olunan formatda ekrana çap edir.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Cari obyekti pickle vasitəsilə ikili (binary) formatda fayla yazır.
        Xəta baş verərsə, None qaytarır.
        """
        try:
            # Faylı "wb" (write binary) rejimində açırıq
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Göstərilən pickle faylından obyekti oxuyub bərpa edir.
        Fayl yoxdursa və ya zədəlidirsə, None qaytarır.
        """
        try:
            # Faylı "rb" (read binary) rejimində açırıq
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
