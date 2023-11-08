#!/usr/bin/python3

"""
Student class Module (based on 9-student.py) that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names
contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module
"""


class Student:
    """
    Class that defines a Student
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize the class objects
        Args: first_name, last_name & age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dict representation of Student instance
        """
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elements], str) for elements in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
