#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Classes and Objects)

This module defines a class.

"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        """
        self.__size = size
