from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPalette, QPixmap
from games.chess.Chess import Chess

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

class ChessView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 400, 400)  
        self.layout = QVBoxLayout()
        self.board_layout = None
        self.game = Chess()

        self.setLayout(self.layout)
        self.update_board(True)
                    
    def set_piece_image(self, row, col, filePath):
        if 0 <= row < 8 and 0 <= col < 8:  
            label = self.uiBoard[row][col]
            pixmap = QPixmap(filePath)
            label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            label.setAlignment(Qt.AlignCenter)

    def create_board(self):
        if not self.board_layout:
            self.board_layout = QGridLayout()
            self.layout.addLayout(self.board_layout)

        colors = [QColor(235, 235, 208), QColor(119, 148, 85)]  

        for row in range(8):
            for col in range(8):
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
        if self.dataBoard[row][col] != None and self.selectedPiece is None:
            self.possible_moves = self.get_moves(row, col)
            for move in self.possible_moves:
                self.highlight_square(move[0], move[1])
        elif self.selectedPiece != None:
            self.move_piece(row, col)

    def get_moves(self, row, col):
        self.selectedPiece = self.dataBoard[row][col]
        return self.selectedPiece.possibleMoves(self.game.getBoard())
    
    def highlight_square(self, row, col):
        label = self.uiBoard[row][col]
        label.setStyleSheet("background-color: yellow;")
        label.isHighlighted = True

    def move_piece(self, row, col):
        if self.uiBoard[row][col].isHighlighted:
            self.selectedPiece.move(self.game.getBoard(), [row, col])
            message = self.game.checkEnd()
            if message != None:
                self.game_ended(message)
            self.update_board(False)
        else: 
            self.selectedPiece = None
            self.update_board(False)

    def update_board(self, isFirst):
        if not isFirst: 
            self.remove_board()
        self.uiBoard = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()
        self.dataBoard = self.game.getBoard().board
        self.selectedPiece = None
        
        for i in range(0, 8):
            for j in range(0, 8):
                if (self.dataBoard[i][j] != None):
                    self.set_piece_image(i, j, self.dataBoard[i][j].img_file)

    def remove_board(self):
        for row in range(8):
            for col in range(8):
                widget = self.uiBoard[row][col]
                if widget:
                    self.layout.removeWidget(widget)
                    widget.deleteLater()
                    self.uiBoard[row][col] = None

    def game_ended(self, message):
        print(message)
        #TODO dodelat vyskakovaci okno na konec hry
        
