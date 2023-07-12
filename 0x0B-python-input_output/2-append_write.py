#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8) and returns the number of characters added to the file"""

def append_write(filename="", text=""):
    """
    function that appends a text file (UTF8) 
    Args:
        filename: name of the file to write to
        text: string to write to the file
    Returns:
        number of characters written to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
    