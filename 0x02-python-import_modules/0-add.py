#!/usr/bin/python3

# Importing the add function from add_0.py
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    # Calling the add function
    result = add(a, b)

    # Printing the result
    print("{} + {} = {}".format(a, b, result))
