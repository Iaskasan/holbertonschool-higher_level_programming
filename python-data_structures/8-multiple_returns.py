#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    first = sentence[0]

    if len(sentence) == 0:
        first = None
        return (first)
    return (lenght, first)
