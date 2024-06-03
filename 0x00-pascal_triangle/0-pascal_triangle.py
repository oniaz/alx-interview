#!/usr/bin/python3
"""Triangle of pascal"""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []
    pascal = [[1]]
    for row_num in range(1, n):
        row = [1]
        for j in range(1, row_num):
            element = pascal[row_num - 1][j - 1] + pascal[row_num - 1][j]
            row.append(element)
        row.append(1)
        pascal.append(row)

    return pascal
