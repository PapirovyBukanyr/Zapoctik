from .Enums import *
import abc

class GameTemplate(abc.ABC):
    """Třída GameTemplate slouží k reprezentaci šablony hry.
    """
    
    
    def __init__(self):
        """Konstruktor třídy GameTemplate
        """
        self.fog = False
        self.withChoosePiece = False
        self.numberOfPlayers = 2
    
