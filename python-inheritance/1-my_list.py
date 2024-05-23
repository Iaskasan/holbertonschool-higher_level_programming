#!/usr/bin/python3
'''Module for the class MyList'''


class MyList(list):
    '''class MyList'''

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
        return new_list

new = MyList.print_sorted([1, 2, 4, 6])
# [1, 2, 4, 6]
print(isinstance(new, list))