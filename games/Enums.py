from enum import Enum
from dataclasses import dataclass

@dataclass
class Field:
  """Třída reprezentující políčko na šachovnici
  """
  color: Enum # Barva políčka (Colors)
  piece: Enum # Figurka na políčku (Figures)
  
  
class Figures(Enum):
  """Enum pro typy figurek
  """
  
  
  PAWN = 1 # Pěšec do šachů, dámy, ...
  ROOK = 2 # Věž do šachů
  BISHOP = 3 # Střelec do šachů
  KNIGHT = 4 # Jezdec do šachů
  QUEEN = 5 # Dáma do šachů, dámy, ...
  KING = 6 # Král do šachů
  X = 7 # X do piškvorek
  O = 8 # O do piškvorek
  FLAG = 9 # Vlajka do hledání min
  EXPLOSION = 10 # Výbuch do hledání min
  MINE = 11 # Mina do hledání min
  ONE = 12 # 1 do hledání min, hledání krtka, ...
  TWO = 13 # 2 do hledání min, hledání krtka, ...
  THREE = 14 # 3 do hledání min, hledání krtka, ...
  FOUR = 15 # 4 do hledání min, hledání krtka, ...
  FIVE = 16 # 5 do hledání min, hledání krtka, ...
  SIX = 17 # 6 do hledání min, hledání krtka, ...
  SEVEN = 18 # 7 do hledání min, hledání krtka, ...
  EIGHT = 19 # 8 do hledání min, hledání krtka, ...
  SHADOW = 20 # Stín do šachů s mlhou války, dám s mlhou války, min, hledání krtka, ...
  MOLE = 21 # Krteček!!!
  
class Colors(Enum):
  """Enum pro barvy
  """
  
  
  WHITE = 1
  BLACK = 2
  RED = 3
  GREEN = 4
  
  
  def __str__(self):
    """Vrací string reprezentaci barvy

    Returns:
        String: reprezentovaná barva
    """
    if self == Colors.WHITE:
      return "W"
    
    elif self == Colors.BLACK:
      return "B"
    
    elif self == Colors.RED:
      return "R"
    
    elif self == Colors.GREEN:
      return "G"
    
    
  def changeColor(self):
    """Vrátí inverzní barvu
    
    Returns:
        Enum Colors: inverzní barva
    """
    return Colors.WHITE if self == Colors.BLACK else Colors.BLACK
  
  
  def changeColorFour(self):
    """Vrátí další barvu
    
    Returns:
        Enum Colors: další barva
    """
    if self == Colors.WHITE:
      return Colors.BLACK
    
    elif self == Colors.BLACK:
      return Colors.RED
    
    elif self == Colors.RED:
      return Colors.GREEN
    
    else:
      return Colors.WHITE
  
  