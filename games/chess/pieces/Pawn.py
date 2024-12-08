from .Piece import *

class Pawn(Piece):
  """
  Třída reprezentující pěšce v šachu. Dědí od třídy Piece.
  
  Attributes:
    color (Colors): barva figurky
    position ([int,int]): pozice figurky
    symbol (str): symbol figurky
    value (int): hodnota figurky
    hasMoved (bool): True, pokud figurka už byla pohnuta, jinak False
    lastMoveWasDouble (bool): True, pokud poslední tah figurkou byl dvojitý, jinak False
  """
  
  
  def __init__(self, color, position):
    """
    Konstruktor třídy Pawn. Volá konstruktor třídy Piece.
    
    Args:
      color (Colors): barva figurky
      position ([int, int]): pozice figurky
    """
    super().__init__(color, position)
    self.symbol = "P"
    self.value = 1
    

  def copy(self):
    """
    Vytvoří kopii instance třídy Pawn.
    
    Returns:
      Pawn: kopie instance třídy Pawn
    """
    copy = Pawn(self.color, self.position)
    copy.hasMoved = self.hasMoved
    copy.lastMoveWasDouble = self.lastMoveWasDouble
    
    return copy
  
  
  def move(self, board, end):
    """
    Zkontroluje, zda je možné provést tah pěšcem a provede ho.
    
    Args:
      board (dict): šachovnice
      end ([int, int]): cílová pozice tahu
    """
    originalPosition = self.position
    
    if not (end[1] == self.col or board[end] is not None):
      board[end] = board[self.position]
      board[self.position] = None
      
      if self.color == Colors.WHITE:
        board[end[0]+1, end[1]] = None
        
      else:
        board[end[0]-1, end[1]] = None
        
      self.position = end
      
    else:
      super().move(board, end)
      
    if abs(originalPosition[0] - self.position[0]) == 2:
      self.lastMoveWasDouble = True
      
      
  def possibleMoves(self, board):
    """
    Vrátí seznam možných tahů pro pěšce.
    
    Args:
      board (dict): šachovnice
      
    Returns:
      List of [int,int]: seznam možných tahů
    """
    possibleMoves = []
    
    if self.color == Colors.WHITE:
      direction = -1
    
    else:
      direction = 1

    # normální tahy
    if not self.hasMoved:
      if board[self.row + direction * 1, self.col] is None:
        possibleMoves.append([self.row + direction * 1, self.col])
        
        if board[self.row + direction * 2, self.col] is None:
          possibleMoves.append([self.row + direction * 2, self.col])
          
    else:
      if board[self.row + direction * 1, self.col] is None:
        possibleMoves.append([self.row + direction * 1, self.col])
        
    # braní figur
    if self.col + 1 <= 7:
      if board[self.row + direction * 1, self.col+1] is not None and board[self.row + direction * 1, self.col+1].color != self.color:
        possibleMoves.append([self.row + direction * 1, self.col+1])
    
    if self.col - 1 >= 0:
      if board[self.row + direction * 1, self.col-1] is not None and board[self.row + direction * 1, self.col-1].color != self.color and self.col - 1 >= 0:
        possibleMoves.append([self.row + direction * 1, self.col-1])
    
    #braní mimochodem
    if self.col + 1 <= 7:
      if isinstance(board[self.row,self.col+1],Pawn) and \
          board[self.row,self.col+1].color != self.color and \
          board[self.row + direction * 1, self.col+1] is None and \
          board[self.row, self.col+1].lastMoveWasDouble:
    
        possibleMoves.append([self.row + direction * 1, self.col+1])
    
    if self.col - 1 >= 0:    
      if isinstance(board[self.row,self.col-1],Pawn) and \
          board[self.row,self.col-1].color != self.color and \
          board[self.row + direction * 1, self.col-1] is None and \
          board[self.row, self.col-1].lastMoveWasDouble:
    
        possibleMoves.append([self.row + direction * 1, self.col-1])
    
    return possibleMoves