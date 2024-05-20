#!/usr/bin/python3
'''a function that indent a text after each . : or ? character'''


def text_indentation(text):
    '''indent the input string by adding new lines and removing spaces'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = False
    for char in text:
        if char == ' ' and prev:
            prev = False
            continue
        elif char in (".", "?", ":"):
            print(char)
            print()
            prev = True
        else:
            print(char, end="")
