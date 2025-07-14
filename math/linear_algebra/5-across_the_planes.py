#!/usr/bin/env python3
"""
This module provides a function to add two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    If the matrices do not have the same shape, returns None.

    Args:
        mat1 (list of list of numbers): The first 2D matrix.
        mat2 (list of list of numbers): The second 2D matrix.

    Returns:
        list or None: A new 2D matrix containing the element-wise sum
                      of the input matrices, or None if shapes do not match.

    Example:
        add_matrices2D([[1, 2]], [[3, 4]]) => [[4, 6]]
    """
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        new_matrix.append(row)
    return new_matrix
