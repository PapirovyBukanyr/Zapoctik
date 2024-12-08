from .Piece import *
from .Bishop import *
from .Rook import *

class Queen(Piece):
  """
  Třída reprezentující figurku královny v šachu. Dědí od třídy Piece.
  
  Attributes:
    color (Colors): Barva figurky
    position ([int,int]): Pozice figurky
    hasMoved (bool): True, pokud figurka už byla pohnuta, jinak False
    lastMoveWasDouble (bool): True, pokud poslední tah figurkou byl dvojitý, jinak False
    value (int): Hodnota figurky
    symbol (str): Symbol figurky
  """ 
  
  
  def __init__(self, color, position):
    """Konstruktor třídy Queen. Volá konstruktor třídy Piece.
    """
    super().__init__(color, position)
    self.symbol = "Q"
    self.value = 9


  def copy(self):
    """
    Vytvoří kopii instance třídy Queen.
    
    Returns:
      Queen: kopie instance
    """
    return Queen(self.color, self.position)
  
  
  def possibleMoves(self, board):
    """
    Vrátí seznam možných tahů pro královnu. 
    
    Args:
      board (dict): šachovnice
      
    Returns:
      List of [int, int]: seznam možných tahů figurky
    """
    possibleMoves = []
    possibleMoves += Rook(self.color, self.position).possibleMoves(board)
    possibleMoves += Bishop(self.color, self.position).possibleMoves(board)
    return possibleMoves