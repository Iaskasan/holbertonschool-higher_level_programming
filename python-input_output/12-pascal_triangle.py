#!/usr/bin/python3
"""oui oui oui"""


def pascal_triangle(n):
    """pascal triangle doc"""
    triangle = [[1]]

    for _ in range(1, n):
        row = [1]
        prev_row = triangle[-1]

        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)
        triangle.append(row)
    return triangle
