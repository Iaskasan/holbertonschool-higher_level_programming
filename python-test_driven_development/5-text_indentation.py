#!/usr/bin/python3
'''a function that indent a text after each . : or ? character'''


def text_indentation(text):
    '''indent the input string by adding new lines and removing spaces'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = [".", "?", ":"]
    for i in range(len(text)):
        if text[i] in char:
            print(text[i])
            print()
        elif text[i] is " " and text[i - 1] is " ":
            continue
        elif text[i] is " " and text[i - 1] not in char:
            print(" ", end="")
        elif text[i] is " " and text[i - 1] in char:
            continue
        else:
            print(text[i], end="")
