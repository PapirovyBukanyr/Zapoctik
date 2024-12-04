from .HumanDoNotWorry import HumanDoNotWorry
from ..Enums import Colors, Figures, Field


class HumanDoNotWorryWithFogOfWar(HumanDoNotWorry):
    """Hra Člověče, nezlob se! s mlhou války
    """
    
    
    def __init__(self):
        """Konstruktor třídy HumanDoNotWorryWithFogOfWar
        """
        super().__init__()
    
    
    def getBoard(self, color=None):
        """Vrací hrací desku
        
        Args:
            color (Enum Colors, optional): Barva hráče na tahu. Defaults to None.

        Returns:
            List[List[Field]]: hrací deska
        """
        board = self.board.getListOfBoard()
        possibleMoves = self.possibleMoves(self.currentPlayer)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].color == color or board[i][j].color in possibleMoves:
                    pass
                else:
                    board[i][j] = Field(color=Colors.WHITE, piece=Figures.SHADOW)
        
        return board