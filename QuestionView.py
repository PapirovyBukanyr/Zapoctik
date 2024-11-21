import sys
from games import Colors
from resources.KatexHtmlTemplate import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MathQuestion(QWidget):
    def __init__(self, question, color, fullscreen, callback):
        super().__init__()
        self.question = question
        self.callback = callback
        self.color = color  
        if color == Colors.WHITE:
            self.setWindowTitle("Otázka pro bílého hráče")
        else:
            self.setWindowTitle("Otázka pro černého hráče")
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

        self.setLayout(layout)
        if fullscreen:
            self.showFullScreen()

    def check_answer(self):
        answer = self.answer_input.text()
        msg_box = QMessageBox()
        if self.question.checkAnswer(answer):
            self.callback(True)
            if self.color == Colors.WHITE:
                msg_box.setText("Odpověď je správná, bílý hráč může táhnout")
            else:
                msg_box.setText("Odpověď je správná, černý hráč může táhnout")
        else:
            self.callback(False)
            msg_box.setText("Odpověď je blbě. Správná odpověď je: " + self.question.doupovcuvOperator())
        msg_box.setWindowTitle("Vyhodnocení odpovědi")
        msg_box.exec_()    
        self.close()
    
    def kill_yourself(self):
        self.close()

    def render_latex_to_katex(self, latexEq):
        html = KATEX_HTML_TEMPLATE.format(equation=latexEq)
        self.question_latex_label.setHtml(html)
