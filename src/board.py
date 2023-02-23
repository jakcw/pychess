"""
Board is going to use a coordinate based system. Each piece will contain information on
it's position; moving and capturing other pieces will be based on this position
"""

from pieces import *
from position import Position as P

class Board:
    def __init__(self):

        self.pieces = []

        for x in range(7):
            self.pieces.append(Pawn('w', 'p', P(x, 1)))
            self.pieces.append(Pawn('b', 'p', P(x, 6)))


        # rather than appending each piece we can just extend the array
        self.pieces.extend(
                [
                    Rook('w', 'r', P(0, 0)),
                    Knight('w', 'n', P(1, 0)),
                    Bishop('w', 'b',  P(2, 0)),
                    Queen('w', 'q',  P(3, 0)),
                    King('w', 'k',  P(4, 0)),
                    Bishop('w', 'b',  P(5, 0)),
                    Knight('w', 'n',  P(6, 0)),
                    Rook('w', 'r',  P(7, 0)),
                ])
        
        self.pieces.extend(
                [
                    Rook('b', 'r', P(0, 7)),
                    Knight('b', 'n', P(1, 7)),
                    Bishop('b', 'b',  P(2, 7)),
                    Queen('b', 'q',  P(3, 7)),
                    King('b', 'k',  P(4, 7)),
                    Bishop('b', 'b',  P(5, 7)),
                    Knight('b', 'n',  P(6, 7)),
                    Rook('b', 'r',  P(7, 7)),
                ])
                 
    # currently, each piece is just sitting in the pieces array with information on its position; outputting it
    # to the console will not display it in chess board format
    def display_board(self):
        for piece in self.pieces:
            pass
            

board = Board()
board.display_board()