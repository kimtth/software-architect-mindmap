def is_valid(board, row, col, num):
    # Check if num is in the same row or column
    for i in range(3):
        if board[row][i] == num or board[i][col] == num:
            return False
    return True


def find_empty(board):
    # Return the next empty cell (row, col) or None if full
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return row, col
    return None


def solve_sudoku(board, depth=0):
    indent = "  " * depth  # Visual indent for stack level
    empty = find_empty(board)
    
    if not empty:
        print(f"{indent}✔️ Solved at depth {depth}")
        return True

    row, col = empty
    for num in range(1, 4):
        if is_valid(board, row, col, num):
            print(f"{indent}Trying {num} at ({row}, {col}) [depth {depth}]")
            board[row][col] = num
            print(f"{indent}Board state: {board}")

            if solve_sudoku(board, depth + 1):
                return True

            print(f"{indent}Backtracking {num} at ({row}, {col}) [depth {depth}]")
            board[row][col] = 0

    return False


if __name__ == "__main__":
    # Example Sudoku board (3x3) with some numbers filled in
    # 0 represents an empty cell
    # This is a simplified version of a Sudoku board for demonstration purposes
    # In a real Sudoku, the board would be 9x9 and have more complex rules

    # simplified 3x3 Sudoku board for demonstration, which is not going to call Backtracking
    board = [
        [0, 2, 0],
        [0, 0, 1],
        [3, 0, 0]
    ]

    '''
    Starting to solve the Sudoku...
    Trying 1 at (0, 0) [depth 0]
    Board state: [[1, 2, 0], [0, 0, 1], [3, 0, 0]]
    Trying 3 at (0, 2) [depth 1]
    Board state: [[1, 2, 3], [0, 0, 1], [3, 0, 0]]
        Trying 2 at (1, 0) [depth 2]
        Board state: [[1, 2, 3], [2, 0, 1], [3, 0, 0]]
        Trying 3 at (1, 1) [depth 3]
        Board state: [[1, 2, 3], [2, 3, 1], [3, 0, 0]]
            Trying 1 at (2, 1) [depth 4]
            Board state: [[1, 2, 3], [2, 3, 1], [3, 1, 0]]
            Trying 2 at (2, 2) [depth 5]
            Board state: [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
                ✔️ Solved at depth 6
    [1, 2, 3]
    [2, 3, 1]
    [3, 1, 2]
    '''

    # simplified 3x3 Sudoku board for demonstration, which is going to call Backtracking
    tboard = [
        [0, 0, 0],
        [1, 0, 3],
        [0, 0, 0]
    ]

    '''
    Starting to solve the Sudoku...
    Trying 2 at (0, 0) [depth 0]
    Board state: [[2, 0, 0], [1, 0, 3], [0, 0, 0]]
    Trying 1 at (0, 1) [depth 1]
    Board state: [[2, 1, 0], [1, 0, 3], [0, 0, 0]]
    Backtracking 1 at (0, 1) [depth 1]
    Trying 3 at (0, 1) [depth 1]
    Board state: [[2, 3, 0], [1, 0, 3], [0, 0, 0]]
        Trying 1 at (0, 2) [depth 2]
        Board state: [[2, 3, 1], [1, 0, 3], [0, 0, 0]]
        Trying 2 at (1, 1) [depth 3]
        Board state: [[2, 3, 1], [1, 2, 3], [0, 0, 0]]
            Trying 3 at (2, 0) [depth 4]
            Board state: [[2, 3, 1], [1, 2, 3], [3, 0, 0]]
            Trying 1 at (2, 1) [depth 5]
            Board state: [[2, 3, 1], [1, 2, 3], [3, 1, 0]]
                Trying 2 at (2, 2) [depth 6]
                Board state: [[2, 3, 1], [1, 2, 3], [3, 1, 2]]
                ✔️ Solved at depth 7
    [2, 3, 1]
    [1, 2, 3]
    [3, 1, 2]
    '''

    print("Starting to solve the Sudoku...")

    if solve_sudoku(board):
        for row in board:
            print(row)
    else:
        print("No solution exists.")
