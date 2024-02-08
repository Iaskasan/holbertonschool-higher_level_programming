#!/usr/bin/python3
"""text indent module"""


def text_indentation(text):
    """indentation text function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    in_sentence = False

    for char in text:
        if char in ('.', '?', ':'):
            in_sentence = False
            print(char, end="")
            print('\n')
        elif char == ' ' and not in_sentence:
            continue
        else:
            in_sentence = True
            print(char, end="")
