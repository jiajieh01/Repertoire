"""
Contains the functions that build the board and the interactive GUI, including pieces.
"""

import os
import logging
import tkinter as tk
import chess
from PIL import Image, ImageTk

logging.basicConfig(level='INFO')

class ChessBoard:
    """Class representing a chess board with interactive GUI."""

    def __init__(self, root, square_size=80):
        """Initialize the ChessBoard instance."""
        self.root = root
        self.square_size = square_size
        self.canvas = tk.Canvas(root, width=8 * square_size, height=8 * square_size)
        self.canvas.pack()
        self.board = chess.Board()
        self.board_pieces = {}
        self.squares = {}
        self.square_coordinates = {}
        self.square_colors = {}
        self.image_dir = os.path.join(os.path.dirname(__file__), "pieces")
        self.selected_square = None

    def create_chess_board(self):
        """Create the tkinter canvas, build the chess board, and place pieces."""
        self._build_chess_board()
        self._place_board_pieces()

    def _build_chess_board(self):
        """Build the chess board on the canvas."""
        for row in range(8):
            for col in range(8):
                self._create_chess_square(row, col)

    def _create_chess_square(self, row, col):
        """Create a single chess square on the canvas."""
        x1, y1 = col * self.square_size, row * self.square_size
        x2, y2 = x1 + self.square_size, y1 + self.square_size
        color = "white" if (row + col) % 2 == 0 else "gray"
        square_index = chess.square(col, 7 - row)
        centre_x, centre_y = (x1 + x2) / 2, (y1 + y2) / 2

        square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        self.squares[square_index] = square
        self.square_coordinates[square_index] = (centre_x, centre_y)
        self.square_colors[square_index] = color

        self._place_piece_on_square(square_index, centre_x, centre_y)

    def _place_piece_on_square(self, square_index, centre_x, centre_y):
        """Place a piece on the given square if it exists."""
        piece = self.board.piece_at(square_index)
        if piece:
            piece_color = "white" if piece.color == chess.WHITE else "black"
            piece_type = chess.piece_name(piece.piece_type)
            filename = f"{piece_color}_{piece_type}.png"
            image_path = os.path.join(self.image_dir, filename)

            piece_image = Image.open(image_path)
            piece_image = piece_image.resize((
                int(self.square_size * 0.9),
                int(self.square_size * 0.9)
            ))
            piece_image_tk = ImageTk.PhotoImage(piece_image)
            self.board_pieces[(centre_x, centre_y)] = piece_image_tk

            # Place the piece image on the canvas at (centre_x, centre_y)
            self.canvas.create_image(centre_x, centre_y, image=piece_image_tk, tags="pieces")

    def _place_board_pieces(self):
        """Place all pieces stored in board_pieces onto the canvas."""
        for (centre_x, centre_y), piece_image_tk in self.board_pieces.items():
            self.canvas.create_image(centre_x, centre_y, image=piece_image_tk)

    def _highlight_square(self, square_index):
        """Change the color of the specified square to green."""
        self.canvas.itemconfig(self.squares[square_index], fill="green")

    def _reset_square_color(self, square_index):
        """Reset the color of the specified square to its original color."""
        original_color = self.square_colors.get(square_index)
        self.canvas.itemconfig(self.squares[square_index], fill=original_color)

    def handle_click(self, event):
        """Handle mouse click event on canvas."""
        x, y = event.x, event.y
        col = x // self.square_size
        row = y // self.square_size
        square_index = chess.square(col, 7 - row)

        if self.selected_square is None:
            # Select piece on the clicked square
            self.selected_square = square_index
            self._highlight_square(square_index)
        else:
            # Move the selected piece to the clicked square if it is a valid move
            move = chess.Move(self.selected_square, square_index)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.update_board_display()
                self._reset_square_color(self.selected_square)
                self.selected_square = None # Clear selection after move

    def update_board_display(self):
        """Update the board display on the canvas."""
        self.canvas.delete("pieces")
        self.board_pieces = {}

        for row in range(8):
            for col in range(8):
                square_index = chess.square(col, 7 - row)
                centre_x = col * self.square_size + self.square_size / 2
                centre_y = row * self.square_size + self.square_size / 2
                self._place_piece_on_square(square_index, centre_x, centre_y)

    def bind_events(self):
        """Bind mouse click event to canvas."""
        self.canvas.bind("<Button-1>", self.handle_click)

    def start_game(self):
        """Start the chess game."""
        self.create_chess_board()
        self.update_board_display()
        self.bind_events()
