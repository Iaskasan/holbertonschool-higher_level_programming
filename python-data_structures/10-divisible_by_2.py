#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []
    for element in my_list:
        result.append(element % 2 == 0)
    return result
