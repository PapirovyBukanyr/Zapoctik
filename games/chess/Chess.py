from .ChessBoard import ChessBoard
from .pieces import *

class Chess:
  def __init__(self):
    self.__movesSinceLastImportantMove = 0
    self.__board = ChessBoard()
    self.__playedPiece = None
    self.__positionsList = [self.__board.copy()]  
    self.__isMoving = Colors.WHITE
    
  
  def getBoard(self):
    return self.__board
  
  def choosePiece (self, positionToPlay, color = None):
    """Funkce pro vyber figurky, kterou chce hrac hrat

    Args:
        positionToPlay ([int, int]): pozice figurky, kterou chce hrac hrat
        color (Enum Colors): Barva hrace, ktery chce hrat

    Returns:
        (list of [int, int]): dostupne pozice, kam muze hrac hrat
    """
    if color is not None:
      self.__isMoving = color
    try:
      if self.__isMoving != self.__board[positionToPlay].color:
        return []
      self.__playedPiece = self.__board[positionToPlay]
      return  self.__playedPiece.possibleMoves(self.__board)
    except:
      return []


  def makeMove(self, playedMove):
    """Provedení tahu hrace

    Args:
        playedMove ([int, int]): pozice, kam chce hrac hrat

    Returns:
        bool: tah se zdařil nebo ne
        string: "Promote" pokud je potreba provest vylepseni pesaka
    """
    
    if self.__playedPiece is None:
      return False
    if playedMove is None:
      return False
    if playedMove not in self.__playedPiece.possibleMoves(self.__board):
      return False

    if isinstance(self.__playedPiece,Pawn) or self.__board[playedMove] is not None:
      self.__movesSinceLastImportantMove = -1
    self.__playedPiece.move(self.__board, playedMove)
    self.__movesSinceLastImportantMove += 1
    self.__positionsList.append(self.__board.copy())
    
    if isinstance(self.__playedPiece, Pawn) and self.__playedPiece.row == (0 if self.__playedPiece.color == Colors.WHITE else 7):
      return "Promote"
      
    return self.__endOfMove()


  def promote(self, newFigure):
    """Promote pesaka

    Args:
        newFigure (string): figurka, na kterou se ma pesak zmenit ("Q", "R", "B", "N")
        
    Returns:
        bool: podle toho zda se tah podaril nebo ne
        string: pokud hra skoncila
    """
    
    if not isinstance(self.__playedPiece, Pawn):
      print("Promote can be called only on pawn")
      return False
    
    match(newFigure):
      case "Q":
        self.__board[self.__playedPiece.position] = Queen(self.__playedPiece.color, self.__playedPiece.position)
      case "R":
        self.__board[self.__playedPiece.position] = Rook(self.__playedPiece.color, self.__playedPiece.position)
      case "B":
        self.__board[self.__playedPiece.position] = Bishop(self.__playedPiece.color, self.__playedPiece.position)
      case "N":
        self.__board[self.__playedPiece.position] = Knight(self.__playedPiece.color, self.__playedPiece.position)
      case _:
        return False
      
    return self.__endOfMove()
    
    
  def __endOfMove(self):
    """Konec tahu
    
    Returns:
        True: novy stav sachovnice po tahu
        string: string pokud hra skoncila
    """
    self.__playedPiece = None

    self.__isMoving = Colors.BLACK if self.__isMoving == Colors.WHITE else Colors.WHITE
    
    self.__printToTerminal()
    
    return True


  def checkEnd(self):
    """Kontrola konce hry
    
    Returns:
        string: "Draw by fifty-move rule" pokud bylo 50 tahu bez pohybu pesaku nebo braneni
        string: "Draw by threefold repetition" pokud se stejna pozice opakovala 3x
        string: "{color} won" pokud byl vyhozen kral
        None: pokud hra neskoncila
    """
    if self.__movesSinceLastImportantMove >= 100:
      return "Draw by fifty-move rule"
    
    for i in range(0,len(self.__positionsList)-1):
      count = 0
      for j in range(i+1, len(self.__positionsList)):
        if self.__positionsList[i].compare(self.__positionsList[j]):
          count += 1
      if count >= 3:
        return "Draw by threefold repetition"
      
    for color in [Colors.WHITE, Colors.BLACK]:
      isKing = False
      for piece in self.__board.pieceList(color):
        if piece.symbol == "K":
          isKing = True
          break
      if not isKing:
        if color == Colors.WHITE:
          color = Colors.BLACK
        else: 
          color = Colors.WHITE
        return f"{color} won"
    return None
      
  def __printToTerminal(self):  
    """Vytiskne hrací desku do konzole
    """
    print(self.__board ) 
    