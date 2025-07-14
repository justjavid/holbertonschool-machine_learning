#!/usr/bin/env python3
"""
This module provides a function to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    If the arrays are not the same length, returns None.

    Args:
        arr1 (list of numbers): The first array.
        arr2 (list of numbers): The second array.

    Returns:
        list or None: A new list with the sum of corresponding elements,
                      or None if arrays are of unequal length.

    Example:
        add_arrays([1, 2, 3], [4, 5, 6]) => [5, 7, 9]
    """
    if len(arr1) != len(arr2):
        return None
    new_list = []
    for i in range(len(arr1)):
        new_list.append(arr1[i] + arr2[i])
    return new_list
