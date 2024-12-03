from ...Enums import *

class Piece:
    """ Třída Piece slouží k reprezentaci jedné herní figurky.
    """
    
    def __init__(self, position):
        """ Konstruktor třídy Piece.
        
        Args:
            color (Colors): Barva figurky
            position ([int,int]): Pozice figurky
        """
        self.color = None
        self.position = position
        self.homePosition = position
        self.isDeployed = False
        self.isInFinal = False 
        self.startPosition = None
        self.finalPosition = None  
        
        
    def returnHome(self, board):
        """ Metoda vrátí figurku domů.
        """
        board[self.position[0], self.position[1]] = None
        board[self.homePosition[0], self.homePosition[1]] = self
        self.position = self.homePosition
        self.isDeployed = False
        
        
    def possibleMoves(self, number, board, position = None):
        """ Metoda vrátí seznam možných tahů figurky.
        
        Args:
            number (int): Počet oček hoděných na kostce
            
        Returns:
            List of [int,int]: Seznam možných tahů figurky
        """                     
        if number == 0:
            return position
        
        if position is None:
            position = self.position
        
        if self.isDeployed == False and self.isInFinal == False and number == 6:
            return self.startPosition
        
        elif self.isDeployed == False or self.isInFinal:
            return []
        
        if position == self.finalPosition:
            return position
            
        else:
            return self.makeStandartMove(number, board, position)
        
        
    def makeStandartMove(self, number, board, position):
        """ Metoda provede standardní tah figurkou.
        
        Args:
            board (Board): Hrací deska
            position ([int,int]): Pozice figurky
        """
        row, col = position        
        if row <= 4:
            if col <= 4:
                if board[row,col+1] == None or (isinstance(board[row,col+1], Piece) and not board[row,col+1].isInFinal):
                    return self.possibleMoves(number-1, board, [row, col+1])
                
                else:
                    return self.possibleMoves(number-1, board, [row-1, col])
                
            else:
                if board[row+1,col] == None or (isinstance(board[row+1,col], Piece) and not board[row+1,col].isInFinal):
                    return self.possibleMoves(number-1, board, [row+1, col])
                
                else:
                    return self.possibleMoves(number-1, board, [row, col+1])
                
        else:
            if col <= 4:
                if board[row-1,col] == None or (isinstance(board[row-1,col], Piece) and not board[row-1,col].isInFinal):
                    return self.possibleMoves(number-1, board, [row-1, col])
                
                else:
                    return self.possibleMoves(number-1, board, [row, col-1])
                
            else:
                if board[row,col-1] == None or (isinstance(board[row,col-1], Piece) and not board[row,col-1].isInFinal):
                    return self.possibleMoves(number-1, board, [row, col-1])
                
                else:
                    return self.possibleMoves(number-1, board, [row+1, col])