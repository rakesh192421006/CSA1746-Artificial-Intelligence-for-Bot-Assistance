def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == row-i:
            return False
    return True

def solve_nqueen(n):
    board = [-1]*n
    def solve(row):
        if row == n:
            print(board)
            return True
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                if solve(row+1):
                    return True
                board[row] = -1
        return False
    solve(0)

solve_nqueen(8)
