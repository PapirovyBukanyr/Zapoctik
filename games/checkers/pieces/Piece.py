class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        
    def posibleMoves(self):
        raise NotImplementedError("Subclass must implement abstract method")
    