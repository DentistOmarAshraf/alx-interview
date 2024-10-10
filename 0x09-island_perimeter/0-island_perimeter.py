#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """island_perimeter
    """
    coordinates = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                start_x = x - 1 if x - 1 >= 0 else 0
                end_x = x + 1 if x + 1 <= len(grid[y]) else x
                for j in range(start_x, end_x + 1):
                    if grid[j][y] == 0:
                        coordinates.append((j, y))

                start_y = y - 1 if y - 1 >= 0 else 0
                end_y = y + 1 if y + 1 <= len(grid[x]) else y
                for j in range(start_y, end_y + 1):
                    if grid[x][j] == 0:
                        coordinates.append((x, j))

    return len(coordinates)
