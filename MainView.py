from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from GameView import *
from games import *
from PyQt5.QtGui import QIcon

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zápočtík Games")
        self.setFixedSize(400, 300)
        icon = QIcon("resources/logo.jpg")  
        self.setWindowIcon(icon)

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
                           
        QLabel#AppName {
            font-size: 16px;
            font-weight: bold;
            text-align: center;
        }
        """)

        # font_database = QFontDatabase()
        # available_fonts = font_database.families()

        # # Print the list of fonts
        # for font in available_fonts:
        #     print(font)

        main_layout = QVBoxLayout()

        title = QLabel("Zápočtík Games")
        title.setObjectName("AppName")  
        title.setAlignment(Qt.AlignCenter)  
        main_layout.addWidget(title)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(spacer)

        grid_layout = QGridLayout()
        games = ["Šachy♛", "Dáma𖣯", "Piškvorky❌⭕", "Matematická hra🔢", "Miny💣", "Šachy s mlhou války☁️", "Dáma s mlhou války☁️", "Hledání krtka🐀"]

        for i, game in enumerate(games):
            button = QPushButton(game)
            button.clicked.connect(lambda checked, g=game: self.start_game(g))
            grid_layout.addWidget(button, i // 2, i % 2) 

        main_layout.addLayout(grid_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(spacer)

        self.setLayout(main_layout)

    def start_game(self, game_name):
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
            