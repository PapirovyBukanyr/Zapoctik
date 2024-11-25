from ..Board import *

class TicTacToeBoard (Board):
    def __init__(self):
        """Konstruktor třídy TicTacToeBoard
        """
        self.board = []
        self.__populateBoard()
        
    def __populateBoard(self):
        """Inicializace herní desky
        """
        self.board = [[None for _ in range(3)] for _ in range(3)]
    
    
    def __str__(self):
        """Vytiskne hrací desku do konzole
        """
        board = "-------\n"
        for i in range(3): 
            board += '|' 
            for j in range(3):
                if self.board[i][j] == None:
                    board += ' '
                else:
                    board += self.board[i][j].__str__()
                board += '|'
            board += '\n-------\n'
        return board
    
    def getListOfBoard(self):
        """Vrací seznam políček na hrací desce

        Returns:
            List of Struct Field: _description_
        """
        board = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != None:
                    if self.board[i][j] == Colors.WHITE:
                        board[i][j] = Field(Colors.WHITE, Figures.X)
                    else:
                        board[i][j] = Field(Colors.BLACK, Figures.O)
                else:
                    board[i][j] = None
        return board
    
    
      