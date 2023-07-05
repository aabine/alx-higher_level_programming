#!/usr/bin/python3

# Import the add_integer function from the 0-add_integer module
add_integer = __import__('0-add_integer').add_integer

# Usage Examples from the documentation

# Addition of Integers
print(add_integer(2, 3))    # Expected output: 5
print(add_integer(-2, 5))   # Expected output: 3

# Addition of Floats
print(add_integer(2.0, 3.0))    # Expected output: 5
print(add_integer(-2.5, 3.2))   # Expected output: 1

# Mixing Integers and Floats
print(add_integer(2, 3.5))    # Expected output: 5
print(add_integer(2.9, 3))    # Expected output: 5

# Optional Second Argument
print(add_integer(2))    # Expected output: 100

# Non-Numbers Handling
try:
    add_integer("hello", 3)
except TypeError as e:
    print(e)    # Expected output: "a must be an integer"

try:
    add_integer(2, "hello")
except TypeError as e:
    print(e)    # Expected output: "b must be an integer"

try:
    add_integer(None)
except TypeError as e:
    print(e)    # Expected output: "a must be an integer"

try:
    add_integer(2.3, None)
except TypeError as e:
    print(e)    # Expected output: "b must be an integer"

try:
    add_integer("hello", "there")
except TypeError as e:
    print(e)    # Expected output: "a must be an integer"

# Handling Infinity and NaN
try:
    add_integer(float('inf'))
except OverflowError as e:
    print(e)    # Expected output: "cannot convert float infinity to integer"

try:
    add_integer(2, float('inf'))
except OverflowError as e:
    print(e)    # Expected output: "cannot convert float infinity to integer"

try:
    add_integer(float('nan'))
except ValueError as e:
    print(e)    # Expected output: "cannot convert float NaN to integer"

try:
    add_integer(2, float('nan'))
except ValueError as e:
    print(e)    # Expected output: "cannot convert float NaN to integer"
