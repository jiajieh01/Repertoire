"""This contains the main execution function"""
import chess
import tkinter as tk
import game.board_builder as bb

def main():
    root = tk.Tk()
    root.title("Simple Chess Board")
    board_canvas = bb.create_chess_board(root)
    root.mainloop()

if __name__ == "__main__":
    main()
