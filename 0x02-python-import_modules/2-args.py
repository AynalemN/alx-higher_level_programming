#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
if argc == 1:
    print(f'{(argc -1):d} arguments.')
else:
    if argc == 2:
        print(f'{(argc - 1):d} argument:')
    else:
        print(f'{(argc - 1):d} arguments:')
    for i in range(1, argc):
        print('{}: {}'.format(i, argv[i]))
