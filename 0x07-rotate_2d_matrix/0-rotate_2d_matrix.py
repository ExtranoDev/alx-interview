#!/usr/bin/python3
"""script Rotate 2D Matrix"""
from copy import deepcopy


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix In place
    Args: n x n matrix"""
    dup_mat = deepcopy(matrix)
    len_mat = len(dup_mat) - 1
    hor = 0
    while len_mat >= 0:
        pos = 0
        for num in dup_mat[len_mat]:
            matrix[pos][hor] = num
            pos += 1
        hor += 1
        len_mat -= 1
