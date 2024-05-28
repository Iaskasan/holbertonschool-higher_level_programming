#!/usr/bin/python3
'''function that creates a pascal triangle'''


def pascal_triangle(n):
    '''n is the number of row of the pascal triangle'''
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
