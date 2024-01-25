#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = sys.argv
    if (len(argc) -1) == 0:
        print("{} argument.".format(len(argc) - 1))
    elif (len(argc) - 1) < 2:
        print("{} argument:".format(len(argc) - 1))
    else:
        print("{} arguments:".format(len(argc) - 1))
    for i in range(len(argc) - 1):
        arg_count = i + 1
        print("{}: {}".format(i + 1, sys.argv[arg_count]))
