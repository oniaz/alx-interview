#!/usr/bin/python3
"""0x09. Island Perimeter"""


def island_perimeter(grid):
    """Calculates and returns the perimeter of the island described in "grid".
    grid is a list of list of integers:
    0 represents a water zone
    1 represents a land zone
    One cell is a square with side length 1
    Grid cells are connected horizontally/vertically (not diagonally).
    Grid is rectangular, width and height don’t exceed 100.
    Grid is completely surrounded by water, and there is one island (or
    nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to the
    water around the island).

    Argument:
        grid (list): 2d list of ints (1 and 0) representing land and water.

    Returns:
        int: permieter of the island.
    """

    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    if cols == 0:
        return 0

    perimeter = 0
    all_water = True

    for r in range(rows):
        water = 0
        for c in range(cols):
            if len(grid[r]) == 0:
                break
            if grid[r][c] == 0:  # 0; water
                water += 1
            else:  # 1; land
                if all_water:
                    all_water = False
                perimeter += 4
                # not necessary since the island must be surrounded by water
                if r > 0:
                    if grid[r-1][c] == 1:  # land above
                        perimeter -= 2
                # not necessary since the island must be surrounded by water
                if c > 0:
                    if grid[r][c-1] == 1:  # land to the left
                        perimeter -= 2
        if water == cols and not all_water:
            return perimeter
    return perimeter
