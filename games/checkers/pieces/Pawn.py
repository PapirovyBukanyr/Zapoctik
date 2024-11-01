from .Piece import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def __str__(self):
        return 'P' + self.color.__str__() 