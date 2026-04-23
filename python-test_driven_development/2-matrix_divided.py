#!/usr/bin/python3
"""
Bu modul matrislərin bölünməsi funksiyasını ehtiva edir.
Sətir uzunluğu 79 simvoldan çox olmamalıdır.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div rəqəminə bölür.

    Arqumentlər:
        matrix: tam və ya onluq ədədlərdən ibarət siyahıların siyahısı.
        div: bölən rəqəm (int və ya float).
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
