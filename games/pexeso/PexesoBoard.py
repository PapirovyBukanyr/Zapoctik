from ..Enums import *
from ..Board import Board
from .PexesoCard import PexesoCard
import random

class PexesoBoard(Board):
    """Reprezentace hrací desky hry Pexeso
    """
    
    
    def __init__(self):
        """Inicializace hrací desky
        """
        super().__init__()
        self.chosenCard = None
        self.__populateBoard()
        
        
    def __populateBoard(self):
        """Vygeneruje náhodné kartičky na hrací desku
        """
        self.board = [
            [PexesoCard(Field(piece=Figures.PAWN, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.RED)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.RED))],
            [PexesoCard(Field(piece=Figures.PAWN, color=Colors.GREEN)), PexesoCard(Field(piece=Figures.PAWN, color=Colors.GREEN)), PexesoCard(Field(piece=Figures.QUEEN, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.QUEEN, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.QUEEN, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.QUEEN, color=Colors.BLACK))],
            [PexesoCard(Field(piece=Figures.KING, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.KING, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.KING, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.KING, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.BISHOP, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.BISHOP, color=Colors.WHITE))],
            [PexesoCard(Field(piece=Figures.ROOK, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.ROOK, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.ROOK, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.ROOK, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.BISHOP, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.BISHOP, color=Colors.BLACK))],
            [PexesoCard(Field(piece=Figures.KNIGHT, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.KNIGHT, color=Colors.WHITE)), PexesoCard(Field(piece=Figures.KNIGHT, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.KNIGHT, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.ONE, color=Colors.RED)), PexesoCard(Field(piece=Figures.ONE, color=Colors.RED))],     
            [PexesoCard(Field(piece=Figures.TWO, color=Colors.GREEN)), PexesoCard(Field(piece=Figures.TWO, color=Colors.GREEN)), PexesoCard(Field(piece=Figures.THREE, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.THREE, color=Colors.BLACK)), PexesoCard(Field(piece=Figures.FOUR, color=Colors.RED)), PexesoCard(Field(piece=Figures.FOUR, color=Colors.RED))]
        ]
        self.shuffleBoard()
        
        
    def shuffleBoard(self):
        """Zamíchá kartičky na hrací desce
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                row = random.randint(0, len(self.board) - 1)
                col = random.randint(0, len(self.board[0]) - 1)
                self.board[i][j], self.board[row][col] = self.board[row][col], self.board[i][j] 
        
        
    def hideCards(self):
        """Schovej všechny kartičky
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j].isCompleted:
                    self.board[i][j].hide()
    
    
    def __str__(self):
        """Vrátí textovou reprezentaci hrací desky
        """
        board = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                board += str(self.board[i][j].getSymbol().piece) + " "
            board += "\n"
        return board
    
    
    def makeMove(self, position):
        """Provede tah
        """
        if self.chosenCard is None:
            self.chosenCard = self.board[position[0]][position[1]]
            self.chosenCard.reveal()
            return None
        
        self.board[position[0]][position[1]].reveal()
        
        if self.chosenCard.equals(self.board[position[0]][position[1]]):
            self.chosenCard.match()
            self.board[position[0]][position[1]].match()
            self.chosenCard = None
            return True
        
        else:
            self.chosenCard = None
            return False
        
        
    def isRevealed(self, position):
        """Vrátí, zda je kartička na dané pozici odhalena
        
        Args:
            position ([int, int]): pozice kartičky
            
        Returns:
            bool: zda je kartička odhalena
        """
        row, col = position
        return self.board[row][col].isRevealed
    
    
    def isCompleted(self, position):
        """Vrátí, zda je kartička na dané pozici uhodnuta
        
        Args:
            position ([int, int]): pozice kartičky
            
        Returns:
            bool: zda je kartička uhodnuta
        """
        row, col = position
        return self.board[row][col].isCompleted
    
    
    def getListOfBoard(self, color):
        """Vrátí hrací plochu
        """
        return [[self.board[i][j].getSymbol() for j in range(len(self.board[0]))] for i in range(len(self.board))]