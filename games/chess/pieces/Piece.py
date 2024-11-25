from ...Enums import *
class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position
    self.hasMoved = False
    self.lastMoveWasDouble = False
    self.value = 0
    self.image = None
    
  def move(self, board, end):
    """
    Metoda pro pohnutí figurky po šachovnici

    Args:
        board (Board): Sachovnice, na kterou se tah províde
        end ([row, col]): Policko, kam se tah províde
    """
    if not self.hasMoved:
      self.hasMoved = True
    board[end] = board[self.position]
    board[self.position] = None
    self.position = end
    pawns = board.pieceList(Colors.BLACK) + board.pieceList(Colors.WHITE)
    pawns = [ pawn for pawn in pawns if pawn.symbol == "P" ]
    for pawn in pawns:
      if pawn.lastMoveWasDouble:
        pawn.lastMoveWasDouble = False
        
        
  @property
  def row (self):
    return self.position[0]
  
  
  @property
  def col (self):
    return self.position[1]
  
  
  def possibleMoves(self, board):
    """
    Funkce pro vypsání všech možných tahů danou figurkou

    Args:
        board (Board): Sachovnice, na kterou se tah províde

    Returns:
        (list of [row, col]): Seznam všech možných tahů ve formátu
    """
    pass
  
  
  def copy(self):
    """
    Vraci kopii objektu. Pouziva se, kdybychom chteli mit kopii objektu, bez toho, aby se menil puvodni objekt.
    Returns:
        (Piece): Kopie objektu
    """
    pass