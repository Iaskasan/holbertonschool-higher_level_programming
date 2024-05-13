#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) < 2:
        print()
    i = len(matrix[0])
    for j in range(i):
        for k in range(i):
            if k == i - 1:
                print("{:d}".format(matrix[j][k]))
            else:
                print("{:d}".format(matrix[j][k]), end=", ")
