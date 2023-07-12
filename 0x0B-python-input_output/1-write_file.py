#!/usr/bin/python3
""" script the write a string to a text file (UTF8) and return the number of characters """

def write_file(filename="", text=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file to write to
        text: string to write to the file

    Returns:
        number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
