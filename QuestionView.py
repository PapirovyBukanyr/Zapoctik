import sys
from games import Colors
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
from matplotlib import rc
from io import BytesIO
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

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

        pixmap = self.render_latex_to_pixmap(self.question.questionLatex)
        self.question_latex_label = QLabel()
        self.question_latex_label.setPixmap(pixmap)
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

    def render_latex_to_pixmap(self, latexEq):
        plt.figure(figsize=(2, 1))  
        print("Rovnice: ", latexEq)
        plt.text(0.5, 0.5, f"${latexEq}$", fontsize=20, ha='center', va='center')
        plt.axis('off') 

        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close()

        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue(), "PNG")
        buf.close()
        return pixmap


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathQuestion("Kolik je 2+2", "4", lambda x: print("Correct" if x else "Incorrect"))
    window.show()
    sys.exit(app.exec_())
