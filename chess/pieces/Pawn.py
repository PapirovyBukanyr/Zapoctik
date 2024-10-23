from chess.pieces.Piece import *


class Pawn(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "P"
  def copy(self):
    copy = Pawn(self.color, self.position)
    copy.hasMoved = self.hasMoved
    copy.lastMoveWasDouble = self.lastMoveWasDouble
    return copy
  def move(self, board, end):
    originalPosition = self.position
    if not (end[1] == self.col or board[end] is not None):
      board[end] = board[self.position]
      board[self.position] = None
      if self.color == Colors.WHITE:
        board[end[0]+1, end[1]] = None
      else:
        board[end[0]-1, end[1]] = None
      self.position = end
    else:
      super().move(board, end)
    if abs(originalPosition[0] - self.position[0]) == 2:
      self.lastMoveWasDouble = True
    if self.row == 0 and self.color == Colors.WHITE or self.row == 7 and self.color == Colors.BLACK:
      # sem prijde logika pro zobrazeni moznych figurek na promotion pesce, po kliknuti se policko nastavi na zvolenou figurku
      pass
    
  def possibleMovesWithoutChecking(self, board):
    possibleMoves = []
    # bílá
    if self.color == Colors.WHITE:
      # normální tahy
      if not self.hasMoved:
        if board[self.row-1, self.col] is None:
          possibleMoves.append([self.row-1, self.col])
          if board[self.row-2, self.col] is None:
            possibleMoves.append([self.row-2, self.col])
      else:
        if board[self.row-1, self.col] is None:
          possibleMoves.append([self.row-1, self.col])
      # braní figur
      if self.col + 1 <= 7:
        if board[self.row-1, self.col+1] is not None and board[self.row-1, self.col+1].color != self.color:
          possibleMoves.append([self.row-1, self.col+1])
      if self.col - 1 >= 0:
        if board[self.row-1, self.col-1] is not None and board[self.row-1, self.col-1].color != self.color and self.col - 1 >= 0:
          possibleMoves.append([self.row-1, self.col-1])
      #braní mimochodem
      if self.col + 1 <= 7:
        if isinstance(board[self.row,self.col+1],Pawn) and \
            board[self.row,self.col+1].color != self.color and \
            board[self.row-1, self.col+1] is None and \
            board[self.row, self.col+1].lastMoveWasDouble:
          possibleMoves.append([self.row-1, self.col+1])
      if self.col - 1 >= 0:    
        if isinstance(board[self.row,self.col-1],Pawn) and \
            board[self.row,self.col-1].color != self.color and \
            board[self.row-1, self.col-1] is None and \
            board[self.row, self.col-1].lastMoveWasDouble:
          possibleMoves.append([self.row-1, self.col-1])
    else:
      #černá
      if not self.hasMoved:
        if board[self.row+1, self.col] is None:
          possibleMoves.append([self.row+1, self.col])
          if board[self.row+2, self.col] is None:
            possibleMoves.append([self.row+2, self.col])
      else:
        if board[self.row+1, self.col] is None:
          possibleMoves.append([self.row+1, self.col])
      # braní figur
      if self.col + 1 <= 7:
        if board[self.row+1, self.col+1] is not None and board[self.row+1, self.col+1].color != self.color:
          possibleMoves.append([self.row+1, self.col+1])
      if self.col - 1 >= 0:
        if board[self.row+1, self.col-1] is not None and board[self.row+1, self.col-1].color != self.color:
          possibleMoves.append([self.row+1, self.col-1])
      #braní mimochodem
      if self.col + 1 <= 7:
        if isinstance(board[self.row,self.col+1],Pawn) and \
            board[self.row,self.col+1].color != self.color and \
            board[self.row+1, self.col+1] is None and \
            board[self.row, self.col+1].lastMoveWasDouble:
          possibleMoves.append([self.row+1, self.col+1])
      if self.col - 1 >= 0:
        if isinstance(board[self.row,self.col-1],Pawn) and \
            board[self.row,self.col-1].color != self.color and \
            board[self.row+1, self.col-1] is None and \
            board[self.row, self.col-1].lastMoveWasDouble:
          possibleMoves.append([self.row+1, self.col-1])
    return possibleMoves
  def possibleMoves(self, board):
    possibleMoves = self.possibleMovesWithoutChecking(board)
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves