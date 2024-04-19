import tkinter as tk
import chess

def create_chess_board(root, num_squares_per_side=8, square_size=80):
    canvas = tk.Canvas(root, width = num_squares_per_side * square_size, height = num_squares_per_side * square_size)
    canvas.pack()

    for row in range(num_squares_per_side):
        for col in range(num_squares_per_side):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    return canvas