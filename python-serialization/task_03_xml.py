#!/usr/bin/env python3
"""
Bu modul Python lüğətlərini XML formatına serialize etmək
və XML fayllarından lüğətləri deserialize etmək üçündür.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML formatına çevirir və fayla yazır.
    """
    # 1. 'data' adlı kök (root) elementi yaradırıq
    root = ET.Element("data")

    # 2. Lüğətdəki hər bir elementi kökün alt elementi (child) edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # XML yalnız mətn formatında məlumat saxlayır, buna görə str() edirik
        child.text = str(value)

    # 3. Yaratdığımız XML ağacını fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """
    XML faylını oxuyur və onu yenidən Python lüğətinə çevirir.
    """
    try:
        # 1. XML faylını parse edirik (oxuyuruq)
        tree = ET.parse(filename)
        # 2. Kök elementi ('data') tapırıq
        root = tree.getroot()

        # 3. Kökün altındakı elementləri lüğətə əlavə edirik
        deserialized_dict = {}
        for child in root:
            # child.tag lüğətin açarı (key), child.text isə dəyəri (value) olur
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
