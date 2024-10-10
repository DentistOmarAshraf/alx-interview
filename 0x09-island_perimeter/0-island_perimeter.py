#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """island_perimeter
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                # chech top
                if x == 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                # Check bottom
                if x == rows - 1 or grid[x + 1][y] == 0:
                    perimeter += 1
                # Check left
                if y == 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                # Check right
                if y == cols - 1 or grid[x][y + 1] == 0:
                    perimeter += 1
    return perimeter
