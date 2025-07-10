N = 8  # Size of the chessboard

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "-" for col in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens(board, row):
    if row >= N:
        print_solution(board)
        return True
    
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = 0  # Backtrack
    
    return res

def solve():
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution exists")
    else:
        print("Solutions found!")

solve()