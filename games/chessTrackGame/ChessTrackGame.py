from .ChessTrackGameBoard import ChessTrackGameBoard
from ..Enums import *
from ..GameTemplate import GameTemplate

class ChessTrackGame(GameTemplate):
    """
    Hra ChessTrackGame.
    
    Attributes:
        board (ChessTrackGameBoard): Hrací deska
        currentPlayer (Enum Colors): Barva hráče, který je na tahu
    """
    
    
    def __init__(self):
        """
        Inicializace hry.
        """
        super().__init__()
        self.board = ChessTrackGameBoard()
        self.currentPlayer = Colors.WHITE
        
        
    def getBoard(self, color = None):
        """
        Vrácení hrací desky.
        
        Args:
            color (Enum Colors): Barva hráče.
        
        Returns:
            ChessTrackGameBoard: Hrací deska.
        """
        return self.board.getListOfBoard()
        
        
    def makeMove(self, position, color = None, rightClick = False): 
        """
        Provedení tahu.
        
        Args:
            position ([int,int]]): Pozice, na kterou se má kámen umístit.
            color (Enum Colors): Barva kamene.
            rightClick (bool): True, pokud se jedná o pravé tlačítko myši.
            
        Returns:
            bool: True, pokud je tah platný, jinak False.
        """
        if color == None:
            color = self.currentPlayer
            
        else:
            self.currentPlayer = color
            
        if position[0] > 3 or position[1] > 3 or position[0] < 0 or position[1] < 0:
            return False
        
        if self.board[position[0],position[1]] == None:
            self.board.makeMove(position, color)
            self.__printToTerminal()
            return True
        
        return False
    
    
    def checkEnd(self):
        """
        Kontrola konce hry.
        
        Returns:
            String: Který hráč vyhrál, pokud hra skončila, jinak None.
        """
        return self.board.checkEnd()
    
    
    def __printToTerminal(self):
        """
        Vypsání hrací desky do terminálu.
        """        
        for i in range(4):
            for j in range(4):
                if self.board[i,j] == None:
                    print("_", end=" ")
                else:
                    print(self.board[i,j].__str__(), end=" ")
            print()
            
        print()