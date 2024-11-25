from .MathGameBoard import *

class MathGame:
    """Třída reprezentující hru MathGame
    """
    
    
    def __init__(self):
        """Konstruktor třídy matematické hry. Vytvoří novou hru a nastaví počáteční hodnoty.
        """
        self.__score = 0
        self.__board = MathGameBoard()
        self.__onTurn = Colors.WHITE
        self.__firstTime = False
        
        
    def __str__(self):
        """Vrátí název hry

        Returns:
            String: název hry
        """
        return "Matematická hra"
        
        
    def getBoard(self, color=None):
        """Vrátí šachovnici ve formě dvourozměrného pole objektů Field
        
        Returns:
            list: dvourozměrné pole objektů Field
        """
        return self.__board.getListOfBoard()
    
    
    def choosePiece(self, position, color = None):
        """Vrátí možné tahy pro danou pozici

        Args:
            position ([int,int]): pozice figury
            color (Enum Colors, optional): Barva figury. Defaults to None.

        Returns:
            List of List of int: List možných tahů figury, prázdný list pokud tah není možný
        """
        if color is None:
            color = self.__onTurn
            
        if self.__board.getPosition(color) == position:
            return self.__board.getPosibleMoves(position)
        
        return []
    
        
    def makeMove(self, move, color = None):
        """Přesune figuru na jinou pozici
        
        Args:
            move ([int,int]): nová pozice figury
            color (Enum Colors, optional): Barva figury. Defaults to None.
            
        Returns:
            bool: True, pokud se tah podařil, jinak False
            List of List of int: List možných tahů figury, pokud se dá pokračovat v pohybu
        """
        if move is None:
            return False
        
        if color is not None:
            if self.__firstTime:
                self.__firstTime = False
                
                if color == Colors.WHITE:
                    self.__score += 1
                    
                else:
                    self.__score -= 1
        else:
            color = self.__onTurn
            
        if self.__board.getPosibleMoves(self.__board.getPosition(color)).__contains__(move):
            if self.__board.board[move[0]][move[1]] == "TASK":
                self.__board.movePiece(move, color)
                self.__firstTime = True
                self.__printToTerminal()
                return True
            
            else:
                self.__board.movePiece(move, color)
                self.__printToTerminal()
                return self.choosePiece(move, color)
            
        else:
            return False


    def checkEnd(self):
        """Zkontroluje, zda hra skončila
        
        Returns:
            String: Vrací výsledek hry, pokud hra skončila, jinak None
        """
        if self.__board.TasksLeft() == 0:
            if self.__score > 0:
                color = Colors.WHITE
                
            elif self.__score < 0:
                color = Colors.BLACK
                
            else:
                return "Draw"
            
            return f"{color} won"
        
        return None
    
    
    def __printToTerminal(self):
        print(self.__board.__str__())
        print(self.__score)