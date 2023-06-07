#!/usr/bin/python3

def uppercase(str):
    for characters in str:
        if ord(characters) >= 97 or ord(characters) <= 122:
            converted_str = characters.upper()
            print("{}".format(converted_str), end= "")
    print()