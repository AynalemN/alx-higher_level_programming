#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_Tuple = tuple_a + ('0', '0')
    b_Tuple = tuple_b + ('0', '0')

    sum1 = int(a_Tuple[0]) + int(b_Tuple[0])
    sum2 = int(a_Tuple[1]) + int(b_Tuple[1])

    return sum1, sum2
