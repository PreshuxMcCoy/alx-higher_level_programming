#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum_total = a / b
    except ZeroDivisionError:
        sum_total = None
    finally:
        print("Inside result: {}".format(sum_total))
        return sum_total
