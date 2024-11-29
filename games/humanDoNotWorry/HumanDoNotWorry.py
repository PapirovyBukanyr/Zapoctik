from .HumanDoNotWorryBoard import HumanDoNotWorryBoard
from ..Enums import *
import random
from .pieces import *

class HumanDoNotWorry:
    """Třída pro hru člověče, nezlob se.
    """
    
    
    def __init__(self):
        """Konstruktor třídy hry člověče, nezlob se.
        """
        self.board = HumanDoNotWorryBoard()
        self.players = []
        self.currentPlayer = Colors.WHITE
        self.selectedPiece = None
        self.rolled = False
      
        
    def __str__(self):
        """Vrátí textovou reprezentaci instance třídy HumanDoNotWorry.
        
        Returns:
            str: Textová reprezentace instance třídy HumanDoNotWorry
        """
        return "Člověče, nezlob se"
          
        
    def getBoard(self, color = None):
        """Metoda vrátí hrací desku.
        
        Returns:
            List of list of field: Hrací deska
        """
        return self.board.getListOfBoard()
    
    
    def choosePiece(self, position, color = None):
        """Metoda zvolí figurku, kterou se bude hrát.
        
        Args:
            position (int): Pozice figurky
        
        Returns:
            bool: True, pokud se podařilo zvolit figurku, jinak False
        """
        if color is None:
            self.currentPlayer = color
        else:
            color = self.currentPlayer
        
        if position[0]>8 or position[1]>8 or position[0]<0 or position[1]<0:
            return []
        
        if not self.rolled:
            self.rollDice()
        else:
            row, col = position
            
            if isinstance(self.board[row, col], Piece):
                if self.board[row, col].color == color:
                    self.selectedPiece = self.board[row, col]

                    return self.selectedPiece.possibleMoves(self.number, self.board)
        
        return []
    
    def makeMove(self, position, color = None):
        """Metoda provede tah figurkou.
        
        Args:
            position ([int,int]): Pozice figurky
        
        Returns:
            bool: True, pokud se podařilo provést tah, jinak False
        """
        if color is not None:
            self.currentPlayer = color
        else:
            color = self.currentPlayer
        
        row, col = position
        if self.selectedPiece is not None and self.selectedPiece.possibleMoves(self.number, self.board).__contains__(position):
            if self.board[row, col] is None:
                self.board[row, col] = self.selectedPiece
                self.board[self.selectedPiece.position[0], self.selectedPiece.position[1]] = None
                self.selectedPiece.position = position
                
            return True
        
        return False
        
    
    def checkEnd(self):
        """Metoda zkontroluje, zda hra skončila.
        
        Returns:
            string: Vrátí barvu hráče, který vyhrál, jinak None
        """
        for color in Colors:
            finished = 0
            
            for i in range(0,9):
                for j in range(0,9):
                    try:
                        if self.board[i, j].color == color and self.board[i, j].inIsHome == True:
                            finished += 1
                            
                    except:
                        pass
            
            if finished == 4:
                return f"{color} won"
            
        return None
    
    def rollDice(self):
        """Metoda hodí kostkou.
        
        Returns:
            int: Hodnota kostky
        """
        self.rolled = True
        self.number = random.randint(1,6)
        
        match(self.number):
                case 1:
                    self.board[4,4] = Figures.ONE
                    
                case 2:
                    self.board[4,4] = Figures.TWO
                    
                case 3:
                    self.board[4,4] = Figures.THREE
                    
                case 4:
                    self.board[4,4] = Figures.FOUR
                    
                case 5:
                    self.board[4,4] = Figures.FIVE
                    
                case 6:
                    self.board[4,4] = Figures.SIX
        