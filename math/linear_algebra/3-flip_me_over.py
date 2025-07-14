#!/usr/bin/env python3
"""
This module provides a function to compute the transpose of a matrix.
"""

def matrix_transpose(matrix):
    """
    Computes the transpose of a 2D matrix.

    The transpose of a matrix is obtained by flipping it over its diagonal,
    switching the row and column indices of the elements.

    Assumes all rows are of equal length.

    Args:
        matrix (list of list of numbers): A 2D matrix to transpose.

    Returns:
        list of list of numbers: The transposed matrix.
    
    """
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append([])
    j = 0
    while(len(transpose[len(transpose) - 1]) != len(matrix)):
        for i in range(len(matrix)):
            transpose[j].append(matrix[i][j])
        j += 1
    return transpose
