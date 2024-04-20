import tkinter as tk
import chess
from PIL import Image, ImageTk
import os
import logging

logging.basicConfig(level='INFO')

board_pieces = {}

def append_to_board_pieces(canvas, centre_x, centre_y, image_path, square_size):
    # Load and resize piece image
    piece_image = Image.open(image_path)
    piece_image = piece_image.resize((int(square_size * 0.8), int(square_size * 0.8)))
    piece_image_tk = ImageTk.PhotoImage(piece_image)

    # Display piece image on the canvas
    canvas.create_image(centre_x, centre_y, image = piece_image_tk)
    canvas.image = piece_image_tk

    board_pieces[(centre_x, centre_y)] = piece_image_tk

def create_chess_board(root, square_size=80):
    canvas = tk.Canvas(root, width = 8 * square_size, height = 8 * square_size)
    canvas.pack()

    board = chess.Board()

    image_dir = os.path.join(os.path.dirname(__file__), "pieces")

    for row in range(8):
        for col in range(8):
            x1, y1 = col * square_size, row * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "gray"

            # Creates rectangle with TL:(x1, y1), BR:(x2, y2)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

            # Calculate centre of the square
            centre_x = (x1 + x2) / 2
            centre_y = (y1 + y2) / 2
            square_index = chess.square(col, 7 - row)

            # Places piece on square if it exists
            piece = board.piece_at(square_index)

            if piece is None: continue

            piece_color = "white" if piece.color == chess.WHITE else "black"
            piece_type = chess.piece_name(piece.piece_type)

            filename = f"{piece_color}_{piece_type}.png"
            image_path = os.path.join(image_dir, filename)

            append_to_board_pieces(canvas, centre_x, centre_y, image_path, square_size)
            logging.info(f"{filename} placed at ({centre_x}, {centre_y})")
    
    return canvas

def place_board_pieces(canvas):
    """Place all pieces stored in board_pieces onto the canvas."""
    for (centre_x, centre_y), piece_image_tk in board_pieces.items():
        canvas.create_image(centre_x, centre_y, image=piece_image_tk)