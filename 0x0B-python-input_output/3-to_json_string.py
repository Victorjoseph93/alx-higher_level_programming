#!/usr/bin/python3
"""Task 3 of ALX Project(Python - Input/Output)

This module defines a function that implements json representation.

"""
import json


def to_json_string(my_obj):
    """Generate a JSON representation of an object.

    Args:
        my_obj (any): The object to be represented

    Returns:
        The JSON representation

    """
    return json.dumps(my_obj)
