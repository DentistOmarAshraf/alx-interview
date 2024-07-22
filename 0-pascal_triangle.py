#!/usr/bin/python3
"""
Pascal Triangle
Should Return List of Lists
[1]                     -
[1, 1]                  |
[1, 2, 1]               |   n: height of triangle
[1, 3, 3, 1]            |
[1, 4, 6, 4, 1]         -
"""


# assume first array will be [[1]]
def pascal_recursive(arr, n):
    """Recursion fucntion for return lists of list"""
    if n == 1:
        return arr
    pascal_recursive(arr, n - 1)

    new_arr = []
    for x in range(n):
        if x == 0:
            new_arr.append(1)
            continue
        try:
            num = arr[-1][x] + arr[-1][x - 1]
        except IndexError:
            num = 1
        new_arr.append(num)
    arr.append(new_arr)
    return arr


def pascal_triangle(n):
    """Main function"""
    if n <= 0:
        return []
    return pascal_recursive([[1]], n)
