#!/usr/bin/python3
"""Task 5 of ALX Project(Python - Input/Output)

This module defines a function that writes to a JSON file.

"""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of an object to a file.

    Args:
        my_obj (any): The object
        filename (str): The path to the file

    """
    with open(filename, "w", encoding="utf-8") as jsonFile:
        jsonFile.write(json.dumps(my_obj))
