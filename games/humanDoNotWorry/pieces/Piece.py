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
        self.isDeployed = False
        self.isInHome = False   
        
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
        
        
        row, col = position 
        

        if row <= 4:
            if col <= 4:
                if board[row,col+1] == None or isinstance(board[row,col+1], Piece):
                    return self.possibleMoves(number-1, board, [row, col+1])
                
                else:
                    return self.possibleMoves(number-1, board, [row-1, col])
                
            else:
                if board[row+1,col] == None or isinstance(board[row+1,col], Piece):
                    return self.possibleMoves(number-1, board, [row+1, col])
                
                else:
                    return self.possibleMoves(number-1, board, [row, col+1])
                
        else:
            if col <= 4:
                if board[row,col-1] == None or isinstance(board[row,col-1], Piece):
                    return self.possibleMoves(number-1, board, [row, col-1])
                
                else:
                    return self.possibleMoves(number-1, board, [row+1, col])
                
            else:
                if board[row-1,col] == None or isinstance(board[row-1,col], Piece):
                    return self.possibleMoves(number-1, board, [row-1, col])
                
                else:
                    return self.possibleMoves(number-1, board, [row, col-1])