from .Board import Board
from .pieces import *

class GameController:
  
  def __init__(self):
    self.movesSinceLastImportantMove = 0
    self.board = Board()
    self.playedPiece = None
    self.board.setupNormalBoard()
    self.positionsList = [self.board.copy()]  
    self.isMoving = Colors.WHITE
  
  def playedPiecePosition (self, positionToPlay, color = None):
    """Funkce pro zjisteni moznych tahu hrace

    Args:
        positionToPlay ([int, int]): pozice figurky, kterou chce hrac hrat
        color (Enum Colors): Barva hrace, ktery chce hrat

    Returns:
        (list of [int, int]): dostupne pozice, kam muze hrac hrat
    """
    if color is not None:
      self.isMoving = color
    try:
      if self.isMoving != self.board[positionToPlay].color:
        return []
      self.playedPiece = self.board[positionToPlay]
      return  self.playedPiece.possibleMoves(self.board)
    except:
      return []


  def makeMove(self, playedMove):
    """Provedení tahu hrace

    Args:
        playedMove ([int, int]): pozice, kam chce hrac hrat

    Returns:
        bool: tah se zdařil nebo ne
        string: "Promote" pokud je potreba provest vylepseni pesaka, jinak konec hry
        board: novy stav sachovnice po tahu
        tuple: (board, string) pokud hra skoncila
    """
    
    if self.playedPiece is None:
      return False
    if playedMove is None:
      return False
    if playedMove not in self.playedPiece.possibleMoves(self.board):
      return False

    if isinstance(self.playedPiece,Pawn) or self.board[playedMove] is not None:
      self.movesSinceLastImportantMove = -1
    self.playedPiece.move(self.board, playedMove)
    self.movesSinceLastImportantMove += 1
    self.positionsList.append(self.board.copy())
    
    if isinstance(self.playedPiece, Pawn) and self.playedPiece.row == (0 if self.playedPiece.color == Colors.WHITE else 7):
      return "Promote"
      
    return self.endOfMove()


  def promote(self, newFigure):
    """Promote pesaka

    Args:
        newFigure (string): figurka, na kterou se ma pesak zmenit ("Q", "R", "B", "N")
        
    Returns:
        bool: podle toho zda se tah podaril nebo ne
        string: pokud hra skoncila
    """
    
    if not isinstance(self.playedPiece, Pawn):
      print("Promote can be called only on pawn")
      return False
    
    match(newFigure):
      case "Q":
        self.board[self.playedPiece.position] = Queen(self.playedPiece.color, self.playedPiece.position)
      case "R":
        self.board[self.playedPiece.position] = Rook(self.playedPiece.color, self.playedPiece.position)
      case "B":
        self.board[self.playedPiece.position] = Bishop(self.playedPiece.color, self.playedPiece.position)
      case "N":
        self.board[self.playedPiece.position] = Knight(self.playedPiece.color, self.playedPiece.position)
      case _:
        return False
      
    return self.endOfMove()
    
    
  def endOfMove(self):
    """Konec tahu
    
    Returns:
        True: novy stav sachovnice po tahu
        string: string pokud hra skoncila
    """
    self.playedPiece = None
    
    result = self.checkGameOver()
    if result is not None:
      return result

    self.isMoving = Colors.BLACK if self.isMoving == Colors.WHITE else Colors.WHITE
    
    return True


  def checkGameOver(self):
    """Kontrola konce hry
    
    Returns:
        string: "Draw by fifty-move rule" pokud bylo 50 tahu bez pohybu pesaku nebo braneni
        string: "Draw by threefold repetition" pokud se stejna pozice opakovala 3x
        string: "Checkmate {color} won" pokud byl vyhozen kral
    """
    if self.movesSinceLastImportantMove >= 100:
      return "Draw by fifty-move rule"
    
    for i in range(0,len(self.positionsList)-1):
      count = 0
      for j in range(i+1, len(self.positionsList)):
        if self.positionsList[i].compare(self.positionsList[j]):
          count += 1
      if count >= 3:
        return "Draw by threefold repetition"
      
    for color in [Colors.WHITE, Colors.BLACK]:
      isKing = False
      for piece in self.board.pieceList(color):
        if piece.symbol == "K":
          isKing = True
          break
      if not isKing:
        if color == Colors.WHITE:
          color = Colors.BLACK
        else: 
          color = Colors.WHITE
        return f"Checkmate {color} won"
    