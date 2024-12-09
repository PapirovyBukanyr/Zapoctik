from .HumanDoNotWorry import HumanDoNotWorry
from ..Enums import *


class HumanDoNotWorryWithFogOfWar (HumanDoNotWorry):
    """Hra Člověče, nezlob se! s mlhou války
    """
    
    
    def __init__(self):
        """Konstruktor třídy HumanDoNotWorryWithFogOfWar
        """
        super().__init__()
        self.fog = True
    
    
    def getBoard(self, color):
        """Vrací hrací desku
        
        Args:
            color (Enum Colors, optional): Barva hráče na tahu. Defaults to None.

        Returns:
            List[List[Field]]: hrací deska
        """
        board = super().getBoard()
        possibleMoves = self.possibleMoves(color)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if not possibleMoves.__contains__([i, j]):
                    if (board[i][j] == None or board[i][j].color != color or board[i][j].piece == Figures.FLAG) and not (board[i][j] is not None and (board[i][j].piece == Figures.ONE or board[i][j].piece == Figures.TWO or board[i][j].piece == Figures.THREE or board[i][j].piece == Figures.FOUR or board[i][j].piece == Figures.FIVE or board[i][j].piece == Figures.SIX)):
                        board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        
        return board