#!/usr/bin/python3
"""Task 6 of ALX Project(Python - Input/Output)

This module defines a function that reads from a JSON file.

"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file

    Args:
        filename (str): The path to the file

    Returns:
        any: The created object

    """
    with open(filename, "r", encoding="utf-8") as jsonFile:
        jsonString = jsonFile.read()
        return json.loads(jsonString)
