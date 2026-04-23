#!/usr/bin/python3#!/usr/bin/python3
"""
Bu modul matris üzərində riyazi əməliyyatlar aparmaq üçün funksiyaları ehtiva edir.
Xüsusi olaraq, matrix_divided funksiyası matrisin hər bir elementini
verilmiş rəqəmə bölür.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div rəqəminə bölür.

    Arqumentlər:
        matrix (list of lists): Tam və ya onluq ədədlərdən ibarət matris.
        div (int, float): Bölən rəqəm.

    Qaytarır:
        list of lists: Bölmə nəticəsində yaranan yeni matris (2 rəqəmə yuvarlaq).

    Xətalar:
        TypeError: Əgər matris düzgün formatda deyilsə və ya sətirlər fərqlidirsə.
        TypeError: Əgər div rəqəm deyilsə.
        ZeroDivisionError: Əgər div 0-a bərabərdirsə.
    """

    # 1. div-in tipini yoxlayaq
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 2. Sıfıra bölünməni yoxlayaq
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Matrisin ümumi strukturunu yoxlayaq
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    # Matrisin içindəki hər bir elementin rəqəm olub-olmadığını yoxlayaq
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(error_msg)

    # 4. Sətirlərin ölçüsünü yoxlayaq
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 5. Hesablama və yeni matrisin qaytarılması
    return [[round(x / div, 2) for x in row] for row in matrix]
