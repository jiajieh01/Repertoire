import tkinter as tk
import chess

def create_chess_board(root, board_size=8, square_size=64):
    canvas = tk.Canvas(root, width=board_size * square_size, height=board_size * square_size)
    canvas.pack()

    for row in range(board_size):
        for col in range(board_size):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    return canvas