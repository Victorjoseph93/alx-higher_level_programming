#!/usr/bin/python3
"""This module defines the class ``Student``.
"""


class Student:
    """This class represents a Student object.
    """
    def __init__(self, first_name, last_name, age):
        """This method initiates the Student class instance
        with the values (first_name, last_name, age)
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The student's age in years.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method retrieves a dictionary representation of a
        student instance.
        Args:
            attrs (list): optional argument list of strings.
        """
        if attrs is None:
            return (self.__dict__)
        else:
            picked_dict = dict()
            for key in attrs:
                if key in self.__dict__.keys():
                    picked_dict[key] = self.__dict__.get(key)
            return picked_dict

    def reload_from_json(self, json):
        """This method replaces all attributes of student instance.
        Args:
            json (str): The json representation of the dict that'll
                replace the Student instance attributes.
        """
        for key, value in json.items():
            self.__dict__[key] = value
