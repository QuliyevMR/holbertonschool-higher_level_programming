#!/usr/bin/python3
"""
Komanda sətrindən gələn bütün arqumentləri Python siyahısına əlavə edir
və onları JSON faylında yadda saxlayır.
"""
import sys

# Əvvəlki tapşırıqlardakı funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Fayl mövcuddursa, daxilindəki siyahını oxumağa çalışırıq
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # Fayl yoxdursa, boş siyahı ilə başlayırıq
    my_list = []

# 2. Komanda sətrindən gələn arqumentləri siyahıya əlavə edirik
# sys.argv[0] skriptin öz adı olduğu üçün [1:] ilə hamısını götürürük
my_list.extend(sys.argv[1:])

# 3. Yenilənmiş siyahını yenidən fayla yazırıq
save_to_json_file(my_list, filename)
