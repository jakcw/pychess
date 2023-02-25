from position import Position as P


class MoveError(Exception):
    pass

class Pawn:
    # hopefully use unicode for pieces at some point, so each init will have a default symbol
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 1
        self.moves_made = 0

    def __repr__(self):
        return self.symbol

    def move(self):

        # if pawn has made no moves, can move 2 positions vertically
        if self.side == 'w':
            if self.moves_made == 0:
                move = P(0, 2)
            else:
                move = P(0, 1)
        else:
            if self.moves_made == 0:
                move = P(0, -2)
            else:
                move = P(0, -1)



class King:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
    
    def __repr__(self):
        return self.symbol

    
    def move(self, new_position):
        self.position = new_position
    
        
class Queen:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 9

    def __repr__(self):
        return self.symbol 
        
    def move(self, new_position):
        self.position = new_position

    
class Rook:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.movement = [P(0, 1), P(0, -1), P(1, 0), P(-1, 0)]
        self.val = 5

    def __repr__(self):
        return self.symbol

    
    def move(self, num_squares, direction):
        """Movement for rooks will be 1 or -1 in each direction, can then multiply that
        by the number of squares moved and add it to current position"""
        self.position += (num_squares * self.movement[direction])
        
class Bishop:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 3

    def __repr__(self):
        return  self.symbol

    def move(self, new_position):
        self.position = new_position

class Knight:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 3

    def __repr__(self):
        return self.symbol
    
    def move(self, new_position):
        self.position = new_position


