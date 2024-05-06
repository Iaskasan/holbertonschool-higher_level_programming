#!/usr/bin/python3
def uppercase(c):
    for char in c:
        ascii = ord(char)
        if ascii > 96:
            ascii -= 32
        print(chr(ascii), end=''.format())
    print("\n".format(), end='')
