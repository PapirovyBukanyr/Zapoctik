from ..Enums import *
from ..Board import Board
import random as rand

class HumanDoNotWorryBoard (Board):
    """ Třída HumanDoNotWorryBoard slouží k reprezentaci hrací desky hry člověče, nezlob se.
    """
    
    def __init__(self):
        """ Konstruktor třídy HumanDoNotWorryBoard.
        """
        self.board = [[None for i in range(8)] for j in range(8)]
        self.__populateBoard()
        
    def __populateBoard(self):
        """ Metoda, která naplní hrací desku figurkami.
        """
        for i in range(11):
            for j in range(11):
                if i == 0 or i == 10 or j == 0 or j == 10:
                    self.board[i][j] = None
                else:
                    self.board[i][j] = rand.choice([Colors.WHITE, Colors.BLACK, None])