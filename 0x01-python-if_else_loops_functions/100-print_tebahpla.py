#!/usr/bin/python3
for alphabet in range(ord('z'), ord('a') - 1, -1):
    if (alphabet % 2 == 0):
        print("{}".format(chr(alphabet)), end="")
    else:
        print("{}".format(chr(alphabet - 32)), end="")
