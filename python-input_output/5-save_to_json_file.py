#!/usr/bin/python3
"""
Bu modul obyekti JSON formatında fayla yazmaq üçün funksiya təmin edir.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Python obyektini JSON təmsili ilə mətn faylına yazır.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
