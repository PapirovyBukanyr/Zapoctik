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
            return Field(Figures.SHADOW, Colors.WHITE)
        
    
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
        self.isCompleted = True