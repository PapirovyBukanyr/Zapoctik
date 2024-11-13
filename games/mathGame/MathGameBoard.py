from ..Board import *
from ..Enums import *
from random import randint

class MathGameBoard (Board):
    def __init__(self):
      super().__init__()
      self.__populateBoard()

    def __getitem__(self, index):
      """Vrací figuru na určeném místě na šachovnici, nebo None, pokud je políčko prázdné. 

      Args:
          index [int, int]: Tuple dvou integerů, (row, col), oba 0-7
      """
      try:
        if index[0] < 0 or index[0] > 9 or index[1] < 0 or index[1] > 9:
          return None
        return super().__getitem__(index)
      except:
        return None
    
    
    def __setitem__(self, index, value):
      """Nastaví políčko na šachovnici jako board[row,col] namísto board.board[row][col] 

      Args:
          index ([int, int]): Tuple dvou integerů, (row, col), oba 0-7
          value (Piece): Instance třídy Piece, nebo None, pokud má být políčko prázdné

      Returns:
          bool: True, pokud se podařilo nastavit políčko, jinak False
      """
      if index[0] < 0 or index[0] > 9 or index[1] < 0 or index[1] > 9:
        return False
      super().__setitem__(index, value)
      return True


    def __str__(self):
      """Vrací string reprezentaci šachovnice. Každé políčko je reprezentováno jako string, který je tvořen z informací o barvě a symbolu figury, nebo jako string "__", pokud je políčko prázdné. Políčka jsou oddělena mezerou a jednotlivé řádky jsou odděleny znakem nového řádku (\n)."""
      result = ""
      for i in range(10):
        for j in range(10):
          try:
              if self.board[i][j]!=None:
                  result += str(self.board[i][j]) + " "
              else:
                  result += "__ "
          except:
            result +=  "__ "
        result += "\n"
      return result
    
    
    def __populateBoard(self):
      """Nastaví šachovnici do počátečního stavu. Bílý je vpravo dole a černý vlevo nahoře."""

      self.board = [[None for i in range(10)] for j in range(10)]

      for i in range(10):
          for j in range(10):
              if i == 0 and i == j:
                  self.board[i][j] = Colors.BLACK
              elif i == 9 and i == j:
                  self.board[i][j] = Colors.WHITE
              else:
                self.board[i][j] = None

      for i in range(10):
          x = randint(0,9)
          y = randint(0,9)
          i = 0
          while self.board[x][y] is not None:
            x = randint(0,9)
            y = randint(0,9)
            i += 1
            if i > 100:
              break
          self.board[x][y] = "TASK"

    def TasksLeft(self):
      """Vrací počet zbývajících úkolů na šachovnici.

      Returns:
          int: Počet zbývajících úkolů
      """
      count = 0
      for i in range(10):
        for j in range(10):
          if self.board[i][j] == "TASK":
            count += 1
      return count

    def getPosition(self, color):
      """Vrací pozici figury dané barvy.

      Args:
          color (Enum Colors): Barva figurek, které chceme najít (Colors.WHITE nebo Colors.BLACK)

      Returns: 
          [int, int]: Pozice figury na šachovnici
      """
      for i in range(10):
        for j in range(10):
          if self.board[i][j] is not None and self.board[i][j] == color:
            return [i,j]
      return None

    def getPosibleMoves(self, position):
      """Vrací možné tahy figury na dané pozici.

      Args:
          position ([int, int]): Pozice figury na šachovnici

      Returns:
          List of [int, int]: List možných tahů figury
      """
      moves = []
      for i in range(-1,2,2):
        if position[0]+i >= 0 and position[0]+i <= 9 and position[1] >= 0 and position[1] <= 9:
            if self.board[position[0]+i][position[1]] is None or self.board[position[0]+i][position[1]] == "TASK":
              moves.append([position[0]+i,position[1]])
        if position[0] >= 0 and position[0] <= 9 and position[1]+i >= 0 and position[1]+i <= 9:
            if self.board[position[0]][position[1]+i] is None or self.board[position[0]][position[1]+i] == "TASK":
              moves.append([position[0],position[1]+i])
      return moves

    def movePiece(self, move, color):
        """Přesune figuru na jiné místo na šachovnici.
    
        Args:
            move ([int, int]): Nová pozice figury
            color (Enum Colors): Barva figury, kterou chceme přesunout
        """
        self.board[self.getPosition(color)[0]][self.getPosition(color)[1]] = None
        self.board[move[0]][move[1]] = color
        
    def getListOfBoard(self):
      """Vrací list všech figurek na šachovnici.

      Returns: 
          List of Fields: List figurek na šachovnici
      """
      pieceList = [[None for i in range(10)] for j in range(10)]
      for i in range(10):
        for j in range(10):
          if isinstance(self.board[i][j], Colors):
            pieceList[i][j] = Field(self.board[i][j], Figures.PAWN)
          else: 
            pieceList[i][j] = None
      return pieceList