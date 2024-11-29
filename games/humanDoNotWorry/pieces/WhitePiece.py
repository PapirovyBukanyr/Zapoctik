from .Piece import *

class WhitePiece(Piece):
    """ Třída WhitePiece slouží k reprezentaci jedné bílé figurky.
    """
    
    
    def __init__(self, position):
        """ Konstruktor třídy WhitePiece.
        
        Args:
            position ([int,int]): Pozice figurky
        """
        super().__init__(position)
        self.color = Colors.WHITE
        self.startPosition = [3,0]
        self.finalPosition = [4,0]


    def __str__(self):
        """ Vrací textovou reprezentaci instance třídy WhitePiece.
        
        Returns:
            str: Textová reprezentace instance třídy WhitePiece
        """
        return "WP"