#!/usr/bin/python3
"""oui oui oui"""
import json


def load_from_json_file(filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, "r") as f:
        file = json.load(f)
        return file
