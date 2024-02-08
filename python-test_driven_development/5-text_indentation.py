#!/usr/bin/python3
"""indent texts"""


def text_indentation(text):
    """indentation text function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Variable to track if we are currently in a sentence
    in_sentence = False

    for char in text:
        # Check for sentence-ending punctuation
        if char in ('.', '?', ':'):
            in_sentence = False
            print(char, end="")
            print('\n')
        # Check for space at the beginning of a sentence
        elif char == ' ' and not in_sentence:
            continue
        # If not a space and not the end of a sentence, set in_sentence to True
        else:
            in_sentence = True
            print(char, end="")
    print()
