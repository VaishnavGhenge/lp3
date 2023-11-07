def is_safe(board, row, col):
    # Check if no queen can attack the (row, col) position
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower-left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

def eight_queens_with_first_queen_placed():
    board = [[0 for _ in range(8)] for _ in range(8)]

    # Place the first queen in the top-left corner (0, 0)
    board[0][0] = 1

    if solve_n_queens(board, 1):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == '__main__':
    eight_queens_with_first_queen_placed()
