from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from GameView import *
from games import *
from PyQt5.QtGui import QFontDatabase

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Menu")
        self.setStyleSheet("""
        QMainWindow {
            background-color: #2e2e2e;
            color: #ffffff;
        }

        QWidget {
            background-color: #2e2e2e;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }

        QPushButton {
            background-color: #444444;
            color: #ffffff;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }

        QPushButton:hover {
            background-color: #0066ff;
        }

        QPushButton:pressed {
            background-color: #3399ff;
        }

        QLabel {
            color: #ffffff;
        }

        QLineEdit {
            background-color: #444444;
            color: #ffffff;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 2px;
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

        games = ["Šachy", "Dáma", "Piškvorky", "Matematická hra", "Miny", "Šachy s mlhou války", "Dáma s mlhou války"]

        for game in games:
            button = QPushButton(game)
            button.clicked.connect(lambda checked, g=game: self.start_game(g))
            layout.addWidget(button)

        self.setLayout(layout)

    def start_game(self, game_name):
        match(game_name):
            case "Šachy":
                self.gameWindow = GameView(Chess())
                self.gameWindow.show()
            case "Dáma":
                self.gameWindow = GameView(Checkers())
                self.gameWindow.show()
            case "Piškvorky":
                self.gameWindow = GameView(TicTacToe())
                self.gameWindow.show()
            case "Matematická hra":
                self.gameWindow = GameView(MathGame())
                self.gameWindow.show()
            case "Miny":
                self.gameWindow = GameView(Mines())
                self.gameWindow.show()
            case "Šachy s mlhou války":
                self.gameWindow = GameView(ChessWithFogOfWar())
                self.gameWindow.show()
            case "Dáma s mlhou války":
                self.gameWindow = GameView(CheckersWithFogOfWar())
                self.gameWindow.show()