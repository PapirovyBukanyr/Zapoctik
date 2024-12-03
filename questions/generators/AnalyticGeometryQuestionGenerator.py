import numpy as np
from ..Question import Question

class AnalyticGeometryQuestionGenerator(Question):    
    """Generátor otázek na analytickou geometrii
    """
    
    
    def __init__(self):
        """Konstruktor třídy AnalyticGeometryQuestionGenerator
        """
        super().__init__()
        self.numberOfQuestions = 1
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na analytickou geometrii

        Args:
            n (int): Číslo otázky, defaultně náhodné

        Returns:
            AnalyticGeometryQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        a = np.random.randint(1, 5)
        b = np.random.randint(1, 5)
        c = np.random.randint(1, 5)
        d = np.random.randint(1, 5)
        
        self.questionText = "Urči průsečík přímek, odpověď zadej ve formátu (x,y):"
        self.questionLatex = f"y = {a}x + {b}\\\\newline y = {c}x + {d}"
        
        if a == c:
            return self.generateQuestion()
        
        x = round( (d - b) / (a - c))
        y = round (a*x + b)
        self.answer = f"({x},{y})"
        
        return self