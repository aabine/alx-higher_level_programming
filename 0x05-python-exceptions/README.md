0x05. Python - Exceptions

Author: Austine Abine

# Python - Exceptions

Functions for Handling Exceptions
This repository contains several functions for handling exceptions in Python.

raise_exception_msg(message="")
This function raises a NameError exception with the given message.

Parameters
message (str, optional) - The message to include with the exception. Defaults to an empty string.
Returns
None

raise_exception()
This function raises a TypeError exception with a default message indicating that it was raised intentionally.

Parameters
None

Returns
None

list_division(my_list_1, my_list_2, list_length)
This function divides the corresponding elements of two lists, and returns a new list with the results.

Parameters
my_list_1 (list) - The first list to divide.
my_list_2 (list) - The second list to divide.
list_length (int) - The length of the lists.
Returns
A new list with the results of the division.
safe_print_division(a, b)
This function safely divides two numbers and prints the result.

Parameters
a (int or float) - The numerator of the division.
b (int or float) - The denominator of the division. It must not be zero.
Returns
float or None - The result of the division if it was successful. None otherwise.
safe_print_list_integers(my_list=[], x=0)
This function prints the first x integers of a list.

Parameters
my_list (list, optional) - The list to print. Defaults to an empty list.
x (int, optional) - The number of integers to print. Defaults to 0.
Returns
None

safe_print_integer(value)
This function safely prints an integer.

Parameters
value (int) - The integer to print.
Returns
None

safe_print_list(my_list=[], x=0)
This function prints the first x elements of a list.

Parameters
my_list (list, optional) - The list to print. Defaults to an empty list.
x (int, optional) - The number of elements to print. Defaults to 0.
Returns
None
