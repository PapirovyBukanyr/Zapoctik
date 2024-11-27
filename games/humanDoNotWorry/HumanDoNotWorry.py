from .HumanDoNotWorryBoard import HumanDoNotWorryBoard
from ..Enums import Colors

class HumanDoNotWorry:
    """Třída pro hru člověče, nezlob se.
    """
    
    def __init__(self)
        """Konstruktor třídy hry člověče, nezlob se.
        """
        self.board = HumanDoNotWorryBoard()
        self.players = []
        self.currentPlayer = Colors.WHITE