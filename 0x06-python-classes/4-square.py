#!/usr/bin/python3

"""
Create class Square that defines a square by private instance attribute: size
And a Public instance method: def area(self):
that returns the current square area
Methods Getter and Setter properties for size.
property def size(self): to retrieve it
property setter def size(self, value): to set it:
"""


class Square:
    """
    Instantiating the variables self and size.
    Raising errors if conditions are not met.
    """
    def __init__(self, size=0):
        # Initialize private attribute
        self.__size = size

    @property  # property to retrieve size
    def size(self):
        return self.__size

    @size.setter  # Setter method for size
    def size(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if value is >= 0
        if value < 0:
            raise ValueError("size must be >= 0")

        # Update the private instance attribute
        self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)
