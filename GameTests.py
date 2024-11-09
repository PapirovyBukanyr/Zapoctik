import unittest
from parameterized import parameterized
from games import Chess, Checkers, TicTacToe, MathGame
from games.Enums import Colors

class TestGames(unittest.TestCase):
    @parameterized.expand([
        ("Chess", Chess),
        ("Checkers", Checkers),
        ("TicTacToe", TicTacToe),
        ("MathGame", MathGame)
    ])
    def test_initial_board(self, name, game_class):
        game = game_class()
        self.assertIsNotNone(game.getBoard())

    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE),
        ("Checkers", Checkers, [5, 5], Colors.WHITE),
        ("MathGame", MathGame, [9, 9], Colors.WHITE)
    ])
    def test_choose_piece(self, name, game_class, position, color):
        game = game_class()
        self.assertIsNotNone(game.choosePiece(position, color))

    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [4, 0]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [4, 4]),
        ("TicTacToe", TicTacToe, [0, 0], None, [0, 0]),
        ("MathGame", MathGame, [9, 9], Colors.WHITE, [9, 8])
    ])
    def test_make_move(self, name, game_class, choose_position, color, move_position):
        game = game_class()
        if choose_position and color:
            game.choosePiece(choose_position, color)
        self.assertTrue(game.makeMove(move_position))

    @parameterized.expand([
        ("Chess", Chess),
        ("Checkers", Checkers),
        ("TicTacToe", TicTacToe),
        ("MathGame", MathGame)
    ])
    def test_check_end(self, name, game_class):
        game = game_class()
        self.assertIsNone(game.checkEnd())

if __name__ == '__main__':
    unittest.main()