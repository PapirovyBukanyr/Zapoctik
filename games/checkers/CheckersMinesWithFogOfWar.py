from .CheckersMines import CheckersMines
from ..Enums import *

class CheckersMinesWithFogOfWar(CheckersMines):
    """
    Třída CheckersWithFogOfWar slouží k reprezentaci hry Dáma s mlhou války.
    
    Attributes:
        mines (List of [int, int]): seznam pozic min
        explosion ([int, int]): pozice exploze
        withChoosePiece (bool): True, pokud je v hře možné vybrat figurku, jinak False
        numberOfPlayers (int): počet hráčů
        fog (bool): True, pokud je ve hře Fog Of War, jinak False
    """
    
    
    def __init__(self):
        """
        Konstruktor třídy CheckersWithFogOfWar
        """
        super().__init__()
        self.fog = True
    
    
    def getBoard(self, color):
        """
        Vrací zakrytou šachovnici
        
        Args:
            color (Enum Colors): Barva hráče na tahu

        Returns:
            Array of Field: zakrytá šachovnice
        """
        board = super().getBoard()
        possibleMoves = self.possibleMoves(color)
    
        for i in range(len(board)):
            for j in range(len(board)):
                if not possibleMoves.__contains__([i, j]):
                    if board[i][j] == None or (board[i][j].color != color and board[i][j].piece != Figures.EXPLOSION):
                        board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
    
        return board
    