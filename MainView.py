from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from ChessView import *

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Menu")

        layout = QVBoxLayout()

        title = QLabel("Select a Game to Play")
        layout.addWidget(title)

        games = ["Šachy", "Dáma"]

        for game in games:
            button = QPushButton(game)
            button.clicked.connect(lambda checked, g=game: self.start_game(g))
            layout.addWidget(button)

        self.setLayout(layout)

    def start_game(self, game_name):
        match(game_name):
            case "Šachy":
                self.chessWindow = ChessView()
                self.chessWindow.show()