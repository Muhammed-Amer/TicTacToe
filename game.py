import tkinter

def set_square_title(row, column):
    global current_player, game_over

    #cheking if the square already has a value
    if(game_over or board[row][column]["text"] != ""):
        return
    
    board[row][column]["text"] = you_o
    board[row][column].config(foreground=blue_color)
    current_player = computer_x
    label["text"] = current_player + "'s turn"
    check_winner()

    if not game_over:
        computer_move()

def computer_move():
    global current_player, game_over

    best_score = -1000
    best_move = (-1, -1)

    for row in range(3):
        for column in range(3):
            if(board[row][column]["text"] == ""):
                board[row][column]["text"] = computer_x
                score = minimax(False)
                board[row][column]["text"] = ""
                if(score > best_score):
                    best_score = score
                    best_move = (row, column)

    if best_move:
        row, column = best_move
        # add wait function maybe 2 seconds at X's turn
        board[row][column]["text"] = computer_x
        board[row][column].config(foreground=blue_color)
        current_player = you_o
        label["text"] = current_player + "'s turn"
        check_winner()

def minimax(is_maximizing):
    global game_over
    winner = evaluate()

    if(winner == computer_x):
        return 1
    elif(winner == you_o):
        return -1
    elif(is_draw()):
        return 0

    if(is_maximizing):
        best_score = -1000
        for row in range(3):
            for column in range(3):
                if(board[row][column]["text"] == ""):
                    board[row][column]["text"] = computer_x
                    score = minimax(False)
                    board[row][column]["text"] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(3):
            for column in range(3):
                if(board[row][column]["text"] == ""):
                    board[row][column]["text"] = you_o
                    score = minimax(True)
                    board[row][column]["text"] = ""
                    best_score = min(score, best_score)
        return best_score
     
def check_winner():
    global turns, game_over
    turns += 1

    if(turns == 9): 
        label.config(text="It's a Draw!", foreground=yellow_color)
        game_over = True

    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):

            highlight_winner(row, 0, row, 1, row, 2)
            return
        
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):

            highlight_winner(0, column, 1, column, 2, column)
            return

    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
        and board[0][0]["text"] != ""):
        highlight_winner(0, 0, 1, 1, 2, 2)
        return
    
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
        and board[1][1]["text"] != ""):
        highlight_winner(0, 2, 1, 1, 2, 0)
        return
        

def evaluate():
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            return board[row][0]["text"]

    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            return board[0][column]["text"]

    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        return board[0][0]["text"]

    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[1][1]["text"] != ""):
        return board[1][1]["text"]

    return

def is_draw():
    for row in range(3):
        for column in range(3):
            if(board[row][column]["text"] == ""):
                return False
    return True

def highlight_winner(r1, c1, r2, c2, r3, c3):
    global game_over
    board[r1][c1].config(foreground=yellow_color, background=light_grey_color)
    board[r2][c2].config(foreground=yellow_color, background=light_grey_color)
    board[r3][c3].config(foreground=yellow_color, background=light_grey_color)
    label.config(text=board[r1][c1]["text"] + " is the Winner!", foreground=yellow_color)
    game_over = True

def new_game():
    global turns, game_over, current_player

    turns = 0
    game_over = False
    current_player = you_o

    label.config(text=current_player + "'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=blue_color, background=grey_color)

turns = 0
game_over = False

computer_x = 'X'
you_o = 'O'
current_player = you_o

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]
]

blue_color = '#4584b6'
yellow_color = '#ffde47'
grey_color = '#343434'
light_grey_color = '#646464'

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=current_player + "'s turn", font=("Consolas", 20), background=grey_color,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=grey_color, foreground=blue_color,
                                            width=4, height=2, command=lambda row=row, column=column: set_square_title(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20, "bold"),
                        background=grey_color, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()
window.mainloop()