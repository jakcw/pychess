class Position:
    def __init__(self, rank, file):
        # rank = x
        # file = y
        
        self.rank = rank
        self.file = file
        
    
    def __add__(self, other):
        return Position(self.rank + other.rank, self.file + other.file)

    def __sub__ (self, other):
        return Position(self.rank - other.rank, self.file - other.file)

    def __repr__(self):
        return f"{self.rank, self.file}"

    def __eq__(self, other): 
            if not isinstance(other, Position):
                # don't attempt to compare against unrelated types
                return NotImplemented

            return self.rank == other.rank and self.file == other.file

