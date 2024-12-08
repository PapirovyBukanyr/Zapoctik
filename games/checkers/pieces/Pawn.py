from .Piece import *

class Pawn(Piece):
    """
    Třída reprezentující pěšáka
    
    Attributes:
        color (Colors): barva figurky
        position ([int,int]): pozice figurky
    """      
        
        
    def __str__(self):
        """
        Funkce na výpis figurky

        Returns:
            str: P + barva figurky
        """
        return 'P' + self.color.__str__() 
    
    
    def possibleMoves(self, board):
        """Funkce najde všechny možné tahy figurky
        
        Args:
            board (two-dimensional array of ints): hrací deska
            
        Returns:
            [int,int]: pole možných tahů
        """
        moves = []
        direction = -1 if self.color == Colors.WHITE else 1
        row, col = self.position
        
        for dc in [-1, 1]:
            new_row, new_col = row + direction, col + dc
            
            if 0 <= new_col < 8 and board[new_row, new_col] is None:
                moves.append([new_row, new_col])
        
        moves += self.possibleJumps(board)
        
        return moves
    
    
    def possibleJumps(self, board, position=None):
        """Funkce najde všechny jednoduché skoky z pozice

        Args:
            board (two-dimensional array of ints): hrací deska
            position ([int,int]], optional): _description_. Defaults to None.

        Returns:
            [int,int]: pole možných skoků
        """
        if position is None:
            position = self.position

        jumps = []
        row, col = position
        direction = -1 if self.color == Colors.WHITE else 1

        for dc in [-1, 1]:
            mid_row, mid_col = row + direction, col + dc
            new_row, new_col = row + 2 * direction, col + 2 * dc
            
            if (0 <= new_row < 8 and 0 <= new_col < 8 and 
                board[mid_row,mid_col] is not None and 
                board[mid_row,mid_col].color != self.color and 
                board[new_row,new_col] is None):
                
                jumps.append([new_row, new_col])

        return jumps
        
    
    def trackJumps(self, endPosition):
        """Funkce na zjištění přeskočených figurek

        Args:
            endPosition ([int, int]): koncová pozice

        Returns:
            [int, int]: pozice přeskoečené figurky
        """
        return [(self.position[0]+ endPosition[0])//2,(self.position[1]+ endPosition[1])//2]
