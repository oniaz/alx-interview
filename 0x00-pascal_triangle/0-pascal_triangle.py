#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Generates Pascal's Triangle in the form of a list of lists,
        where each inner list respresents a row int he triangle
    """
    pascal = []
    for row in range(n):
        pascal.append([1])
        for col in range(row + 1):
            if (row > 0):
                if (col == 0):
                    pass
                elif (col < (row / 2) or col == (row / 2)):
                    pascal[row].append(
                        pascal[row - 1][col - 1] + pascal[row - 1][col])
                else:
                    pascal[row].append(pascal[row][row-col])
    return pascal
