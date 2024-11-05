from .pieces import *
from ..Board import *
from ..Enums import *

class CheckersBoard (Board):
  def __init__(self):
    super().__init__()
    self.__populateBoard()
    
  def __getitem__(self, index):
    """Vrací figuru na určeném místě na šachovnici, nebo None, pokud je políčko prázdné. 
    
    Args:
        index [int, int]: Tuple dvou integerů, (row, col), oba 0-7
    """
    try:
      if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
        return None
      return super().__getitem__(index)
    except:
      return None
  
  
  def __setitem__(self, index, value):
    """Nastaví políčko na šachovnici jako board[row,col] namísto board.board[row][col] 
    
    Args:
        index ([int, int]): Tuple dvou integerů, (row, col), oba 0-7
        value (Piece): Instance třídy Piece, nebo None, pokud má být políčko prázdné
        
    Returns:
        bool: True, pokud se podařilo nastavit políčko, jinak False
    """
    if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
      return False
    super().__setitem__(index, value)
    return True
    
    
  def __str__(self):
    """Vrací string reprezentaci šachovnice. Každé políčko je reprezentováno jako string, který je tvořen z informací o barvě a symbolu figury, nebo jako string "__", pokud je políčko prázdné. Políčka jsou oddělena mezerou a jednotlivé řádky jsou odděleny znakem nového řádku (\n)."""
    result = ""
    for i in range(8):
      for j in range(8):
        try:
            if self.board[i][j]!=None:
                result += str(self.board[i][j]) + " "
            else:
                result += "__ "
        except:
          result +=  "__ "
      result += "\n"
    return result
  
  
  def __populateBoard(self):
    """Nastaví šachovnici do počátečního stavu. Bílý je dole a černý nahoře."""
    self.board = [[None for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            if i < 3 and i%2 == j%2:
                self.board[i][j] = Pawn(Colors.BLACK, [i,j])
            elif i > 4 and i%2 == j%2:
                self.board[i][j] = Pawn(Colors.WHITE, [i,j])
            else:
              self.board[i][j] = None
    
    
  def pieceList(self, color):
    """Vrací list všech figurek dané barvy na šachovnici.
    
    Args:
        color (Enum Colors): Barva figurek, které chceme najít (Colors.WHITE nebo Colors.BLACK)
        
    Returns: 
        List of Pieces: List figurek dané barvy
    """
    pieceList = []
    for i in range(8):
      for j in range(8):
        if self.board[i][j] is not None and self.board[i][j].color == color:
          pieceList.append(self.board[i][j])
    return pieceList
  
  def getListOfBoard(self):
    """Vrací list všech figurek na šachovnici.
    
    Returns: 
        List of Fields: List figurek na šachovnici
    """
    pieceList = [[None for i in range(8)] for j in range(8)]
    for i in range(8):
      for j in range(8):
        if self.board[i][j] is  None:
          pieceList[i][j] = None
        elif isinstance(self.board[i][j], Pawn): 
          pieceList[i][j] = Field(self.board[i][j].color, Figures.PAWN)
        elif isinstance(self.board[i][j], Queen):
          pieceList[i][j] = Field(self.board[i][j].color, Figures.QUEEN)
    return pieceList