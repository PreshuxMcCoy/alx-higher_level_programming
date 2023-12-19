#!/usr/bin/python3
import sys


def safe_print_integer_err(sum_total):
    try:
        print("{:d}".format(sum_total))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
