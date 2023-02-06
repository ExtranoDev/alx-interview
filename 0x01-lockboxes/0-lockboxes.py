#!/usr/bin/python3
"""Script solves the lockbox problem
"""


def canUnlockAll(boxes):
    """method determines if all the boxes can be opened
        Args: boxes (list of list) - contains box to be opened"""

    box_length = len(boxes)
    box_cmp = [boxes[0]]
    index = 0

    for box in boxes:
        if boxes[index] == []:
            break
        for val in box:
            if val < box_length:
                if boxes[val] not in box_cmp:
                    box_cmp.append(boxes[val])
                    index = val
                break
            else:
                return False
    if len(box_cmp) == box_length:
        return True
    else:
        return False
