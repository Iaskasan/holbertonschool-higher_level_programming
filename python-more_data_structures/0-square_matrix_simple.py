#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            squared_element = element ** 2
            new_row.append(squared_element)
        new_matrix.append(new_row)
    return new_matrix
