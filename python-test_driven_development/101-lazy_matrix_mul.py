#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Contains a function that multiplies two matrices using the NumPy module.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
