#!/usr/bin/python3
"""
Script reads stdin line by line and logs metrics
"""

import sys

DEF_VAL = 9
count = 0
status = {"fsize": 0, "codes": dict()}


def printer(status):
    """
    Outputs formatted log
    """
    print("File size: {}".format(status["fsize"]))
    status["codes"] = dict(sorted(status["codes"].items()))
    for code, val in status["codes"].items():
        print("{}: {}".format(code, val))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            stats = line.strip().split(" ")
            if len(stats) == DEF_VAL:
                count += 1
                status["fsize"] += int(stats[-1])
                if type(int(stats[-2])) == int:
                    if stats[-2] in status["codes"].keys():
                        status["codes"][stats[-2]] += 1
                    else:
                        status["codes"][stats[-2]] = 1
            if count == DEF_VAL:
                count = 0
                printer(status)
    finally:
        printer(status)
