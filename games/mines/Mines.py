from .MinesBoard import *

class Mines:
    def __init__(self):
        self.__board = MinesBoard()
        self.__firstMove = True
        
    def makeMove(self, position, color = Colors.WHITE):
        self.__color = color
        if self.__firstMove:
            row, col = position
            if self.__board[row, col] != None:
                self.__board = MinesBoard()
                return self.makeMove(position, color)
            self.__firstMove = False
        self.__board.makeMove(position[0], position[1])
        return True
        
    def __str__(self):
        return str(self.__board.__str__())
    
    def checkEnd(self):
        if self.__board.minesRemaining() == 0:
            return f"{self.__color} win!"
        elif self.__board.kaboom:
            return f"{self.__color} lose!"
        else:
            return None
        
    def getBoard(self):
        board = [[None for x in range(10)] for y in range(10)]
        if self.checkEnd() == None:
            for i in range(10):
                for j in range(10):
                    if self.__board[i, j] == None or self.__board[i, j] == "M":
                        board[i][j] = None
                    elif self.__board[i, j] == "F":
                        board[i][j] = Field(Colors.WHITE, Figures.FLAG)
        else:
            for i in range(10):
                for j in range(10):
                    if self.__board[i, j] == "M":
                        board[i][j] = Field(Colors.WHITE, Figures.MINE)
                    elif self.__board[i, j] == "F":
                        board[i][j] = Field(Colors.WHITE, Figures.FLAG)
                    if self.__board[i, j] == None:
                        board[i][j] = None
                    
                
        