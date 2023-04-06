#!/usr/bin/python3
"""A class Rectangle that defines a rectangle based on 6-rectangle.py"""


class Rectangle:
    """defining area and perimeter"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initalize width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                print(self.print_symbol, end='')
            if i != self.height - 1:
                print()
        return string[:-1]

    def __repr__(self):
        """representation to enable creating new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Deleting"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
