from Enums import *
class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position
    self.hasMoved = False
    self.lastMoveWasDouble = False
  def move(self, board, end):
    """
    Metoda provede tah figurek.
    Tato metoda provede tah z aktualni pozice figurek na pozici end. Rozhodne se podle typu figurek, zda se ma nastavit lastMoveWasDouble na True.
    _param_ board: Sachovnice, na ktere se tah provede
    _param_ end: Konecna pozice, na kterou se ma figura presunout
    """
    if not self.hasMoved:
      self.hasMoved = True
    if abs(end[0] - self.position[0]) == 2:
      self.lastMoveWasDouble = True
    else:
      self.lastMoveWasDouble = False
    board[end] = board[self.position]
    board[self.position] = None
    self.position = end
  @property
  def row (self):
    return self.position[0]

  @property
  def col (self):
    return self.position[1]
  def possibleMoves(self, board):
    """
    Metoda vraci list vsech moznosti, na ktere se figura muze presunout.
    Tato metoda vraci list vsech moznosti, na ktere se figura muze presunout. V listu jsou pouze ty pozice, na ktere se figura muze presunout, protoze jsou volne, nebo jsou obsazene figurou opacne barvy.
    _param_ board: Sachovnice, na ktere se presouvame
    _return_: List pozic, na ktere se figura muze presunout
    """
    pass
  def copy(self):
    """
    Vraci kopii objektu. Pouziva se, kdybychom chteli mit kopii objektu, bez toho, aby se menil puvodni objekt.
    _return_: Kopia objektu
    """
    pass


class Pawn(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "P"
  def copy(self):
    copy = Pawn(self.color, self.position)
    copy.hasMoved = self.hasMoved
    copy.lastMoveWasDouble = self.lastMoveWasDouble
    return copy
  def possibleMoves(self, board):
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
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves


class Rook(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "R"
  def copy(self):
    copy = Rook(self.color, self.position)
    copy.hasMoved = self.hasMoved
    return copy
  def possibleMoves(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0:
      if board[self.row-i, self.col] is not None and board[self.row-i, self.col].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col])
      i += 1
    i = 1
    while self.row + i <= 7:
      if board[self.row+i, self.col] is not None and board[self.row+i, self.col].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col])
      i += 1
    i = 1
    while self.col - i >= 0:
      if board[self.row, self.col-i] is not None and board[self.row, self.col-i].color == self.color:
        break
      possibleMoves.append([self.row, self.col-1])
      i += 1
    i = 1
    while self.col + i <= 7:  
      if board[self.row, self.col+i] is not None and board[self.row, self.col+i].color == self.color:
        break 
      possibleMoves.append([self.row, self.col+i])
      i += 1
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves
  


class Knight(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "N"
  def copy(self):
    return Knight(self.color, self.position)
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
    possibleMoves = [x for x in possibleMoves if x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7]
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves
  


class Bishop(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "B"
  def copy(self):
    return Bishop(self.color, self.position)
  def possibleMoves(self, board):
    possibleMoves = []
    i = 1
    while self.row - i >= 0 and self.col - i >= 0:
      if board[self.row-i, self.col-i] is not None and board[self.row-i, self.col-i].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col-i])
      i += 1
    i = 1
    while self.row - i >= 0 and self.col + i <= 7:
      if board[self.row-i, self.col+i] is not None and board[self.row-i, self.col+i].color == self.color:
        break
      possibleMoves.append([self.row-i, self.col+i])
      i += 1
    i = 1
    while self.row + i <= 7 and self.col - i >= 0:
      if board[self.row+i, self.col-i] is not None and board[self.row+i, self.col-i].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col-i])
      i += 1  
    i = 1
    while self.row + i <= 7 and self.col + i <= 7:  
      if board[self.row+i, self.col+i] is not None and board[self.row+i, self.col+i].color == self.color:
        break
      possibleMoves.append([self.row+i, self.col+i])
      i += 1
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    return possibleMoves
  

class Queen(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "Q"
  def copy(self):
    return Queen(self.color, self.position)
  def possibleMoves(self, board):
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMoves(board)
    possibleMoves += Bishop(self.color, self.position).possibleMoves(board)
    return possibleMoves
  


class King(Piece):
  def __init__(self, color, position):
    super().__init__(color, position)
    self.symbol = "K"
  def copy(self):
    copy = King(self.color, self.position)
    copy.hasMoved = self.hasMoved
    return copy
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
    possibleMoves = [x for x in possibleMoves if not board.wouldKingBeInCheck(self.color, self.position, x)]
    # rosady
    if not self.hasMoved:
      if board[self.row, self.col+1] is None and \
          board[self.row, self.col+2] is None and \
          not board.wouldKingBeInCheck(self.color, self.position, [self.row, self.col+2]) and \
          not board.wouldKingBeInCheck(self.color, self.position, [self.row, self.col+1]) and \
          not board[self.row, 7].hasMoved:
        possibleMoves.append([self.row, self.col+2])
      if board[self.row, self.col-1] is None and \
          board[self.row, self.col-2] is None and \
          not board.wouldKingBeInCheck(self.color, self.position, [self.row, self.col-2]) and \
          not board.wouldKingBeInCheck(self.color, self.position, [self.row, self.col-1]) and\
          not board[self.row, 0].hasMoved:
        possibleMoves.append([self.row, self.col-2])
    return possibleMoves