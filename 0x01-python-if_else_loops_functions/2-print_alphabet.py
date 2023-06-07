#!/usr/bin/python3

alphabets = ''
for alphabet in range(97, 122 + 1):
    alphabets += chr(alphabet)

print("{}".format(alphabets), end="")