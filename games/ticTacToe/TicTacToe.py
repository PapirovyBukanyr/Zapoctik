from ..Enums import Colors 

class TicTacToe:
    def __init__(self):
        """Inicializace hry
        """
        self.__board = [['' for _ in range(3)] for _ in range(3)]
        self.__current_player = Colors.BLACK
        
    def getBoard(self):
        """Vrátí hrací desku

        Returns:
            List: hrací deska
        """
        board = [['' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for cell in range(3):
                board[row][cell] = self.__board[row][cell].__str__()
        return board
    
    def makeMove(self, row, col, player = None):
        """Metoda na zahrání tahu

        Args:
            row (int): _description_
            col (int): _description_
            player (Enum Colors, optional): Hráč co má být na tahu. Výchozí je nastaveno na střídání.

        Returns:
            Boolean: true pokud se tah podařil, jinak false
        """
        try:    
            if player is None:
                player = self.__current_player
            else:
                self.__current_player = player
            if self.__board[row][col] == '':
                self.__board[row][col] = player
                self.__current_player = self.__current_player.changeColor()
                self.__printToTerminal()
                return True
            else:
                return False
        except:
            return False
    
    def checkEnd(self):
        """Kontroluje jestli hra skončila

        Returns:
            String: "DRAW" pokud je remíza
            Enum Colors: barva hráče, který vyhrál
            None: pokud hra neskončila
        """
        if self.__checkDraw():
            return "DRAW"
        else:
            return self.__checkWinner()
        
    def reset(self):
        """Resetuje hru
        """
        self.__board = [['' for _ in range(3)] for _ in range(3)]
        self.__current_player = Colors.WHITE
    
    def __printToTerminal(self):  
        """Vytiskne hrací desku do konzole
        """
        board = "-------\n"
        for i in range(3): 
            board += '|' 
            for j in range(3):
                if self.__board[i][j] == '':
                    board += ' '
                else:
                    board += self.__board[i][j].__str__()
                board += '|'
            board += '\n-------\n'
        print(board ) 
    
    def __checkWinner(self):
        """Kontroluje jestli někdo vyhrál

        Returns:
            Enum Colors: barva hráče, který vyhrál
            None: pokud nikdo nevyhrál
        """
        for row in self.__board:
            if row[0] == row[1] == row[2] and row[0] != '':
                return row[0]
        for col in range(3):
            if self.__board[0][col] == self.__board[1][col] == self.__board[2][col] != '':
                return self.__board[0][col]
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != '':
            return self.__board[0][0]
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != '':
            return self.__board[0][2]
        return None
    
    def __checkDraw(self):
        """Kontroluje jestli je remíza
        
        Returns:
            Boolean: true pokud je remíza, jinak false
        """
        for row in self.__board:
            if '' in row:
                return False
        return True