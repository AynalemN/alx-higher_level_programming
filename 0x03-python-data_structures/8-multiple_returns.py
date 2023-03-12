#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = sentence[0]
    if leng > 0:
        return (leng, first_char)
    else:
        return None
