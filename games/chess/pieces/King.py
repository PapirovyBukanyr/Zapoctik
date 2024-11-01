from .Piece import *

class King(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "K"
  def copy(self):
    copy = King(self.color, self.position)
    copy.hasMoved = self.hasMoved
    return copy
  def move(self, board, end):
    if end[1] - self.col == 2:
      board[self.row, 7].move(board, [self.row, 5])
    if end[1] - self.col == -2:
      board[self.row, 0].move(board, [self.row, 3])
    super().move(board, end)
  def possibleMoves(self, board):
    possibleMoves = []
    # normalni tahy
    possibleMoves.append([self.row-1, self.col])
    possibleMoves.append([self.row-1, self.col+1])
    possibleMoves.append([self.row, self.col+1])
    possibleMoves.append([self.row+1, self.col+1])
    possibleMoves.append([self.row+1, self.col])
    possibleMoves.append([self.row+1, self.col-1])
    possibleMoves.append([self.row, self.col-1])
    possibleMoves.append([self.row-1, self.col-1])
    possibleMoves = [x for x in possibleMoves if (x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7)]
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    # rosady
    if not self.hasMoved:
      if board[self.row, self.col+1] is None and \
          board[self.row, self.col+2] is None and \
          not board[self.row, 7].hasMoved:
        possibleMoves.append([self.row, self.col+2])
      if board[self.row, self.col-1] is None and \
          board[self.row, self.col-2] is None and \
          not board[self.row, 0].hasMoved:
        possibleMoves.append([self.row, self.col-2])
    return possibleMoves