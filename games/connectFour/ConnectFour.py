from .ConnectFourBoard import *

class ConnectFour:
    """ Hrací deska pro hru ConnectFour 
    """
    
    
    def __init__(self):
        """Inicializace hry ConnectFour
        """
        self.board = ConnectFourBoard()
        self.player = Colors.WHITE
    
        
    def getBoard(self, color = None):
        """Vrací hrací desku
        
        Args:
            color (Enum, optional): Barva hráče. Defaults to None.
        
        Returns:
            List of Struct: Hrací deska
        """
        return self.board.getListOfBoard()
    
    
    def makeMove(self, position, color = None, rightClick = False):
        """Provedení tahu
        
        Args:
            position ([int,int]): Pozice tahu
            color (Enum, optional): Barva hráče. Defaults to None.
            rightClick (bool, optional): True, pokud se jedná o pravé tlačítko myši. Defaults to False.
        
        Returns:
            bool: True, pokud se tah podařil, jinak False
        """
        if rightClick:
            return False
        
        position = [position[1], position[0]]
        
        if position[0] < 0 or position[0] > 6 or position[1] < 0 or position[1] > 5:
            return False
        
        if color is None:
            color = self.player
        
        else:
            self.player = color
            
        move = self.board.findMove(position)
        
        if move == []:
            return False
        
        success = self.board.makeMove(move, color)
        self.__printToTerminal()
        return success
    
    
    def checkEnd(self):
        """Zjištění konce hry
        
        Returns:
            Enum: Barva vítěze
        """
        return self.board.checkEnd()
    
    
    def __printToTerminal(self):
        """Výpis hrací desky do konzole
        """
        print()
        print(self.board)
        print()
    
    
                
        
        