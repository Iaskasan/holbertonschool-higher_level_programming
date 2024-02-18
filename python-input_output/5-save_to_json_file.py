#!/usr/bin/python3
"""oui oui oui"""
import json


def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
