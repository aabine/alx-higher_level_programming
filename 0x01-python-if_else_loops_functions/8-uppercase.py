#!/usr/bin/python3

def is_upper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        print("{}".format(c), end=" ")
    else:
        print("{}\n".format(c), end=" ")