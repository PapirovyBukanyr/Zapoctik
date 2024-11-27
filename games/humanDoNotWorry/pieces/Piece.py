from ...Enums import *

class Piece:
    """ Třída Piece slouží k reprezentaci jedné herní figurky.
    """
    
    def __init__(self, position):
        """ Konstruktor třídy Piece.
        
        Args:
            color (Colors): Barva figurky
            position ([int,int]): Pozice figurky
        """
        self.color = None
        self.position = position
        self.isDeployed = False
        self.isInHome = False            
            