import tkinter as tk

N = 8  # Number of queens

class EightQueensGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8-Queens Problem")
        self.cell_size = 60
        self.canvas = tk.Canvas(self.master, width=N*self.cell_size, height=N*self.cell_size)
        self.canvas.pack()
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.solve(0)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(N):
            for col in range(N):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                fill = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill)

                if self.board[row][col] == 1:
                    self.canvas.create_text(x1 + self.cell_size // 2, y1 + self.cell_size // 2, text="♛", font=("Arial", 32), fill="red")

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col]:
                return False

        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if self.board[i][j]:
                return False

        for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
            if self.board[i][j]:
                return False

        return True

    def solve(self, row):
        if row >= N:
            return True

        for col in range(N):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(row + 1):
                    return True
                self.board[row][col] = 0
        return False

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = EightQueensGUI(root)
    root.mainloop()
