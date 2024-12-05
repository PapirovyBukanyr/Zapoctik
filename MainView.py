from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
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
        self.setWindowTitle("Zápočtík Games")
        self.setFixedSize(500, 400)
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
        
        games = ListOfGames.getListOfGames()
        
        for i, game in enumerate(games):
            button = QPushButton(game.name)
            button.clicked.connect(lambda checked, g=game: self.start_game(g))
            tooltip = f"<H1>{game.name}</H1><H3 style='width: 200px;'>{game.description}</H3>"
            button.setToolTip(tooltip)
            grid_layout.addWidget(button, i // 2, i % 2) 

        main_layout.addLayout(grid_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        main_layout.addSpacerItem(spacer)

        self.setLayout(main_layout)


    def start_game(self, game):
        """Spustí hru dle jména hry

        Args:
            game (Game): objekt Game, který obsahuje název hry a objekt hry
        """
        self.gameWindow = GameView(game.game, game.name)
        self.gameWindow.show()
        self.showMinimized()
