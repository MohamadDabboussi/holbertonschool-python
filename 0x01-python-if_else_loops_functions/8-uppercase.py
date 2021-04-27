#!/usr/bin/python3
def uppercase(str):
    for x in str:
        flag = 0
        if 97 <= ord(x) <= 122:
            flag = 32
        print('{:c}'.format(ord(x) - flag), end="")
    print()
