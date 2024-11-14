import unittest
from parameterized import parameterized
from games import Chess, Checkers, TicTacToe, MathGame
from .Enums import Colors

class GameTests(unittest.TestCase):
    __allClasses = [
        ("Chess", Chess),
        ("Checkers", Checkers),
        ("TicTacToe", TicTacToe),
        ("MathGame", MathGame)
    ]
    
    @parameterized.expand(__allClasses)
    def testInitialBoard(self, name, game_class):
        """Testuje, zda se vytvoří hrací pole
        
        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game_class()
        self.assertIsNotNone(game.getBoard())

    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE),
        ("Checkers", Checkers, [5, 5], Colors.WHITE),
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
        ("Checkers", Checkers, [-1, -1], Colors.WHITE),
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
        ("Checkers", Checkers, [2, 2], Colors.WHITE),
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
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [4, 4]),
        ("TicTacToe", TicTacToe, [0, 0], None, [0, 0]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [7, 6])
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
        self.assertTrue(game.makeMove(move_position))
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [-1, -1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [-1, -1]),
        ("TicTacToe", TicTacToe, [-1, -1], None, [-1, -1]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [8, 8])
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
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [1, 1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [1, 1]),
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
        

    @parameterized.expand(__allClasses)
    def testCheckEnd(self, name, game_class):
        """Testuje, zda hra skončila

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game_class()
        self.assertIsNone(game.checkEnd())