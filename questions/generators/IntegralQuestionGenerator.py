import numpy as np
import sympy as sp
from ..Question import Question

class IntegralQuestionGenerator(Question):
    """Generátor otázek na určení hodnoty integrálu
    """
    
    
    def __init__(self):
        """Konstruktor třídy IntegralQuestionGenerator
        """
        super().__init__()
        self.numberOfQuestions = 3
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na určení hodnoty integrálu

        Args:
            n (int): Číslo otázky, defaultně náhodné
        
        Returns:
            IntegralQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 3):
            randomQuestion = n
        else:
            randomQuestion = np.random.randint(0, 2)
            
        a = np.random.randint(1, 3)
        b = np.random.randint(4, 6)
        c = np.random.randint(1, 5)
        d = np.random.randint(-2, 2)
        x = sp.symbols('x')
        
        if randomQuestion == 0:
            function = c * x**d
            integral = sp.integrate(function, (x, a, b))

            self.questionText = "Urči hodnotu výrazu:"
            self.questionLatex = sp.latex(sp.Integral(function, (x, a, b)))

            self.questionLatex = self.questionLatex.replace("\\limits", "")
            self.questionLatex = self.questionLatex.replace("\\", "\\\\")
            
        elif randomQuestion == 1:
            function = c * sp.cos(sp.pi*d*x/2)
            integral = sp.integrate(function, (x, a, b))
            
            self.questionText = "Urči hodnotu výrazu:"
            self.questionLatex = sp.latex(sp.Integral(function, (x, a, b)))
            
            self.questionLatex = self.questionLatex.replace("\\limits", "")
            self.questionLatex = self.questionLatex.replace("\\", "\\\\")
            
        else:
            function = c * sp.sin(sp.pi*d*x/2)
            integral = sp.integrate(function, (x, a, b))
            
            self.questionText = "Urči hodnotu výrazu:"
            self.questionLatex = sp.latex(sp.Integral(function, (x, a, b)))
            
            self.questionLatex = self.questionLatex.replace("\\limits", "")
            self.questionLatex = self.questionLatex.replace("\\", "\\\\")
            
        self.answer = float(integral.evalf())
        
        return self