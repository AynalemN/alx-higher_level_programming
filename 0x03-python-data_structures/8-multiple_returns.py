#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        r = len(sentence), sentence[0]
        return r
    else:
        r = len(sentence), None
        return r
