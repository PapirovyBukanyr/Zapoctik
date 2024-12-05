from .Checkers import Checkers
from ..Enums import *
import random

class CheckersMines(Checkers):
    """Hra dáma s minami.
    """
    
    
    def __init__(self):
        """Inicializace hry.
        """
        super().__init__()
        self.__placeMines()
        self.explosion = None
        
        
    def __placeMines(self):
        """Umístí miny na náhodné pozice.
        """
        self.mines = []
        for _ in range(12):
            x = random.randint(3, 4)
            y = random.randint(0, 7)
            
            while [x, y] in self.mines:
                x = random.randint(3, 4)
                y = random.randint(0, 7)
            
            self.mines.append([x, y])
            
    
    def getBoard(self, color=None):
        """Vrátí hrací desku.
        """
        board = super().getBoard()
        
        if self.explosion is not None:
            board[self.explosion[0]][self.explosion[1]] = Field(Colors.WHITE, Figures.EXPLOSION)
        
        return board
    
    
    def makeMove(self, move, color=None, rightClick=False):
        """Zpracuje tah.
        """
        if rightClick:
            return False
        
        if color == None:
            color = self.__isMoving
            
        makeMove = super().makeMove(move, color)
            
        if makeMove == True or isinstance(makeMove, list):
            if move in self.mines:
                self.explosion = move
                self.killPiece(move)
                return makeMove
            
            else:
                self.explosion = None
                return makeMove
            
        else:
            return makeMove