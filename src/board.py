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
            self.pieces.append(Pawn('w', 'r', P(x, 1)))
            self.pieces.append(Pawn('b', 'p', P(x, 6)))



board = Board()
print(board)
                    
