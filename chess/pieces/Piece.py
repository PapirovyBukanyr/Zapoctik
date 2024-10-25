from chess.Enums import *
class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position
    self.hasMoved = False
    self.lastMoveWasDouble = False
    self.value = 0
  def move(self, board, end):
    """
    Metoda provede tah figurek.
    Tato metoda provede tah z aktualni pozice figurek na pozici end. Rozhodne se podle typu figurek, zda se ma nastavit lastMoveWasDouble na True.
    _param_ board: Sachovnice, na ktere se tah provede
    _param_ end: Konecna pozice, na kterou se ma figura presunout
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
    Metoda vraci list vsech moznosti, na ktere se figura muze presunout.
    Tato metoda vraci list vsech moznosti, na ktere se figura muze presunout. V listu jsou pouze ty pozice, na ktere se figura muze presunout, protoze jsou volne, nebo jsou obsazene figurou opacne barvy.
    _param_ board: Sachovnice, na ktere se presouvame
    _return_: List pozic, na ktere se figura muze presunout
    """
    pass
  def possibleMovesWithoutChecking(self, board):
    """
    Metoda vraci list vsech moznosti, na ktere se figura muze presunout, nehlede na to, zda by kral byl v sachu.
    Tato metoda vraci list vsech moznosti, na ktere se figura muze presunout. V listu jsou vsechny pozice, na ktere se figura muze presunout, nezalezi na tom, zda by kral byl po provedeni tahu v sachu.
    _param_ board: Sachovnice, na ktere se presouvame
    _return_: List pozic, na ktere se figura muze presunout
    """
    pass
  def copy(self):
    """
    Vraci kopii objektu. Pouziva se, kdybychom chteli mit kopii objektu, bez toho, aby se menil puvodni objekt.
    _return_: Kopia objektu
    """
    pass






  



  



    
 
  


  


