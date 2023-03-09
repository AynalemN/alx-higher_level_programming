#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    sum = 0
if argc == 0:
    print(f'{int(argc)}')
for i in range(1, argc):
    sum += int(argv[i])
print(f'{sum: d}')
