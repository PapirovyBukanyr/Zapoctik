import numpy as np
from ..Question import Question

class AnalyticGeometryQuestionGenerator(Question):
    def generateQuestion(self):
        """Generování náhodné otázky na analytickou geometrii

        Returns:
            AnalyticGeometryQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
        
        self.questionText = "Urči průsečík přímek, odpověď zadej ve formátu (x,y):"
        self.questionLatex = f"y = {a}x + {b}\\\\newline y = {c}x + {d}"
        if a == c:
            return self.generateQuestion()
        x = round( (d - b) / (a - c))
        y = round (a*x + b)
        self.answer = f"({x},{y})"
        
        return self