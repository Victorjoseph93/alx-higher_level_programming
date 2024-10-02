#!/usr/bin/python3
"""Task 5 of ALX Project(Python - Classes and Objects)

This module defines a class.

"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int, optional): The size of the new square. Default to 0

        """

        self.__size = size

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    def area(self):
        """Get the current area of the square

        Returns:
            Area of square

        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with # character"""
        if self.__size == 0:
            print()
            return
        [print("{}".format("#" * self.__size)) for i in range(self.__size)]
