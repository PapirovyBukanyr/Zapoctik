from abc import ABC
from .Enums import *

class Board(ABC):
    """Třída reprezentující hrací desku hry
    """
    
    
    def __init__(self):
        """Konstruktor třídy Board
        """
        self.board = []
        self.__populateBoard()
        
        
    def __populateBoard(self):
        """Inicializace herní desky
        """
        pass
    
    
    def __str__(self):
        """Vytvoří string hrací desky na výpis do konzole
        """
        pass
    
    
    def getListOfBoard(self):
        """Vrací šachovnici jako list
        
        Returns:
            List of Struct : List, kde každý řádek je list obsahující figury na daném řádku
        """
        return self.board
    
    
    def __getitem__(self, index):
      """Pro možnost přstupovat k poli board jako board[row,col] místo board.board[row][col]
      
      Args:
          index: Tuple dvou integerů, (row, col)
          
      Returns:
          Figuru na určeném místě na šachovnici, případně None, pokud je prázdné
      """
      row, col = index
      return self.board[row][col]
  
  
    def __setitem__(self, index, value):
      """Nastaví políčko na šachovnici jako board[row,col] namísto board.board[row][col] 

      Args:
          index ([int, int]): Tuple dvou integerů, (row, col)
          value (any): Co se má nastavit na dané políčko
      """
      row, col = index
      self.board[row][col] = value
      