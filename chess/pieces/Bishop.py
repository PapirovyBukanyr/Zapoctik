from chess.pieces.Piece import *

class Bishop(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "B"
  def copy(self):
    return Bishop(self.color, self.position)
  def possibleMovesWithoutChecking(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0 and self.col - i >= 0:
      if board[self.row-i, self.col-i] is not None:
        if board[self.row-i, self.col-i].color != self.color:
          possibleMoves.append([self.row-i, self.col-i])
        break
      possibleMoves.append([self.row-i, self.col-i])
      i += 1
    i = 1
    while self.row - i >= 0 and self.col + i <= 7:
      if board[self.row-i, self.col+i] is not None:
        if board[self.row-i, self.col+i].color != self.color:
          possibleMoves.append([self.row-i, self.col+i])
        break
      possibleMoves.append([self.row-i, self.col+i])
      i += 1
    i = 1
    while self.row + i <= 7 and self.col - i >= 0:
      if board[self.row+i, self.col-i] is not None:
        if board[self.row+i, self.col-i].color != self.color:
          possibleMoves.append([self.row+i, self.col-i])
        break
      possibleMoves.append([self.row+i, self.col-i])
      i += 1  
    i = 1
    while self.row + i <= 7 and self.col + i <= 7:  
      if board[self.row+i, self.col+i] is not None:
        if board[self.row+i, self.col+i].color != self.color:
          possibleMoves.append([self.row+i, self.col+i])
        break
      possibleMoves.append([self.row+i, self.col+i])
      i += 1
    return possibleMoves
  def possibleMoves(self, board):
    possibleMoves = self.possibleMovesWithoutChecking(board)
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves