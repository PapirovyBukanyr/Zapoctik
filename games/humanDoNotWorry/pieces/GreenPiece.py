from .Piece import *

class GreenPiece(Piece):
    """ Třída GreenPiece slouží k reprezentaci jedné zelené figurky.
    """
    
    
    def __init__(self, position):
        """ Konstruktor třídy GreenPiece.
        
        Args:
            position ([int,int]): Pozice figurky
        """
        super().__init__(position)
        self.color = Colors.GREEN


    def __str__(self):
        """ Vrací textovou reprezentaci instance třídy GreenPiece.
        
        Returns:
            str: Textová reprezentace instance třídy GreenPiece
        """
        return "GP"