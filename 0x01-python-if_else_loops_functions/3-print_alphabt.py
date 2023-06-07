#!/usr/bin/python3

alphabets = ''

for counter in range(97, 122 + 1):
    if chr(counter) == 'e' or chr(counter) == 'q':
        continue
    alphabets += chr(counter)
print("{}".format(alphabets), end="")
