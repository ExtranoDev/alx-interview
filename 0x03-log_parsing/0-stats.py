#!/usr/bin/python3
"""
Script reads stdin line by line and logs metrics
"""

import sys

DEF_VAL = 9
count = 0
status = {"fsize": 0, "codes": dict()}
codes = ["200", "301", "400", "401", "403", "404", "405", "500"]


def printer(status):
    """
    Outputs formatted log
    """
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
            code = stats[-2]
            if code in codes:
                if code in status["codes"].keys():
                    status["codes"][code] += 1
                else:
                    status["codes"][code] = 1
            status["fsize"] += int(stats[-1])
            if count == DEF_VAL:
                count = 0
                printer(status)
        printer(status)
    except KeyboardInterrupt:
        printer(status)
