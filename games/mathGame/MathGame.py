from .MathGameBoard import *

class MathGame:
    def __init__(self):
        self.__score = 0
        self.__board = MathGameBoard()
        self.__onTurn = Colors.WHITE
        
    def __str__(self):
        """Vrátí název hry

        Returns:
            String: název hry
        """
        return "Matematická hra"
        
    def getBoard(self):
        return self.__board.getListOfBoard()
    
    def choosePiece(self, position, color = None):
        if color is None:
            color = self.__onTurn
        else:
            if color == Colors.WHITE:
                self.__score += 1
            else:
                self.__score -= 1
        if self.__board.getPosition(color) == position:
            return self.__board.getPosibleMoves(position)
        return []
        
    def makeMove(self, move, color = None):
        print("move")
        if move is None:
            return False
        color = self.__onTurn
        if self.__board.getPosibleMoves(self.__board.getPosition(color)).__contains__(move):
            if self.__board.board[move[0]][move[1]] == "TASK":
                self.__board.movePiece(move, color)
                self.__printToTerminal()
                return True
            else:
                self.__board.movePiece(move, color)
                self.__printToTerminal()
                return self.choosePiece(move, color)
        else:
            return False

    def checkEnd(self):
        if self.__board.TasksLeft() == 0:
            if self.__score > 0:
                color = Colors.WHITE
            elif self.__score < 0:
                color = Colors.BLACK
            else:
                return "Draw"
            return f"{color} won"
        return None
    
    def __printToTerminal(self):
        print(self.__board.__str__())
        print(self.__score)