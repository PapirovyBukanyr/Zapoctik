from ..Enums import Colors
from .pieces import *
from .CheckersBoard import CheckersBoard

class Checkers:
    def __init__(self):
        """Konstruktor třídy Checkers
        """
        self.board = CheckersBoard()
        self.currentPlayer = Colors.WHITE
        self.pieceToPlay = None
    
    def getBoard(self):
        return self.board.__str__()
    
    def choosePiece(self, index, color = None):
        """Funkce pro vyber figurky, kterou chce hrac hrat

        Args:
            index ([int,int]]): pozice figurky, kterou chce hrac hrat
            color (Enum Colors, optional): barva hráče na tahu. Výchozí nastavení je na pravidelném střídání.

        Returns:
            List of [int, int]: seznam dostupných pozic, kam může hráč hrát
        """
        try:
            if color == None:
                color = self.currentPlayer
            start_row = index[0]
            start_col = index[1]
            piece = self.board[start_row, start_col]
            if piece == None:
                return []
            if piece.color == color:
                self.pieceToPlay = piece
                return piece.possibleMoves(self.board)
            else:
                return []
        except:
            return []
    
    def makeMove(self, index):
        """Funkce pro provedení tahu figurkou
        
        Args:
            index ([int,int]): pozice, kam chce hráč hrát
            
        Returns:
            bool: True, pokud se tah podařil, jinak False
        """
        try:
            if self.pieceToPlay == None:
                return False 
            
            end_row = index[0]
            end_col = index[1]
            
            if [end_row, end_col] not in self.pieceToPlay.possibleMoves(self.board):
                return False
            
            if [end_row, end_col] not in self.pieceToPlay.possibleJumps(self.board):
                self.board[end_row,end_col] = self.pieceToPlay
                self.board[self.pieceToPlay.position[0], self.pieceToPlay.position[1]] = None
                self.pieceToPlay.position = [end_row, end_col]
                
            else:
                
                for piece in self.pieceToPlay.trackJumps(self.board, [end_row, end_col]):
                    self.board[piece[0], piece[1]] = None
                    
                self.board[end_row, end_col] = self.pieceToPlay
                self.board[self.pieceToPlay.position[0], self.pieceToPlay.position[1]] = None
                self.pieceToPlay.position = [end_row, end_col]
                
            if isinstance(self.pieceToPlay, Pawn) and end_row == 0 and self.pieceToPlay.color == Colors.WHITE:
                self.board[end_row, end_col] = Queen(self.pieceToPlay)
            elif isinstance(self.pieceToPlay, Pawn) and end_row == 7 and self.pieceToPlay.color == Colors.BLACK:
                self.board[end_row, end_col] = Queen(self.pieceToPlay)

            return self.__endOfTurn()
        
        except:
            
            return False
    
    def reset(self):
        """Funkce pro resetování hry
        """
        self.board = CheckersBoard()
        self.currentPlayer = Colors.WHITE
        
    def checkEnd(self):
        """Funkce pro kontrolu konce hry
        
        Returns:
            string: Vrací vítěze "{barva} won", pokud hra skončila, jinak None
        """
        for piece in self.board.pieceList(self.currentPlayer.changeColor()):
            if isinstance(piece, Piece):
                if piece.possibleMoves(self.board) != [] or piece.possibleJumps(self.board) != []:
                    return None
                
        return f"{self.currentPlayer} won"
        
    def __endOfTurn(self):
        """Funkce pro ukončení tahu
        """
        self.currentPlayer = self.currentPlayer.changeColor()
        
        if self.checkEnd() != None:
            return self.checkEnd()
        
        self.pieceToPlay = None
        
        return True
    