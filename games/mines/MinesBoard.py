from ..Board import Board
from ..Enums import *
from random import randint

class MinesBoard(Board):
    def __init__(self):
        super().__init__()
        self.__populateBoard()
        self.kaboom = False
        
    def __populateBoard(self):
        self.board = [[None for x in range(10)] for y in range(10)]
        self.__placeMines(10)
        self.__placeNumbers()
        
    def __placeMines(self, number):
        for i in range(number):
            row = randint(0, 9)
            col = randint(0, 9)
            while self.board[row][col] != None:
                row = randint(0, 9)
                col = randint(0, 9)
            self.board[row][col] = "M"
            
    def __placeNumbers(self):
        for row in range(10):
            for col in range(10):
                if self.board[row][col] == None:
                    self.board[row][col] = self.__countMinesAroundSymbol(row, col)
    
    def __countMinesAroundSymbol(self, row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r >= 0 and r < 10 and c >= 0 and c < 10:
                    if self.board[r][c] == "M":
                        count += 1
        return count
    
    def minesRemaining(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell == "M":
                    count += 1
        return count
    
    def makeMove(self, row, col):
        if self.board[row][col] == "M":
            self.kaboom = True
            return True
        else:
            return True
    
    def __str__(self):
        s = ""
        for row in self.board:
            for cell in row:
                if cell == None:
                    s += "_ "
                else:
                    s += str(cell) + " "
            s += "\n"
        return s
    
    def getBoard(self):
        raise NotImplementedError("Method getBoard not implemented")