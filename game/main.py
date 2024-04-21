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
    chess_board.start_game()

    root.mainloop()

if __name__ == "__main__":
    main()
