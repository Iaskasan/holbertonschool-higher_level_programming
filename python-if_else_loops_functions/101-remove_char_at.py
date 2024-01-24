#!/usr/bin/python3
def remove_char_at(str, n):
    result_str = ''
    for i in range(len(str)):
        if i != n:
            result_str += str[i]
    return (result_str)
