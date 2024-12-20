import unittest
from parameterized import parameterized
from games import *
import random
 
class GameTests(unittest.TestCase):
    """Testy na hry
    """
    
    
    @parameterized.expand(ListOfGames.getListOfGames())
    def testInitialBoard(self, game):
        """Testuje, zda se vytvoří hrací pole
        
        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        self.assertIsNotNone(game.getBoard(Colors.WHITE))
        self.assertIsNotNone(game.getBoard(Colors.BLACK))
        self.assertNotEqual(game.getBoard(Colors.WHITE), [])
        self.assertNotEqual(game.getBoard(Colors.BLACK), [])
        


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
        self.assertNotEqual(game.choosePiece(position, color), [])
        

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
        self.assertEqual(game.choosePiece(position, color), [])
        

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
        self.assertEqual(game.choosePiece(position, color), [])
        
    
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [4, 0]),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE, [4, 0]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [4, 4]),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE, [4, 4]),
        ("TicTacToe", TicTacToe, [0, 0], None, [0, 0]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [7, 6]),
        ("Mines", Mines, [0, 0], None, [1, 1]),
        ("Filipova výzva", ChallengeAccepted, [0, 0], None, [0, 0]),
        ("Connect four", ConnectFour, [0, 0], None, [0, 0]),
        ("Chess track game", ChessTrackGame, [0, 0], None, [1, 1])
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
            
        self.assertTrue(game.makeMove(move_position, color, False))
        
        
    @parameterized.expand([
        ("Chess", Chess, [6, 0], Colors.WHITE, [-1, -1]),
        ("Chess with fog of war", ChessWithFogOfWar, [6, 0], Colors.WHITE, [-1, -1]),
        ("Checkers", Checkers, [5, 5], Colors.WHITE, [-1, -1]),
        ("Checkers with fog of war", CheckersWithFogOfWar, [5, 5], Colors.WHITE, [-1, -1]),
        ("TicTacToe", TicTacToe, [-1, -1], None, [-1, -1]),
        ("MathGame", MathGame, [7, 7], Colors.WHITE, [8, 8]),
        ("Mines", Mines, [0, 0], None, [-1, -1]),
        ("Filipova výzva", ChallengeAccepted, [0, 0], None, [-1, -1]),
        ("Connect four", ConnectFour, [0, 0], None, [-1, -1])
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
            
        self.assertFalse(game.makeMove(move_position, color))
        

    @parameterized.expand(ListOfGames.getListOfGames())
    def testCheckEnd(self, game):
        """Testuje, zda hra skončila

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        self.assertIsNone(game.checkEnd())
        
        
    @parameterized.expand(ListOfGames.getListOfGames())
    def testWithChoosingPiece(self, game):
        """Testuje, zda je definováno vybírání figurky

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        self.assertIsNotNone(game.withChoosePiece)    
        
        
    @parameterized.expand(ListOfGames.getListOfGames())
    def testFog(self, game):
        """Testuje, zda je definován mlhový efekt
        
        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        self.assertIsNotNone(game.fog)
        
        
    @parameterized.expand(ListOfGames.getListOfGames())
    def testNumberOfPlayers(self, game):
        """Testuje, zda je definován počet hráčů

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        self.assertIsNotNone(game.numberOfPlayers)
        
    
    @parameterized.expand(ListOfGames.getListOfGames())
    def testSimulateFullGame(self, game):
        """Testuje, zda se hra zahraje do konce

        Args:
            name (string): jméno hry
            game_class (game): třída hry
        """
        game = game.game
        colorOnMove = Colors.WHITE
        counter = 0
        limit = 10000

        while game.checkEnd() is None and counter < limit:
            move = []
            
            if game.withChoosePiece:
                while move == []:
                    move = game.choosePiece([random.randint(0, 10), random.randint(0, 15)], colorOnMove)
                
                if isinstance(move, list) and isinstance(move[0], list):
                    move = random.choice(move)
            else:
                move = [random.randint(0, 10), random.randint(0, 15)]
                                                        
            newMove = False
            
            while newMove != True:
                if game.withChoosePiece:
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
           
            counter += 1
            
            if isinstance(game, HumanDoNotWorry):
                colorOnMove = colorOnMove.changeColorFour()
            else:
                colorOnMove = colorOnMove.changeColor()
            
            
        print(game.checkEnd())
        self.assertGreater(limit, counter)
    
