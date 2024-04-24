#!/usr/bin/env python3
"""
Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix
    """
    row = len(matrix)
    col = row - 1

    for i in range(0, int(row / 2)):
        for j in range(i, col - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[col - j][i]
            matrix[col - j][i] = matrix[col - i][col - j]
            matrix[col - i][col - j] = matrix[j][col - i]
            matrix[j][col - i] = temp

    return matrix
