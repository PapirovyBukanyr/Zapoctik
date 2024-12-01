from ..Board import Board
from ..Enums import *

class ChessTrackGameBoard(Board):
    """Hrací deska hry ChessTrackGame.
    """
    
    
    def __init__(self):
        """Inicializace hrací desky.
        """
        super().__init__()
        self.moves = 0
        self.__populateBoard()
        
        
    def __populateBoard(self):
        """Inicializace hrací desky.
        """
        self.board = [[None for _ in range(4)] for _ in range(4)]
        
        
    def spinBoard(self):
        """Otočení hrací desky.
        """
        board = [[None for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            for j in range(4):
                if self.board[i][j] is not None:
                    board[3 - i][3 - j] = self.board[i][j]