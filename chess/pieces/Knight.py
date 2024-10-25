from chess.pieces.Piece import *

class Knight(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "N"
    self.value = 3
  def copy(self):
    return Knight(self.color, self.position)
  def possibleMovesWithoutChecking(self, board):
    possibleMoves = []
    possibleMoves.append([self.row-1, self.col-2])
    possibleMoves.append([self.row-1, self.col+2])
    possibleMoves.append([self.row+1, self.col-2])
    possibleMoves.append([self.row+1, self.col+2])
    possibleMoves.append([self.row-2, self.col-1])
    possibleMoves.append([self.row-2, self.col+1])
    possibleMoves.append([self.row+2, self.col-1])
    possibleMoves.append([self.row+2, self.col+1])
    possibleMoves = [x for x in possibleMoves if x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7]
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    return possibleMoves
  def possibleMoves(self, board):
    possibleMoves = self.possibleMovesWithoutChecking(board)
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves