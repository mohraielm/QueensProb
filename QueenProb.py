import tkinter as tk
import random

class NQueensGUI:
    def __init__(self, master, size):
        self.master = master
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.create_board()

    def create_board(self):
        self.buttons = [[tk.Button(self.master, width=2, height=1, command=lambda row=row, col=col: self.toggle_queen(row, col))
                         for col in range(self.size)] for row in range(self.size)]

        for row in range(self.size):
            for col in range(self.size):
                self.buttons[row][col].grid(row=row, column=col)
                self.buttons[row][col].config(bg="lightpink")

        view_solution_button = tk.Button(self.master, text="View Solution", command=self.view_solution)
        view_solution_button.grid(row=self.size, columnspan=self.size)

    def toggle_queen(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = 1
            self.buttons[row][col].config(text="Q", relief=tk.SUNKEN)
        else:
            self.board[row][col] = 0
            self.buttons[row][col].config(text="", relief=tk.RAISED)

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.size, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_n_queens_util(self, col):
        if col == self.size:
            return True

        res = False
        for i in range(self.size):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_n_queens_util(col + 1) or res
                if res:
                    return True
                self.board[i][col] = 0

        return False

    def view_solution(self):
        self.reset_board()
        self.solve_n_queens_util(0)

        random.shuffle(self.board)

        for row, solution_row in enumerate(self.board):
            for col, cell in enumerate(solution_row):
                label_text = "Q" if cell == 1 else "."
                self.buttons[row][col].config(text=label_text)

    def reset_board(self):
        for row in range(self.size):
            for col in range(self.size):
                self.board[row][col] = 0
                self.buttons[row][col].config(text="", relief=tk.RAISED)

if __name__ == "__main__":
    root = tk.Tk()
    size = 8
    root.title("N-Queens Puzzle")
    gui = NQueensGUI(root, size)
    root.mainloop()
