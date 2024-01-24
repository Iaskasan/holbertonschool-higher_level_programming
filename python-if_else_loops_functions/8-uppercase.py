#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""

    for char in input_str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            uppercase_char = chr(ascii_val - 32)
            result_str += uppercase_char
        else:
            result_str += char

    print(result_str, end='\n')
