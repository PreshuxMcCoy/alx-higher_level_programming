#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and returns its value"""
    last_number = abs(number) % 10
    print("{}".format(last_number), end="")
    return last_number
