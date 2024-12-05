from games import Colors
from resources.KatexHtmlTemplate import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer, QTime

class MathQuestion(QWidget):
    """Třída MathQuestion slouží k zobrazení matematické otázky.
    """
    
    
    def __init__(self, question, color, fullscreen, callback):
        """Konstruktor třídy
        
        Args:
            question (Question): Otázka, která se má zobrazit
            color (Colors): Barva hráče, který má odpovídat
            fullscreen (bool): Zda se má zobrazit na celou obrazovku
            callback (function): Funkce, která se má zavolat po zodpovězení otázky
        """
        super().__init__()
        self.question = question
        self.callback = callback
        self.color = color  
        self.remaining_time = 60

        self.setStyleSheet("""
        QMainWindow {
            background-color: #FFFFFF;
            color: #FFFFFF;
        }

        QWidget {
            background-color: #FFFFFF;
            color: #000000;
            font-family: Segoe UI;
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

        if color == Colors.WHITE:
            self.setWindowTitle("Otázka pro bílého hráče")
        elif color == Colors.BLACK:
            self.setWindowTitle("Otázka pro černého hráče")
        elif color == Colors.RED:
            self.setWindowTitle("Otázka pro červeného hráče")
        elif color == Colors.GREEN:
            self.setWindowTitle("Otázka pro zeleného hráče")
            
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.question_label = QLabel(self.question.questionText)
        layout.addWidget(self.question_label)

        self.question_latex_label = QWebEngineView()
        self.question_latex_label.setFixedHeight(300)
        self.render_latex_to_katex(self.question.questionLatex)
        layout.addWidget(self.question_latex_label)
        
        self.answer_input = QLineEdit(self)
        self.answer_input.setPlaceholderText("Vaše odpověď")
        layout.addWidget(self.answer_input)

        submit_button = QPushButton("Odpovědět")
        submit_button.clicked.connect(self.check_answer)
        layout.addWidget(submit_button)

        self.timer_label = QLabel(f"{self.remaining_time} s")
        layout.addWidget(self.timer_label)

        self.setLayout(layout)
        self.fullscreen = fullscreen
        if fullscreen:
            self.showFullScreen()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)


    def update_timer(self):
        """Metoda na aktualizaci časovače
        """
        self.remaining_time -= 1
        self.timer_label.setText(f"Zbývající čas: {self.remaining_time} s")
        if self.remaining_time <= 0:
            self.timer.stop()
            self.time_out()


    def time_out(self):
        """Metoda na oznámení, že čas vypršel
        """
        if self.fullscreen:
            self.showNormal()
        msg_box = QMessageBox()
        self.callback(False)
        msg_box.setText("Vypršel čas! Správná odpověď je: " + self.question.doupovcuvOperator())
        msg_box.setWindowTitle("Čas vypršel")
        msg_box.exec_()
        self.kill_yourself()


    def check_answer(self):
        """Metoda na kontrolu odpovědi
        """
        self.timer.stop()
        answer = self.answer_input.text()
        msg_box = QMessageBox()
        if self.fullscreen:
            self.showNormal()
        
        if self.question.checkAnswer(answer):
            self.callback(True)
            
            if self.color == Colors.WHITE:
                msg_box.setText("Odpověď je správná, bílý hráč může táhnout")
                
            elif self.color == Colors.BLACK:
                msg_box.setText("Odpověď je správná, černý hráč může táhnout")
                
            elif self.color == Colors.RED:
                msg_box.setText("Odpověď je správná, červený hráč může táhnout")
                
            elif self.color == Colors.GREEN:
                msg_box.setText("Odpověď je správná, zelený hráč může táhnout")
                
        else:
            self.callback(False)
            msg_box.setText("Odpověď je blbě!! Správná odpověď je: " + self.question.doupovcuvOperator())
            
        msg_box.setWindowTitle("Vyhodnocení odpovědi")
        msg_box.exec_()  
        self.kill_yourself()
    
    
    def kill_yourself(self):
        """ Metoda pro ukončení okna galantní cestou
        """
        self.timer.stop()
        if self.fullscreen:
            self.showNormal()
        self.close()


    def render_latex_to_katex(self, latexEq):
        """Metoda na vytvoření rovnic ve formátu LaTeX

        Args:
            latexEq (string): rovnice, které se mají vykreslit v LaTeXu
        """
        html = KATEX_HTML_TEMPLATE.format(equation=latexEq)
        self.question_latex_label.setHtml(html)