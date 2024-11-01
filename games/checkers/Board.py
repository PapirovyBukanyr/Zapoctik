from pieces import *
from Enums import Colors

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.__populateBoard()
        
    def __populateBoard(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.board[i][j] = Pawn(Colors.BLACK, (i, j))
                    elif i > 4:
                        self.board[i][j] = Pawn(Colors.WHITE, (i, j))
                    else:
                        self.board[i][j] = None

    def __str__(self):
        board = []
        for row in self.board:
            board.append([str(cell) if cell is not None else '--' for cell in row])
        return '\n'.join([' '.join(row) for row in board])
    
    
if __name__ == '__main__':
    board = Board()
    print(board)