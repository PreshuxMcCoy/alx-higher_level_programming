#!/usr/bin/python3

for tens_number in range(9):
    for ones_number in range(tens_number + 1, 10):
        if tens_number * 10 + ones_number < 89:
            print("{:d}{:d}".format(tens_number, ones_number), end=", ")
print("{:d}".format(89))
