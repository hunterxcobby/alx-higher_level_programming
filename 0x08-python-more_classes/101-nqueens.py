#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)

    for solution in solutions:
        for row in solution:
            queens_positions = [row_idx for row_idx, value in enumerate(row) if value == 1]
            print(queens_positions)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except (ValueError, TypeError):
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

solve_nqueens(n)
