#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = sentence[0]
    if leng > 0:
        r = leng, first_char
        return r
    else:
        r = leng, None
        return r
