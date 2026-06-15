#!/usr/bin/env python3
"""
Bu modul Python lüğətini (dictionary) JSON faylına yazmaq (serialize) və
JSON faylından yenidən Python lüğətinə oxumaq (deserialize) üçündür.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Python lüğətini (data) JSON formatında qeyd edilən fayla (filename) yazır.
    Fayl artıq mövcuddursa, köhnə məlumatın üzərinə yazılır.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Qeyd edilən JSON faylından məlumatı oxuyur və onu
    Python lüğəti (dictionary) şəklində qaytarır.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
