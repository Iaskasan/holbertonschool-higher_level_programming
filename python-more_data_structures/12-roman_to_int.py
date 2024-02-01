#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    roman_numbers = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        value = roman_numbers[roman_string[i]]
        if result == 0:
            prev_value = value
        else:
            prev_value = roman_numbers[roman_string[i - 1]]
        if value > prev_value:
            result += value
        else:
            result -= value
    return abs(result)
