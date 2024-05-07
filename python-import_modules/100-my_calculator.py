#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

def parser(a, op, b):
    result = 0
    if op == "+":
        result = add(a, b)
    if op == "-":
        result = sub(a, b)
    if op == "*":
        result = mul(a, b)
    if op == "/":
        result = div(a, b)
    print(f"{a} {op} {b} = {result}")

if __name__ == "__main__":
    operator = argv[2]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        parser(int(argv[1]), operator, int(argv[3]))
