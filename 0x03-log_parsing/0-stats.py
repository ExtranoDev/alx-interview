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
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    print("File size: {}".format(status["fsize"]))
    for code in codes:
        if code in status["codes"].keys():
            val = status["codes"][code]
            print("{}: {}".format(code, val))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            count += 1
            stats = line.strip().split()
            try:
                status["fsize"] += int(stats[-1])
                if stats[-2].isdecimal():
                    if stats[-2] in status["codes"].keys():
                        status["codes"][stats[-2]] += 1
                    else:
                        status["codes"][stats[-2]] = 1
            except Exception:
                pass
            if count == DEF_VAL:
                count = 0
                printer(status)
        printer(status)
    finally:
        printer(status)
