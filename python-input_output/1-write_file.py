#!/usr/bin/python3
"""oui oui oui"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, "w") as f:
        f.write(text)
