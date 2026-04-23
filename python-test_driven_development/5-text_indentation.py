#!/usr/bin/python3
"""
Bu modul mətni formatlaşdıran funksiyanı ehtiva edir.
Xüsusi simvollardan sonra yeni sətirlər əlavə olunur.
"""


def text_indentation(text):
    """
    '.', '?' və ':' simvollarından sonra 2 yeni sətir çap edir.
    Sətir başındakı və sonundakı boşluqlar təmizlənir.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # flag = 0 o deməkdir ki, biz hazırda sətir başındakı boşluqları atırıq
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        
        if flag == 1:
            if a in "?:.":
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
