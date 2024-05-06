#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("{} arguments.".format(len(argv)))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv)))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments.".format(len(argv)))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
