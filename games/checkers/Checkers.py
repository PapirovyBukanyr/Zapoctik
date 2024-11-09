from ..Enums import Colors
from .pieces import *
from .CheckersBoard import CheckersBoard

class Checkers:
    def __init__(self):
        """Konstruktor třídy Checkers
        """
        self.__board = CheckersBoard()
        self.__currentPlayer = Colors.WHITE
        self.__pieceToPlay = None
        self.__firstMove = True
    
    def getBoard(self):
        return self.__board.__str__()
    
    def choosePiece(self, index, color = None):
        """Funkce pro vyber figurky, kterou chce hrac hrat

        Args:
            index ([int,int]): pozice figurky, kterou chce hrac hrat
            color (Enum Colors, optional): barva hráče na tahu. Výchozí nastavení je na pravidelném střídání.

        Returns:
            List of [int, int]: seznam dostupných pozic, kam může hráč hrát
        """
        try:
            if color == None:
                color = self.__currentPlayer
            else :
                self.__currentPlayer = color
            start_row = index[0]
            start_col = index[1]
            piece = self.__board[start_row, start_col]
            if piece == None:
                return []
            if piece.color == color:
                self.__pieceToPlay = piece
                return piece.possibleMoves(self.__board)
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
            if self.__pieceToPlay == None:
                return False 
            
            end_row = index[0]
            end_col = index[1]
            
            if [end_row, end_col] not in self.__pieceToPlay.possibleMoves(self.__board):
                return False
            
            if [end_row, end_col] not in self.__pieceToPlay.possibleJumps(self.__board) and self.__firstMove == True:
                index = [-1, -1]
                for figure in self.__board.pieceList(self.__currentPlayer):
                    if figure.possibleJumps(self.__board) != []:
                        self.__board[figure.row, figure.col] = None
                        index = figure.position
                        break
                if index != [end_row, end_col]:
                    self.__board[end_row,end_col] = self.__pieceToPlay
                    self.__board[self.__pieceToPlay.position[0], self.__pieceToPlay.position[1]] = None
                    self.__pieceToPlay.position = [end_row, end_col]
                
            else:
                
                self.__firstMove = False
                row, col = self.__pieceToPlay.trackJumps(end_row, end_col)
                self.__board[row, col] = None
                    
                self.__board[end_row, end_col] = self.__pieceToPlay
                self.__board[self.__pieceToPlay.position[0], self.__pieceToPlay.position[1]] = None
                self.__pieceToPlay.position = [end_row, end_col]
                
                if self.__pieceToPlay.possibleJumps(self.__board) != []:
                    self.__printToTerminal()
                    return self.__pieceToPlay.possibleJumps(self.__board) 
                
            if isinstance(self.__pieceToPlay, Pawn) and end_row == 0 and self.__pieceToPlay.color == Colors.WHITE:
                self.__board[end_row, end_col] = Queen(self.__pieceToPlay)
            elif isinstance(self.__pieceToPlay, Pawn) and end_row == 7 and self.__pieceToPlay.color == Colors.BLACK:
                self.__board[end_row, end_col] = Queen(self.__pieceToPlay)

            return self.__endOfTurn()
        
        except:
            
            return False
    
    def reset(self):
        """Funkce pro resetování hry
        """
        self.__board = CheckersBoard()
        self.__currentPlayer = Colors.WHITE
        
    def checkEnd(self):
        """Funkce pro kontrolu konce hry
        
        Returns:
            string: Vrací vítěze "{barva} won", pokud hra skončila, jinak None
        """
        for piece in self.__board.pieceList(self.__currentPlayer.changeColor()):
            if isinstance(piece, Piece):
                if piece.possibleMoves(self.__board) != [] or piece.possibleJumps(self.__board) != []:
                    return None
                
        return f"{self.__currentPlayer} won"
        
    def __endOfTurn(self):
        """Funkce pro ukončení tahu
        """
        self.__currentPlayer = self.__currentPlayer.changeColor()
        
        if self.checkEnd() != None:
            return self.checkEnd()
        
        self.__pieceToPlay = None
        
        self.__firstMove = True
        
        self.__printToTerminal()
        
        return True
    
    def __printToTerminal(self):
        """Funkce pro výpis stavu hry na terminál
        """
        print(self.__board.__str__())