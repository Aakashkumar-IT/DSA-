def solveNQueens(n):

    result = []

    # Create an empty chessboard
    board = [["." for _ in range(n)] for _ in range(n)]

    # Sets to keep track of attacked positions
    cols = set()
    positiveDiagonal = set()
    negativeDiagonal = set()

    def backtrack(row):

        # If all queens are placed
        if row == n:
            copy = ["".join(r) for r in board]
            result.append(copy)
            return

        # Try every column in the current row
        for col in range(n):

            # Check whether the position is safe
            if (col in cols or
                (row + col) in positiveDiagonal or
                (row - col) in negativeDiagonal):
                continue

            # Place the queen
            cols.add(col)
            positiveDiagonal.add(row + col)
            negativeDiagonal.add(row - col)
            board[row][col] = "Q"

            # Move to the next row
            backtrack(row + 1)

            # Backtrack: remove the queen
            cols.remove(col)
            positiveDiagonal.remove(row + col)
            negativeDiagonal.remove(row - col)
            board[row][col] = "."

    # Start from row 0
    backtrack(0)

    return result


# Get input from the user
n = int(input("Enter the value of n: "))

# Solve the N-Queens problem
solutions = solveNQueens(n)

# Display the solutions
print("\nNumber of solutions:", len(solutions))

for solution in solutions:
    print()

    for row in solution:
        print(row)