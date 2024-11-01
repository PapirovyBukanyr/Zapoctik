from enum import Enum

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
    self = Colors.WHITE if self == Colors.BLACK else Colors.BLACK
    return self
  