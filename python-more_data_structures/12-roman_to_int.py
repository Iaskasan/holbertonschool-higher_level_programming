#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return None
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
            }
    result = 0
    str_list = list(roman_string)
    Bool = False
    for i in range(len(str_list)):
        if i + 1 < len(str_list):
            if str_list[i + 1] != "I":
                Bool = True
        for key, value in dict.items():
            if Bool:
                result -= 1
                Bool = False
            elif key == str_list[i] and Bool is False:
                result += value
    return result
