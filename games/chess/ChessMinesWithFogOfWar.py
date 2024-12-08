from .ChessMines import ChessMines
from ..Enums import *

class ChessMinesWithFogOfWar(ChessMines):
    """
    Hra šachy s minami a mlhou války.
    
    Attributes:
        fog (bool): True, pokud je mlha války zapnutá, jinak False
    """
    
    
    def __init__(self):
        """
        Konstruktor třídy ChessMinesWithFogOfWar
        """
        super().__init__()
        self.fog = True
    
    
    def getBoard(self, color=None):
        """
        Vrátí hrací desku.
        
        Args:
            color (Enum Colors): Barva hráče, pro kterého se má šachovnice vykreslit
        """
        if color is None:
            color = self.__isMoving
            
        board = super().getBoard(color)
        
        for i in range(8):
            for j in range(8):
                if board[i][j] is None or (board[i][j].color != color or board[i][j].piece != Figures.EXPLOSION and [i,j] not in self.possibleMoves(color)):
                    board[i][j] = Field(color, Figures.SHADOW)
        
        return board