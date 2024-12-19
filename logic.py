import threading

def minimax(board, is_maximizing, computer_symbol, player_symbol):
    winner = evaluate(board, computer_symbol, player_symbol)

    if(winner == computer_symbol):
        return 1
    elif(winner == player_symbol):
        return -1
    elif(is_draw(board)):
        return 0

    best_score = float('-inf') if is_maximizing else float('inf')
    for row in range(3):
        for col in range(3):
            if(board[row][col] == ""):
                board[row][col] = computer_symbol if is_maximizing else player_symbol
                score = minimax(board, not is_maximizing, computer_symbol, player_symbol)
                board[row][col] = ""
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)

    return best_score

def evaluate(board, computer_symbol, player_symbol):
    for row in range(3):
        if(board[row][0] == board[row][1] == board[row][2] != ""):
            return board[row][0]
    for col in range(3):
        if(board[0][col] == board[1][col] == board[2][col] != ""):
            return board[0][col]
    if(board[0][0] == board[1][1] == board[2][2] != ""):
        return board[0][0]
    if(board[0][2] == board[1][1] == board[2][0] != ""):
        return board[0][2]
    return None

def is_draw(board):
    for row in range(3):
        for column in range(3):
            if(board[row][column] == ""):
                return False
    return True


def computer_move(board, computer_symbol, player_symbol, gui_callback):
    def calculate_best_move():
        best_score = -float('inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if(board[row][col] == ""):
                    board[row][col] = computer_symbol
                    score = minimax(board, False, computer_symbol, player_symbol)
                    board[row][col] = ""
                    if(score > best_score):
                        best_score = score
                        best_move = (row, col)

        if(best_move):
            gui_callback(best_move)

    threading.Thread(target=calculate_best_move, daemon=True).start()
