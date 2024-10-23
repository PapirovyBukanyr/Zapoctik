from chess.pieces.Piece import *
from chess.pieces.Bishop import *
from chess.pieces.Rook import *

class Queen(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "Q"
  def copy(self):
    return Queen(self.color, self.position)
  def possibleMovesWithoutChecking(self, board):
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMovesWithoutChecking(board)
    possibleMoves += Bishop(self.color, self.position).possibleMovesWithoutChecking(board)
    return possibleMoves
  def possibleMoves(self, board):
    possibleMoves = self.possibleMovesWithoutChecking(board)
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves