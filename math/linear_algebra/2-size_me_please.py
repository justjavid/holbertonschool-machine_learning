#!/usr/bin/env python3
def matrix_shape(matrix):
    """
    Returns the shape of a matrix as a list of integers.

    Args:
        matrix (list): A list of lists representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
