from .Piece import *

class BlackPiece(Piece):
    """ Třída BlackPiece slouží k reprezentaci jedné černé figurky.
    """
    
    
    def __init__(self, position):
        """ Konstruktor třídy BlackPiece.
        
        Args:
            position ([int,int]): Pozice figurky
        """
        super().__init__(position)
        self.color = Colors.BLACK


    def __str__(self):
        """ Vrací textovou reprezentaci instance třídy BlackPiece.
        
        Returns:
            str: Textová reprezentace instance třídy BlackPiece
        """
        return "BP"