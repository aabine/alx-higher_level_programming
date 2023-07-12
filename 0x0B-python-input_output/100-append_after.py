#!/usr/bin/python3
""" inserts a line of text to a file, after each line containing a specific string """

def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file, after each line containing a specific string

    Args:
        filename: name of the file to write to
        search_string: string to search for 
        new_string: string to insert after the search_string

    Returns:
        number of characters written to the file
    """
    file = ""
    with open(filename) as r:
        for line in r:
            file += line
            if search_string in line:
                file += new_string
    with open(filename, "w") as w:
        w.write(file)
