#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items()))
    print(sorted_dic)
    # for i in range(len(a_dictionary)):
    #     print(sorted_dic.items())