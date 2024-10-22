from Enums import *
class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position
    self.hasMoved = False
  def move(self, board, end):
    board[end] = board[self.position]
    board[self.position] = None
    self.position = end
    if not self.hasMoved:
      self.hasMoved = True
  @property
  def row (self):
    return self.position[0]

  @property
  def col (self):
    return self.position[1]


class Pawn(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "P"
  def possibleMoves(self, board):
    possibleMoves = []
    if self.color == Colors.WHITE:
      if not self.hasMoved:
        possibleMoves.append([self.row-1, self.col])
        possibleMoves.append([self.row-2, self.col])
      else:
        possibleMoves.append([self.row-1, self.col])
    else:
      if not self.hasMoved:
        possibleMoves.append([self.row+1, self.col])
        possibleMoves.append([self.row+2, self.col])
      else:
        possibleMoves.append([self.row+1, self.col])
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    return possibleMoves


class Rook(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "R"
  def possibleMoves(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0:
      if board[[self.row-i, self.col]] is not None and board[[self.row-i, self.col]].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col])
      i += 1
    i = 1
    while self.row + i <= 7:
      if board[[self.row+i, self.col]] is not None and board[[self.row+i, self.col]].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col])
      i += 1
    i = 1
    while self.col - i >= 0:
      if board[[self.row, self.col-i]] is not None and board[[self.row, self.col-i]].color == self.color:
        break
      possibleMoves.append([self.row, self.col-1])
      i += 1
    i = 1
    while self.col + i <= 7:  
      if board[[self.row, self.col+i]] is not None and board[[self.row, self.col+i]].color == self.color:
        break 
      possibleMoves.append([self.row, self.col+i])
      i += 1
    return possibleMoves
  


class Knight(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "N"
  def possibleMoves(self, board):
    possibleMoves = []
    possibleMoves.append([self.row-1, self.col-2])
    possibleMoves.append([self.row-1, self.col+2])
    possibleMoves.append([self.row+1, self.col-2])
    possibleMoves.append([self.row+1, self.col+2])
    possibleMoves.append([self.row-2, self.col-1])
    possibleMoves.append([self.row-2, self.col+1])
    possibleMoves.append([self.row+2, self.col-1])
    possibleMoves.append([self.row+2, self.col+1])
    possibleMoves = [x for x in possibleMoves if (board[x] is None or board[x].color != self.color) and (x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7)]
    return possibleMoves
  


class Bishop(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "B"
  def possibleMoves(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0 and self.col - i >= 0:
      if board[[self.row-i, self.col-i]] is not None and board[[self.row-i, self.col-i]].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col-i])
      i += 1
    i = 1
    while self.row - i >= 0 and self.col + i <= 7:
      if board[[self.row-i, self.col+i]] is not None and board[[self.row-i, self.col+i]].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col+i])
      i += 1
    i = 1
    while self.row + i <= 7 and self.col - i >= 0:
      if board[[self.row+i, self.col-i]] is not None and board[[self.row+i, self.col-i]].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col-i])
      i += 1  
    i = 1
    while self.row + i <= 7 and self.col + i <= 7:  
      if board[[self.row+i, self.col+i]] is not None and board[[self.row+i, self.col+i]].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col+i])
      i += 1
    return possibleMoves
  

class Queen(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "Q"
  def possibleMoves(self, board):
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMoves(board)
    possibleMoves += Bishop(self.color, self.position).possibleMoves(board)
    return possibleMoves
  


class King(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "K"
  def possibleMoves(self, board):
    possibleMoves = []
    possibleMoves.append([self.row-1, self.col])
    possibleMoves.append([self.row-1, self.col+1])
    possibleMoves.append([self.row, self.col+1])
    possibleMoves.append([self.row+1, self.col+1])
    possibleMoves.append([self.row+1, self.col])
    possibleMoves.append([self.row+1, self.col-1])
    possibleMoves.append([self.row, self.col-1])
    possibleMoves.append([self.row-1, self.col-1])
    possibleMoves = [x for x in possibleMoves if (board[x] is None or board[x].color != self.color) and (x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7)]
    return possibleMoves