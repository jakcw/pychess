
from board import Board
from position import Position as P


board = Board()

while True:

   board.display_board()
   x, y = input("Enter a location e.g., (0, 2): ").split(", ")
   x, y = int(x), int(y)
   piece = board.board[x][y]
   x_new, y_new = input("Enter position to move to: ").split(", ")
   x_new, y_new = int(x_new), int(y_new)
   piece.position = P(x_new, y_new)
   board.board[x_new][y_new] = piece.symbol
   board.board[x][y] = "x"   


