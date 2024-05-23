#!/usr/bin/python3
'''Module for the class MyList'''


class MyList(list):
    '''class MyList'''

    def print_sorted(self):
        new_list = print(sorted(self))
        return new_list
