#!/usr/bin/python3
import sys


def main(argv):
    Num_arg = len(argv)
    result = 0
    for i in range(Num_arg):
        result += int(argv[i])
    print('{:d}'.format(result))

if __name__ == '__main__':
    main(sys.argv[1:])
