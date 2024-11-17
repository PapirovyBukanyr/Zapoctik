from ..Board import Board
from ..Enums import *
import random as rand 

class MinesBoard(Board):
    def __init__(self, numberOfMines):
        """Inicializace hrací desky Miny
        
        Args:
            numberOfMines (int): počet min na hrací desce
        """
        super().__init__()
        self.__numberOfMines = numberOfMines
        self.__populateBoard()
        self.kaboom = False
        
    def __populateBoard(self):
        """Naplní hrací desku minami
        """
        self.board = [[None for x in range(16)] for y in range(8)]
        self.__placeMines()
        
    def __placeMines(self):
        """Umístí miny na hrací desku
        """
        for _ in range(self.__numberOfMines):
            row = rand.randint(1, 8)
            col = rand.randint(1, 16)
            while self.board[row-1][col-1] is not None:
                row = rand.randint(1, 8)
                col = rand.randint(1, 16)
            self.board[row-1][col-1] = "M"
            
    def countMinesAroundSymbol(self, row, col):
        """Spočítá miny kolem symbolu
        
        Args:
            row (int): řádek
            col (int): sloupec
            
        Returns:
            int: počet min kolem symbolu
        """
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r >= 0 and r < 8 and c >= 0 and c < 16:
                    if self.board[r][c] == "M" or self.board[r][c] == "FM" or self.board[r][c] == "K":
                        count += 1
        return count
    
    def minesRemaining(self):
        """Spočítá zbývající neoznačené miny na hrací desce
        
        Returns:
            int: počet zbývajících neoznačených min
        """
        count = 0
        for row in self.board:
            for cell in row:
                if cell == "M":
                    count += 1
        return count
    
    def flagsPlanted(self):
        """Spočítá počet vlajek na hrací desce
        
        Returns:
            int: počet vlajek
        """
        count = 0
        for row in self.board:
            for cell in row:
                if cell == "F" or cell == "FM":
                    count += 1
        return count
    
    def makeMove(self, row, col):
        """Provede tah na hrací desce
        
        Args:
            row (int): řádek
            col (int): sloupec
            
        Returns:
            bool: True, pokud tah byl úspěšný, jinak False
        """
        if row < 0 or row >= 8 or col < 0 or col >= 16:
            return False
        if self.board[row][col] != "S" and self.board[row][col] != "F" and self.board[row][col] != "FM":
            if self.board[row][col] == "M":
                self.kaboom = True
                self.board[row][col] = "K"
                return True
            else:
                if self.board[row][col] == "S" or self.board[row][col] == "F":
                    return False
                if self.countMinesAroundSymbol(row, col) != 0:
                    self.board[row][col] = self.countMinesAroundSymbol(row, col)
                if self.board[row][col] == None:
                    self.__showBoard(row, col)
                return True
        else:
            return False
            
    def __showBoard(self, row, col):
        """Odkryje dostupné symboly na hrací desce po odkrytí políčka
        
        Args:
            row (int): řádek
            col (int): sloupec
        """
        if row < 0 or row >= 8 or col < 0 or col >= 16:
            return
        if self.board[row][col] == "S":
            return
        if self.countMinesAroundSymbol(row, col) != 0:
            self.board[row][col] = self.countMinesAroundSymbol(row, col)
        if self.board[row][col] == None:
            self.board[row][col] = "S"
            for i in [row-1, row, row+1]:
                for j in [col-1, col, col+1]:
                    self.__showBoard(i, j)
                    
    def placeFlag(self, row, col):
        """Umístí vlajku na hrací desku
        
        Args:
            row (int): řádek
            col (int): sloupec
            
        Returns:
            bool: False, pokud se vlajka neumístí
            int: -1, pokud se správná vlajka odstraní, 1, pokud se vlajka umístí správně a 0, pokud se vlajka odstraní nebo přidá na špatné místo
        """
        if self.board[row][col] == "F" and self.__numberOfMines > self.flagsPlanted():
            self.board[row][col] = None
            return 0
        elif self.board[row][col] == None:
            self.board[row][col] = "F"
            return 0
        elif self.board[row][col] == "M" and self.__numberOfMines > self.flagsPlanted():
            self.board[row][col] = "FM"
            return 1
        elif self.board[row][col] == "FM":
            self.board[row][col] = "M"
            return -1
        else:
            return False
                
    def __str__(self):
        """Vygeneruje textovou reprezentaci hrací desky

        Returns:
            string: textová reprezentace hrací desky
        """
        s = ""
        for row in self.board:
            for cell in row:
                if cell == None:
                    s += "_ "
                else:
                    s += str(cell) + " "
            s += "\n"
        return s