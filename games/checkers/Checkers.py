from ..Enums import Colors
from .pieces import *
from .CheckersBoard import CheckersBoard
from ..GameTemplate import GameTemplate

class Checkers (GameTemplate):
    """Třída reprezentující hru dáma
    """
    
    
    def __init__(self):
        """Konstruktor třídy hry dáma
        """
        super().__init__()
        self.withChoosePiece = True
        self.__board = CheckersBoard()
        self.__currentPlayer = Colors.WHITE
        self.__pieceToPlay = None
        self.__firstMove = True
        
        
    def getBoard(self, color=None):
        """Funkce pro získání hrací desky
        
        Args:
            color (Enum Colors, optional): barva hráče na tahu. Výchozí nastavení je na pravidelném střídání.
            
        Returns:
            List of List of [int, int]: hrací deska
        """
        return self.__board.getListOfBoard()
    
    
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
        
    
    def makeMove(self, index, color = None, rightClick = False):
        """Funkce pro provedení tahu figurkou
        
        Args:
            index ([int,int]): pozice, kam chce hráč hrát
            color (Enum Colors, optional): barva hráče na tahu. Výchozí nastavení je na pravidelném střídání.
            rightClick (bool, optional): True, pokud se jedná o pravé tlačítko myši. Výchozí nastavení je False.
            
        Returns:
            bool: True, pokud se tah podařil, jinak False
        """
        if rightClick:
            return False
        
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
            row, col = self.__pieceToPlay.trackJumps([end_row, end_col])
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
        hasMoves = [False, False]
        for color in [Colors.WHITE, Colors.BLACK]:
            if self.__board.pieceList(color) == []:
                return f"{color.changeColor()} won"
            
            for piece in self.__board.pieceList(color):
                if isinstance(piece, Piece):
                    if piece.possibleMoves(self.__board) != [] or piece.possibleJumps(self.__board) != []:
                        hasMoves[0 if color == Colors.WHITE else 1] = True
                        break
                    
        if hasMoves[0] == False:
            return f"{Colors.WHITE} won"
        
        elif hasMoves[1] == False:
            return f"{Colors.BLACK} won"
        
        else:
            return None
        
        
    def __endOfTurn(self):
        """Funkce pro ukončení tahu
        """
        self.__currentPlayer = self.__currentPlayer.changeColor()
        
        self.__pieceToPlay = None
        
        self.__firstMove = True
        
        self.__printToTerminal()
        
        return True
    
    
    def possibleMoves(self, color):
        """Funkce pro získání možných tahů pro hráče, primárně pro rozšíření Fog Of War
        
        Args:
            color (Enum Colors): barva hráče, pro kterého se mají tahy získat
            
        Returns:
            List of [int, int]: seznam možných tahů
        """
        listOfMoves = []
        
        for piece in self.__board.pieceList(color):
            
            for move in piece.possibleMoves(self.__board):
                listOfMoves.append(move)
                
            for jump in piece.possibleJumps(self.__board):
                listOfMoves.append(piece.trackJumps(jump))
                
        return listOfMoves
    
    
    def killPiece(self, piecePosition):
        """Funkce pro odstranění figurky z hrací desky
        
        Args:
            piecePosition ([int, int]): pozice figurky, která má být odstraněna
        """
        self.__board[piecePosition[0], piecePosition[1]] = None
    
    
    def __printToTerminal(self):
        """Funkce pro výpis stavu hry na terminál
        """
        print(self.__board.__str__())