import random
import sympy as sp
from ..Question import Question

class DerivativeQuestionGenerator(Question):    
    """Generátor otázek na derivace
    """
    
    
    def __init__(self):
        """Konstruktor třídy DerivativeQuestionGenerator
        """
        super().__init__()
        self.hoderovaDanger = True
        self.numberOfQuestions = 4
    
    
    def generatePolynomial(self, degree):
        """Generování náhodného polynomu
        
        Args:
            degree (int): stupeň polynomu
            
        Returns:
            sympy symbol: polynom 
        """
        x = sp.symbols('x')
        polynomial = sum(random.randint(-5, 5) * x**i for i in range(0,degree))
    
        return polynomial
    
    
    def generateQuestion(self, n = None):
        """Generování náhodné otázky na derivace

        Args:
            n (int): Číslo otázky, defaultně náhodné
            
        Returns:
            DerivativeQuestionGenerator: Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        if n is not None and n in range(0, 4):
            randomQuestion = n
            
        else:
            randomQuestion = random.randint(0, 3)
    
        degree = random.randint(1, 3)
        polynomial = self.generatePolynomial(degree)
        x = sp.symbols('x')
        i = random.randint(-2, 2)
        
        if randomQuestion == 0:
            self.questionText = f"Urči hodnotu první derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x).subs(x, i)
        
        elif randomQuestion == 1:
            self.questionText = f"Urči hodnotu druhé derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x, 2).subs(x, i)
        
        elif randomQuestion == 2:
            self.questionText = f"Urči hodnotu třetí derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x, 3).subs(x, i)
        
        else:
            self.questionText = f"Urči hodnotu čtvrté derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x, 4).subs(x, i)
            
        return self


if __name__ == "__main__":
    dqg = DerivativeQuestionGenerator()
    print(dqg.generateDerivativeQuestion().__str__())