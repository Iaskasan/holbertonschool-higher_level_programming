#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    if len(my_list) == 0:
        return 0
    a = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] != my_list[i - 1]:
            a += my_list[i]
    return a
    
my_list = [1, 1, 2]
result = uniq_add(my_list)
print("Result: {:d}".format(result))