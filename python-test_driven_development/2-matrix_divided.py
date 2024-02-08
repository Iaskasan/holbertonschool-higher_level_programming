#!/usr/bin/python3
"""matrix 1"""


def matrix_divided(matrix, div):
    """matrix reloaded"""
    def err(str):
        if str == "list":
            raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        if str == "row":
            raise TypeError("Each row of the matrix must have the same size")
        if str == "div":
            raise TypeError("div must be a number")
        if str == "div0":
            raise TypeError("division by zero")

    if not isinstance(matrix, list):
        err("list")
    ref_size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            err("list")
        if len(row) != ref_size:
            err("row")
        for nb in row:
            if not isinstance(nb, (int, float)):
                err("list")
    if not isinstance(div, (int, float)):
        err("div")
    if div == 0:
        err("div0")

    matrix_divided = [[round((nb / div), 2) for nb in row] for row in matrix]
    return matrix_divided
