#!/usr/bin/python3
"""Real defination of a Rectangle class based on 0-rectangle.py"""


class Rectangle:
    """class that define a rectangle """

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
