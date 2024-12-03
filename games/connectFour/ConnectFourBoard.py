from ..Enums import *
from ..Board import Board

class ConnectFourBoard(Board):
    """ Hrací deska pro hru ConnectFour 
    """
    
    
    def __init__(self):
        """Inicializace hry ConnectFour
        """
        super().__init__()
        self.__populateBoard()
        self.moves = 0
        
        
    def __str__(self):
        """Vytvoří string hrací desky na výpis do konzole
        """
        return "\n".join([" ".join([str(cell) if cell is not None else "-" for cell in row]) for row in self.board])
    
    
    def __populateBoard(self):
        """Inicializace herní desky
        """
        self.board = [[None for _ in range(7)] for _ in range(6)]
    
    
    def findMove(self, position, up = False):
        """Provedení tahu
        
        Args:
            position ([int,int]): Pozice tahu
            up (bool, optional): Směr zjišťování umístění. Defaults to False, tedy dolů.
            
        Returns:
            [int,int]: Pozice, kam se má umístit kámen            
        """
        if up:
            for i in range(6):
                if self.board[i][position[0]] is None:
                    return [position[0], i]
        else:
            for i in range(5, -1, -1):
                if self.board[i][position[0]] is None:
                    return [position[0], i]
        return []
        
        
    def makeMove(self, position, color):
        """Provedení tahu
        
        Args:
            position ([int,int]): Pozice tahu
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud se tah podařil, jinak False
        """
        move = self.findMove(position)
        if move != []:
            self.board[move[1]][move[0]] = color
            self.moves += 1
            return True
        return False
    
    
    def isFull(self):
        """Zjistí, zda je herní deska plná
        
        Returns:
            bool: True, pokud je deska plná, jinak False
        """
        return self.moves == 42
    
    
    def checkEnd(self):
        """Zjistí, zda je konec hry
        
        Args:
            position ([int,int]): Pozice tahu
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud je konec hry, jinak False
        """
        if self.isFull():
            return "Draw"
        
        for color in [Colors.WHITE, Colors.BLACK]:
            if self.checkWin(color):
                return f"{color} won"
        
        return None
    
    
    def checkWin(self, color):
        """Zjistí, zda hráč vyhrál
        
        Args:
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud hráč vyhrál, jinak False
        """
        return self.checkHorizontal(color) or self.checkVertical(color) or self.checkDiagonal(color)
    
    
    def checkHorizontal(self, color):
        """Zjistí, zda hráč vyhrál horizontálně
        
        Args:
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud hráč vyhrál horizontálně, jinak False
        """
        for row in self.board:
            for i in range(4):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == color:
                    return True
        return False
    
    
    def checkVertical(self, color):
        """Zjistí, zda hráč vyhrál vertikálně
        
        Args:
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud hráč vyhrál vertikálně, jinak False
        """
        for i in range(7):
            for j in range(3):
                if self.board[j][i] == self.board[j + 1][i] == self.board[j + 2][i] == self.board[j + 3][i] == color:
                    return True
        return False
    
    
    def checkDiagonal(self, color):
        """Zjistí, zda hráč vyhrál diagonálně
        
        Args:
            color (Enum): Barva hráče
            
        Returns:
            bool: True, pokud hráč vyhrál diagonálně, jinak False
        """
        for i in range(4):
            for j in range(3):
                if self.board[j][i] == self.board[j + 1][i + 1] == self.board[j + 2][i + 2] == self.board[j + 3][i + 3] == color:
                    return True
        for i in range(3, 7):
            for j in range(3):
                if self.board[j][i] == self.board[j + 1][i - 1] == self.board[j + 2][i - 2] == self.board[j + 3][i - 3] == color:
                    return True
        return False
    
    
    def getListOfBoard(self):
        """Vrací šachovnici jako list
        
        Returns:
            List of Struct : List, kde každý řádek je list obsahující figury na daném řádku
        """
        board = [[None for _ in range(7)] for _ in range(6)]
        for i in range(6):
            for j in range(7):
                if self.board[i][j] is not None:
                    if self.board[i][j] == Colors.WHITE:
                        board[i][j] = Field(Colors.WHITE, Figures.X)
                    else:
                        board[i][j] = Field(Colors.BLACK, Figures.O)
        return board
    
    
        
    
    