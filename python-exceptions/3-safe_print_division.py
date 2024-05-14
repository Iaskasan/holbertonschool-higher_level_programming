#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0
        c = a / b
    except (UnboundLocalError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(c))
        if c == 0:
            return None
        return c
