#!/usr/bin/python3
'''a function that indent a text after each . : or ? character'''


def text_indentation(text):
    '''indent the input string by adding new lines and removing spaces'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    next_is_space = False
    for char in text:
        if char in (".", "?", ":"):
            print(char)
            print()
            next_is_space = True
        elif next_is_space:
            next_is_space = False
            continue
        else:
            print(char, end="")
