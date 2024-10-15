#!/usr/bin/python3
"""Task 0 of ALX Project(Python - Input/Output)

This module defines a function that outputs the contents of a file.

"""


def read_file(filename=""):
    """Read a file and print the contents to stdout.

    Args:
        filename (str): The path to the file

    """
    with open(filename, encoding="utf-8") as thisFile:
        print(thisFile.read(), end="")
