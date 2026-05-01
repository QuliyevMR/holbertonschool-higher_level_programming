#!/usr/bin/python3
"""
Bu modul obyektin miras alma (inheritance) vəziyyətini yoxlayır.
"""


def inherits_from(obj, a_class):
    """
    Obyektin bir sinifdən (birbaşa və ya dolayısı ilə) 
    miras alıb-almadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        True - əgər obyekt a_class-ın alt sinfinin nümunəsidirsə.
        False - əks halda (və ya obyektin özü a_class tipindədirsə).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
