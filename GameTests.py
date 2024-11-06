import unittest
from games import Chess
from games import Checkers
from games import TicTacToe
from games import MathGame  
from games.Enums import Colors

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_initial_board(self):
        self.assertIsNotNone(self.game.getBoard())
        
    def test_choose_piece(self):
        self.assertIsNotNone(self.game.choosePiece([6, 0]), Colors.WHITE)
    
    def test_make_move(self):
        self.game.choosePiece([6, 0]), Colors.WHITE
        self.assertTrue(self.game.makeMove([4, 0])) 
        
    def test_check_end(self):
        self.assertIsNone(self.game.checkEnd())

class TestCheckers(unittest.TestCase):
    def setUp(self):
        self.game = Checkers()

    def test_initial_board(self):
        self.assertIsNotNone(self.game.getBoard())

    def test_choose_piece(self):
        self.assertIsNotNone(self.game.choosePiece([5, 5]), Colors.WHITE)

    def test_make_move(self):
        self.game.choosePiece([5, 5]), Colors.WHITE
        self.assertTrue(self.game.makeMove([4, 4]))  
        
    def test_check_end(self):
        self.assertIsNone(self.game.checkEnd())

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        self.assertIsNotNone(self.game.getBoard())

    def test_make_move(self):
        self.assertTrue(self.game.makeMove([0, 0])) 
        
    def test_check_end(self):
        self.assertIsNone(self.game.checkEnd())

class TestMathGame(unittest.TestCase):
    def setUp(self):
        self.game = MathGame()

    def test_initial_board(self):
        self.assertIsNotNone(self.game.getBoard())
        
    def test_choose_piece(self):
        self.assertTrue(self.game.choosePiece([9, 9], Colors.WHITE))

    def test_make_move(self):
        self.assertTrue(self.game.makeMove([9, 8]))  

    def test_check_end(self):
        self.assertIsNone(self.game.checkEnd())

if __name__ == '__main__':
    unittest.main()