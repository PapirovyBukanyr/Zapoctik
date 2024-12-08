from .Chess import Chess
from ..Enums import *
import random

class ChessMines(Chess):
    """
    Hra šachy s minami.
    
    Attributes:
        mines (list of [int, int]): seznam min
        explosion ([int, int]): pozice exploze
    """
    
    
    def __init__(self):
        """
        Inicializace hry.
        """
        super().__init__()
        self.__placeMines()
        self.explosion = None
        
        
    def __placeMines(self):
        """
        Umístí miny na náhodné pozice.
        """
        self.mines = []
        for _ in range(random.randint(8, 24)):
            x = random.randint(2, 5)
            y = random.randint(0, 7)
            
            while [x, y] in self.mines:
                x = random.randint(2, 5)
                y = random.randint(0, 7)
            
            self.mines.append([x, y])
            
    
    def getBoard(self, color=None):
        """
        Vrátí hrací desku.
        """
        board = super().getBoard()
        
        if self.explosion is not None:
            board[self.explosion[0]][self.explosion[1]] = Field(Colors.WHITE, Figures.EXPLOSION)
        
        return board
    
    
    def makeMove(self, move, color=None, rightClick=False):
        """
        Zpracuje tah.
        """
        if rightClick:
            return False
        
        if color == None:
            color = self.__isMoving
            
        makeMove = super().makeMove(move, color)
        
        if makeMove or makeMove == "Promote":
            if move in self.mines:
                self.explosion = move
                self.killPiece(move)
                return makeMove
            else:
                self.explosion = None
                return makeMove
        else:
            return makeMove