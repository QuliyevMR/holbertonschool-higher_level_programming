#!/usr/bin/env python3
"""
Bu modul CSV formatında olan faylı oxuyub məlumatları
JSON formatına çevirmək üçün funksiyanı ehtiva edir.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur, hər sətri lüğətə (dict) çevirir və 
    nəticəni 'data.json' faylına yazır.
    
    Uğurlu çevrilmə zamanı True, xəta olduqda False qaytarır.
    """
    try:
        # 1. CSV faylını oxuma rejimində açırıq
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            # DictReader məlumatları birbaşa lüğət kimi oxumağa kömək edir
            csv_reader = csv.DictReader(csv_file)
            
            # Oxunan lüğətləri bir siyahıya yığırıq
            data = list(csv_reader)

        # 2. Yaratdığımız siyahını 'data.json' faylına yazırıq
        with open("data.json", "w", encoding="utf-8") as json_file:
            # indent=4 parametriyə JSON faylını səliqəli və oxunaqlı edir
            json.dump(data, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarır
        return False
    except Exception:
        # Hər hansı digər gözlənilməz xəta ehtimalına qarşı False qaytarır
        return False
