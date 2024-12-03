from ..Enums import *
from ..Board import Board
from .pieces import *
import random as rand


class HumanDoNotWorryBoard (Board):
    """ Třída HumanDoNotWorryBoard slouží k reprezentaci hrací desky hry člověče, nezlob se.
    """
    
    
    def __init__(self):
        """ Konstruktor třídy HumanDoNotWorryBoard.
        """
        self.board = [[None for i in range(9)] for j in range(9)]
        self.__populateBoard()
        
        
    def __str__(self):
        """ Vrátí textovou reprezentaci instance třídy HumanDoNotWorryBoard.
        """
        board = ""
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] is None:
                    board += "-"
                    
                elif self.board[i][j] == Figures.SHADOW:
                    board += "X"
                
                elif self.board[i][j] == Figures.FLAG:
                    board += "F"
                
                elif isinstance( self.board[i][j], Figures):
                    board += "-"
                
                else:
                    board +=  self.board[i][j].__str__()
                    
            board += "\n"
            
        return board
        
        
    def isDeployed(self, color):
        """Metoda, která zjistí, zda je alespoň jedna figurka zadané barvy nasazena.

        Args:
            color (Colors): Barva figurky
        """
        for i in range(0,9):
            for j in range(0,9):
                if isinstance(self.board[i][j], Piece) and self.board[i][j].color == color and self.board[i][j].isDeployed:
                    return True
                
        return False
        
        
    def __populateBoard(self):
        """ Metoda, která naplní hrací desku figurkami.
        """
        for i in range(0,2):
            for j in range(0,2):
                self.board[i][j] = WhitePiece([i,j])
                
        for i in range(0,2):
            for j in range(7,9):
                self.board[i][j] = GreenPiece([i,j])
                
        for i in range(7,9):
            for j in range(0,2):
                self.board[i][j] = BlackPiece([i,j])
                
        for i in range(7,9):
            for j in range(7,9):
                self.board[i][j] = RedPiece([i,j])
                
        for i in range(1,8):
            self.board[i][4] = Figures.FLAG
            self.board[4][i] = Figures.FLAG

        self.board[4][4] = Figures.SHADOW
        
        for i in range(0,3):
            self.board[2][i] = Figures.SHADOW
            self.board[i][2] = Figures.SHADOW
            self.board[6][i] = Figures.SHADOW
            self.board[i][6] = Figures.SHADOW
            self.board[2][8-i] = Figures.SHADOW
            self.board[8-i][2] = Figures.SHADOW
            self.board[6][8-i] = Figures.SHADOW
            self.board[8-i][6] = Figures.SHADOW
                

    def getListOfBoard(self):
        """ Metoda, která vrátí seznam seznamů reprezentující hrací desku.
        
        Returns:
            List of List of Field: Seznam seznamů reprezentující hrací desku
        """
        board = [[None for _ in range(9)] for _ in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if self.board[i][j] is None:
                    board[i][j] = None
                    
                elif self.board[i][j] == Figures.SHADOW:
                    board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
                
                elif self.board[i][j] == Figures.FLAG:
                    board[i][j] = Field(Colors.WHITE, Figures.FLAG)
                
                elif isinstance( self.board[i][j], Figures):
                    board[i][j] = Field(Colors.WHITE, self.board[i][j])
                
                elif self.board[i][j].color == Colors.BLACK:
                    board[i][j] = Field(Colors.BLACK, Figures.PAWN)
                
                elif self.board[i][j].color == Colors.RED:
                    board[i][j] = Field(Colors.RED, Figures.PAWN)
                    
                elif self.board[i][j].color == Colors.WHITE:
                    board[i][j] = Field(Colors.WHITE, Figures.PAWN)
                    
                elif self.board[i][j].color == Colors.GREEN:
                    board[i][j] = Field(Colors.GREEN, Figures.PAWN)
                    
        return board
        