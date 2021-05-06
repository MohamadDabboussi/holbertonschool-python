#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    err = False
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            err = True
            break
    print("")
    if err == False:
        return i+1
    return i
