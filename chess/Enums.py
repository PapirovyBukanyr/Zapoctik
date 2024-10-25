from enum import Enum
class Colors(Enum):
  WHITE = 1
  BLACK = 2
  NULL = 3

  def __str__(self):
    if self == Colors.WHITE:
      return "Bily"
    elif self == Colors.BLACK:
      return "Cerny"
    else:
      return "NULL"