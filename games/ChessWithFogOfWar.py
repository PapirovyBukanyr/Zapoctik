from .chess import Chess
from .Enums import *

class ChessWithFogOfWar(Chess):
    """Třída ChessWithFogOfWar slouží k reprezentaci hry Šachy s mlhou války.
    """
    
    
    def __init__(self):
        """Konstruktor třídy ChessWithFogOfWar
        """
        super().__init__()
        self.fog = True
    
    
    def getBoard(self, color):
        """Vrací zakrytou šachovnici
        
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
                    if board[i][j] == None or board[i][j].color != color:
                        board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        return board
        