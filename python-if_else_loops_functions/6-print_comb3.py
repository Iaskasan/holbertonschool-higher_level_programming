#!/usr/bin/python3
for last_digit in range(0, 90):
    if last_digit / 10 < last_digit % 10:
        if last_digit < 89:
            print("{:02d}".format(last_digit), end=", ")
        else:
            print("{:02d}".format(last_digit))
