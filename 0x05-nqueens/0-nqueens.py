#!/usr/bin/python3
"""
N queens Problem
"""

import sys


def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """
    Use backtracking to find all solutions.
    """
    if col >= len(board):
        solutions.append(
            [[r, c] for r in range(len(board))
                for c in range(len(board))
                if board[r][c] == 1]
        )
        return
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

if not n.isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(n)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for _ in range(n)] for _ in range(n)]
solutions = []
solve_nqueens(board, 0, solutions)

for solution in solutions:
    print(solution)
