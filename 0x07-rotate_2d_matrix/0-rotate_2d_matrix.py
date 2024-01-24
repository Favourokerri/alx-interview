#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""

def rotate_2d_matrix(matrix):
    """ function to rotate a 2dmatrix """
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i + 1, cols):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(rows):
        matrix[i].reverse()
