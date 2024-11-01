from .Piece import Piece

class Queen(Piece):
    def __init__(self, pawn):
        super().__init__(pawn.color, pawn.position)
        
    def __str__(self):
        return 'Q' + self.color.__str__()
        
    def posibleMoves(self):
        moves = []
        for i in range(1, 8):
            moves.append(self.position[0] + i, self.position[1] + i)
            moves.append (self.position[0] + i, self.position[1] - i)
            moves.append (self.position[0] - i, self.position[1] + i)
            moves.append (self.position[0] - i, self.position[1] - i)
        for i in moves:
            if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
                moves.remove(i)
        return moves