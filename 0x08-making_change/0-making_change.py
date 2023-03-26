#!/usr/bin/python3
"""
Determining the fewest number of coins for a transaction
"""


def makeChange(coins: list, total: int):
    """
    determine the fewest number of coins needed
    for a given amount total
    """
    if total <= 0 or coins == []:
        return 0
    coins.sort(reverse=True)
    idx = 0
    count = 0
    while True:
        if total >= coins[idx]:
            if (total - coins[idx]) >= 0:
                total -= coins[idx]
            count += 1
        if total < coins[idx]:
            idx += 1
        if total == 0:
            return count
        if idx == len(coins) - 1 and total > coins[idx]:
            return -1
