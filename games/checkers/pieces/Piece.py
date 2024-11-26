import abc as ABC
from ...Enums import *

class Piece (ABC.ABC):
    def __init__(self, color, position):
        """Konstruktor třídy Piece

        Args:
            color (Enum Colors): požadovaná barva figurky
            position ([int,int]): výchozí pozice figurky
        """
        self.color = color
        self.position = position
        
        
    def possibleMoves(self, board):
        """Metoda pro zjištění možných tahů figurky

        Args:
            board (Board): hrací deska, na které se figurka nachází
        """
        pass
      
      
    def possibleJumps(self, board, position = None):
        """Metoda pro zjištění možných skoků figurky
        
        Args:
            board (Board): hrací deska, na které se figurka nachází
            position ([int, int], optional): pozice, ze které se má skákat. Výchozí hodnota je None, což znamená, že se skáče ze současné pozice figurky
        """
        pass
    
    
    def trackJumps(self, board, endPosition):
        """Metoda pro zjištění možných skoků figurky
        
        Args:
            board (Board): hrací deska, na které se figurka nachází
            endPosition ([int, int]): pozice, kam se má skákat
        """
        pass   
     
    
    @property
    def row (self):
        """Vlastnost pro získání řádku, na kterém se figurka nachází

        Returns:
            int: řádek, na kterém se figurka nachází
        """
        return self.position[0]
    
    
    @property
    def col (self):
        """Vlastnost pro získání sloupce, na kterém se figurka nachází
        
        Returns:
            int: sloupec, na kterém se figurka nachází
        """
        return self.position[1]