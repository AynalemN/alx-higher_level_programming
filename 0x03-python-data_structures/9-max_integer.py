#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for idx in range(0, len(my_list)):
            if my_list[idx] < my_list[idx + 1]:
                return my_list[idx + 1]
            else:
                return my_list[idx]
