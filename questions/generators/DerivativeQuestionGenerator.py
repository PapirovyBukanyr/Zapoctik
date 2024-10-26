import random
import sympy as sp
from questions.Question import Question

class DerivativeQuestionGenerator(Question):    
    def generatePolynomial(self, degree):
        """Generování náhodného polynomu
        
        Args:
            degree: stupeň polynomu
            
        Returns:
            polynom ve tvaru sympy
        """
        x = sp.symbols('x')
        polynomial = sum(random.randint(-10, 10) * x**i for i in range(0,degree + 1))
        return polynomial
    
    def generateQuestion(self):
        """Generování náhodné otázky na derivace

        Returns:
            Vrací samo sebe s vygenerovanou otázkou a odpovědí
        """
        randomQuestion = random.randint(1, 3)
        degree = random.randint(1, 4)
        polynomial = self.generatePolynomial(degree)
        x = sp.symbols('x')
        i = random.randint(-5, 5)
        
        if randomQuestion == 1:
            self.questionText = f"Urči hodnotu první derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x).subs(x, i)
        
        elif randomQuestion == 2:
            self.questionText = f"Urči hodnotu druhé derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x, 2).subs(x, i)
        
        else:
            self.questionText = f"Urči hodnotu třetí derivace v bodě x = {i}"
            self.questionLatex = sp.latex(polynomial)
            self.answer = sp.diff(polynomial, x, 3).subs(x, i)
        
        return self

if __name__ == "__main__":
    dqg = DerivativeQuestionGenerator()
    print(dqg.generateDerivativeQuestion().__str__())