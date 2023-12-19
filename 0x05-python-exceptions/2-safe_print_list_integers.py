#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    sum_total = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end='')
            sum_total += 1
        except (TypeError, ValueError):
            continue
    print()
    return sum_total
