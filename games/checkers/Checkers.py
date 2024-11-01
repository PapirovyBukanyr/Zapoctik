from ..Enums import Colors
from .Board import Board
class Checkers:
    def __init__(self):
        self.board = Board()
        self.current_player = Colors.WHITE
    
    def __str__(self):
        return '\n'.join(['.'.join(row) for row in self.board])
    
    def playedPiecePosition(self, position, color = None):
        if color is None:
            color = self.current_player
        if self.board[position[0]][position[1]] == color:
            self.playedPiece = position
            return self.posibleMoves(position)
        return []
    
    def choosePiece(self, start_row, start_col):
        """TODO"""
    
    def makeMove(self, end_row, end_col):
        """TODO"""
    
    def reset(self):
        self.board = self.create_initial_board()
        self.current_player = Colors.WHITE