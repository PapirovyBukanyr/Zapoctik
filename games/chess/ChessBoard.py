from .pieces import *
from ..Board import *

class ChessBoard (Board):
  def __init__(self):
    super().__init__()
    self.board = [[None for _ in range(8)] for _ in range(8)]
    self.__populateBoard()
    
  def __getitem__(self, index):
    """Vrací figuru na určeném místě na šachovnici, nebo None, pokud je políčko prázdné. 
    
    Args:
        index [int, int]: Tuple dvou integerů, (row, col), oba 0-7
    """
    if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
      return None
    return super().__getitem__(index)
  
  
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
          result += str(self.board[i][j].color) + str(self.board[i][j].symbol) + " "
        except:
          result +=  "__ "
      result += "\n"
    return result
  
  
  def __populateBoard(self):
    """Nastaví šachovnici do normálního stavu. Všichni pěšáci jsou v druhém a sedmém řádku, všechny ostatní figury jsou v prvním a osmém řádku. Barva figurek je v souladu s konvencí, že bílý je dole a černý nahoře."""
    for i in range(8):
      self.board[1][i] = Pawn(Colors.BLACK, [1,i])
      self.board[6][i] = Pawn(Colors.WHITE, [6,i])
    self.board[0][0] = Rook(Colors.BLACK, [0,0])
    self.board[0][7] = Rook(Colors.BLACK, [0,7])
    self.board[7][0] = Rook(Colors.WHITE, [7,0])
    self.board[7][7] = Rook(Colors.WHITE, [7,7])
    self.board[0][1] = Knight(Colors.BLACK, [0,1])
    self.board[0][6] = Knight(Colors.BLACK, [0,6])
    self.board[7][1] = Knight(Colors.WHITE, [7,1])
    self.board[7][6] = Knight(Colors.WHITE, [7,6])
    self.board[0][2] = Bishop(Colors.BLACK, [0,2])
    self.board[0][5] = Bishop(Colors.BLACK, [0,5])
    self.board[7][2] = Bishop(Colors.WHITE, [7,2])
    self.board[7][5] = Bishop(Colors.WHITE, [7,5])
    self.board[0][3] = Queen(Colors.BLACK, [0,3])
    self.board[0][4] = King(Colors.BLACK, [0,4])
    self.board[7][3] = Queen(Colors.WHITE, [7,3])
    self.board[7][4] = King(Colors.WHITE, [7,4])
    
    
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
  
  
  def copy(self):
    """Vrátí kopii šachovnice. Každá figura z originální šachovnice je nahrazena její kopií.
    
    Returns:
        ChessBoard: Kopie šachovnice
    """
    newBoard = ChessBoard()
    for i in range(8):
      for j in range(8):
        if self[i,j] is not None:
          newBoard[i,j] = self[i,j].copy()
    return newBoard
  
  
  def compare(self, board):
    """Porovná dvě šachovnice.
    Tato metoda porovná dvě šachovnice a vrátí True, pokud jsou stejné. Jinak vrátí False.
    
    Args: 
        board: Šachovnice, která se má porovnat s aktuální šachovnicí
    
    Returns: 
        Boolean:True, pokud jsou šachovnice stejné, jinak False
    """
    for i in range(8):
      for j in range(8):
        if self[i,j] is None or board[i,j] is None:
          if self[i,j] is None and board[i,j] is None:
            continue
          return False
        if self[i,j].__dict__ != board[i,j].__dict__:
          return False
    return True
  
  def getListOfBoard(self):
    """Vrátí šachovnici jako list of Field.

    Returns:
        List of Struct Field: šachovnice jako list of Field
    """
    board = [[None for _ in range(8)] for _ in range(8)]
    for i in range(8):
      for j in range(8):
        if self.board[i][j] is None:
          board[i][j] = None
        elif isinstance(self.board[i][j], Pawn):
          board[i][j] = Field(self.board[i][j].color, Figures.PAWN)
        elif isinstance(self.board[i][j], Rook):
          board[i][j] = Field(self.board[i][j].color, Figures.ROOK)
        elif isinstance(self.board[i][j], Bishop):
          board[i][j] = Field(self.board[i][j].color, Figures.BISHOP)
        elif isinstance(self.board[i][j], Knight):
          board[i][j] = Field(self.board[i][j].color, Figures.KNIGHT)
        elif isinstance(self.board[i][j], Queen):
          board[i][j] = Field(self.board[i][j].color, Figures.QUEEN)
        elif isinstance(self.board[i][j], King):
          board[i][j] = Field(self.board[i][j].color, Figures.KING)
    return board