#!/usr/bin/python3
def no_c(my_string):
    # Yeni mətni saxlamaq üçün boş sətir yaradırıq
    new_string = ""
    for char in my_string:
        # Əgər simvol 'c' və ya 'C' deyilsə, yeni mətnə əlavə edirik
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
