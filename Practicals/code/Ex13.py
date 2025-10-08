import math

# Function to check for a win
def check_win(board, player):
    # Rows, columns, diagonals
    for i in range(3):
        if all([board[i][j]==player for j in range(3)]): return True
        if all([board[j][i]==player for j in range(3)]): return True
    if all([board[i][i]==player for i in range(3)]): return True
    if all([board[i][2-i]==player for i in range(3)]): return True
    return False

# Minimax algorithm
def minimax(board, depth, is_max):
    if check_win(board, "O"): return 1
    if check_win(board, "X"): return -1
    if all(cell!=" " for row in board for cell in row): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="O"
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j]=" "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="X"
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j]=" "
        return best

# Find best move
def best_move(board):
    best_val = -math.inf
    move = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="O"
                val = minimax(board,0,False)
                board[i][j]=" "
                if val>best_val:
                    best_val = val
                    move = (i,j)
    return move

# Example board
board = [["X","O","X"],[" ","O"," "],[" "," ","X"]]
move = best_move(board)
print("Best Move for O:", move)
