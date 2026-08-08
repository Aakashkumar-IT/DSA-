from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []

        board = [["." for _ in range(n)] for _ in range(n)]

        cols = set()
        positiveDiagonal = set()   # row + col
        negativeDiagonal = set()   # row - col

        def backtrack(row):

            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return

            for col in range(n):

                if (col in cols or
                    (row + col) in positiveDiagonal or
                    (row - col) in negativeDiagonal):
                    continue

                cols.add(col)
                positiveDiagonal.add(row + col)
                negativeDiagonal.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                positiveDiagonal.remove(row + col)
                negativeDiagonal.remove(row - col)
                board[row][col] = "."

        backtrack(0)

        return result