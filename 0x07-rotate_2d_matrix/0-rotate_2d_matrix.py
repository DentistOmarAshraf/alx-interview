#!/usr/bin/python3
"""
rotate_2d_matrix - clockwise rotation
"""


def rotate_2d_matrix(arr):
    """rotate_2d_matrix
    """
    N = len(arr[0])
    for i in range(N):
        for j in range(N-i):
            arr[i][j], arr[N - 1 - j][N - 1 -
                                      i] = arr[N - 1 - j][N - 1 - i], arr[i][j]

    for i in range(N//2):
        for j in range(N):
            arr[i][j], arr[N - 1 - i][j] = arr[N - 1 - i][j], arr[i][j]
