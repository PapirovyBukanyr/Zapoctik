from .Board import Board
from .pieces import *

class GameController:
  def __init__(self):
    self.board = None
    self.makingMove = Colors.WHITE
    self.movesSinceLastImportantMove = 0
    self.positionsList = []

  def startGame(self):
    self.board = Board()
    self.board.setupNormalBoard()
    self.positionsList.append(self.board.copy())
    print(self.board)
    while True:
      self.makeMove()
      print(self.board)
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
    print(len(self.positionsList))
    print(self.movesSinceLastImportantMove)
    self.changePlayer()
  def changePlayer(self):
    if self.makingMove == Colors.WHITE:
      self.makingMove = Colors.BLACK
    else:
      self.makingMove = Colors.WHITE

