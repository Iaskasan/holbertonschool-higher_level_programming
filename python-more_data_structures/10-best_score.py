#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dic = sorted(a_dictionary.values())
    last_val = int(sorted_dic[-1])
    for key, value in a_dictionary.items():
        if value == last_val:
            return key
