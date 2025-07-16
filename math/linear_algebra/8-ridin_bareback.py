"""
This module provides a function for performing matrix multiplication.
"""


#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    """
    Multiplies two matrices.

    Args:
        mat1 (list of list): The first matrix.
        mat2 (list of list): The second matrix.

    Returns:
        list of list or None: A new matrix representing the product of mat1
                              and mat2, or None if the matrices cannot be
                              multiplied due to incompatible dimensions.
    """
    if len(mat1[0]) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat1[0])):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        new_matrix.append(row)
    return new_matrix
