#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    a = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] != my_list[i - 1]:
            a += my_list[i]
    return a
