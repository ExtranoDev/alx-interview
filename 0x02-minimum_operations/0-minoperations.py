#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer
        If n is impossible to achieve, return 0
    """
    def_char = 'H'
    target = n * 'H'
    temp = ''
    ops = 0
    while len(def_char) < len(target):
        if len(target) % len(def_char) == 0:
            ops += 2
            temp = def_char
            def_char *= 2
        if len(target) % len(def_char) != 0:
            ops += 1
            def_char += temp
    return ops
