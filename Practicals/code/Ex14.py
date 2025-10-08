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

# Alpha-Beta Pruning algorithm
def alphabeta(board, depth, alpha, beta, is_max):
    if check_win(board, "O"): return 1
    if check_win(board, "X"): return -1
    if all(cell!=" " for row in board for cell in row): return 0

    if is_max:
        value = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="O"
                    value = max(value, alphabeta(board, depth+1, alpha, beta, False))
                    board[i][j]=" "
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
        return value
    else:
        value = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="X"
                    value = min(value, alphabeta(board, depth+1, alpha, beta, True))
                    board[i][j]=" "
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
        return value

# Function to find the best move for O
def best_move(board):
    best_val = -math.inf
    move = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="O"
                val = alphabeta(board,0,-math.inf,math.inf,False)
                board[i][j]=" "
                if val>best_val:
                    best_val = val
                    move = (i,j)
    return move

# Example board
board = [["X","O","X"],[" ","O"," "],[" "," ","X"]]
move = best_move(board)
print("Best Move for O:", move)
