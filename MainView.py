from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from GameView import *
from games import *

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Menu")

        layout = QVBoxLayout()

        title = QLabel("Select a Game to Play")
        layout.addWidget(title)

        games = ["Šachy", "Dáma", "Piškvorky", "Matematická hra", "Miny", "Šachy s mlhou války", "Dáma s mlhou války", "Hledání krtka"]

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
            case "Hledání krtka":
                self.gameWindow = GameView(ChallengeAccepted())
                self.gameWindow.show()
            