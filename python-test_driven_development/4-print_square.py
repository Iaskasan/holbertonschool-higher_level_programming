#!/usr/bin/python3
'''a function that prints a square with a given size'''


def print_square(size):
    '''prints a square with # as character'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size > 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
