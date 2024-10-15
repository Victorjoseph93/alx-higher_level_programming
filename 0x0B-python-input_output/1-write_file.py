#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Input/Output)

This module defines a function that writes to a file.

"""


def write_file(filename="", text=""):
    """Write some text to a specified file.

    Args:
        filename (str): The path to the file
        text (str): The text that is to be written to the file

    """
    with open(filename, "w", encoding="utf-8") as thisFile:
        return thisFile.write(text)
