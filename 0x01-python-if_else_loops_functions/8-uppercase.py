#!/usr/bin/python3

def uppercase(str):
    char_printed = ""
    for characters in str:
        if ord('a') <= ord(characters) <= ord('z'):
            converted_str = chr(ord(characters) - ord('a') + ord('A'))
            char_printed += converted_str
        else:
            char_printed += characters
    print("{}".format(char_printed))