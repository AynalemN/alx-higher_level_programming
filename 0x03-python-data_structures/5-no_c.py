#!/usr/bin/python3
def no_c(my_string):
    return_str = []
    for letter in my_string:
        if letter != "c" and letter != "C":
            return_str.append(letter)
    return ''.join(return_str)
