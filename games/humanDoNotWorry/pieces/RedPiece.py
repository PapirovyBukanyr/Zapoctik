from .Piece import *

class RedPiece(Piece):
    """ Třída RedPiece slouží k reprezentaci jedné červené figurky.
    """
    
    
    def __init__(self, position):
        """ Konstruktor třídy RedPiece.
        
        Args:
            position ([int,int]): Pozice figurky
        """
        super().__init__(position)
        self.color = Colors.RED
        self.startPosition = [5,8]
        self.finalPosition = [4,8]
        

    def __str__(self):
        """ Vrací textovou reprezentaci instance třídy RedPiece.
        
        Returns:
            str: Textová reprezentace instance třídy RedPiece
        """
        return "R"