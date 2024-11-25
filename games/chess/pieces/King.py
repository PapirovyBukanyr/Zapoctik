from .Piece import *

class King(Piece):
  """Třída reprezentující figurku krále v šachu. Dědí od třídy Piece.
  """
  
  
  def __init__(self, color, position):
    """Konstruktor třídy King. Volá konstruktor třídy Piece.
    """
    super().__init__(color, position)
    self.symbol = "K"
    
  def copy(self):
    """Vytvoří kopii instance třídy King.
    """
    copy = King(self.color, self.position)
    copy.hasMoved = self.hasMoved
    
    return copy
  
  
  def move(self, board, end):
    """Zkontroluje, zda je možné provést tah králem a provede ho.
    
    Args:
      board - šachovnice
      end - cílová pozice tahu
    """
    if end[1] - self.col == 2:
      board[self.row, 7].move(board, [self.row, 5])
      
    if end[1] - self.col == -2:
      board[self.row, 0].move(board, [self.row, 3])
      
    super().move(board, end)
    
    
  def possibleMoves(self, board):
    """Vrátí seznam možných tahů pro krále. 
    """
    possibleMoves = []
    
    # normalni tahy
    for i in range(-1,2):
      
      for j in range(-1,2):
        
        if i == 0 and j == 0:
          continue
        
        possibleMoves.append([self.row+i, self.col+j])
        
    possibleMoves = [x for x in possibleMoves if (x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7)]
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    
    # rosady
    if not self.hasMoved:
      
      if board[self.row, 7] is not None:
      
        if board[self.row, self.col+1] is None and \
            board[self.row, self.col+2] is None and \
            not board[self.row, 7].hasMoved:
      
          possibleMoves.append([self.row, self.col+2])
      
      if board[self.row, 0] is not None:
        if board[self.row, self.col-1] is None and \
            board[self.row, self.col-2] is None and \
            board[self.row, self.col-3] is None and \
            not board[self.row, 0].hasMoved:
      
          possibleMoves.append([self.row, self.col-2])
    
    return possibleMoves