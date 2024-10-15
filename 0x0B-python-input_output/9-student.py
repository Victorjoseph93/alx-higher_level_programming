#!/usr/bin/python3
"""Task 9 of ALX Project(Python - Input/Output)

This module defines a student class.

"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of a Student"""
        return self.__dict__
