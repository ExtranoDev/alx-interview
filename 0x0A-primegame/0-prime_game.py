#!/usr/bin/python3
"""Prime Game"""


def isWinner(x: int, nums: list) -> str:
    """Determine winner based on Prime number rounds"""
    if nums and x > 0:
        players = {"Ben": 0, "Maria": 0}
        for i in nums:
            if i == 1:
                players["Ben"] += 1
                continue
            numArr = list(range(1, i + 1))
            count = 1

            while len(numArr) > 1:
                sNum = numArr[1]
                tempArr = []
                for x in numArr:
                    if x % sNum != 0:
                        tempArr.append(x)
                count += 1
                numArr = tempArr

            if count % 2 == 0:
                players["Maria"] += 1
            elif count % 2 == 1:
                players["Ben"] += 1
        return max(players, key=players.get)
    return None
