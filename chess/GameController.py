from .Board import Board
from .pieces import *

class GameController:
  def __init__(self):
    self.board = None
    self.makingMove = Colors.WHITE
    self.movesSinceLastImportantMove = 0
    self.positionsList = []

  def startGame(self):
    """
    Metoda startGame zapne hru. Vytvori sachovnici, nastavi ji do normalniho stavu a zapne smycku, ktera bude volat metodu makeMove, dokud hra neskonci.
    """
    self.board = Board()
    self.board.setupNormalBoard()
    self.positionsList.append(self.board.copy())
    self.play()
    
  def play(self):
    """
    Metoda play provede kolo hry. Vyzve hrace, aby provedli tah, a pak kontroluje, zda hra skoncila. Pokud hra skoncila, vypise vysledek a ukonci kolo. Pokud hra neskoncila, vypise novou pozici sachovnice, prenese hru na druhého hrace a opakuje kolo.
    """
    print(self.board)
    while True:
      self.makeMove()
      result = self.checkGameOver()
      if result is not None:
        print(self.board)
        print(result)
        break
      print(self.board)
      self.changePlayer()
      print(f"Hraje {self.makingMove}")


  def makeMove(self):
    #vsechno tohle do budoucna zmenit za klikani a zobrazovani v GUI, zatim v konzolovce
    """
    Metoda makeMove provede tah hrace. Vyzve hrace, aby zvolil figuru, kterou chce tahnout, a pak zvolil, kam chce tahnout. Pokud je tah platny, provede ho a zapise si novou pozici sachovnice do historie. Pokud je tah neplatny, vyzve hrace znovu. Pokud je tahnuta pesaka na druhe strane sachovnice, vyvolava se metoda promote.
    """
    playedPiecePosition = None
    playedMove = None
    while True:
      try:
        playedPiecePosition = input("Zvolte figuru, kterou chcete táhnout: ")
        if playedPiecePosition.upper() == "QUIT":
          quit()
        playedPiecePosition = [int(x) for x in playedPiecePosition.split(",")]
      except:
        print("Neplatné pole, zkuste to znovu")
        continue
      if self.board[playedPiecePosition] is not None and self.board[playedPiecePosition].color == self.makingMove and self.board[playedPiecePosition].possibleMoves(self.board) != []:
        print(self.board[playedPiecePosition].possibleMoves(self.board))
        break
      print("Neplatné pole, zkuste to znovu")
    playedPiece = self.board[playedPiecePosition]
    while True:
      playedMove = input("Zvolte, kam chcete táhnout: ")
      if playedMove.upper() == "QUIT":
        quit()
      try:
        playedMove = [int(x) for x in playedMove.split(",")]
      except:
        print("Neplatné pole, zkuste to znovu")
        continue
      if playedMove in self.board[playedPiecePosition].possibleMoves(self.board):
        if isinstance(self.board[playedPiecePosition],Pawn) or self.board[playedMove] is not None:
          self.movesSinceLastImportantMove = -1
        self.board[playedPiecePosition].move(self.board, playedMove)
        self.movesSinceLastImportantMove += 1
        self.positionsList.append(self.board.copy())
        break
      print("Neplatné pole, zkuste to znovu")
    if isinstance(playedPiece, Pawn) and playedPiece.row == (0 if playedPiece.color == Colors.WHITE else 7):
      self.promote(playedPiece)
  def changePlayer(self):
    """
    Metoda changePlayer zmeni hrace, ktery ma tahnout. Pokud je self.makingMove Colors.WHITE, zmeni se na Colors.BLACK, jinak se zmeni na Colors.WHITE.
    """
    if self.makingMove == Colors.WHITE:
      self.makingMove = Colors.BLACK
    else:
      self.makingMove = Colors.WHITE
  def promote(self, pawn):
    """
    Metoda promote provede promote (nevim, jak se to rekne cesky) peshaka, ktery dosahl posledniho radku.
    Metoda se vola, pokud pesak dosahl posledniho radku a hráč muze zvolit, na kterou figurku se pesak zmeni.
    _param_ pawn: Pesak, ktery se ma promotovat
    """
    choice = input("Zvolte figurku, kterou chcete zvolit: ")  
    match(choice):
      case "Q":
        self.board[pawn.position] = Queen(pawn.color, pawn.position)
      case "R":
        self.board[pawn.position] = Rook(pawn.color, pawn.position)
      case "B":
        self.board[pawn.position] = Bishop(pawn.color, pawn.position)
      case "N":
        self.board[pawn.position] = Knight(pawn.color, pawn.position)
      case _:
        print("Neplatné pole, zkuste to znovu")
        self.promote(pawn)

  def checkGameOver(self):
    """
    Zkontroluje, zda hra skoncila.
    Metoda zkontroluje, zda je remiza, nebo checkmate. Pokud je remiza, vrati string "Draw by ...", jinak vrati None. Pokud je checkmate, vrati string "Checkmate {color} won", kde {color} je barva vitezne strany.
    """
    def isInsufficientMaterial():
      """
      Kontroluje, zda jsou na sachovnici insufficient material, tedy situace, kdy hra skonci remizou, protoze nelze dat mat.
      Vraci True, pokud je insufficient material, jinak False.
      """
      whitePieces = self.board.pieceList(Colors.WHITE)
      blackPieces = self.board.pieceList(Colors.BLACK)
      #kral vs kral
      if len(whitePieces) < 2 and len(blackPieces) < 2:
        return True
      #kral vs kun nebo strelec
      if (len(whitePieces) == 1 and len(blackPieces) == 2):
        for piece in blackPieces:
          if piece.symbol == "K":
            continue
          if piece.symbol == "N" or piece.symbol == "B":
            return True
      if (len(whitePieces) == 2 and len(blackPieces) == 1):
        for piece in whitePieces:
          if piece.symbol == "K":
            continue
          if piece.symbol == "N" or piece.symbol == "B":
            return True
      #strelec vs strelec stejne barvy
      if (len(whitePieces) == 2 and len(blackPieces) == 2):
        whitePieces = [piece for piece in whitePieces if piece.symbol != "K"]
        blackPieces = [piece for piece in blackPieces if piece.symbol != "K"]
        if whitePieces[0].symbol == "B" and blackPieces[0].symbol == "B":
          if abs(whitePieces[0].col - whitePieces[0].row) % 2 == abs(blackPieces[0].col - blackPieces[0].row) % 2:
            return True
      return False

    if self.movesSinceLastImportantMove == 100:
      return "Draw by fifty-move rule"
    for i in range(0,len(self.positionsList)-1):
      count = 0
      for j in range(i+1, len(self.positionsList)):
        if self.positionsList[i].compare(self.positionsList[j]):
          count += 1
      if count >= 3:
        return "Draw by threefold repetition"
    if isInsufficientMaterial():
      return "Draw by insufficient material"
    enemyColor = Colors.WHITE if self.makingMove == Colors.BLACK else Colors.BLACK
    for piece in self.board.pieceList(enemyColor):
      if piece.possibleMoves(self.board) != []:
        return None
    if self.board.isKingInCheck(enemyColor):
      return f"Checkmate {self.makingMove} won"
    else:
      return "Draw by stalemate"
    