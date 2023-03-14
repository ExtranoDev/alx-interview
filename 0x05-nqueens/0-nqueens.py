#!/usr/bin/python3
""""""
import sys


def verify():
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)
    return N

def blackList(pos, black_list, n):
    temp_range = range(n)
    # horizontal & vertical
    for i in temp_range:
        hor_pos = [pos[0], i]
        ver_pos = [i, pos[1]]
        if hor_pos not in black_list:
            black_list.append(hor_pos)
        if ver_pos not in black_list:
            black_list.append(ver_pos)
    n -= 1
    # diagonal x-y
    diff1 = pos[0] - pos[1]
    diff1 = diff1 if diff1 > 0 else 0
    diff2 = pos[1] - pos[0]
    diff2 = diff2 if diff2 > 0 else 0
    diff4 = pos[1] + pos[0]
    diff3 = diff4 - n if diff4 - n > 0 else 0
    diff4 = diff4 if diff4 <= n else n

    # diag cordinates
    for i in temp_range:
        if diff1 in temp_range and diff2 in temp_range:
            if [diff1, diff2] not in black_list:
                black_list.append([diff1, diff2])
        diff1 += 1
        diff2 += 1
        if diff3 in temp_range and diff4 in temp_range:
            if [diff3, diff4] not in black_list:
                black_list.append([diff3, diff4])
        diff3 += 1
        diff4 -= 1


if __name__ == '__main__':
    N = verify()
    solutions = []
    temp_sol = []
    black_list = []

    for i in range(N):
        top_cor = [0, i]
        temp_sol.append(top_cor) 
        blackList(top_cor, black_list, N)
        # blacklist horizontal, vertical, diagonals-x-y
        for a in range(1, N):
            for b in range(0, N):
                temp = [a, b]
                if temp not in black_list and temp not in temp_sol:
                    temp_sol.append(temp)
                    blackList(temp, black_list, N)
        if len(temp_sol) == N:
            solutions.append(temp_sol)
        temp_sol = []
        black_list = []
    for solution in solutions:
        print(solution)
