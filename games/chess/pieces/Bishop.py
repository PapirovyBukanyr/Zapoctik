from .Piece import *

class Bishop(Piece):
  """
  Třída reprezentující figurku střelce v šachu. Dědí od třídy Piece.
  
  Attributes:
    color (Colors): barva figurky
    position ([int,int]): pozice figurky
    symbol (str): symbol figurky
    value (int): hodnota figurky
  """
  
  
  def __init__(self, color, position):
    """
    Konstruktor třídy Bishop. Volá konstruktor třídy Piece.
    
    Args:
      color (Colors): barva figurky
      position ([int,int]): pozice figurky
    """
    super().__init__(color, position)
    self.symbol = "B"
    self.value = 3
    
    
  def copy(self):
    """
    Vytvoří kopii instance třídy Bishop.
    
    Returns:
      Bishop: kopie instance třídy Bishop
    """
    return Bishop(self.color, self.position)
  
  
  def possibleMoves(self, board):
    """
    Vrátí seznam možných tahů pro střelce. 
    
    Args:
      board (Board): šachovnice, na které se figurka nachází
    """
    possibleMoves = []
    
    for i in [-1,1]:
      
      for j in [-1,1]:
        x = self.row + i
        y = self.col + j
      
        while x >= 0 and x <= 7 and y >= 0 and y <= 7:
      
          if board[x, y] is not None:
      
            if board[x, y].color != self.color:
              possibleMoves.append([x, y])
      
            break
      
          possibleMoves.append([x, y])
          x += i
          y += j
      
    return possibleMoves