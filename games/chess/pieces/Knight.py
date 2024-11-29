from .Piece import *

class Knight(Piece):
  """Třída reprezentující figurku jezdce v šachu. Dědí od třídy Piece.
  """
  
  def __init__(self, color, position):
    """Konstruktor třídy Knight. Volá konstruktor třídy Piece
    
    Args:
      color (Colors): barva figurky
      position ([int, int]): pozice figurky
    """
    super().__init__(color, position)
    self.symbol = "N"
    self.value = 3
    
  def copy(self):
    """Vytvoří kopii instance třídy Knight.
    """
    return Knight(self.color, self.position)
  
  
  def possibleMoves(self, board):
    """Vrátí seznam možných tahů pro jezdce.
    
    Args:
      board (dict): šachovnice
    """
    possibleMoves = []
    
    for i in [-1,1]:
      for j in [-2,2]:
        possibleMoves.append([self.row+i, self.col+j])
    
    for i in [-2,2]:
      for j in [-1,1]:
        possibleMoves.append([self.row+i, self.col+j])
        
    possibleMoves = [x for x in possibleMoves if x[0] >= 0 and x[0] <= 7 and x[1] >= 0 and x[1] <= 7]
    possibleMoves = [x for x in possibleMoves if board[x] is None or board[x].color != self.color]
    
    return possibleMoves