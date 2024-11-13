from .Piece import *
from .Bishop import *
from .Rook import *

class Queen(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "Q"
    self.value = 9
    self.img_file = "resources//queenW.png" if self.color == Colors.WHITE else "resources//queenB.png"

  def copy(self):
    return Queen(self.color, self.position)
  
  def possibleMoves(self, board):
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMoves(board)
    possibleMoves += Bishop(self.color, self.position).possibleMoves(board)
    return possibleMoves