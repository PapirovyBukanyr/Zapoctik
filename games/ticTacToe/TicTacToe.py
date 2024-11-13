from ..Enums import Colors 
from .TicTacToeBoard import TicTacToeBoard

class TicTacToe:    
    def __init__(self):
        """Inicializace hry
        """
        self.__board = TicTacToeBoard()
        self.__current_player = Colors.BLACK
        
    def __str__(self):
        """Vrátí název hry

        Returns:
            String: název hry
        """
        return "Piškvorky"
        
    def getBoard(self):
        """Vrátí hrací desku

        Returns:
            List: hrací deska
        """
        return self.__board.getListOfBoard()
    
    def makeMove(self, index, player = None):
        """Metoda na zahrání tahu

        Args:
            index ([int,int]): pozice kterou chce hráč obsadit
            player (Enum Colors, optional): Hráč co má být na tahu. Výchozí je nastaveno na střídání.

        Returns:
            Boolean: true pokud se tah podařil, jinak false
        """
        row, col = index
        
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        
        if player is None:
            player = self.__current_player
        else:
            self.__current_player = player
            
        if self.__board[row,col] == None:
            self.__board[row,col] = player
            self.__current_player = self.__current_player.changeColor()
            self.__printToTerminal()
            return True
        else:
            return False
        
    
    def checkEnd(self):
        """Kontroluje jestli hra skončila

        Returns:
            String: "Draw" pokud je remíza
            String: "{barva} won" pokud někdo vyhrál
            None: pokud hra neskončila
        """
        if self.__checkDraw():
            return "Draw"
        elif self.__checkWinner() == None:
            return None
        else:
            return f"{self.__checkWinner()} won"
        
    def reset(self):
        """Resetuje hru
        """
        self.board = TicTacToeBoard()
        self.__current_player = Colors.WHITE
    
    def __printToTerminal(self):  
        """Vytiskne hrací desku do konzole
        """
        print(self.__board.__str__()) 
    
    def __checkWinner(self):
        """Kontroluje jestli někdo vyhrál

        Returns:
            Enum Colors: barva hráče, který vyhrál
            None: pokud nikdo nevyhrál
        """
        for i in range(3):
            if self.__board[i,0] == self.__board[i,1] == self.__board[i,2] and self.__board[i,0] != None:
                return self.__board[i,0]
        for col in range(3):
            if self.__board[0,col] == self.__board[1,col] == self.__board[2,col] != None:
                return self.__board[0,col]
        if self.__board[0,0] == self.__board[1,1] == self.__board[2,2] != None:
            return self.__board[0,0]
        if self.__board[0,2] == self.__board[1,1] == self.__board[2,0] != None:
            return self.__board[0,2]
        return None
    
    def __checkDraw(self):
        """Kontroluje jestli je remíza
        
        Returns:
            Boolean: true pokud je remíza, jinak false
        """
        for i in range(3):
            for j in range(3):
                if self.__board[i,j] == None:
                    return False
        return True