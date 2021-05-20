#!/usr/bin/python3


def canUnlockAll(boxes):
    i = 0
    keys = [0]
    while(i < len(keys)):
        for key in boxes[keys[i]]:
            if not key in keys:
                keys.append(key)
        i = i+1
    if len(keys) == len(boxes):
        return True
    else:
        return False
