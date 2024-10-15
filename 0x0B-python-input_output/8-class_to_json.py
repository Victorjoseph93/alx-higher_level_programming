#!/usr/bin/python3
"""Task 8 of ALX Project(Python - Input/Output)

This module defines a class-to-JSON function.

"""


def class_to_json(obj):
    """Return the dictionary representation of an object
    for JSON serialization.

    Args:
        obj (any): the object to be represented

    """
    return obj.__dict__
