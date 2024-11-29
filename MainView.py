from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from GameView import *
from games import *
from PyQt5.QtGui import QFontDatabase

class MainView(QWidget):
    """Třída MainView slouží k zobrazení hlavního menu aplikace.
    """
    
    
    def __init__(self):
        """Konstruktor třídy
        """
        super().__init__()
        self.setWindowTitle("Game Menu")
        self.setStyleSheet("""
        QMainWindow {
            background-color: #FFFFFF;
            color: #FFFFFF;
        }

        QWidget {
            background-color: #FFFFFF;
            color: #000000;
            font-family: Yu Gothic UI;
        }

        QPushButton {
            background-color: #DDDDDD;
            color: #000000;
            border: 2px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }

        QPushButton:hover {
            background-color: #0066ff;
        }

        QPushButton:pressed {
            background-color: #3399ff;
        }
        """)

        # font_database = QFontDatabase()
        # available_fonts = font_database.families()

        # # Print the list of fonts
        # for font in available_fonts:
        #     print(font)

        layout = QVBoxLayout()

        title = QLabel("Select a Game to Play")
        layout.addWidget(title)

        games = ["Šachy♛", "Dáma𖣯", "Piškvorky❌⭕", "Matematická hra🔢", "Miny💣", "Šachy s mlhou války☁️", "Dáma s mlhou války☁️", "Hledání krtka🐀", "Člověče, nezlob se🎲"]

        for game in games:
            button = QPushButton(game)
            button.clicked.connect(lambda checked, g=game: self.start_game(g))
            layout.addWidget(button)

        self.setLayout(layout)


    def start_game(self, game_name):
        """Spustí hru podle jména
        
        Args:
            game_name (string): název hry
        """
        match(game_name):
            case "Šachy♛":
                self.gameWindow = GameView(Chess())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Dáma𖣯":
                self.gameWindow = GameView(Checkers())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Piškvorky❌⭕":
                self.gameWindow = GameView(TicTacToe())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Matematická hra🔢":
                self.gameWindow = GameView(MathGame())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Miny💣":
                self.gameWindow = GameView(Mines())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Šachy s mlhou války☁️":
                self.gameWindow = GameView(ChessWithFogOfWar())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Dáma s mlhou války☁️":
                self.gameWindow = GameView(CheckersWithFogOfWar())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Hledání krtka🐀":
                self.gameWindow = GameView(ChallengeAccepted())
                self.gameWindow.show()
                self.showMinimized()
                
            case "Člověče, nezlob se🎲":
                self.gameWindow = GameView(HumanDoNotWorry())
                self.gameWindow.show()
                self.showMinimized()
            