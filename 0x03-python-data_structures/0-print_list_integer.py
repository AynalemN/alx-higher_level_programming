#!/usr/bin/python3
def print_list_integer(my_list=[]):
    leng = len(my_list)
    for i in range(0, leng):
        print('{:d}'.format(my_list[i]), end='\n')
