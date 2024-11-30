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
        self.startPosition = [8,3]
        self.finalPosition = [8,4]


    def __str__(self):
        """ Vrací textovou reprezentaci instance třídy BlackPiece.
        
        Returns:
            str: Textová reprezentace instance třídy BlackPiece
        """
        return "B"