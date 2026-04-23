#!/usr/bin/python3
"""
Bu modul mətnin formatlaşdırılması funksiyasini ehtiva edir.
Xüsusi simvollardan sonra yeni sətir əlavə edir.
"""


def text_indentation(text):
    """
    Mətndə '.', '?' və ':' simvollarından sonra 2 yeni sətir çap edir.

    Arqumentlər:
        text (str): Formatlaşdırılacaq mətn.

    Xətalar:
        TypeError: Əgər 'text' string deyilsə.
    """

    # Tip yoxlanışı
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Simvolların yoxlanması üçün siyahı
    separators = [".", "?", ":"]

    # Mətni simvol-simvol gəzirik
    # skip_space dəyişəni sətir başındakı boşluqları tutmaq üçündür
    skip_space = True

    for char in text:
        # Əgər sətir başındayıqsa və simvol boşluqdursa, onu keçirik
        if skip_space and char == " ":
            continue

        # Boşluq olmayan simvol tapdıqda çap edirik və skip_space-i söndürürük
        print(char, end="")
        skip_space = False

        # Əgər simvol xüsusi ayırıcıdırsa, 2 yeni sətir çap edirik
        if char in separators:
            print("\n")
            skip_space = True
