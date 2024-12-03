from .MinesBoard import *
import random

class Mines:
    """Třída reprezentující hru Miny
    """
    
    
    def __init__(self):
        """Inicializace hry Miny
        """
        self.__numberOfMines = random.randint(15,20)
        self.__board = MinesBoard(self.__numberOfMines)
        self.__firstMove = True
        self.score = 0
        
    
    def makeMove(self, position, color = Colors.WHITE, rightClick = False):
        """Provede tah hráče
        
        Args:
            position ([int, int]): pozice, kam se má hráč pohnout
            color (Enum Colors): barva na tahu
            rightClick (bool): True, pokud hráč klikl pravým tlačítkem myši, jinak False
            
        Returns:
            bool: úspěšnost tahu
        """
        if rightClick:
            return self.placeFlag(position, color)
        
        return self.makeUncoverMove(position, color)
        
    
    def makeUncoverMove(self, position, color = Colors.WHITE):
        """Provede tah 
        
        Args:
            position ([int, int]): pozice, kam se má hráč pohnout
            color (Enum Colors): barva na tahu
            
        Returns:
            bool: úspěšnost tahu
        """
        if position[0] < 0 or position[0] > 7 or position[1] < 0 or position[1] > 15:
            return False
        
        self.__color = color
        
        if self.__firstMove:
            row, col = position
        
            while self.__board[row, col] != None or self.__board.countMinesAroundSymbol(row, col) != 0:
                self.__board = MinesBoard(self.__numberOfMines)
            self.__firstMove = False
        
        result = self.__board.makeMove(position[0], position[1])
        self.__printToTerminal()
        
        return result
        
    
    def checkEnd(self):
        """Zkontroluje, zda hra skončila
        
        Returns:
            None: pokud hra neskončila
            string: výsledek hry
        """
        if self.__board.kaboom:
            return f"{self.__color.changeColor()} won"
        
        if self.__board.minesRemaining() == 0 and self.__board.flagsPlanted() == self.__numberOfMines:
            if self.score > 0:
                return f"{Colors.WHITE} won"
        
            elif self.score < 0:
                return f"{Colors.BLACK} won"
        
            else:
                return "Draw"
        
        else:
            return None
        
        
    def placeFlag(self, position, color = Colors.WHITE):
        """Umístí vlajku na danou pozici
        
        Args:
            position ([int, int]): pozice, kam se má vlajka umístit
            color (Enum Colors): barva na tahu
            
        Returns:
            bool: úspěšnost umístění vlajky
        """
        success = self.__board.placeFlag(position[0], position[1])
        if success == 2:
            return False
        
        if color == Colors.WHITE:
            self.score += success
        
        else:   
            self.score -= success
                
        self.__printToTerminal()
        
        return True
    
        
    def getBoard(self, color=None):
        """Vrátí herní desku
        
        Args:
            color (Enum Colors, optional): Barva, která je na tahu. Výchozí je None.
        
        Returns:
            list: herní deska
        """
        board = [[None for x in range(16)] for y in range(8)]
        
        if self.checkEnd() == None or self.__board.kaboom == False:
            for i in range(8):
                for j in range(16):
                    match(self.__board[i, j]):
        
                        case "M":
                            board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        
                        case "F":
                            board[i][j] = Field(Colors.WHITE, Figures.FLAG)
        
                        case "FM":
                            board[i][j] = Field(Colors.WHITE, Figures.FLAG)
        
                        case "S":
                            board[i][j] = None
        
                        case 1:
                            board[i][j] = Field(Colors.WHITE, Figures.ONE)
        
                        case 2:
                            board[i][j] = Field(Colors.WHITE, Figures.TWO)
        
                        case 3:
                            board[i][j] = Field(Colors.WHITE, Figures.THREE)
        
                        case 4:
                            board[i][j] = Field(Colors.WHITE, Figures.FOUR)
        
                        case 5:
                            board[i][j] = Field(Colors.WHITE, Figures.FIVE)
        
                        case 6:
                            board[i][j] = Field(Colors.WHITE, Figures.SIX)
        
                        case 7:
                            board[i][j] = Field(Colors.WHITE, Figures.SEVEN)
        
                        case 8:
                            board[i][j] = Field(Colors.WHITE, Figures.EIGHT)
        
                        case None:
                            board[i][j] = Field(Colors.WHITE, Figures.SHADOW)
        else:
            for i in range(8):
                for j in range(16):
        
                    if self.__board.countMinesAroundSymbol(i, j) != 0 and self.__board[i, j] == None:
                        self.__board[i,j] = self.__board.countMinesAroundSymbol(i, j)
        
                    if self.__board[i, j] == "FM":
                        self.__board[i, j] = "M"    
        
                    match(self.__board[i, j]):
                        case "M":
                            board[i][j] = Field(Colors.WHITE, Figures.MINE)
        
                        case "F":
                            board[i][j] = Field(Colors.WHITE, Figures.FLAG)
        
                        case "S":
                            board[i][j] = None
        
                        case "K":
                            board[i][j] = Field(Colors.WHITE, Figures.EXPLOSION)
        
                        case 1:
                            board[i][j] = Field(Colors.WHITE, Figures.ONE)
        
                        case 2:
                            board[i][j] = Field(Colors.WHITE, Figures.TWO)
        
                        case 3:
                            board[i][j] = Field(Colors.WHITE, Figures.THREE)
        
                        case 4:
                            board[i][j] = Field(Colors.WHITE, Figures.FOUR)
        
                        case 5:
                            board[i][j] = Field(Colors.WHITE, Figures.FIVE)
        
                        case 6:
                            board[i][j] = Field(Colors.WHITE, Figures.SIX)
        
                        case 7:
                            board[i][j] = Field(Colors.WHITE, Figures.SEVEN)
        
                        case 8:
                            board[i][j] = Field(Colors.WHITE, Figures.EIGHT)
        
                        case None:
                            board[i][j] = None
                            
        return board
    
    def __printToTerminal(self):
        """Vypíše herní desku do konzole
        """
        for i in range(8):
            for j in range(16):
        
                if self.__board[i, j] == None:
                    print("N", end = " ")
        
                else:
                    print(self.__board[i, j], end = " ")
        
            print()
        print()
                     
                
        