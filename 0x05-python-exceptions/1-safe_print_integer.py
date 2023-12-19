#!/usr/bin/python3
def safe_print_integer(sum_total):
    try:
        print("{:d}".format(sum_total))
        return True
    except (ValueError, TypeError):
        return False
