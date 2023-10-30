#!/usr/bin/python3

"""
Create class Rectangle that defines a rectangle by
everything from Module 8-rectangle
and expanding that to include:
Class method that returns a new Rectangle instance with
`width == height == size`
"""


class Rectangle:
    """
    Instantiating variables of width and height

    Class attribute to keep track of number of instances:
        number_of_instances

    Class attributre to set a default symbol for printing
    Args:
        width (int)
        height (int)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        # initialize private attributes
        self.width = width
        self.height = height
        # increment Rectangle population at instantiation
        Rectangle.number_of_instances += 1

    @property
    def width(self):  # property to retrive width
        return self.__width

    @width.setter  # setter method for width
    def width(self, value):
        # verify that value is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("width must be an integer")
        # check that value is >= 0
        if value < 0:
            raise ValueError("width must be >= 0")
        # update private instance attribute
        self.__width = value

    @property
    def height(self):  # property to retrive height
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        # verify that value is an integer
        if type(value) is not int or isinstance(value, (float, bool)):
            raise TypeError("height must be an integer")
        # check that value is >= 0
        if value < 0:
            raise ValueError("height must be >= 0")
        # update private instance attribute
        self.__height = value

    def area(self):
        """
        Calculate the area of rectangle
        based on valid widths and heights provided.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of rectangle
        based on valid widths and heights given.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print out a rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""

        for r in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]  # to remove the trailing newline

    def __repr__(self):
        """String representation of the rectangle
        to recreate new instance.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Recognize if a rectangle is being deleted
        and print message.
        """
        print("Bye rectangle...")
        # decrement Rectangle population at deletion
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Method to determine the biggest rectangle
        Args:
            rect_1: a class Rectangle instance
            rect_2: a class Rectangle instance
        Return: biggest rect based on area.
        """
        # verify that bothe rects are instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        # determine the bigger rectangle
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Method that allows us to create a new instance
        representing a square with the same width and height (size)
        """
        return cls(size, size)
