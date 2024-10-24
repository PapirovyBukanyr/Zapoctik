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
    while True:
      try:
        playedPiece = [int(x) for x in input("Zvolte figuru, kterou chcete táhnout: ").split(",")]
      except:
        print("Neplatné pole, zkuste to znovu")
        continue
      if self.board[playedPiece] is not None and self.board[playedPiece].color == self.makingMove and self.board[playedPiece].possibleMoves(self.board) != []:
        print(self.board[playedPiece].possibleMoves(self.board))
        break
      print("Neplatné pole, zkuste to znovu")
    while True:
      playedMove = input("Zvolte, kam chcete táhnout: ")
      try:
        playedMove = [int(x) for x in playedMove.split(",")]
      except:
        print("Neplatné pole, zkuste to znovu")
        continue
      if playedMove in self.board[playedPiece].possibleMoves(self.board):
        if isinstance(self.board[playedPiece],Pawn) or self.board[playedMove] is not None:
          self.movesSinceLastImportantMove = -1
        self.board[playedPiece].move(self.board, playedMove)
        self.movesSinceLastImportantMove += 1
        self.positionsList.append(self.board.copy())
        break
      print("Neplatné pole, zkuste to znovu")
  def changePlayer(self):
    if self.makingMove == Colors.WHITE:
      self.makingMove = Colors.BLACK
    else:
      self.makingMove = Colors.WHITE

  def checkGameOver(self):
    def isInsufficientMaterial():
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
    