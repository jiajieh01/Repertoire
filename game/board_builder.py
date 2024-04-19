import tkinter as tk
import chess

def create_chess_board(root, square_size=80):
    canvas = tk.Canvas(root, width = 8 * square_size, height = 8 * square_size)
    canvas.pack()

    square_centres = {}

    board = chess.Board()

    for row in range(8):
        for col in range(8):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="") # Rectangle with TL:(x1, y1), BR:(x2, y2)

            # Calculate centre of the square
            centre_x = (x1 + x2) / 2
            centre_y = (y1 + y2) / 2
            square_index = chess.square(col, 7 - row)
            square_centres[square_index] = (centre_x, centre_y)

            # Places piece on square if it exists
            piece = board.piece_at(square_index)
            if piece is not None:
                canvas.create_text(centre_x, centre_y, text = piece.symbol(), font = ("Arial", int(square_size / 2)), fill = "black")
    
    return canvas, square_centres