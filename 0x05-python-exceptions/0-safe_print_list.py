#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum_total = 0

    for element in my_list:
        if sum_total < x:
            try:
                print(f"{element}", end='')
                sum_total += 1
            except IndexError:
                break
    print()
    return sum_total
