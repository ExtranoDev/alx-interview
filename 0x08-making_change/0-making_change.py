#!/usr/bin/python3
"""
Determining the fewest number of coins for a transaction
"""


def makeChange(coins: list, total: int) -> int:
    """
    determine the fewest number of coins needed
    for a given amount total
    """
    if total <= 0:
        return 0
    if coins == []:
        return -1

    coins.sort(reverse=True)
    count = 0
    i = 0
    while True:
        if total >= coins[i]:
            total -= coins[i]
            count += 1
            continue
        if total <= 0:
            return count
        if total < coins[i] and i == len(coins) - 1:
           return -1
        i += 1
