#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
       Calculates the perimeter of an island
       Args: grid(list(list)) -- Islands
    """
    rowLen = len(grid)
    colLen = len(grid[0])

    perimeter = 0

    for x in range(rowLen):
        for y in range(colLen):
            if grid[x][y] == 1:
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                if x == rowLen - 1 or grid[x + 1][y] == 0:
                    perimeter += 1
                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                if y == colLen - 1 or grid[x][y + 1] == 0:
                    perimeter += 1
    return perimeter
