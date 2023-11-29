#!/usr/bin/python3
for alph in range (97, 123):
    if alph == 101 or alph == 113:
        alph += 1
        continue
    else:
        print("{:c}".format(alph), end="")
        alph += 1
