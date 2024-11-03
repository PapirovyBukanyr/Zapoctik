from .Piece import *
import random as rnd

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def __str__(self):
        return 'P' + self.color.__str__() 
    
    def possibleMoves(self, board):
        moves = []
        direction = -1 if self.color == Colors.WHITE else 1
        row, col = self.position
        
        # Check for simple moves
        for dc in [-1, 1]:
            new_row, new_col = row + direction, col + dc
            if 0 <= new_col < 8 and board[new_row, new_col] is None:
                moves.append([new_row, new_col])
        
        moves += self.possibleJumps(board)
        
        return moves
    
    def possibleJumps(self, board, position=None):
        if position is None:
            position = self.position
            
        jumps = []
        row, col = position
        direction = -1 if self.color == Colors.WHITE else 1
        
        for dc in [-1, 1]:
            mid_row, mid_col = row + direction, col + dc
            new_row, new_col = row + 2 * direction, col + 2 * dc
            if (0 <= new_row < 8 and 0 <= new_col < 8 and 
                board[mid_row, mid_col] is not None and 
                board[mid_row, mid_col].color != self.color and 
                board[new_row, new_col] is None):
                jumps.append([new_row, new_col])
                jumps += self.possibleJumps(board, [new_row, new_col])
                
        return jumps
    
    def possibleJump(self, board, position=None):
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
        
    
    def trackJumps(self, board, endPosition):
        jumps = []
        row, col = self.position
        new_row, new_col = endPosition
        work_row1 = row
        work_col1 = col
        work_row2 = row
        work_col2 = col
        while True:
            if work_row1 == new_row and work_col1 == new_col:
                break
            new_jumps = self.possibleJump(board, [work_row1, work_col1])
            if new_jumps != []:
                work_row2, work_col2 = rnd.choice(new_jumps)
                jumps.append([(work_row1+work_row2)//2, (work_col1+work_col2)//2])
            if work_row1 == work_row2 and work_col1 == work_col2:
                jumps = []
                work_row2, work_col2 = row, col
                work_row1, work_col1 = work_row2, work_col2
            work_row1 = work_row2
            work_col1 = work_col2
        return jumps
    
