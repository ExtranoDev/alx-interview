#!/usr/bin/python3
"""
Script reads stdin line by line and logs metrics
"""

import sys

DEF_VAL = 10
count = 0
status = {"fsize": 0, "codes": dict()}


def printer(status):
    """
    Outputs formatted log
    """
    print("File size: {}".format(status["fsize"]))
    for code, val in sorted(status["codes"].items()):
        print("{}: {}".format(code, val))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            stats = line.split(" ")
            try:
                code = int(stats[-2])
                if code in status["codes"].keys():
                    status["codes"][code] += 1
                else:
                    status["codes"][code] = 1
            except Exception:
                pass
            try:
                status["fsize"] += int(stats[-1])
            except Exception:
                pass
            if count == DEF_VAL:
                count = 0
                printer(status)
        printer(status)
    except KeyboardInterrupt:
        printer(status)
