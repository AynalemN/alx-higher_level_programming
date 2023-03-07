#!/usr/bin/python3
def uppercase(str):
    for alp in str:
        if ord(alp) >= ord('a') and ord(alp) <= ord('z'):
            alp = chr(ord(alp) - 32)
        print("{}".format(alp), end="")
    print()
