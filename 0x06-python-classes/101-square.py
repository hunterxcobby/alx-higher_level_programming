#!/usr/bin/python3

"""
class Square that defines a square
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Private instance attribute: position
which takes a default (0, 0) tuple.
property def position(self): to retrieve it
property setter def position(self, value): to set it:

And a Public instance method: def area(self):
that returns the current square area
Method my_print prints the square using "#".
"""


class Square:
    """initializes square, determines size, calculates area, prints"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes instance of square
        Args:
            size: size of square
            position: position to indent square"""
        self.__size = size
        self.__position = position

    def area(self):
        """Determines area"""
        result = self.__size ** 2
        return result

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1]:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """prints square offsetting it by position with symbol #"""
        if self.size == 0:
            print('')
            return
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))

    def __str__(self):
        """prints square offsetting it by position with symbol #"""
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
