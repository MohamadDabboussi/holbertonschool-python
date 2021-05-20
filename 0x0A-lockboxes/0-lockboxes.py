#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        for x in boxes[key]:
            if x < len(boxes):
                if x not in keys:
                    keys.append(x)
    if len(keys) != len(boxes):
        return False
    return True
