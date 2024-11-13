from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette, QPixmap
from GetResource import GetResource
from games import *

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
        if 0 <= row < len(self.game.getBoard()) and 0 <= col < len(self.game.getBoard()[0]):  
            label = self.uiBoard[row][col]
            pixmap = QPixmap(filePath)
            label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            label.setAlignment(Qt.AlignCenter)

    def create_board(self):
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
        if self.selectedPiece == False and (isinstance(self.game, Checkers) or isinstance(self.game, Chess) or isinstance(self.game, MathGame)):
            self.update_board()
            self.possible_moves = self.game.choosePiece([row, col], self.player)
            for move in self.possible_moves:
                self.highlight_square(move[0], move[1])
            self.selectedPiece = True
        else:
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
                for result in self.possible_moves:
                    self.highlight_square(result[0], result[1])
                return
            if self.game.checkEnd() != None:
                self.game_ended(self.game.checkEnd())
            self.player = self.player.changeColor()
    
    def highlight_square(self, row, col):
        label = self.uiBoard[row][col]
        label.setStyleSheet("background-color: yellow;")
        label.isHighlighted = True

    def update_board(self, isFirst = False):
        if not isFirst: 
            self.remove_board()
        self.uiBoard = [[None for _ in range(len(self.game.getBoard()))] for _ in range( len(self.game.getBoard()[0]))]
        self.create_board()
        for i in range(0, len(self.game.getBoard())):
            for j in range(0, len(self.game.getBoard()[i])):
                if (self.game.getBoard()[i][j] != None):
                    self.set_piece_image(i, j, GetResource.getResource(self.game.getBoard()[i][j]))

    def remove_board(self):
        for row in range(len(self.game.getBoard())):
            for col in range( len(self.game.getBoard()[0])):
                widget = self.uiBoard[row][col]
                if widget:
                    self.layout.removeWidget(widget)
                    widget.deleteLater()
                    self.uiBoard[row][col] = None

    def game_ended(self, message):
        print(message)
        #TODO dodelat vyskakovaci okno na konec hry
        
    def promote_pawn(self):
        raise NotImplementedError("Promote pawn")
        
