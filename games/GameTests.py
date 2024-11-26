import unittest
from parameterized import parameterized
from games import Chess, Checkers, TicTacToe, MathGame, Mines, ChessWithFogOfWar, CheckersWithFogOfWar, ChallengeAccepted
import random
from .Enums import Colors

class GameTests(unittest.TestCase):
    """Testy na hry
    """
    
    
    __allClasses = [
        ("Chess", Chess),
        ("Checkers", Checkers),
        ("TicTacToe", TicTacToe),
        ("MathGame", MathGame),
        ("Mines", Mines),
        ("ChessWithFogOfWar", ChessWithFogOfWar),
        ("CheckersWithFogOfWar", CheckersWithFogOfWar),
        ("Filipova výzva", ChallengeAccepted)     
    ]
    """list: Seznam všech tříd her
    """
    
    
    @parameterized.expand(__allClasses)
    def testInitialBoard(self, name, game_class):
        """Testuje, zda se vytvoří hrací pole
        
        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game_class()
        self.assertIsNotNone(game.getBoard(Colors.WHITE))
        self.assertIsNotNone(game.getBoard(Colors.BLACK))

    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE),
        ("Checkers", Checkers, [5, 5], Colors.WHITE),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE),
        ("MathGame", MathGame, [7, 7], Colors.WHITE)
    ])
    def testChoosePiece(self, name, game_class, position, color):
        """Testuje, zda se figurka dá vybrat
        
        Args:
            name (string): jméno hry
            game_class (game): třída hry
            position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
        """
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))
        

    @parameterized.expand([
        ("Chess", Chess, [-1, -1], Colors.WHITE),
        ("Chess with fog of war", ChessWithFogOfWar, [-1, -1], Colors.WHITE),
        ("Checkers", Checkers, [-1, -1], Colors.WHITE),
        ("Checkers with fog of war", CheckersWithFogOfWar, [-1, -1], Colors.WHITE),
        ("MathGame", MathGame, [-1, -1], Colors.WHITE)
    ])
    def testChooseWrongPiece(self, name, game_class, position, color):
        """Testuje, zda se figurka nedá vybrat

        Args:
            name (string): jméno hry
            game_class (game): třída hry
            position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
        """
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))
        

    @parameterized.expand([
        ("Chess", Chess, [1, 1], Colors.WHITE),
        ("Chess with fog of war", ChessWithFogOfWar, [1, 1], Colors.WHITE),
        ("Checkers", Checkers, [2, 2], Colors.WHITE),
        ("Checkers with fog of war", CheckersWithFogOfWar, [2, 2], Colors.WHITE),
        ("MathGame", MathGame, [0, 0], Colors.WHITE)
    ])
    def testChooseUnablePiece(self, name, game_class, position, color):
        """Testuje, zda se figurka nedá vybrat

        Args:
            name (string): jméno hry
            game_class (game): třída hry
            position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
        """
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))
        
    
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [4, 0]),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE, [4, 0]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [4, 4]),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE, [4, 4]),
        ("TicTacToe", TicTacToe, [0, 0], None, [0, 0]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [7, 6]),
        ("Mines", Mines, [0, 0], None, [1, 1]),
        ("Filipova výzva", ChallengeAccepted, [0, 0], None, [0, 0])
    ])
    def testMakeMove(self, name, game_class, choose_position, color, move_position):
        """Testuje, zda se pohyb provede

        Args:
            name (string): jméno hry
            game_class (game): třída hry
            choose_position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
            move_position ([int, int]): pozice, kam se má figurka pohnout
        """
        game = game_class()
        
        if choose_position and color:
            game.choosePiece(choose_position, color)
        self.assertTrue(game.makeMove(move_position, color))
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [-1, -1]),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE, [-1, -1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [-1, -1]),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE, [-1, -1]),
        ("TicTacToe", TicTacToe, [-1, -1], None, [-1, -1]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [8, 8]),
        ("Mines", Mines, [0, 0], None, [-1, -1]),
        ("Filipova výzva", ChallengeAccepted, [0, 0], None, [-1, -1])
    ])
    def testMakeWrongMove(self, name, game_class, choose_position, color, move_position):
        """Testuje, zda se pohyb nelze provést

        Args:
            name (string): jméno hry
            game_class (game): třída hry
            choose_position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
            move_position ([int, int]): pozice, kam se má figurka pohnout
        """
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
            self.assertFalse(game.makeMove(move_position))
        else:
            self.assertFalse(game.makeMove(move_position, color))
        
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [1, 1]),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE, [1, 1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [1, 1]),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE, [1, 1]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [1, 1])
    ])
    def testMakeUnableMove(self, name, game_class, choose_position, color, move_position):
        """Testuje, zda se pohyb nelze provést

        Args:
            name (string): jméno hry
            game_class (game): třída hry
            choose_position ([int, int]): pozice figurky, se kterou se má pohnout
            color (Enum Colors): barva na tahu
            move_position ([int, int]): pozice, kam se má figurka pohnout
        """
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
            self.assertFalse(game.makeMove(move_position))
        else:
            self.assertFalse(game.makeMove(move_position, color))
        

    @parameterized.expand(__allClasses)
    def testCheckEnd(self, name, game_class):
        """Testuje, zda hra skončila

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game_class()
        self.assertIsNone(game.checkEnd())
        
    
    @parameterized.expand(__allClasses)
    def testSimulateFullGame(self, name, game_class):
        """Testuje, zda se hra zahraje do konce

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game_class()
        colorOnMove = Colors.WHITE
        counter = 0
        limit = 10000

        while game.checkEnd() is None and counter < limit:
            move = []

            if self.isGameWithChoosingPiece(game):
                while move == []:
                    move = game.choosePiece([random.randint(0, 10), random.randint(0, 15)], colorOnMove)
                
                if isinstance(move, list) and isinstance(move[0], list):
                    move = random.choice(move)
            else:
                move = [random.randint(0, 10), random.randint(0, 15)]
                                                        
            newMove = False
            
            while newMove != True:
                if self.isGameWithChoosingPiece(game):
                    newMove = game.makeMove(move, colorOnMove)
                    if not isinstance(newMove,bool) and not isinstance(newMove, str) and isinstance(newMove[0], list) and isinstance(newMove[0][0], int):
                        move = random.choice(newMove)
                        
                    elif newMove == "Promote":
                        move = game.promote("Q")
                        newMove = True
                    
                    elif not isinstance(newMove,bool) and isinstance(newMove, list) and isinstance(newMove[0], int):
                        move = newMove
                
                else:
                    newMove = game.makeMove([random.randint(0, 10), random.randint(0, 15)], colorOnMove)

            colorOnMove = colorOnMove.changeColor()
            counter += 1
            
        print(game.checkEnd())
        self.assertFalse(counter >= limit)
    
    
    def isGameWithChoosingPiece(self, game):
        """Zjistí, zda hra vyžaduje výběr figurky

        Args:
            game (game): hra

        Returns:
            bool: True, pokud hra vyžaduje výběr figurky
        """
        return isinstance(game, Chess) or isinstance(game, Checkers) or isinstance(game, MathGame) or isinstance(game, ChessWithFogOfWar) or isinstance(game, CheckersWithFogOfWar)

