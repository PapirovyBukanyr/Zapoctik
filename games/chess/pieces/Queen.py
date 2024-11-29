from .Piece import *
from .Bishop import *
from .Rook import *

class Queen(Piece):
  """Třída reprezentující figurku královny v šachu. Dědí od třídy Piece.
  """ 
  
  
  def __init__(self, color, position):
    """Konstruktor třídy Queen. Volá konstruktor třídy Piece.
    """
    super().__init__(color, position)
    self.symbol = "Q"
    self.value = 9

  def copy(self):
    """Vytvoří kopii instance třídy Queen.
    """
    return Queen(self.color, self.position)
  
  def possibleMoves(self, board):
    """Vrátí seznam možných tahů pro královnu. 
    """
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMoves(board)
    possibleMoves += Bishop(self.color, self.position).possibleMoves(board)
    return possibleMoves