import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Helvetica', 20), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)
        
    def on_button_click(self, i, j):
        if self.board[i][j] == "":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def check_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
    
    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                
    def run(self):
        self.root.mainloop()

if _name_ == "_main_":
    game = TicTacToe()
    game.run()