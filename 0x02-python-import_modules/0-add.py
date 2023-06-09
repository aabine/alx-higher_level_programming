#!/usr/bin/python3
# main.py

# Assigning values to variables a and b
a = 1
b = 2

# Importing the add function from add_0.py
if __name__ == "__main__":
    from add_0 import add

    # Calling the add function
    result = add(a, b)

    # Printing the result
    print("{} + {} = {}".format(a, b, result))
