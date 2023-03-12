#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = sentence[0]
    if leng == 0:
        return None
    else:
        return leng, first_char
