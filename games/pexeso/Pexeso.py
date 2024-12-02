from .PexesoBoard import *

class Pexeso:
    """ Třída reprezentující hru Pexeso
    """
    
    
    def __init__(self):
        """Inicializace hry Pexeso
        """
        self.__board = PexesoBoard()
        self.__firstMove = True
        self.score = 0
        
        
    def getBoard(self, color):
        """ Vrátí hrací plochu
        
        Args:
            color (Enum Colors): barva hráče
        
        Returns:
            list: hrací plocha
        """
        return self.__board.getListOfBoard(color)
        
        
    def makeMove(self, position, color = Colors.WHITE):
        """ Provede tah
        
        Args:
            position ([int, int]): pozice, kterou chce hráč otočit
            color (Enum Colors): barva na tahu
            
        Returns:
            bool: úspěšnost tahu
        """
        raise NotImplementedError("Metoda není implementována")
    
    
    def checkEnd(self):
        """ Zkontroluje, zda hra skončila
        
        Returns:
            None: pokud hra neskončila
            string: výsledek hry
        """
        return None