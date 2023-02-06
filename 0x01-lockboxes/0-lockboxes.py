#!/usr/bin/python3
"""Script solves the lockbox problem
"""


def canUnlockAll(boxes):
    """method determines if all the boxes can be opened
        Args: boxes (list of list) - contains box to be opened"""

    if type(boxes) is not list:
        return False
    unboxed = [0]
    for i in unboxed:
        for box in boxes[i]:
            if box not in unboxed and box < len(boxes):
                unboxed.append(box)
    print(unboxed)
    return (len(unboxed) == len(boxes))
