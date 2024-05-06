#!/usr/bin/python3
def uppercase(c):
    for char in c:
        ascii_value = ord(char)
        if ascii_value > 96:
            ascii_value -= 32
        print(chr(ascii_value), end="")
    print()
