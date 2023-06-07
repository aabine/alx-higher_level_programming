#!/usr/bin/python3

def uppercase(str):
    for characters in str:
        if ord('a') <= ord(characters) <= ord('z'):
            converted_str = chr(ord(characters) - ord('a') + ord('A'))
            print("{}".format(converted_str), end="")
        else:
            print("{}".format(characters), end="")
    print()
