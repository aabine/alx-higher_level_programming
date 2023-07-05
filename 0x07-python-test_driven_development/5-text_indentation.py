def text_indentation(text):
    """
    Takes a string `text` as input and performs text indentation.

    Parameters:
    - text (str): The string to be indented.

    Raises:
    - TypeError: If `text` is not a string.

    Returns:
    - str: The indented text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0
    result = ""
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        result += text[index]
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                result += "\n"
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1

    return result
