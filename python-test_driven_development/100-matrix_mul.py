#!/usr/bin/python3
"""Module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a (list of lists): First matrix (ints/floats)
        m_b (list of lists): Second matrix (ints/floats)

    Raises:
        TypeError: If matrices are not lists, list of lists,
                   contain non-numbers, or are not rectangular.
        ValueError: If matrices are empty or cannot be multiplied.

    Returns:
        list of lists: The product of m_a and m_b.
    """

    # 1. List yoxlanışı
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. List of lists yoxlanışı
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Boş olub-olmaması yoxlanışı
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. İnteger və ya Float yoxlanışı
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Düzbucaqlı (hər sətir eyni ölçüdə) yoxlanışı
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Vurulma imkanı (A-nın sütun sayı = B-nin sətir sayı)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matris vurulması alqoritmi
    # Nəticə matrisi: m_a-nın sətir sayı x m_b-nin sütun sayı
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)

    return result
