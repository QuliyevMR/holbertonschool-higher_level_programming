#!/usr/bin/python3
"""
Bu modul obyektin sinfini dəqiq yoxlayan funksiyanı ehtiva edir.
"""


def is_same_class(obj, a_class):
    """
    Obyektin tam olaraq göstərilən sinfin nümunəsi olub olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        True - əgər obyekt tam olaraq həmin sinifdəndirsə.
        False - əks halda.
    """
    return type(obj) is a_class
