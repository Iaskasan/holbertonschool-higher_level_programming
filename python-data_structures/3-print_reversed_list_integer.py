#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for elements in my_list:
        print("{:d}".format(elements))
