#!/usr/bin/python3
"""
Bu modul Paskal üçbucağını quran funksiyanı təyin edir.
"""


def pascal_triangle(n):
    """
    n ölçülü Paskal üçbucağını təmsil edən siyahıların
    siyahısını qaytarır.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # İlk sətir həmişə [1] olur

    for i in range(1, n):
        prev_row = triangle[-1]  # Bir əvvəlki sətir
        # Yeni sətirin ilk elementi həmişə 1-dir
        current_row = [1]

        # Ortadakı elementləri hesablayırıq
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # Yeni sətirin son elementi həmişə 1-dir
        current_row.append(1)
        triangle.append(current_row)

    return triangle
