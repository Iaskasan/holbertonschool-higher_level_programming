#!/usr/bin/python3
'''a function that indent a text after each . : or ? character'''


def text_indentation(text):
    '''indent the input string by adding new lines and removing spaces'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = False
    for char in text:
        if char == ' ' and prev:
            print(char)
            prev = False
        elif char in (".", "?", ":"):
            print(char, end="")
            print()
            prev = True
        else:
            print(char, end="")
