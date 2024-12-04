from .ChessMines import ChessMines
from ..Enums import *

class ChessMinesWithFogOfWar(ChessMines):
    """Hra šachy s minami a mlhou války.
    """
    
    
    def getBoard(self, color=None):
        """Vrátí hrací desku.
        """
        if color is None:
            color = self.__isMoving
            
        board = super().getBoard(color)
        
        for i in range(8):
            for j in range(8):
                if board[i][j] is None or (board[i][j].color != color or board[i][j].piece != Figures.EXPLOSION and [i,j] not in self.possibleMoves(color)):
                    board[i][j] = Field(color, Figures.SHADOW)
        
        return board