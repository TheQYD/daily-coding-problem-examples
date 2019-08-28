#!/usr/bin/python

from collections import deque

def minimum_turns(snakes, ladders):
    board = {square: square for square in range(1, 101)}

    for start, end in snakes.items():
        board[start] = end

    for start, end in ladders.items():
        board[start] = end

    start, end = 0, 100
    turns = 0

    path = deque([(start, turns)])
    visited = set()

    while path:
        square, turns = path.popleft()

        for move in range(square + 1, square + 7):
            if move >= end:
                return turns + 1

            if move not in visited:
                visited.add(move)
                path.append((board[move], turns + 1))

if __name__ == "__main__":

    snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
    ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}

    print minimum_turns(snakes, ladders)
