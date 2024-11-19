from .checkers import Checkers
from .Enums import *

class CheckersWithFogOfWar(Checkers):
    def __str__(self):
        """Vrací název hry
        """
        return "Dáma s mlhou války"
    
    def getBoard(self, color):
        """Vrací zakrytou šachovnici

        Returns:
            Array of Field: zakrytá šachovnice
        """
        board = super().getBoard()
        possibleMoves = self.possibleMoves(color)
        for i in range(len(board)):
            for j in range(len(board)):
                if not possibleMoves.__contains__([i, j]):
                    if board[i][j] == None or board[i][j].color != color:
                        board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        return board