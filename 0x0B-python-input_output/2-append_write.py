#!/usr/bin/python3
"""Task 2 of ALX Project(Python - Input/Output)

This module defines a function that modifies a file.

"""


def append_write(filename="", text=""):
    """Append some text to a specified file.
        Create the file if it doesn't exist.

    Args:
        filename (str): The path to the file
        text (str): The text that is to be appended to the file

    """
    with open(filename, "a", encoding="utf-8") as thisFile:
        return thisFile.write(text)
