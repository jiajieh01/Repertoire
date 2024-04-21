"""This contains the main execution function"""
import tkinter as tk
from game.board_builder import ChessBoard

def main():
    """The main execution function"""
    root = tk.Tk()
    root.title("Simple Chess Board")

    # Create ChessBoard instance
    chess_board = ChessBoard(root)

    # Build and render the chess board
    chess_board.create_chess_board()
    chess_board.place_board_pieces()

    root.mainloop()

if __name__ == "__main__":
    main()
