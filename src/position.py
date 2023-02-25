class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__ (self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"{self.x, self.y}"

    # dunder method to compare positions of two pieces
    def __eq__(self, other): 
            if not isinstance(other, Position):
                return NotImplemented
            return self.x == other.x and self.y == other.y
    
