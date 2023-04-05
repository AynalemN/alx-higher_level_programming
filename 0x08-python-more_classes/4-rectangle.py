#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 3-rectangle.py"""


class Rectangle:
    """defining area and perimeter"""

    def __init__(self, width=0, height=0):
        """Initalize width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """return area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """ return the perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):
        """string representation"""
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        for i in range(self.height):
            for j in range(self.width):
                print("#", end='')
            if i != self.height - 1:
                print()
        return string[:-1]

    def __repr__(self):
        """representation to enable creating new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
