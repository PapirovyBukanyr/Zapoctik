from .PexesoBoard import *
from ..GameTemplate import GameTemplate

class Pexeso (GameTemplate):
    """ Třída reprezentující hru Pexeso
    """
    
    
    def __init__(self):
        """Inicializace hry Pexeso
        """
        super().__init__()
        self.__board = PexesoBoard()
        self.__firstMove = True
        self.score = 0
        self.__viewMode = False
        self.__found = False
        
        
    def getBoard(self, color):
        """ Vrátí hrací plochu
        
        Args:
            color (Enum Colors): barva hráče
        
        Returns:
            list: hrací plocha
        """
        return self.__board.getListOfBoard(color)
        
        
    def makeMove(self, position, color = Colors.WHITE, rightClick = False):
        """ Provede tah
        
        Args:
            position ([int, int]): pozice, kterou chce hráč otočit
            color (Enum Colors): barva na tahu
            rightClick (bool): True, pokud hráč klikl pravým tlačítkem myši, jinak False
            
        Returns:
            bool: úspěšnost tahu
        """
        if rightClick:
            return False
        
        if self.__viewMode:
            self.__viewMode = False
            self.__board.hideCards()
            return not self.__found
        
        if position[0] < 0 or position[0] >= len(self.__board.board) or position[1] < 0 or position[1] >= len(self.__board.board[0]):
            return False
        
        if self.__firstMove:
            self.__found = False
            if self.__board.isCompleted(position):
                return False
            
            self.__firstMove = False
            self.__board.makeMove(position)
            return False
        
        if self.__board.isRevealed(position) or self.__board.isCompleted(position):
            return False
        
        self.__firstMove = True
        
        if self.__board.makeMove(position):
            self.__found = True
            self.score += 1 if color == Colors.WHITE else -1
            return True
        
        else:
            self.__viewMode = True
            return False        
    
    
    def checkEnd(self):
        """ Zkontroluje, zda hra skončila
        
        Returns:
            None: pokud hra neskončila
            string: výsledek hry
        """
        for i in range(len(self.__board.board)):
            for j in range(len(self.__board.board[0])):
                if not self.__board.isCompleted([i, j]):
                    return None
        
        if self.score > 0:
            return f"{Colors.WHITE} won"
        elif self.score < 0:
            return f"{Colors.BLACK} won"
        else:
            return "Draw"
    
    def __printToTerminal(self):
        """ Funkce pro vypsání hrací plochy do terminálu
        """
        print(self.__board.__str__())