#!/usr/bin/python3
"""
Bu modul obyektin atributlarını axtaran funksiyanı ehtiva edir.
"""


def lookup(obj):
    """Obyektin mövcud atribut və metodlarının siyahısını qaytarır."""
    return dir(obj)
