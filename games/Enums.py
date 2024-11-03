from enum import Enum
from dataclasses import dataclass

@dataclass
class Field:
  """Třída reprezentující políčko na šachovnici
  """
  Color: Enum
  Piece: Enum
  
class Colors(Enum):
  """Enum pro barvy
  """
  WHITE = 1
  BLACK = 2
  def __str__(self):
    """Vrací string reprezentaci barvy

    Returns:
        String: reprezentovaná barva
    """
    if self == Colors.WHITE:
      return "W"
    else:
      return "B"
    
  def changeColor(self):
    """Vrátí inverzní barvu
    
    Returns:
        Enum Colors: inverzní barva
    """
    return Colors.WHITE if self == Colors.BLACK else Colors.BLACK
  
class Figures(Enum):
  """Enum pro typy figurek
  """
  PAWN = 1
  ROOK = 2
  BISHOP = 3
  KNIGHT = 4
  QUEEN = 5
  KING = 6
  X = 7
  O = 8
  