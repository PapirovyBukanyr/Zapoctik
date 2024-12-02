from ..Enums import *

class PexesoCard:
    """ Reprezentace jedné kartičky hry Pexeso
    """
    
    
    def __init__(self, symbol, odhalena = False):
        """Inicializace kartičky
        
        Args:
            symbol (Field): symbol kartičky
            odhalena (bool): zda je kartička odhalena
        """
        self.symbol = symbol
        self.isRevealed = odhalena
        self.isCompleted = False
        
    
    def getSymbol(self):
        """Vrátí symbol kartičky
        
        Returns:
            Field: symbol kartičky
        """
        if self.isRevealed:
            return self.symbol
        else:
            return Field(Colors.WHITE, Figures.SHADOW)
        
        
    def equals(self, other):
        """Porovná symboly dvou kartiček
        
        Args:
            other (PexesoCard): druhá kartička
        
        Returns:
            bool: zda jsou symboly stejné
        """
        if isinstance(other, PexesoCard):
            return self.getSymbol().color == other.getSymbol().color and self.getSymbol().piece == other.getSymbol().piece
        return False
        
    
    def turn(self):
        """Otočí kartičku
        """
        self.isRevealed = not self.isRevealed
        
        
    def hide(self):
        """Schovej kartičku
        """
        self.isRevealed = False
        
        
    def reveal(self):
        """Odhal kartičku
        """
        self.isRevealed = True    
        
        
    def match(self):
        """Označ kartičku jako vyřešenou
        """
        self.isRevealed = True
        self.isCompleted = True