#!/usr/bin/python3
"""
Bu modul JSON faylından obyekt yaratmaq üçün funksiya təmin edir.
"""
import json


def load_from_json_file(filename):
    """
    JSON faylından məlumatı oxuyur və onu Python obyekti kimi qaytarır.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
