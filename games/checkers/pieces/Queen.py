from .Piece import *

class Queen(Piece):
    def __init__(self, pawn):
        """Konstruktor třídy Queen

        Args:
            pawn (Pawn): Pěšák, který se má proměnit na dámu
        """
        super().__init__(pawn.color, pawn.position)
        
        
    def __str__(self):
        """Vrací string reprezentaci dámy

        Returns:
            string: string reprezentace dámy
        """
        return 'Q' + self.color.__str__()
        
        
    def possibleMoves(self, board):
        """Vrací seznam možných tahů dámy

        Args:
            board (CheckersBoard): šachovnice, na které se dáma nachází

        Returns:
            List of [int, int] : seznam možných tahů dámy
        """
        moves = []
        for j in [-1,1]:
            for k in [-1,1]:
                for i in range(1, 8):
                    if self.position[0] + i*j < 8 and self.position[0] + i*j >= 0 and self.position[1] + i*k < 8 and self.position[1] + i*k >= 0:
                        if board[self.position[0] + i*j,self.position[1] + i*k] is None:
                            moves.append([self.position[0] + i*j, self.position[1] + i*k])
                        else:
                            break
                    else:
                        break
                    
        moves += self.possibleJumps(board)    
            
        return moves
    
    
    def possibleJumps(self, board, position = None):
        """Vrací seznam možných prvních skoků dámy
        
        Args:
            board (CheckersBoard): šachovnice, na které se dáma nachází
            position ([int, int], optional): pozice, ze které se má skákat. Výchozí hodnota je None, což znamená, že se skáče ze současné pozice dámy
            
        Returns:
            List of [int, int]: seznam možných prvních skoků dámy
        """
        if position == None:
            position = self.position
        jumps = []
        
        for j in [-1,1]:
            for k in [-1,1]:
                for i in range(1, 8):
                    if position[0] + i*j + j< 8 and position[0] + i*j + j>= 0 and position[1] + i*k + k < 8 and position[1] + i*k + k>= 0:
                        if board[position[0] + i*j,position[1] + i*k] != None:
                            if board[position[0] + i*j,position[1] + i*k].color == self.color:
                                break
                            
                            if board[position[0] + i*j,position[1] + i*k].color == self.color.changeColor() and board[position[0] + i*j + j,position[1] + i*k + k] == None:
                                jumps.append([position[0] + i*j + j, position[1] + i*k + k])
                            else:
                                break
                    else:
                        break
        print(jumps)
        return jumps
    
    
    def trackJumps(self, endPosition):
        """Vrací seznam pozic figurek, které dáma přeskočí, než se dostane na koncovou pozici
        
        Args:
            endPosition ([int, int]): koncová pozice, na kterou se má dáma dostat
            
        Returns:
            List of [int, int]: seznam pozic figurek, které dáma přeskočí, než se dostane na koncovou pozici
        """
        jumps=([endPosition[0]-(endPosition[0]-self.position[0])//abs(endPosition[0]-self.position[0]), endPosition[1]-(endPosition[1]-self.position[1])//abs(endPosition[1]-self.position[1])])
        return jumps
    
