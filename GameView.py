from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette, QPixmap
from GetResource import GetResource
from games import *
from games.Enums import Figures
import gc

class ClickableLabel(QLabel):
    clicked = pyqtSignal(int, int)  

    def __init__(self, row, col, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.row = row
        self.col = col
        self.isHighlighted = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.row, self.col)

class GameView(QWidget):
    def __init__(self, game):
        """Konstruktor

        Args:
            game (game): Hra, kterou chceme zobrazit
        """
        super().__init__()
        self.setWindowTitle(game.__str__())
        self.setGeometry(100, 100, 400, 400)  
        self.layout = QVBoxLayout()
        self.board_layout = None
        self.game = game
        self.player = Colors.WHITE
        self.selectedPiece = False
        
        self.setLayout(self.layout)
        self.update_board(True)
                    
    def set_piece_image(self, row, col, filePath):
        """Funkce pro nastavení obrázku figurky na dané pozici

        Args:
            row (int): řádek
            col (int): sloupec
            filePath (string): cesta k obrázku
        """
        if 0 <= row < len(self.game.getBoard()) and 0 <= col < len(self.game.getBoard()[0]):  
            label = self.uiBoard[row][col]
            pixmap = QPixmap(filePath)
            label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            label.setAlignment(Qt.AlignCenter)

    def create_board(self):
        """Funkce pro vytvoření herní desky
        """
        if not self.board_layout:
            self.board_layout = QGridLayout()
            self.layout.addLayout(self.board_layout)

        colors = [QColor(235, 235, 208), QColor(119, 148, 85)]  

        for row in range(len(self.game.getBoard()[0])):
            for col in range(len(self.game.getBoard())):
                label = ClickableLabel(row, col)  
                label.clicked.connect(self.handle_square_click)
                color = colors[(row + col) % 2]  
                palette = label.palette()
                palette.setColor(QPalette.Window, color)

                label.setAutoFillBackground(True)
                label.setPalette(palette)
                label.setFixedSize(100, 100)  

                self.board_layout.addWidget(label, row, col) 
                self.uiBoard[row][col] = label
 
    def handle_square_click(self, row, col):
        """Funkce pro obsluhu kliknutí na políčko

        Args:
            row (int): řádek
            col (int): sloupec
        """
        if self.selectedPiece == False and (isinstance(self.game, Checkers) or isinstance(self.game, Chess) or isinstance(self.game, MathGame)):
            self.choose_piece(row, col)
        else:
            self.make_move(row, col)
    
    def choose_piece(self, row, col):
        """Funkce pro výběr figurky
        
        Args:
            row (int): řádek
            col (int): sloupec
        """
        self.update_board()
        self.possible_moves = self.game.choosePiece([row, col], self.player)
        for move in self.possible_moves:
            self.highlight_square(move[0], move[1])
        self.selectedPiece = True
        
    def make_move(self, row, col):
        """Funkce pro provedení tahu
        
        Args:
            row (int): řádek
            col (int): sloupec
        """
        result = self.game.makeMove([row, col], self.player)
        if result == "Promote":
            self.promote_pawn()
        elif result == False:
            self.selectedPiece = False
            self.update_board()   
            return
        elif result == True:
            self.selectedPiece = False
            self.update_board()
        else:
            self.update_board()
            for move in result:
                self.highlight_square(move[0], move[1])
            return
        if self.game.checkEnd() != None:
            self.game_ended(self.game.checkEnd())
        self.player = self.player.changeColor()
    
    def highlight_square(self, row, col):
        """Funkce pro zvýraznění políčka
        
        Args:
            row (int): řádek
            col (int): sloupec
        """
        label = self.uiBoard[row][col]
        label.setStyleSheet("background-color: yellow;")
        label.isHighlighted = True

    def update_board(self, isFirst = False):
        """Funkce pro aktualizaci herní desky
        
        Args:
            isFirst (bool, optional): Je to první aktualizace?. Defaults to False.
        """
        if not isFirst: 
            self.remove_board()
        self.uiBoard = [[None for _ in range(len(self.game.getBoard()))] for _ in range( len(self.game.getBoard()[0]))]
        self.create_board()
        for i in range(0, len(self.game.getBoard())):
            for j in range(0, len(self.game.getBoard()[i])):
                if (self.game.getBoard()[i][j] != None):
                    self.set_piece_image(i, j, GetResource.getResource(self.game.getBoard()[i][j]))

    def remove_board(self):
        """Funkce pro odstranění herní desky
        """
        for row in range(len(self.game.getBoard())):
            for col in range( len(self.game.getBoard()[0])):
                widget = self.uiBoard[row][col]
                if widget:
                    self.layout.removeWidget(widget)
                    widget.deleteLater()
                    self.uiBoard[row][col] = None
        gc.collect()

    def game_ended(self, message):
        """Funkce pro zobrazení dialogového okna s výsledkem hry
        
        Args:
            message (string): Výsledek hry
        """
        if isinstance(self.game, TicTacToe):
            if message == "B won":
                message = "Vyhrál hráč O"
            elif message == "W won":
                message = "Vyhrál hráč X"
            else:
                message = "Remíza"
        else:
            if message == "W won":
                message = "Vyhrál hráč bílý"
            elif message == "B won":
                message = "Vyhrál hráč černý"
            else:
                message = "Remíza"
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle("Konec hry")
        msg_box.exec_()
        self.close()
        
    def promote_pawn(self):
        """Funkce pro výběr figurky, na kterou se má pesák změnit
        """
        items = ["Dáma", "Věž", "Střelec", "Kůň", "Král"]
        item, ok = QInputDialog.getItem(self, "Promote Pawn", "Select piece to promote to:", items, 0, False)
        
        if ok and item:
            match(item):
                case "Dáma":
                    item = Figures.QUEEN
                case "Věž":
                    item = Figures.ROOK
                case "Střelec":
                    item = Figures.BISHOP
                case "Kůň":
                    item = Figures.KNIGHT
                case "Král":
                    item = Figures.KING
                case _:
                    raise ValueError("Invalid piece")
            self.game.promote(item)
            self.update_board()