#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "m", getattr(magic_string, "m", -1) + 1)
    return "Holberton" + ", Holberton" * magic_string.m
