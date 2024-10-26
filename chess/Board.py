from chess.pieces.Piece import *
from chess.pieces.Pawn import *
from chess.pieces.Rook import *
from chess.pieces.Knight import *
from chess.pieces.Bishop import *
from chess.pieces.Queen import *
from chess.pieces.King import *
class Board:
  def __init__(self):
    self.board = [[None for _ in range(8)] for _ in range(8)]
  
  def __getitem__(self, index):
    """Pro možnost přstupovat k poli board jako board[row,col] místo board.board[row][col]
    Args:
        index: Tuple dvou integerů, (row, col), oba 0-7
    Returns:
        Figuru na určeném místě na šachovnici, případně None, pokud je prázdné
    """
    row, col = index
    return self.board[row][col]
  def __setitem__(self, index, value):
    """Nastaví políčko na šachovnici jako board[row,col] namísto board.board[row][col] 
    Args:
        index: Tuple dvou integerů, (row, col), oba 0-7
        value: Instance třídy Piece, nebo None, pokud má být políčko prázdné
    """
    row, col = index
    self.board[row][col] = value
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
  def setupNormalBoard(self):
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
    
    color: Barva figurek, které chceme najít (Colors.WHITE nebo Colors.BLACK)
    _return_: List.figurek dané barvy
    """
    pieceList = []
    for i in range(8):
      for j in range(8):
        if self.board[i][j] is not None and self.board[i][j].color == color:
          pieceList.append(self.board[i][j])
    return pieceList
  def copy(self):
    """Vrátí kopii šachovnice. Každá figura z originální šachovnice je nahrazena její kopií."""
    newBoard = Board()
    for i in range(8):
      for j in range(8):
        if self[i,j] is not None:
          newBoard[i,j] = self[i,j].copy()
    return newBoard
  def compare(self, board):
    """Porovná dvě šachovnice.
    
    Tato metoda porovná dvě šachovnice a vrátí True, pokud jsou stejné. Jinak vrátí False.
    _param_ board: Šachovnice, která se má porovnat s aktuální šachovnicí
    _return_: True, pokud jsou šachovnice stejné, jinak False
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