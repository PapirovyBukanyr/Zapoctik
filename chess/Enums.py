from enum import Enum
class Colors(Enum):
  WHITE = 1
  BLACK = 2
  def __str__(self):
    if self == Colors.WHITE:
      return "W"
    else:
      return "B"