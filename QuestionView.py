import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

class MathQuestion(QWidget):
    def __init__(self, question):
        super().__init__()
        self.question = question

        self.setWindowTitle("Otázka")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.question_label = QLabel(self.question)
        layout.addWidget(self.question_label)

        self.answer_input = QLineEdit(self)
        self.answer_input.setPlaceholderText("Vaše odpověď")
        layout.addWidget(self.answer_input)

        submit_button = QPushButton("Odpovědět")
        submit_button.clicked.connect(self.check_answer)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def check_answer(self):
        answer = self.answer_input.text()
        #TODO checkovani odpovedi

app = QApplication(sys.argv)
window = MathQuestion("Kolik je 2+2")
window.show()
sys.exit(app.exec_())
