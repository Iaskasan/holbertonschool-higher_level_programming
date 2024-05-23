#!/usr/bin/python3
'''a function that indent a text after each . : or ? character'''


def text_indentation(text):
    '''indent the input string by adding new lines and removing spaces'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print("\n")
        elif char is " ":
            continue
        else:
            print(char, end="")
