#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                i -= 1
                continue
    except TypeError:
        pass
    print()
    return i
