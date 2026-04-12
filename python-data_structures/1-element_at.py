#!/usr/bin/python3
def element_at(my_list, idx):
    # İndeks mənfidirsə və ya siyahının uzunluğundan böyükdürsə None qaytar
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
