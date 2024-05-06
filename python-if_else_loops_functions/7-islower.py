#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if ascii_value < 97:
        return False
    else:
        return True
