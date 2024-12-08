from .Piece import *

class Rook(Piece):
  """
  Třída reprezentující figurku věže v šachu. Dědí od třídy Piece.
  
  Attributes:
    color (Colors): Barva figurky
    position ([int,int]): Pozice figurky
    hasMoved (bool): True, pokud figurka už byla pohnuta, jinak False
    lastMoveWasDouble (bool): True, pokud poslední tah figurkou byl dvojitý, jinak False
    value (int): Hodnota figurky
    symbol (str): Symbol figurky
  """
  
  
  def __init__(self, color, position):
    """
    Konstruktor třídy Rook. Volá konstruktor třídy Piece.
    
    Args:
      color (Colors): Barva figurky
      position ([int,int]): Pozice figurky
    """
    super().__init__(color, position)
    self.symbol = "R"
    self.value = 5


  def copy(self):
    """
    Vytvoří kopii instance třídy Rook.
    
    Returns:
      Rook: kopie instance
    """
    copy = Rook(self.color, self.position)
    copy.hasMoved = self.hasMoved
    
    return copy
  
  
  def possibleMoves(self, board):
    """Vrátí seznam možných tahů pro věž.
    
    Args:
      board (dict): šachovnice
      
    Returns:
      List of [int, int]: seznam možných tahů figurky
    """
    possibleMoves = []
    i = 1
    
    for i in [-1,1]:
      for j in [-1,1]:
        x1 = self.row + i
        y1 = self.col
        x2 = self.row
        y2 = self.col + j 
        
        while x1 >= 0 and x1 <= 7 and y1 >= 0 and y1 <= 7:
          if board[x1, y1] is not None:
            if board[x1, y1].color != self.color:
              possibleMoves.append([x1, y1])
        
            break
        
          possibleMoves.append([x1, y1])
          x1 += i
          
        while x2 >= 0 and x2 <= 7 and y2 >= 0 and y2 <= 7:
          if board[x2, y2] is not None:
            if board[x2, y2].color != self.color:
              possibleMoves.append([x2, y2])
        
            break
        
          possibleMoves.append([x2, y2])
          y2 += j
        
    return possibleMoves