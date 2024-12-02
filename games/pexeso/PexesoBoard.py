from ..Enums import *
from ..Board import Board
from itertools import permutations, chain
from .PexesoCard import PexesoCard
import random

class PexesoBoard(Board):
    """Reprezentace hrací desky hry Pexeso
    """
    
    
    def __init__(self):
        """Inicializace hrací desky
        """
        super().__init__()
        self.__populateBoard()
        
        
    def __populateBoard(self):
        """Vygeneruje náhodné kartičky na hrací desku
        """
        board = [
            [PexesoCard(Field(Figures.PAWN, Colors.WHITE)), PexesoCard(Field(Figures.PAWN, Colors.WHITE)), PexesoCard(Field(Figures.PAWN, Colors.BLACK)), PexesoCard(Field(Figures.PAWN, Colors.BLACK)), PexesoCard(Field(Figures.PAWN, Colors.RED)), PexesoCard(Field(Figures.PAWN, Colors.RED))],
            [PexesoCard(Field(Figures.PAWN, Colors.GREEN)), PexesoCard(Field(Figures.PAWN, Colors.GREEN)), PexesoCard(Field(Figures.QUEEN, Colors.WHITE)), PexesoCard(Field(Figures.QUEEN, Colors.WHITE)), PexesoCard(Field(Figures.QUEEN, Colors.BLACK)), PexesoCard(Field(Figures.QUEEN, Colors.BLACK))],
            [PexesoCard(Field(Figures.KING, Colors.WHITE)), PexesoCard(Field(Figures.KING, Colors.WHITE)), PexesoCard(Field(Figures.KING, Colors.BLACK)), PexesoCard(Field(Figures.KING, Colors.BLACK)), PexesoCard(Field(Figures.BISHOP, Colors.WHITE)), PexesoCard(Field(Figures.BISHOP, Colors.WHITE))],
            [PexesoCard(Field(Figures.ROOK, Colors.WHITE)), PexesoCard(Field(Figures.ROOK, Colors.WHITE)), PexesoCard(Field(Figures.ROOK, Colors.BLACK)), PexesoCard(Field(Figures.ROOK, Colors.BLACK)), PexesoCard(Field(Figures.BISHOP, Colors.BLACK)), PexesoCard(Field(Figures.BISHOP, Colors.BLACK))],
            [PexesoCard(Field(Figures.KNIGHT, Colors.WHITE)), PexesoCard(Field(Figures.KNIGHT, Colors.WHITE)), PexesoCard(Field(Figures.KNIGHT, Colors.BLACK)), PexesoCard(Field(Figures.KNIGHT, Colors.BLACK)), PexesoCard(Field(Figures.ONE, Colors.RED)), PexesoCard(Field(Figures.ONE, Colors.RED))],     
            [PexesoCard(Field(Figures.TWO, Colors.GREEN)), PexesoCard(Field(Figures.TWO, Colors.GREEN)), PexesoCard(Field(Figures.THREE, Colors.BLACK)), PexesoCard(Field(Figures.THREE, Colors.BLACK)), PexesoCard(Field(Figures.FOUR, Colors.RED)), PexesoCard(Field(Figures.FOUR, Colors.RED))]
        ]   
        symbols = sorted([i[:6], i[6:]] for i in set(permutations(chain.from_iterable(board))))
        self.board = random.choice(symbols)
        print(self)
        
        
    def __str__(self):
        """Vrátí textovou reprezentaci hrací desky
        """
        return "\n".join(" ".join(str(card) for card in row) for row in self.board)
    
    
    def getListOfBoard(self):
        return self.board