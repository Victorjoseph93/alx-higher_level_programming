#!/usr/bin/python3
"""Task 3 of ALX Project(Python - Classes and Objects)

This module defines a class.

"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Default to 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the area of the square

        Returns:
            Area of square

        """
        return self.__size ** 2
