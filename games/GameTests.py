import unittest
from parameterized import parameterized
from games import Chess, Checkers, TicTacToe, MathGame
from .Enums import Colors

class GameTests(unittest.TestCase):
    allClasses = [
        ("Chess", Chess),
        ("Checkers", Checkers),
        ("TicTacToe", TicTacToe),
        ("MathGame", MathGame)
    ]
    
    @parameterized.expand(allClasses)
    def testInitialBoard(self, name, game_class):
        game = game_class()
        self.assertIsNotNone(game.getBoard())

    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE),
        ("Checkers", Checkers, [5, 5], Colors.WHITE),
        ("MathGame", MathGame, [9, 9], Colors.WHITE)
    ])
    def testChoosePiece(self, name, game_class, position, color):
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))

    @parameterized.expand([
        ("Chess", Chess, [-1, -1], Colors.WHITE),
        ("Checkers", Checkers, [-1, -1], Colors.WHITE),
        ("MathGame", MathGame, [-1, -1], Colors.WHITE)
    ])
    def testChooseWrongPiece(self, name, game_class, position, color):
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))

    @parameterized.expand([
        ("Chess", Chess, [1, 1], Colors.WHITE),
        ("Checkers", Checkers, [2, 2], Colors.WHITE),
        ("MathGame", MathGame, [0, 0], Colors.WHITE)
    ])
    def testChooseUnablePiece(self, name, game_class, position, color):
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))
    
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [4, 0]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [4, 4]),
        ("TicTacToe", TicTacToe, [0, 0], None, [0, 0]),
        ("MathGame", MathGame, [9, 9], Colors.WHITE, [9, 8])
    ])
    def testMakeMove(self, name, game_class, choose_position, color, move_position):
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
        self.assertTrue(game.makeMove(move_position))
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [-1, -1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [-1, -1]),
        ("TicTacToe", TicTacToe, [-1, -1], None, [-1, -1]),
        ("MathGame", MathGame, [9, 9], Colors.WHITE, [10, 10])
    ])
    def testMakeWrongMove(self, name, game_class, choose_position, color, move_position):
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
        self.assertFalse(game.makeMove(move_position))
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [1, 1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [1, 1]),
        ("MathGame", MathGame, [9, 9], Colors.WHITE, [1, 1])
    ])
    def testMakeUnableMove(self, name, game_class, choose_position, color, move_position):
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
        self.assertFalse(game.makeMove(move_position))
        

    @parameterized.expand(allClasses)
    def testCheckEnd(self, name, game_class):
        game = game_class()
        self.assertIsNone(game.checkEnd())

if __name__ == '__main__':
    unittest.main()