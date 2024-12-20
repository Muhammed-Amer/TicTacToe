import tkinter as tk
from logic import computer_move, evaluate, is_draw


class TicTacToe:
    # constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player_symbol = "O"
        self.computer_symbol = "X"

        # first turn 0
        # second turn x
        self.current_player = self.player_symbol

        # if all buttons has a value (x, o)
        # if someone won
        self.game_over = False

        self.board_state = [["" for _ in range(3)] for _ in range(3)]

        self.player_color = "#D8A25E"
        self.computer_color = "#A04747"
        self.grey_color = "#343131"
        self.light_grey_color = "#EEDF7A"

        self.initialize_ui()

    def initialize_ui(self):
        # fixed size
        self.root.resizable(False, False)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        window_width = int(screen_width * 0.295) 
        window_height = int(screen_height * 0.55)

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        self.frame = tk.Frame(self.root, bg=self.grey_color)
        self.frame.pack()

        self.status_label = tk.Label(self.frame, text=f"{self.current_player}'s turn", font=("Consolas", 20),
                                     bg=self.grey_color, fg="white")
        self.status_label.grid(row=0, column=0, columnspan=3, sticky="we")

        self.board = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.frame, text="", font=("Consolas", 50, "bold"),
                                   bg=self.grey_color, fg=self.player_color,
                                   width=4, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row + 1, column=col)
                self.board[row][col] = button

        self.restart_button = tk.Button(self.frame, text="Restart", font=("Consolas", 20, "bold"),
                                        bg=self.grey_color, fg="white", command=self.restart_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

    def update_status_label(self, text, color="white"):
        self.status_label.config(text=text, fg=color)

    def make_move(self, row, col):
        # check if the button already has a value
        if(self.game_over or self.board_state[row][col] != ""):
            return

        self.board_state[row][col] = self.player_symbol
        self.board[row][col]["text"] = self.player_symbol
        self.board[row][col].config(foreground=self.player_color)
        self.check_winner()

        if(not self.game_over):
            self.current_player = self.computer_symbol
            self.update_status_label(f"{self.current_player}'s turn")
            computer_move(self.board_state, self.computer_symbol, self.player_symbol, self.computer_move_callback)

    def computer_move_callback(self, move):
        row, col = move
        self.board_state[row][col] = self.computer_symbol
        self.board[row][col]["text"] = self.computer_symbol
        self.board[row][col].config(foreground=self.computer_color)
        self.check_winner()

        if(not self.game_over):
            self.current_player = self.player_symbol
            self.update_status_label(f"{self.current_player}'s turn")

    def check_winner(self):
        winner = evaluate(self.board_state, self.computer_symbol, self.player_symbol)
        if(winner):
            self.game_over = True
            self.update_status_label(f"{winner} wins!", self.computer_color if winner == self.computer_symbol else self.player_color)
            self.highlight_winner(winner)
        elif(is_draw(self.board_state)):
            self.game_over = True
            self.update_status_label("It's a Draw!", self.computer_color)

    def highlight_winner(self, winner_symbol):
        for row in range(3):
            if(self.board_state[row][0] == self.board_state[row][1] == self.board_state[row][2] == winner_symbol):
                for col in range(3):
                    self.board[row][col].config(bg=self.light_grey_color)
                return
        for col in range(3):
            if(self.board_state[0][col] == self.board_state[1][col] == self.board_state[2][col] == winner_symbol):
                for row in range(3):
                    self.board[row][col].config(bg=self.light_grey_color)
                return
        if(self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] == winner_symbol):
            for i in range(3):
                self.board[i][i].config(bg=self.light_grey_color)
            return
        if(self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] == winner_symbol):
            for i in range(3):
                self.board[i][2 - i].config(bg=self.light_grey_color)

    def restart_game(self):
        self.board_state = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.current_player = self.player_symbol
        self.update_status_label(f"{self.current_player}'s turn")
        for row in range(3):
            for col in range(3):
                self.board[row][col].config(text="", bg=self.grey_color, fg=self.player_color)

if(__name__ == "__main__"):
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
