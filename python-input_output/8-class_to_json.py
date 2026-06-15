#!/usr/bin/python3
"""
Bu modul obyektin atributlarını lüğət (dict) şəklində
qaytaran funksiyanı ehtiva edir.
"""


def class_to_json(obj):
    """
    JSON serialization üçün obyektin lüğət təsvirini qaytarır.
    """
    return obj.__dict__
