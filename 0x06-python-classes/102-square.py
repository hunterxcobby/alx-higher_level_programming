#!/usr/bin/python3

"""
Class Square that defines a square by private instance attribute: size
Methods Getter and Setter properties for size.
property def size(self): to retrieve it
property setter def size(self, value): to set it:
And a Public instance method: def area(self):
that returns the current square area
`Square` instance can answer to comparators:
==, !=, >, >=, < and <= based on the square area
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
        if not isinstance(value, (float, int)):
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

    # functions for comparators based on square area
    def __eq__(self, other):
        """
        Compares current square with next
        and return if both are equal
        """
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        if isinstance(other, Square):
            return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares squares and return if current is less than next
        """
        if isinstance(other, Square):
            return self.area() < other.area()

    def __lteq__(self, other):
        """
        Compares squares and return if curr is less than
        OR equal to the next
        """
        if isinstance(other, Square):
            return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares squares and return if current is greater than next
        """
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares squares and return if curr is greater than
        OR equal to the next
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
