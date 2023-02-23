from position import Position as P

class Pawn:

    # hopefully use unicode for pieces at some point, so each init will have a default symbol
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 1

    def __repr__(self):
        return self.side + self.symbol

    def legal_move(self):
        pass



class King:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
    
    def __repr__(self):
        return self.side + self.symbol
        
class Queen:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 9

    def __repr__(self):
        return self.side + self.symbol

class Rook:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 5

    def __repr__(self):
        return self.side + self.symbol

class Bishop:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 3

    def __repr__(self):
        return self.side + self.symbol

class Knight:
    def __init__(self, side: str, symbol: str, position):
        self.symbol = symbol
        self.side = side
        self.position = position
        self.val = 3

    def __repr__(self):
        return self.side + self.symbol


