from .Piece import *

class Rook(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "R"
    self.value = 5
  def copy(self):
    copy = Rook(self.color, self.position)
    copy.hasMoved = self.hasMoved
    return copy
  def possibleMoves(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0:
      if board[self.row-i, self.col] is not None:
        if board[self.row-i, self.col].color != self.color:
          possibleMoves.append([self.row-i, self.col])
        break
      possibleMoves.append([self.row-i, self.col])
      i += 1
    i = 1
    while self.row + i <= 7:
      if board[self.row+i, self.col] is not None:
        if board[self.row+i, self.col].color != self.color:
          possibleMoves.append([self.row+i, self.col])
        break
      possibleMoves.append([self.row+i, self.col])
      i += 1
    i = 1
    while self.col - i >= 0:
      if board[self.row, self.col-i] is not None:
        if board[self.row, self.col-i].color != self.color: 
          possibleMoves.append([self.row, self.col-i])
        break
      possibleMoves.append([self.row, self.col-1])
      i += 1
    i = 1
    while self.col + i <= 7:  
      if board[self.row, self.col+i] is not None:
        if board[self.row, self.col+i].color != self.color:
          possibleMoves.append([self.row, self.col+i])
        break 
      possibleMoves.append([self.row, self.col+i])
      i += 1
    return possibleMoves