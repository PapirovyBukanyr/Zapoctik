from .ChessMines import ChessMines
from ..Enums import *

class ChessMinesWithFogOfWar(ChessMines):
    """Hra šachy s minami a mlhou války.
    """
    
    
    def __init__(self):
        """Konstruktor třídy ChessMinesWithFogOfWar
        """
        super().__init__()
        self.fog = True
    
    
    def getBoard(self, color=None):
        """Vrátí hrací desku.
        """
        if color is None:
            color = self.__isMoving
            
        board = super().getBoard(color)
        possibleMoves = self.possibleMoves(color)
        
        for i in range(8):
            for j in range(8):
                if self.explosion == [i, j]:
                    board[i][j] = Field(Colors.WHITE, Figures.EXPLOSION)
                    
                if not possibleMoves.__contains__([i, j]):
                    if board[i][j] == None or board[i][j].color != color:
                        board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        
        return board