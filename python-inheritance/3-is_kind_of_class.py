#!/usr/bin/python3
"""
Bu modul obyektin sinif mənsubiyyətini yoxlayan funksiyanı ehtiva edir.
"""


def is_kind_of_class(obj, a_class):
    """
    Obyektin sinifdən və ya miras alınmış sinifdən olub olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        True - əgər obyekt həmin sinifdən və ya onun alt sinifindəndirsə.
        False - əks halda.
    """
    return isinstance(obj, a_class)
