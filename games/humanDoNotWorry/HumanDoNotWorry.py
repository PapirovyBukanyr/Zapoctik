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
        self.passTurn = False
      
        
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
        if color is not None:
            self.currentPlayer = color
            
        else:
            color = self.currentPlayer
        
        if position[0]>8 or position[1]>8 or position[0]<0 or position[1]<0:
            return []
        
        if not self.rolled:
            self.passTurn = False
            self.rollDice()
            
        else:
            if not self.board.isDeployed(color) and self.number != 6:
                self.passTurn = True
                self.rolled = False
                self.board[4,4] = Figures.SHADOW
                return [4,4]
                
            row, col = position
            
            if isinstance(self.board[row, col], Piece):
                if self.board[row, col].color == color:
                    self.selectedPiece = self.board[row, col]

                    move = self.selectedPiece.possibleMoves(self.number, self.board)
                    
                    if move == []:
                        return []
                    
                    if move[0]>8 or move[1]>8 or move[0]<0 or move[1]<0:
                        move = []
                    
                    if isinstance(self.board[move[0], move[1]], Piece) and self.board[move[0], move[1]].color == color:
                        move = []
                        
                    return move
        
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
        
        if self.passTurn:
            self.passTurn = False
            self.rolled = False
            self.board[4,4] = Figures.SHADOW
            return True
        
        if self.selectedPiece is not None and self.selectedPiece.possibleMoves(self.number, self.board) == position:
            if self.board[row, col] is None or self.board[row, col] == Figures.FLAG:
                pass
            
            elif self.board[row, col].color != color:
                self.board[row, col].returnHome(self.board)
                
            elif self.board[row, col].color == color:
                return False
                
            if self.selectedPiece.isDeployed == False and self.number == 6:
                self.selectedPiece.isDeployed = True
                
            if self.selectedPiece.finalPosition == position:
                self.selectedPiece.isInFinal = True
                self.__placeToFinal()
                return True
                
            self.__makeStandartMove(row, col)
            
            return True
        
        return False
    
    
    def __makeStandartMove(self, row, col):
        """Metoda provede standardní tah figurkou.

        Args:
            row (int): řádek
            col (int): sloupec
        """
        self.board[row, col] = self.selectedPiece
        self.board[self.selectedPiece.position[0], self.selectedPiece.position[1]] = None
        self.selectedPiece.position = [row, col]
        self.selectedPiece = None
        self.rolled = False
        self.board[4,4] = Figures.SHADOW
        
        self.__printToTerminal()
        
        
    def __placeToFinal(self):
        """Metoda umístí figurku do cíle.
        
        Args:
            board (Board): Hrací deska
            piece (Piece): Figurka
        """
        finalPosition = [4,4]
        
        while self.board[finalPosition[0], finalPosition[1]] is not None and self.board[finalPosition[0], finalPosition[1]] != Figures.FLAG:
            finalPosition[0]+=int((self.selectedPiece.finalPosition[0]-4)/4)
            finalPosition[1]+=int((self.selectedPiece.finalPosition[1]-4)/4)
            
        self.board[finalPosition[0], finalPosition[1]] = self.selectedPiece
        self.board[self.selectedPiece.position[0], self.selectedPiece.position[1]] = None
        self.selectedPiece.position = finalPosition
        self.selectedPiece.isDeployed = False
        self.selectedPiece = None
        self.rolled = False
        self.board[4,4] = Figures.SHADOW
        
        self.__printToTerminal()
        
    
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
                        if self.board[i, j].color == color and self.board[i, j].isInFinal == True:
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
                    
                    
    def __printToTerminal(self):
        """Metoda vytiskne hrací desku na obrazovku.
        """
        print(self.board)
        