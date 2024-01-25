#!/usr/bin/python3
import sys
if __name__ == "__main__":
    final_value = 0
    args = sys.argv

    for i in range(1, len(args)):
        final_value += int(args[i])
    print(final_value)
