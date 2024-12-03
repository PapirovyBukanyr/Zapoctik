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
        
        
    def __spinBoard(self):
        """Otočení hrací desky.
        """
        board = [[None for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            for j in range(4):
                
                if (i in range(1,4) and j == 0) or (i == 2 and j == 1):
                    board[i][j] = self.board[i-1][j]
                    
                elif (i == 3 and j in range(1,4)) or (i == 2 and j == 2):
                    board[i][j] = self.board[i][j-1]
                    
                elif (i in range(0,3) and j == 3) or (i == 1 and j == 2):
                    board[i][j] = self.board[i+1][j]
                    
                elif (i == 0 and j in range(0,3)) or (i == 1 and j == 1):
                    board[i][j] = self.board[i][j+1]
                    
        self.board = board
        
        
    def __placeStone(self, position, color):
        """Umístění kamene na desku.
        
        Args:
            position ([int,int]]): Pozice, na kterou se má kámen umístit.
            color (Enum Colors): Barva kamene.
        """
        if self.board[position[0]][position[1]] == None:
            self.board[position[0]][position[1]] = color
            self.moves += 1
        else:
            raise ValueError("Invalid move.")
        
        
    def makeMove(self, position, color):
        """Provedení tahu.
        
        Args:
            position ([int,int]]): Pozice, na kterou se má kámen umístit.
            color (Enum Colors): Barva kamene.
        """
        self.__placeStone(position, color)
        self.__spinBoard()
        
        
    def getListOfBoard(self):
        """Vrátí seznam seznamů reprezentující hrací desku.
        
        Returns:
            list: Seznam seznamů reprezentující hrací desku.
        """
        board = [[None for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != None:
                    if self.board[i][j] == Colors.WHITE:
                        board[i][j] = Field(Colors.WHITE, Figures.X)
                    else:
                        board[i][j] = Field(Colors.BLACK, Figures.O)
                        
        return board
    
    
    def checkEnd(self):
        """Kontrola konce hry.
        
        Returns:
            str: Výsledek hry.
        """
        if self.moves >= 16:
            return "Draw"
        
        return self.__checkWinner()
    
    
    def __checkWinner(self):
        """Kontrola výherce.
        
        Returns:
            str: Výsledek hry.
        """
        for i in range(4):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] != None:
                return f"{self.board[i][0]} won"
            
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] != None:
                return f"{self.board[0][i]} won"
        
        return None