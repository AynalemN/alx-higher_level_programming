#!/usr/bin/python3


"""Addition"""


def add_integer(a, b=98):
    """adding two numbers"""
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
