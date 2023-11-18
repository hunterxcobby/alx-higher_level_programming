#!/usr/bin/python3

"""
Rectangle Class Module that inherits from Base:

Init Superclass' `id` (Base)
Private instance attributes, each with its own public getter and setter:
__width -> width, __height -> height, __x -> x, __y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Contain public methods of area and display:
def area(self): that returns the area value of the Rectangle instance
def display(self): prints Rectangle instance to stdout with the `#` character
:- improve display method to take care of x and y.
Update Rectangle class by overriding the __str__ method
so that it returns "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
Contain public method: def update(self, *args, **kwargs):
that assigns a key/value argument to attributes: if *args,
set attrs in this order arg1=id, arg2=width, arg3=height, arg4=x, arg5=y
if no args given, set according to kwargs.
Add public method def to_dictionary(self):
that returns the dictionary representation of a Rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """
    Defines Rectangle class that inherits from base.
    Inherited attribute of: id
    Class attributes of:
        __width, __height, __x & __y
    Public methods of:
        area(), display(), __str__, update(*args, **kwargs)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # call superclass constructor with id parameter
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Set public getters and setters for each attribute
    # Width
    @property
    def width(self):
        """ Getter for width.
        Return: width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format('width'))
        if value <= 0:
            raise ValueError("width must be > 0")
        # update private instance atrribute
        self.__width = value

    # Height
    @property
    def height(self):
        """Getter for height.
        Return: height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        # update private instance attribute
        self.__height = value

    # X
    @property
    def x(self):
        """Getter for X
        Return: x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter fo x.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        # update private instance attribute
        self.__x = value

    # Y
    @property
    def y(self):
        """Getter for Y
        Return: y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        # update private instance attribute
        self.__y = value

    # Public Methods:
    # Area
    def area(self):
        """Calculate and returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    # Display
    def display(self):
        """Function that display(print) to stdout
        the Rectangle instance with the `#` character."""
        [print() for j in range(self.__y)]
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    # __str__
    def __str__(self):
        """Return string representation of Rectangle class instance.
        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[{:s}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height))

    # *Args
    def update(self, *args, **kwargs):
        """Assign arguments to attributes in the order:
        args1: id, args2: width, args3: height, args4: x, args5: y
        or kwargs if args not given."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            keys = ['id', 'width', 'height', 'x', 'y']
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key in keys:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Function to return dictionary representation of Rectangle instance.
        Returns:
            dict: Dictionary containing id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
