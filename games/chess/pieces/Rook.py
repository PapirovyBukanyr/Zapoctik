from .Piece import *

class Rook(Piece):
  """Třída reprezentující figurku věže v šachu. Dědí od třídy Piece.
  """
  
  def __init__(self, color, position):
    """Konstruktor třídy Rook. Volá konstruktor třídy Piece.
    """
    super().__init__(color, position)
    self.symbol = "R"
    self.value = 5

  def copy(self):
    """Vytvoří kopii instance třídy Rook.
    """
    copy = Rook(self.color, self.position)
    copy.hasMoved = self.hasMoved
    
    return copy
  
  def possibleMoves(self, board):
    """Vrátí seznam možných tahů pro věž.
    
    Args:
      board (dict): šachovnice
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