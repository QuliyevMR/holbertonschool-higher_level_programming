#!/usr/bin/python3
"""
Bu modul JSON string-dən obyektə çevrilmə funksiyasını təmin edir.
"""
import json


def from_json_string(my_str):
    """
    JSON string-i (my_str) Python data strukturuna çevirir və qaytarır.
    """
    return json.loads(my_str)
