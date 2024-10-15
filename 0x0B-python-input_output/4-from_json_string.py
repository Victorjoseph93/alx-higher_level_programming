#!/usr/bin/python3
"""Task 4 of ALX Project(Python - Input/Output)

This module defines a function that creates an object from a JSON string

"""
import json


def from_json_string(my_str):
    """Generate an object from a JSON string.

    Args:
        my_str (str): The JSON representation

    Returns:
        The object

    """
    return json.loads(my_str)
