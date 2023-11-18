#!/usr/bin/python3

"""
Square Class Module that inherits from Rectangle:
Inits superclass' id, width (as size), height (as size), x, y
Class constructor: __init__(self, size, x=0, y=0, id=None)
Contains public attribute size
Contain public method of:
update(*args, **kwargs)
to_dictionary(self)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines Square class that inherits from Rectangle.
    Inherited attributes of:
        id (Base), __width, __height, __x & __y
    Inherited methods of:
        Base.init(self, id=None);
        Rectangle.init(self, width, height, x=0, y=0, id=None);
        update(self, *args, **kwargs); width(self), width(self, value);
        height(self), height(self, value); x(self), x(self, value);
        y(self), y(self, value); area(self); display(self);
    Class Attribute:
        size
    Class Method:
        update(*args, **kwargs)
        to_dictionary(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        Args:
            size (int): Size of the square.
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        # call superclass constructor with all parameters
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for Size.
        Return: size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size. Same validations as width/height from superclass.
        Raise exceptions where value is not an int or < 0."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Print out string representation of the Square instance.
        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Assign arguments or keyword args to attribute.
        Args:
            *args: positional arguments in this order - id, size, x, y.
            **kwargs: keyword arguments to assign attributes (attribute=value).
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            keys = ['id', 'size', 'x', 'y']
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key in keys:
                        setattr(self, key, value)

    def to_dictionary(self):
        """Function to return dictionary representation of Square instance.
        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.width,  # size is the same as width
            'x': self.x,
            'y': self.y
        }
