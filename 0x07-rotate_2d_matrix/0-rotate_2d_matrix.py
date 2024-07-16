#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise"""
    size = len(matrix)
    s = 0
    e = size - 1
    outer = int(size / 2)
    flag = False
    for i in range(outer):
        if flag:
            s += 1
            e -= 1
        flag = True
        inner = e - s
        k = 0
        for j in range(inner):
            matrix[s][j], matrix[j][e] = matrix[j][e], matrix[s][j]
            matrix[s][j], matrix[e][e - k] = matrix[e][e - k], matrix[s][j]
            matrix[s][j], matrix[e - k][s] = matrix[e - k][s], matrix[s][j]
            k += 1
