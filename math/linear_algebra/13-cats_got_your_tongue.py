#!/usr/bin/env python3
"""function to concatenate 2 matrices along
    a specific axis"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ concatenate two matrices
     with an specific axis

    Args:
        mat1, mat2: Given matrices
        axis: Given axis

    Return:
        the new mat: new_mat

    """
    new_mat = np.concatenate((mat1, mat2), axis)
    return new_mat
