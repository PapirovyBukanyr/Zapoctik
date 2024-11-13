from enum import Enum
from dataclasses import dataclass

@dataclass
class Field:
  """Třída reprezentující políčko na šachovnici
  """
  Color: Enum
  Piece: Enum
  
  
class Figures(Enum):
  """Enum pro typy figurek
  """
  # Šachové a dámové figurky
  PAWN = 1 
  ROOK = 2
  BISHOP = 3
  KNIGHT = 4
  QUEEN = 5
  KING = 6
  # Křížky a kolečka pro hru piškvorky
  X = 7
  O = 8
  # Symboly pro hru miny
  FLAG = 9
  EXPLOSION = 10
  ZERO = 11
  ONE = 12
  TWO = 13
  THREE = 14
  FOUR = 15
  FIVE = 16
  SIX = 17
  SEVEN = 18
  EIGHT = 19
  MINE = 20
  
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
  
  