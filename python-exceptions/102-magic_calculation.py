#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if i < a:
            raise Exception("Too far")
        result = a ** b / i
        result = b + a
        break
    return result
