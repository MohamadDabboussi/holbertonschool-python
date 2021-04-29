#!/usr/bin/python3
import sys


def main(argv):
    Num_arg = len(argv)
    result = str(Num_arg)
    result += ' argument' if Num_arg == 1 else ' arguments'
    result += '.' if Num_arg == 0 else ':'
    print(result)
    for i in range(Num_arg):
        print('{:d}: {}'.format(i + 1, argv[i]))

if __name__ == '__main__':
    main(sys.argv[1:])
