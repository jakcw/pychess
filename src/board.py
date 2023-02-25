"""
Board is going to use a coordinate based system. Each piece will contain information on
it's position; moving and capturing other pieces will be based on this position
"""

from pieces import *
from position import Position as P

class Board:
    def __init__(self):

        self.board = [["x" for x in range(8)] for y in range(8)]
        self.check: bool = False

        # Each piece contains positional information as well as a regular array index
        for x in range(8):
            self.board[1][x] = Pawn('b', '\u265F', P(x, 1))
            self.board[6][x] = Pawn('w', '\u2659', P(x, 6))

        # Pieces using chess unicode for clarity in terminal
        self.board[0][0] = Rook('b', "\u2656", P(0, 0))
        self.board[0][1] = Knight('b', "\u2658", P(1, 0))
        self.board[0][2] = Bishop('b', "\u2657", P(2, 0))
        self.board[0][3] = Queen('b',  "\u2655", P(3, 0))
        self.board[0][4] = King('b', "\u2654", P(4, 0))
        self.board[0][5] = Bishop('b', "\u2657", P(5, 0))
        self.board[0][6] = Knight('b', "\u2658", P(6, 0))
        self.board[0][7] = Rook('b', "\u2656", P(7, 0))


        self.board[7][0] = Rook('w', "\u265C", P(0, 0))
        self.board[7][1] = Knight('w', "\u265E", P(1, 0))
        self.board[7][2] = Bishop('w', "\u265D", P(2, 0))
        self.board[7][3] = Queen('w', "\u265B", P(3, 0))
        self.board[7][4] = King('w', "\u265A", P(4, 0))
        self.board[7][5] = Bishop('w', "\u265D", P(5, 0))
        self.board[7][6] = Knight('w', "\u265E", P(6, 0))
        self.board[7][7] = Rook('w', "\u265C", P(7, 0))


    def capture(self):
        # if new position of piece is not empty, returns true
        if self.board[x][y] != "x":
            return True
        return False


    # makeshift board display for now
    def display_board(self):

        ranks = '12345678'
        files = 'abcdefgh'

        for i in range(8):
            print()
            print(ranks[i], end=" ")
            for j in range(8):
                print(self.board[i][j], end=" ")

        print()
        print(" ", end=" ")
        

        for i in range(len(files)):
            print(files[i], end=" ")
        print()



