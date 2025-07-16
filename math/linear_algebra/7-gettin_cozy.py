"""
This module provides a function to concatenate two 2D matrices along a
specified axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specified axis.

    Args:
        mat1 (list of list): The first 2D matrix.
        mat2 (list of list): The second 2D matrix.
        axis (int, optional): The axis along which to concatenate.
                              Defaults to 0 (row-wise concatenation).

    Returns:
        list of list or None: A new matrix representing the concatenation,
                              or None if the matrices cannot be concatenated
                              along the specified axis due to dimension mismatch.
    """
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None
    new_matrix = []
    if axis == 0:
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    for row in range(len(mat1)):
        new_matrix.append(mat1[row] + mat2[row])
    return new_matrix
