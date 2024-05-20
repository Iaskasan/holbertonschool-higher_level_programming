#!/usr/bin/python3
'''Module for the division of a matrix'''


def matrix_divided(matrix, div):
    '''this method divides each element of a matrix by an int/float div'''
    new_matrix = []
    if not isinstance(matrix, list) or len(matrix) == 0 or not\
        all(isinstance(row, list) for row in matrix) or not\
            all(isinstance(element, (int, float))
                for row in matrix for element in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)
    return new_matrix
