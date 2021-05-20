#!/usr/bin/python3


def recursive_unlock(k, keys, boxes):
    if k == []:
        return 0
    boxkeys = boxes[k[0]]
    kk = list(set(boxkeys)-set(keys))
    keys = list(set().union(keys, boxkeys))
    k.pop(0)
    return 1 + recursive_unlock(k, keys, boxes) + recursive_unlock(kk, keys, boxes)


def canUnlockAll(boxes):
    keys = [0]
    nb = recursive_unlock(keys, keys, boxes)
    if nb == len(boxes):
        return True
    else:
        return False
