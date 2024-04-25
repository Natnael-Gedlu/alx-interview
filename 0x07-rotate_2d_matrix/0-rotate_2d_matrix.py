#!/usr/bin/python3
"""
Rotate 2D Matrix Challenge.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D square matrix 90 degrees clockwise.

    Args:
    matrix (list): The 2D square matrix to be rotated.

    Returns:
    None:
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = (matrix[i][n - 1 - j],
                                                  matrix[i][j])
