#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının surətini yaradırıq
    copy_list = my_list[:]

    # İndeks mənfidirsə və ya kənardırsa, surəti (dəyişilməmiş halda) qaytar
    if idx < 0 or idx >= len(my_list):
        return copy_list

    # Yalnız surət üzərində dəyişiklik edirik
    copy_list[idx] = element
    return copy_list
